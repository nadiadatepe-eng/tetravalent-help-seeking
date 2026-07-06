#!/usr/bin/env python3
"""
run_confirmatory.py -- Test 4 CONFIRMATORY batch: 72 seeds/arm, both arms
(coordinated, independent), R=3, llama3.1:8b. Nadi-approved overnight run
(2026-07-06), POWERED UP same day (2026-07-06): seeds 101-124 (batch #1,
24/arm) already complete on disk; seeds 125-172 (48 more/arm) added to give
the underpowered headline contrast (d=0.53, p~0.07 at 24 seeds/arm) an
honest shot at significance -- 72/arm total. Idempotent checkpointing means
this run SKIPS 101-124 automatically and only executes the new 96 units
(48 seeds x 2 arms).

This script REUSES run_pilot.py's run_arm() unmodified -- all four
refinements (#1 graded-belief primary metric, #2 neutralized shared
briefing, #3 real model-driven ask-targeting, #3b per-call roster
randomization) are already the default behaviour baked into run_arm() and
are NOT reimplemented here. This script only adds:
  - the 24-seeds x 2-arms loop (fixed, reproducible seed list: 101..124)
  - per-(arm, seed) idempotent checkpointing (own output files + a marker
    file written LAST, only after every write for that unit succeeds)
  - a tailable progress log (human-readable via print(), plus a structured
    progress_log.jsonl for the analyze script / quick scripting)
  - per-unit try/except so one bad seed can never kill the whole batch

Idempotent checkpointing contract: each (arm, seed) writes
  events_{arm}_seed{N}.jsonl, setup_log_{arm}_seed{N}.json,
  grade_report_{arm}_seed{N}.json, grade_belief_report_{arm}_seed{N}.json,
  raw_responses_{arm}_seed{N}.jsonl, trajectories_{arm}_seed{N}.json,
  ask_graph_{arm}_seed{N}.jsonl, ask_graph_summary_{arm}_seed{N}.json,
  run_stats_{arm}_seed{N}.json
followed by a marker file `.done_{arm}_seed{N}` (JSON stub, cheap to stat).
On (re)start, any (arm, seed) whose marker already exists is SKIPPED
entirely (no re-read of its content, just an existence check) -- a crash or
kill mid-write for a unit leaves NO marker for that unit, so a restart
safely redoes that one unit from scratch. A unit is never considered done
based on partial files existing; only the marker (written after everything
else) counts.

Usage:
    python3 run_confirmatory.py                       # full 72x2 batch (skips 101-124, already done)
    python3 run_confirmatory.py --seeds 101 --arms coordinated   # 1-seed sanity check
    setsid nohup python3 run_confirmatory.py \
        > confirmatory_output/progress.log 2>&1 < /dev/null &
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from engine import schema  # noqa: E402
from engine.backend import OllamaBackend  # noqa: E402
import run_pilot  # noqa: E402 -- reuse run_arm() + compute_ask_graph_summary(), no reimplementation

OUT_DIR = Path(__file__).resolve().parent / "confirmatory_output"
PROGRESS_JSONL = OUT_DIR / "progress_log.jsonl"

SEEDS_DEFAULT = list(range(101, 173))          # 72 seeds, fixed + reproducible
                                                 # (101-124 = batch #1, complete;
                                                 #  125-172 = power-up batch #2)
ARMS_DEFAULT = list(run_pilot.domain.ARMS)      # ("coordinated", "independent")


def marker_path(arm: str, seed: int) -> Path:
    return OUT_DIR / f".done_{arm}_seed{seed}"


def is_complete(arm: str, seed: int) -> bool:
    return marker_path(arm, seed).exists()


def log_progress(msg: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{ts}] {msg}", flush=True)


def append_progress_record(record: dict) -> None:
    record["ts"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(PROGRESS_JSONL, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")


def write_arm_seed_outputs(arm: str, seed: int, result: dict, wall_s: float, model: str) -> dict:
    """Write the full output file set for one (arm, seed) -- same file shapes
    run_pilot.main() writes, just suffixed _seed{seed} and rooted under
    confirmatory_output/ -- then a marker file LAST, only reached if every
    write above succeeded (so a crash mid-write never leaves a marker)."""
    sfx = f"_seed{seed}"
    events = result["events"]
    ok, errors = schema.validate_log(events)

    (OUT_DIR / f"events_{arm}{sfx}.jsonl").write_text(
        "\n".join(json.dumps(ev) for ev in events) + "\n", encoding="utf-8")
    (OUT_DIR / f"setup_log_{arm}{sfx}.json").write_text(
        json.dumps(result["setup_log"], indent=2), encoding="utf-8")
    (OUT_DIR / f"grade_report_{arm}{sfx}.json").write_text(
        json.dumps(result["grade_report"], indent=2, default=str), encoding="utf-8")
    (OUT_DIR / f"grade_belief_report_{arm}{sfx}.json").write_text(
        json.dumps(result["grade_belief_report"], indent=2, default=str), encoding="utf-8")
    (OUT_DIR / f"raw_responses_{arm}{sfx}.jsonl").write_text(
        "\n".join(json.dumps(r) for r in result["raw_log"]) + "\n", encoding="utf-8")
    traj_serializable = {name: [[r, bs] for r, bs in traj] for name, traj in result["trajectories"].items()}
    (OUT_DIR / f"trajectories_{arm}{sfx}.json").write_text(
        json.dumps(traj_serializable, indent=2), encoding="utf-8")

    ask_graph_log = result["ask_graph_log"]
    (OUT_DIR / f"ask_graph_{arm}{sfx}.jsonl").write_text(
        "\n".join(json.dumps(e) for e in ask_graph_log) + "\n", encoding="utf-8")
    ask_summary = run_pilot.compute_ask_graph_summary(ask_graph_log)
    (OUT_DIR / f"ask_graph_summary_{arm}{sfx}.json").write_text(
        json.dumps(ask_summary, indent=2), encoding="utf-8")

    stats = result["run_stats"]
    stats["wall_seconds"] = round(wall_s, 1)
    stats["schema_ok"] = ok
    if not ok:
        stats["schema_errors"] = errors[:20]
    (OUT_DIR / f"run_stats_{arm}{sfx}.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")

    # marker written LAST -- only reached if every write above succeeded
    marker_path(arm, seed).write_text(
        json.dumps({"arm": arm, "seed": seed, "model": model, "wall_seconds": round(wall_s, 1),
                     "schema_ok": ok, "completed_at": datetime.now(timezone.utc).isoformat()}),
        encoding="utf-8")

    # clean up a stale failure marker from an earlier crashed attempt at this
    # same unit, now that it has actually succeeded
    failed_marker = OUT_DIR / f"FAILED_{arm}_seed{seed}.txt"
    if failed_marker.exists():
        failed_marker.unlink()

    gbr = result["grade_belief_report"]
    return {
        "schema_ok": ok,
        "collective_culprit_landed_rate": gbr["collective"]["culprit_landed_rate"],
        "calls_ok": stats["calls_ok"],
        "calls_attempted": stats["calls_attempted"],
        "hard_failures": len(stats["hard_failures"]),
        "wall_seconds": round(wall_s, 1),
    }


def run_one(arm: str, seed: int, rounds: int, backend, model: str) -> None:
    t0 = time.monotonic()
    result = run_pilot.run_arm(arm, seed, rounds, backend, model)
    wall_s = time.monotonic() - t0
    quick = write_arm_seed_outputs(arm, seed, result, wall_s, model)
    log_progress(
        f"DONE arm={arm} seed={seed} wall={quick['wall_seconds']}s "
        f"calls_ok={quick['calls_ok']}/{quick['calls_attempted']} "
        f"hard_failures={quick['hard_failures']} schema_ok={quick['schema_ok']} "
        f"collective_culprit_landed_rate={quick['collective_culprit_landed_rate']:.3f}")
    append_progress_record({"event": "done", "arm": arm, "seed": seed, **quick})


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="llama3.1:8b")
    ap.add_argument("--host", default="http://127.0.0.1:11434/api/chat")
    ap.add_argument("--rounds", type=int, default=run_pilot.domain.ROUNDS_DEFAULT)
    ap.add_argument("--seeds", type=int, nargs="+", default=SEEDS_DEFAULT)
    ap.add_argument("--arms", nargs="+", default=ARMS_DEFAULT)
    args = ap.parse_args()

    OUT_DIR.mkdir(exist_ok=True)
    backend = OllamaBackend(model=args.model, url=args.host, keep_alive="10m")

    total_units = len(args.seeds) * len(args.arms)
    already_done = sum(1 for s in args.seeds for a in args.arms if is_complete(a, s))
    log_progress(f"CONFIRMATORY BATCH START: seeds={args.seeds[0]}..{args.seeds[-1]} "
                 f"({len(args.seeds)} seeds) x arms={args.arms} = {total_units} units, "
                 f"rounds={args.rounds}, model={args.model}, "
                 f"{already_done}/{total_units} already complete on disk (will be skipped)")

    done_count = 0
    skip_count = 0
    fail_count = 0

    # seed-major loop (both arms for a seed before moving to the next seed) --
    # correctness never depends on order (every (arm,seed) unit is independent
    # and checkpointed on its own); seed-major just means a same-seed
    # coordinated-vs-independent comparison becomes available earliest.
    for seed in args.seeds:
        for arm in args.arms:
            if is_complete(arm, seed):
                skip_count += 1
                log_progress(f"SKIP arm={arm} seed={seed} (marker exists, already complete)")
                append_progress_record({"event": "skip", "arm": arm, "seed": seed})
                continue
            try:
                run_one(arm, seed, args.rounds, backend, args.model)
                done_count += 1
            except Exception as e:  # noqa: BLE001 -- one bad seed must never kill the whole batch
                fail_count += 1
                tb = traceback.format_exc()
                log_progress(f"FAIL arm={arm} seed={seed} error={e!r}")
                append_progress_record({"event": "fail", "arm": arm, "seed": seed,
                                          "error": str(e), "traceback": tb})
                (OUT_DIR / f"FAILED_{arm}_seed{seed}.txt").write_text(
                    f"{datetime.now(timezone.utc).isoformat()}\n{e!r}\n\n{tb}", encoding="utf-8")
                continue

    log_progress(f"CONFIRMATORY BATCH END: done={done_count} skipped={skip_count} "
                 f"failed={fail_count} (of {total_units} total units)")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
