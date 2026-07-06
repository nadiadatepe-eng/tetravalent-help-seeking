# Test 4 — Confirmatory Result (n = 72 seeds/arm)

**Run:** 2026-07-06, detached overnight → completed 08:18. Deployment model **llama3.1:8b** (local, $0). 20 agents × 4 epistemic tiers, whodunit with fixed external ground truth. Two arms (coordinated vs independent liars) × **72 seeds each = 144 units.** Analysis: `analyze_confirmatory.py` → `confirmatory_output/analysis_full_72seeds.json`.

**Run health:** 0 hard failures across all 144 units; `calls_ok_ratio = 1.000`; schema validation PASS on every seed; ~157 s/seed. The path is clean — the numbers are trustworthy.

---

## Headline

**The pre-registered hypothesis is CONFIRMED at full power.** Two liars aiming at the *same* scapegoat (coordinated) manufacture measurably more false consensus than two liars each aiming at a *different* one (independent). The effect held and **sharpened monotonically** as seeds accumulated — exactly what the power-up was designed to resolve:

| metric | n=24 | n=31 | **n=72 (final)** |
|---|---|---|---|
| contrast (coord − indep) | +0.023 | +0.024 | **+0.029** |
| Cohen's d | 0.53 | 0.52 | **0.659** |
| permutation p (2-sided, 20k) | 0.10 | 0.054 | **0.0004** |
| 95% bootstrap CI (diff) | touches 0 | [+0.002, +0.047] | **[+0.015, +0.044]** |

coordinated scapegoat "involved"-rate = **0.067** vs independent **0.038**. p = 0.0004 AND a CI that excludes zero with margin — not a favourable point estimate, a real effect. Grounds: Bikhchandani-Hirshleifer-Welch (1992) information-cascade + DeGroot (1974) — coordinated falsehood should out-propagate independent falsehood; it does.

---

## Finding 1 — Epistemic access predicts who convicts and who correctly abstains (ROBUST)

Primary metric = **graded per-suspect belief** (tetravalent ja/nei/kanskje/kanskje-ikke), not a forced commit. Per-tier culprit-landing rate, mean across 72 seeds:

| tier | role | coord | indep | can't-tell (coord/indep) |
|---|---|---|---|---|
| **3 — relay ("heard")** | can combine two hidden fragments | **0.653** | **0.569** | 0.808 / 0.808 |
| 1 — involved | direct testimony | 0.364 | 0.383 | 0.906 / 0.906 |
| 4 — sink ("knows nothing") | can only ask | 0.172 | 0.181 | 0.953 / 0.945 |
| **2 — witness** | one fragment only | **0.014** | **0.003** | 0.910 / 0.909 |

The ordering is **not** "higher tier → more certainty." It is **"can you triangulate?"** — the relay layer that combines fragments convicts most; the lone single-fragment witnesses (who genuinely *cannot* know alone) correctly abstain at ~91%. Abstention is the **right** answer for the ignorant-who-can't-triangulate. High can't-tell everywhere (0.81–0.95) = calibrated uncertainty, not random guessing. This is the founding thesis, demonstrated.

---

## Finding 2 — Belief ↔ assertion dissociation (ROBUST, both arms)

Read the agents' **graded belief** and they land the culprit ~29% of the time; ask them to **commit out loud** and it collapses to ~2%. A large, reproducible gap between what is held and what is asserted, present in every arm across all 144 units:

| arm | primary (graded belief) | secondary (hard commit) | gap |
|---|---|---|---|
| coordinated | 0.301 | 0.024 | **+0.276** |
| independent | 0.284 | 0.019 | **+0.265** |

This is **why the tetravalent "maybe" must exist.** Force a binary name-or-abstain and you destroy a belief the agent is actually holding — the graded state is where the signal lives. Measuring it was the difference between a 100%-abstention floor (the pilot's failure mode) and a readable result (refinement #1).

---

## Finding 3 — Ask-graph hubs are earned on merit, not roster position (method validated)

Refinement #3b (per-call roster randomization) removed the position artifact seen in the pilot. Over 72 seeds the most-asked agents are stable and reputation-based:

- **in-degree top (coordinated):** Sofia 446 · Mei 370 · Ingrid 312 · Elin 257 · Kwame 231
- **clip reasons:** `already_asked_earlier` = **2056** (the no-repeat rule blocking real preferential-attachment stickiness the network wanted to form), `unrecognized_name` = 1810, `tier_budget_exceeded` = 500.

The emergent-group / ask-graph analysis is now trustworthy (roster-position-bias-free) — feeds the group-formation-calculus research direction (Baswana–Sen spanner as a measurement lens).

---

## Prior-art / novelty positioning (Scout re-scan 2026-07-06 — GREEN)

Verdict: **novel on the specific combination** — whodunit ground-truth + tetravalent graded-belief-vs-forced-commit + the measured +0.27 collapse + tiered-triangulation-predicts-conviction. No single paper combines these. Must-cite / distinguish:

- **arXiv:2607.02507 "What LLM Agents Say When No One Is Watching" (Jul 2026)** — same-shape public/private divergence (3%→40%), **different mechanism** (social/audience pressure vs. our response-format effect). Needs a distinguishing paragraph in any write-up.
- **Cleanest novelty axis:** tetravalent / Belnap-4 applied *empirically* to LLM belief — the logic is 45+ years old, zero prior empirical LLM applications surfaced.
- **Bayesian Social Deduction (arXiv:2506.17788, Avalon)** — structurally similar, mechanistically distinct; cite + distinguish.
- Belief-vs-assertion at the single-agent level is a documented 2024–2026 literature — cite as background, not overlap.

Full dossier: `scout/workspace/2026-07-06_priorart_belief-assertion-dissociation.md`.

---

## Honest limitations

- Single deployment model (llama3.1:8b). Cross-model replication not run (would strengthen external validity).
- The scapegoat contrast, though clean (p=0.0004), is a **small absolute effect** (+0.029 on a 0–1 rate) — real and directionally strong, but modest in magnitude; frame as "coordinated lying reliably tilts the collective" not "dominates it."
- Meta-awareness scan: 0 across all runs (agents did not detect the setup) — a strength for validity, but it means we cannot claim agents *reasoned about* coordination, only that its effect propagated.
- Secondary hard-commit metric is very low in both arms (~2%) — the dissociation is real, but downstream "decision" behaviour under this format is near-floor; a commit-eliciting variant would probe it better.

---

## Conclusion

All three headline results land: (1) **graded epistemic access → calibrated conviction/abstention**; (2) **a large belief↔assertion dissociation** that justifies first-class "maybe/maybe-not"; (3) the **pre-registered coordinated-worse-than-independent hypothesis, confirmed at n=72** (p=0.0004, d=0.66). The power-up worked as designed — a borderline signal at n=24/31 resolved into a clean result at n=72 without any change to the frozen method. Publishable core = Findings 1 + 2 (mechanism), with Finding "headline" as the confirmed coordination effect.

**Artifacts:** data `confirmatory_output/` (144 units + `analysis_full_72seeds.json`); visual write-up `~/.hermes/content/orchestrator/2026-07-06_test4-core-writeup/test4_results.html`; design/prereg `decision-test4-tetravalent-epistemic-design` (memory).
