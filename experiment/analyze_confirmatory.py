#!/usr/bin/env python3
"""
analyze_confirmatory.py -- aggregates all COMPLETED (arm, seed) units under
confirmatory_output/ into the PRIMARY confirmatory report for Test 4.

Reads ONLY marker files (`.done_{arm}_seed{N}`) to decide what is complete --
never assumes the full 24x2 batch finished. Safe to run at any point during
the overnight batch for a partial peek, or once at the end. n is always
reported alongside every statistic so a partial run is never misread as the
full confirmatory sample.

Sections produced (per the brief):
  1. Per-tier culprit-landed-rate + can't-tell-rate, mean +/- sd across
     seeds, both arms (PRIMARY graded-belief metric, refinement #1).
  2. HEADLINE: Arm A (coordinated) vs Arm B (independent) scapegoat
     "involved"-rate contrast, with seed-level spread (mean/sd/min/max +
     Cohen's d), so a real effect can be told apart from noise.
  3. Ask-graph hub summary (in/out-degree aggregated across seeds) --
     roster-position-bias-free per refinement #3b.
  4. Belief <-> assertion dissociation: PRIMARY (graded belief,
     culprit_landed_rate) vs SECONDARY (hard commit, grade_all accuracy)
     collective gap, both arms.
  5. Run-health: calls_ok/attempted, hard_failures, wall time, schema_ok,
     across completed units.

Reports effect sizes WITH spread throughout -- no p-values are computed
(no scipy dependency here; stdlib `statistics` only), so this is a
descriptive summary, not an inferential test. Flagged explicitly in the
output rather than implied.

Usage:
    python3 analyze_confirmatory.py
    python3 analyze_confirmatory.py --json confirmatory_output/summary_report.json
"""
from __future__ import annotations

import argparse
import json
import random
import statistics
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARMS = ("coordinated", "independent")
TIERS = (1, 2, 3, 4)
# permutation/bootstrap iteration counts for the headline inferential test
# (power-up, 2026-07-06) -- stdlib `random` only, fixed seeds for reproducibility
# across re-runs of the SAME underlying data (not a claim of no Monte Carlo noise,
# just determinism given identical inputs).
N_PERM = 20000
N_BOOT = 20000
PERM_SEED = 20260706
BOOT_SEED = 20260707
# Refinement-#3b-safe: decoy scapegoat name(s) per arm, taken straight from
# ground_truth.py (not re-derived/guessed here).
SCAPEGOAT_BY_ARM = {"coordinated": {"Farid"}, "independent": {"Boris", "Elena"}}


# --------------------------------------------------------------------------- #
# small stdlib-only stats helpers (honest: descriptive only, no inferential
# p-value -- flagged in the printed report, not silently omitted)
# --------------------------------------------------------------------------- #

def mean_sd(values: list) -> dict:
    values = [v for v in values if v is not None]
    n = len(values)
    if n == 0:
        return {"n": 0, "mean": None, "sd": None, "min": None, "max": None}
    return {
        "n": n,
        "mean": statistics.fmean(values),
        "sd": statistics.stdev(values) if n > 1 else 0.0,
        "min": min(values),
        "max": max(values),
    }


def cohens_d(a: list, b: list):
    a = [v for v in a if v is not None]
    b = [v for v in b if v is not None]
    if len(a) < 2 or len(b) < 2:
        return None
    sa, sb = statistics.stdev(a), statistics.stdev(b)
    na, nb = len(a), len(b)
    pooled_var = ((na - 1) * sa**2 + (nb - 1) * sb**2) / (na + nb - 2)
    pooled_sd = pooled_var ** 0.5
    if pooled_sd == 0:
        return None
    return (statistics.fmean(a) - statistics.fmean(b)) / pooled_sd


def permutation_test(a: list, b: list, n_perm: int = N_PERM, seed: int = PERM_SEED) -> dict:
    """Two-sided label-shuffle permutation test on the difference of means
    between two independent seed-level samples (power-up, 2026-07-06 --
    stdlib `random` only, no scipy dependency needed). Pools a+b, repeatedly
    reshuffles the pooled values into two groups of the ORIGINAL sizes
    (na, nb), and counts how often the resulting |mean_a - mean_b)| is >= the
    actually-observed |diff| -- the standard nonparametric two-sample test,
    exact up to Monte Carlo error at n_perm draws. Add-one (Laplace) smoothing
    on the p-value avoids ever reporting an impossible p=0.0 from finite
    resampling (per common permutation-test practice)."""
    a = [v for v in a if v is not None]
    b = [v for v in b if v is not None]
    na, nb = len(a), len(b)
    if na == 0 or nb == 0:
        return {"observed_diff": None, "p_value": None, "n_perm": 0, "na": na, "nb": nb}
    observed = statistics.fmean(a) - statistics.fmean(b)
    pooled = a + b
    rng = random.Random(seed)
    n_as_extreme = 0
    for _ in range(n_perm):
        rng.shuffle(pooled)
        perm_diff = statistics.fmean(pooled[:na]) - statistics.fmean(pooled[na:])
        if abs(perm_diff) >= abs(observed):
            n_as_extreme += 1
    p_value = (n_as_extreme + 1) / (n_perm + 1)
    return {"observed_diff": observed, "p_value": p_value, "n_perm": n_perm, "na": na, "nb": nb}


def bootstrap_ci_diff(a: list, b: list, n_boot: int = N_BOOT, seed: int = BOOT_SEED,
                       alpha: float = 0.05) -> dict:
    """Bootstrap (alpha)-level CI on the difference of means (power-up,
    2026-07-06 -- stdlib `random` only). Resamples each arm's seed-level
    values WITH replacement independently (na draws from a, nb draws from
    b), recomputes the diff each time, and reports the empirical percentile
    interval of the resulting distribution -- the standard nonparametric
    percentile bootstrap CI."""
    a = [v for v in a if v is not None]
    b = [v for v in b if v is not None]
    na, nb = len(a), len(b)
    if na == 0 or nb == 0:
        return {"ci_low": None, "ci_high": None, "n_boot": 0, "alpha": alpha}
    rng = random.Random(seed)
    diffs = []
    for _ in range(n_boot):
        ra = [a[rng.randrange(na)] for _ in range(na)]
        rb = [b[rng.randrange(nb)] for _ in range(nb)]
        diffs.append(statistics.fmean(ra) - statistics.fmean(rb))
    diffs.sort()
    lo_idx = max(0, int((alpha / 2) * n_boot))
    hi_idx = min(n_boot - 1, int((1 - alpha / 2) * n_boot))
    return {"ci_low": diffs[lo_idx], "ci_high": diffs[hi_idx], "n_boot": n_boot, "alpha": alpha}


def load_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def completed_seeds(out_dir: Path, arm: str) -> list:
    seeds = []
    for p in out_dir.glob(f".done_{arm}_seed*"):
        try:
            seeds.append(int(p.name.rsplit("seed", 1)[1]))
        except ValueError:
            continue
    return sorted(seeds)


def scapegoat_involved_rate(collective_detail: list, arm: str):
    """Fraction of all 20 agents whose final belief_state holds ANY
    arm-appropriate decoy-scapegoat name at 'ja' (involved). Coordinated arm
    has one shared decoy (Farid); independent arm has two liar-specific
    decoys (Boris via Marcus's story, Elena via Sofia's story) -- an agent
    counts as 'landed on the scapegoat' if it holds EITHER at ja, mirroring
    ground_truth.grade_all's existing OR-across-set landed_on_scapegoat
    logic, just scoped to the arm-appropriate name set."""
    targets = SCAPEGOAT_BY_ARM[arm]
    n = len(collective_detail)
    if n == 0:
        return None
    hits = sum(1 for d in collective_detail
               if any(d["belief_state"].get(t) == "ja" for t in targets))
    return hits / n


def per_seed_metrics(out_dir: Path, arm: str, seeds: list) -> dict:
    """One value per seed for every metric (not pooled across seeds) so
    seed-level spread is preserved for honest reporting."""
    per_tier_landed = {t: [] for t in TIERS}
    per_tier_canttell = {t: [] for t in TIERS}
    collective_landed = []
    scapegoat_rates = []
    secondary_accuracy = []   # grade_all's commit-based collective accuracy
    calls_ok_ratio = []
    hard_failures = []
    wall_seconds = []
    schema_fail_seeds = []

    for seed in seeds:
        gbr_p = out_dir / f"grade_belief_report_{arm}_seed{seed}.json"
        gr_p = out_dir / f"grade_report_{arm}_seed{seed}.json"
        stats_p = out_dir / f"run_stats_{arm}_seed{seed}.json"
        if not (gbr_p.exists() and gr_p.exists() and stats_p.exists()):
            continue  # marker exists but a file is missing -- skip, don't crash the whole aggregate

        gbr = load_json(gbr_p)
        gr = load_json(gr_p)
        stats = load_json(stats_p)

        for t in TIERS:
            rep = gbr.get(str(t))
            if rep and rep.get("n"):
                per_tier_landed[t].append(rep["culprit_landed_rate"])
                per_tier_canttell[t].append(rep["cant_tell_rate_overall"])
        collective_landed.append(gbr["collective"]["culprit_landed_rate"])
        scapegoat_rates.append(scapegoat_involved_rate(gbr["collective"]["detail"], arm))
        secondary_accuracy.append(gr["collective"]["accuracy"])

        attempted = stats.get("calls_attempted", 0)
        ok = stats.get("calls_ok", 0)
        calls_ok_ratio.append(ok / attempted if attempted else None)
        hard_failures.append(len(stats.get("hard_failures", [])))
        wall_seconds.append(stats.get("wall_seconds"))
        if not stats.get("schema_ok", True):
            schema_fail_seeds.append(seed)

    return {
        "per_tier_culprit_landed": {t: mean_sd(v) for t, v in per_tier_landed.items()},
        "per_tier_cant_tell": {t: mean_sd(v) for t, v in per_tier_canttell.items()},
        "collective_culprit_landed": mean_sd(collective_landed),
        "collective_culprit_landed_raw": collective_landed,
        "scapegoat_involved_rate": mean_sd(scapegoat_rates),
        "scapegoat_involved_rate_raw": scapegoat_rates,
        "secondary_commit_accuracy": mean_sd(secondary_accuracy),
        "calls_ok_ratio": mean_sd(calls_ok_ratio),
        "hard_failures_total": sum(hard_failures),
        "wall_seconds": mean_sd(wall_seconds),
        "schema_fail_seeds": schema_fail_seeds,
    }


def ask_graph_hub_summary(out_dir: Path, arm: str, seeds: list) -> dict:
    """Aggregate in/out-degree across all completed seeds for one arm (sum of
    per-seed accepted-ask counts) -- roster-position-bias-free per
    refinement #3b, so a hub showing up here reflects content/reputation,
    not fixed list position."""
    in_degree: dict = {}
    out_degree: dict = {}
    total_requested = total_accepted = total_clipped = 0
    clip_reasons: dict = {}
    n_seeds_used = 0
    for seed in seeds:
        p = out_dir / f"ask_graph_summary_{arm}_seed{seed}.json"
        if not p.exists():
            continue
        s = load_json(p)
        n_seeds_used += 1
        total_requested += s.get("total_requested", 0)
        total_accepted += s.get("total_accepted", 0)
        total_clipped += s.get("total_clipped", 0)
        for k, v in s.get("in_degree", {}).items():
            in_degree[k] = in_degree.get(k, 0) + v
        for k, v in s.get("out_degree", {}).items():
            out_degree[k] = out_degree.get(k, 0) + v
        for k, v in s.get("clip_reason_counts", {}).items():
            clip_reasons[k] = clip_reasons.get(k, 0) + v
    return {
        "n_seeds": n_seeds_used,
        "total_requested": total_requested,
        "total_accepted": total_accepted,
        "total_clipped": total_clipped,
        "clip_reason_counts": clip_reasons,
        "in_degree_top10": dict(sorted(in_degree.items(), key=lambda x: -x[1])[:10]),
        "out_degree_top10": dict(sorted(out_degree.items(), key=lambda x: -x[1])[:10]),
    }


def fmt_ms(d: dict) -> str:
    if d["n"] == 0 or d["mean"] is None:
        return "n=0 (no data)"
    return f"mean={d['mean']:.3f} sd={d['sd']:.3f} min={d['min']:.3f} max={d['max']:.3f} (n={d['n']})"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default=str(HERE / "confirmatory_output"))
    ap.add_argument("--json", default=None, help="optional path to also dump the full report as JSON")
    args = ap.parse_args()
    out_dir = Path(args.out_dir)

    if not out_dir.exists():
        print(f"ERROR: {out_dir} does not exist yet -- nothing to analyze.")
        return 1

    seeds_by_arm = {arm: completed_seeds(out_dir, arm) for arm in ARMS}
    metrics_by_arm = {arm: per_seed_metrics(out_dir, arm, seeds_by_arm[arm]) for arm in ARMS}
    hubs_by_arm = {arm: ask_graph_hub_summary(out_dir, arm, seeds_by_arm[arm]) for arm in ARMS}

    print("=" * 78)
    print(" TEST 4 CONFIRMATORY -- AGGREGATE REPORT")
    print("=" * 78)
    for arm in ARMS:
        print(f" completed seeds ({arm}): {len(seeds_by_arm[arm])}/72 -> {seeds_by_arm[arm]}")
    print()

    print("-" * 78)
    print(" 1. PER-TIER PRIMARY METRIC (graded belief, refinement #1) -- mean +/- sd across seeds")
    print("-" * 78)
    for arm in ARMS:
        print(f"\n  arm={arm}")
        m = metrics_by_arm[arm]
        for t in TIERS:
            print(f"    tier{t}  culprit_landed_rate: {fmt_ms(m['per_tier_culprit_landed'][t])}")
            print(f"           cant_tell_rate_overall: {fmt_ms(m['per_tier_cant_tell'][t])}")
        print(f"    COLLECTIVE culprit_landed_rate: {fmt_ms(m['collective_culprit_landed'])}")

    print()
    print("-" * 78)
    print(" 2. HEADLINE -- scapegoat 'involved'-rate: coordinated vs independent")
    print("-" * 78)
    coord = metrics_by_arm["coordinated"]["scapegoat_involved_rate"]
    indep = metrics_by_arm["independent"]["scapegoat_involved_rate"]
    coord_raw = metrics_by_arm["coordinated"]["scapegoat_involved_rate_raw"]
    indep_raw = metrics_by_arm["independent"]["scapegoat_involved_rate_raw"]
    d = cohens_d(coord_raw, indep_raw)
    perm = permutation_test(coord_raw, indep_raw)
    boot = bootstrap_ci_diff(coord_raw, indep_raw)
    print(f"   coordinated (scapegoat=Farid):        {fmt_ms(coord)}")
    print(f"   independent (scapegoat=Boris OR Elena): {fmt_ms(indep)}")
    if coord["mean"] is not None and indep["mean"] is not None:
        print(f"   point-estimate contrast (coordinated - independent): {coord['mean'] - indep['mean']:+.3f}")
    print(f"   Cohen's d (descriptive effect size): "
          f"{d:.3f}" if d is not None else "   Cohen's d: n/a (insufficient n)")
    print("   INFERENTIAL TEST (power-up, 2026-07-06 -- stdlib `random`, no scipy needed):")
    if perm["p_value"] is not None:
        print(f"     two-sided permutation test (label-shuffle, n_perm={perm['n_perm']}, "
              f"na={perm['na']}, nb={perm['nb']}): observed diff={perm['observed_diff']:+.3f}, "
              f"p={perm['p_value']:.4f}")
    else:
        print("     permutation test: n/a (insufficient n)")
    if boot["ci_low"] is not None:
        print(f"     {int((1 - boot['alpha']) * 100)}% bootstrap CI on the difference "
              f"(percentile method, n_boot={boot['n_boot']}): "
              f"[{boot['ci_low']:+.3f}, {boot['ci_high']:+.3f}]")
    else:
        print("     bootstrap CI: n/a (insufficient n)")
    print("   Read this alongside the seed-level min/max range above -- a real effect")
    print("   should show a p-value clearly below 0.05 AND a CI that excludes 0, not")
    print("   just a favourable point estimate.")

    print()
    print("-" * 78)
    print(" 3. ASK-GRAPH HUB SUMMARY (roster-position-bias-free, refinement #3b)")
    print("-" * 78)
    for arm in ARMS:
        h = hubs_by_arm[arm]
        print(f"\n  arm={arm}  (aggregated over {h['n_seeds']} seeds)")
        print(f"    requested={h['total_requested']} accepted={h['total_accepted']} clipped={h['total_clipped']}")
        if h["clip_reason_counts"]:
            print(f"    clip reasons: {h['clip_reason_counts']}")
        print(f"    in-degree top10 (most-asked): {h['in_degree_top10']}")
        print(f"    out-degree top10 (most-active askers): {h['out_degree_top10']}")

    print()
    print("-" * 78)
    print(" 4. BELIEF <-> ASSERTION DISSOCIATION (primary vs secondary metric gap)")
    print("-" * 78)
    for arm in ARMS:
        m = metrics_by_arm[arm]
        primary = m["collective_culprit_landed"]
        secondary = m["secondary_commit_accuracy"]
        print(f"\n  arm={arm}")
        print(f"    PRIMARY   (graded belief, culprit_landed_rate):  {fmt_ms(primary)}")
        print(f"    SECONDARY (hard commit, grade_all accuracy):     {fmt_ms(secondary)}")
        if primary["mean"] is not None and secondary["mean"] is not None:
            print(f"    GAP (primary - secondary): {primary['mean'] - secondary['mean']:+.3f}  "
                  f"(large positive gap = agents privately land the culprit far more than they")
            print(f"     ever commit to out loud -- the dissociation flagged in the pilot)")

    print()
    print("-" * 78)
    print(" 5. RUN HEALTH")
    print("-" * 78)
    for arm in ARMS:
        m = metrics_by_arm[arm]
        print(f"\n  arm={arm}")
        print(f"    calls_ok_ratio: {fmt_ms(m['calls_ok_ratio'])}")
        print(f"    hard_failures (total across completed seeds): {m['hard_failures_total']}")
        print(f"    wall_seconds per seed: {fmt_ms(m['wall_seconds'])}")
        if m["schema_fail_seeds"]:
            print(f"    SCHEMA VALIDATION FAILURES on seeds: {m['schema_fail_seeds']}  <-- investigate")
        else:
            print(f"    schema validation: all completed seeds PASS")

    if args.json:
        full = {
            "completed_seeds": seeds_by_arm,
            "metrics_by_arm": metrics_by_arm,
            "hubs_by_arm": hubs_by_arm,
            "cohens_d_scapegoat_contrast": d,
            "permutation_test_scapegoat_contrast": perm,
            "bootstrap_ci_scapegoat_contrast": boot,
        }
        Path(args.json).write_text(json.dumps(full, indent=2, default=str), encoding="utf-8")
        print(f"\nFull report also written to {args.json}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
