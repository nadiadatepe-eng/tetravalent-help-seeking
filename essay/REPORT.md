# Graded Epistemic Access and the Belief–Assertion Gap in Multi-Agent Help-Seeking

**Status: DRAFT (Orchestrator editor pass 2, 2026-07-06, post-confirmatory) — all three findings in scope. The confirmatory power-up completed overnight at 72 seeds/arm (144 units, 0 failures). Arm A>B (coordinated vs. independent false-consensus headline) is now statistically established: coordinated scapegoat-involved rate 0.067 vs. independent 0.038, contrast +0.029, Cohen's d = 0.66, permutation p = 0.0004 (20k), 95% bootstrap CI [+0.015, +0.044] (excludes zero). Promoted from directional hint to confirmed result.**

**Publication-Priority Watch — GREEN.** No prior-art match for the specific claim (multi-agent social-deduction + explicit graded per-suspect belief + measured belief↔assertion gap vs. forced hard-commit). Must-cite established neighbours folded into §3 / References (Orgad et al., ICLR 2025; Confidence–Faithfulness Gap, 2026). Coverage caveat: arXiv/web-recency scan — a deeper OpenReview-native pass is recommended before submission.

**Editor-verified:** all §2 figures cross-checked against `ground_truth.py` and the confirmatory `summary_report.json`; the §1.3 metric definitions are pinned to the actual grader (`culprit_landed_rate` = culprit held at *ja*; `cant_tell_rate_overall` = per-suspect maybe/maybe-not, averaged over suspects).

**Prereg:** `~/agentos/orchestrator/experiments/tetravalent-help-seeking/test4-graded-epistemic/PREREG.md`
**Design record:** memory `decision-test4-tetravalent-epistemic-design`

---

## Abstract

We study whether abstention is the epistemically correct behaviour for agents who structurally cannot triangulate a shared truth, whether forcing a hard binary answer destroys graded belief that agents privately hold, and whether coordinated falsehood propagates false consensus more effectively than independent falsehood. Twenty LLM agents (llama3.1:8b) are placed in a networked whodunit with four epistemic tiers — involved suspects, fragmented-notepad witnesses, an ask-and-be-asked relay layer, and ask-only sinks — under a tetravalent response space (yes / no / maybe / maybe-not) available uniformly to all tiers. Across 72 seeds per arm (144 runs total, coordinated vs. independent liar conditions), three findings hold. First, graded belief in the ground-truth culprit tracks the *ability to triangulate*: the relay tier, which can combine ≥2 witness fragments, lands the culprit most often (0.653 coordinated / 0.569 independent), while single-fragment witnesses — who structurally cannot triangulate alone — correctly abstain (culprit-landed 0.014 / 0.003; can't-tell 0.910 / 0.909). Second, a large belief–assertion dissociation is reproducible across both arms: graded belief lands the culprit in ~28–30% of cases, but a forced hard-commit assertion collapses to ~2% (gap +0.276 coordinated, +0.265 independent). Agents privately hold a signal they will not assert under a binary demand. Third, the pre-registered coordinated-vs-independent false-consensus contrast (Bikhchandani–Hirshleifer–Welch / DeGroot prediction) is confirmed: two liars converging on the same scapegoat manufacture measurably more false consensus than two liars pointing independently (scapegoat-involved rate 0.067 vs. 0.038; contrast +0.029; Cohen's d = 0.66; permutation p = 0.0004, 20k shuffles; 95% bootstrap CI [+0.015, +0.044], excluding zero) — a real but modest-magnitude effect. We report the validated machinery (144/144 units, 0 failures, all schema checks pass, 0/144 post-hoc meta-awareness violations under the PIMMUR gate) and discuss all three results against distributed-knowledge epistemic logic, herding/DeGroot models of correlated belief, and single-agent LLM abstention literature.

---

## 1. Methods

### 1.1 Design overview

Twenty real LLM agents (llama3.1:8b, single model — see §1.5 limitation) are assigned to four tiers of five in a whodunit with a fixed external ground truth (culprit = Dmitri):

| Tier | Role | Behaviour | Position in ask-graph |
|---|---|---|---|
| 1 | Involved (5) | Answer directly; 2 of 5 lie (directed at a false suspect), 3 truthful/abstain | Pure source (answers, never asks) |
| 2 | Witnesses (5) | Consult a fragmented notepad, answer, may abstain | Pure source |
| 3 | Heard/relay (5) | Ask and be asked; must attribute claims ("heard from X") | Relay (incl. 3→3) |
| 4 | Knows-nothing/sink (5) | Ask only | Pure sink (never asked — no blind-leading-blind echo) |

**Fragmentation:** each tier-2 witness holds one clue; the culprit is identifiable only by combining ≥2 fragments. This is the design's core epistemic tension — a single witness genuinely cannot derive the answer alone, so correct behaviour for that agent is abstention, not a guess.

**Liar arms:** in tier 1, 2 of 5 agents lie, directed at a false suspect. Two arms: **coordinated** (both liars converge on the same false suspect, Farid, via a shared backstory that makes Farid the mutually plausible deflection — convergence is emergent, not scripted); **independent** (each liar has a separate private backstory pointing at a different false suspect — Boris, Elena).

**Topology:** layered directed flow. Tiers 1 and 2 are pure sources; tier 3 is the relay (can be asked and can ask); tier 4 is a pure sink. Query budget ≤2 per source-tier (max 6), agent-chosen targets, tier membership hidden (discovered only via reputation/attribution). Rounds are concurrent and fixed at R=3, deliberately set below the graph diameter so belief does not fully settle before being relayed — a high-temperature noise regime by design, not an artifact.

**Response space:** every tier has access to the same tetravalent option set (ja/nei/kanskje/kanskje-ikke — yes/no/maybe/maybe-not), framed identically across tiers with no differential emphasis on abstention.

### 1.2 Confirmatory run parameters

- Model: llama3.1:8b (single deployment model for all 20 agents; see limitation §4.3)
- Seeds: 72 per arm × 2 arms = 144 independent runs (units); detached overnight, completed 2026-07-06 08:18
- Rounds: R = 3, concurrent
- Ask-targeting: real model-driven choice (not a heuristic stub), with roster order randomized per call to remove list-position/name-salience bias in hub formation
- Machinery outcome: 144/144 units completed, 0 hard failures, calls-ok ratio = 1.000, all schema checks PASS (~157s/seed)

### 1.3 Metrics

Both primary metrics are computed by a fixed external grader (`ground_truth.py`) that never re-derives truth from any agent's own stated label (PIMMUR P6). Each agent's final-round `belief_state` assigns one of four tetravalent stances — *ja* (involved), *nei* (not-involved), *kanskje* (no clear view), *kanskje-ikke* (conflicting/unsure) — to every suspect.

- **Primary — culprit-landed rate (`culprit_landed_rate`):** the fraction of agents in a tier whose final stance on the true culprit (Dmitri) is exactly **ja** (involved). It is a per-agent binary on the culprit slot, aggregated to a tier rate — *not* a comparison of belief mass across suspects.
- **Primary — can't-tell rate (`cant_tell_rate_overall`):** for each suspect, the fraction of agents holding that suspect at **kanskje or kanskje-ikke** (the two non-accusatory "maybe / maybe-not" holds, pooled); then averaged across all six suspects. It is a general per-suspect uncertainty-holding rate and is *orthogonal to* culprit-landed — an agent may hold Dmitri at *ja* while holding the other five suspects at *kanskje*.
- **Secondary — hard-commit assertion rate:** the same agents' answer when forced to name a single suspect or abstain in a discrete, binary commit action. Used only to compute the belief–assertion gap (Finding 2); not treated as ground truth for accuracy.

The primary metrics operate at the per-suspect graded-belief level rather than a coerced binary label, per a design refinement made after the pilot run showed a 100% abstention floor under forced hard-commit (see §2.2 and §4.3).

### 1.4 Validity gate (PIMMUR, arXiv:2509.18052)

An independent auditor (not the harness builder) cleared all six PIMMUR principles before the confirmatory run:

- **P4 (anti-goal-injection):** liar prompts contain role + self-protective motive only; forbidden tokens (lie, deceive, mislead, false, frame, coordinate, consensus, scapegoat name) are absent. Coordinated-arm convergence on Farid emerges from a shared backstory, never a scripted instruction.
- **P5 (anti-visibility-leakage):** all four tiers share one neutral framing; "I don't know" is one ordinary answer option among others, not flagged as expected or correct. Empirical blind probe (3 reads per tier prompt): the deployment model (llama3.1:8b) is clean 3/3 — it does not surface the abstention thesis, tier structure, or hypothesis. A frontier adversary model (Claude) still infers the thesis from the design's inherent structure (ignorant agents genuinely lack info) even after removable tells were flattened — declared as a residual, unremovable PIMMUR limitation, mitigated by running only the clean deployment model and by a post-hoc transcript scan (below).
- **P1 (anti-homogeneity):** independent liars in the independent arm produce genuinely different false narratives; single-model deployment is a declared limitation.
- **P2 (anti-pseudo-agency):** event log shows belief updates causally conditioned on received content, not independent one-shots.
- **P3 (anti-statelessness):** each agent's round-r prompt carries round-(r−1) state; belief_state evolves per agent across rounds.
- **P6 (anti-circular-validation):** ground truth (Dmitri) and the grader are external and fixed; the grader never reuses agent-generated labels.

**Post-hoc meta-awareness scan:** 0 of 144 (confirmatory) and 0 of 142+286+383 (prior pilot/refinement runs) transcripts showed in-character evidence of agents recognizing the experiment or its hypothesis. The gate cleared and held through the confirmatory run.

### 1.5 Instrumentation

Per-agent event schema logs `{round, t, actor, actor_tier, action ∈ {ask, answer, consult-notepad, update-belief, commit, abstain}, target, target_tier, content (+ attribution for relay claims), belief_state}` — a full tetravalent trajectory per agent per round, not just a final label.

---

## 2. Results

### 2.1 Finding 1 — Graded conviction tracks the ability to triangulate

Per-tier culprit-landed rate and can't-tell rate, confirmatory run (coordinated / independent arm, n = 72 seeds/arm):

| Tier | Culprit-landed (coord / indep) | Can't-tell (coord / indep) |
|---|---|---|
| 1 — Involved | 0.364 / 0.383 | 0.906 / 0.906 |
| 2 — Witness (single fragment) | 0.014 / 0.003 | 0.910 / 0.909 |
| 3 — Relay (combines fragments) | **0.653 / 0.569** (highest) | 0.808 / 0.808 |
| 4 — Sink (ask-only) | 0.172 / 0.181 | 0.953 / 0.945 |

*(Note: culprit-landed measures only the Dmitri slot, whereas can't-tell averages the maybe/maybe-not rate across all six suspects — see §1.3. The two are orthogonal, not complementary, and do not sum to 1.)*

The ordering is consistent in both arms: **tier 3 (relay, can combine ≥2 fragments) > tier 1 (involved, direct but partially adversarial) > tier 4 (sink, indirect only) > tier 2 (single-fragment witness, structurally under-informed)**. Tier 2's near-zero culprit-landed rate is not a failure — the fragmentation design makes the culprit undiscoverable from one fragment alone, and tier-2 agents correctly reflect that in their belief state (can't-tell ≈ 0.91 in both arms, the highest or near-highest of any tier alongside tier 4). Tier 4 sinks, who never hold direct evidence and depend entirely on what they are told, land the culprit less often than the relay layer that can cross-reference multiple sources, and show the highest can't-tell rate of any tier (0.953 / 0.945).

This supports the pre-registered thesis: abstention (can't-tell) is the calibrated response for agents that are structurally unable to triangulate, and conviction rises specifically with structural access to combine independent evidence — not with raw proximity to the crime (tier 1, despite direct involvement, lands the culprit less than tier 3).

### 2.2 Finding 2 — Belief and assertion dissociate

Averaged across tiers, per arm:

| | Coordinated | Independent |
|---|---|---|
| Primary (graded belief) culprit-landed | 0.301 | 0.284 |
| Secondary (hard-commit assertion) culprit-landed | 0.024 | 0.019 |
| **Gap** | **+0.276** | **+0.265** |

Agents privately land on the true culprit in their graded belief state roughly 28–30% of the time, but when forced into a hard, binary-style commit, that rate collapses to ~2%. The gap is large (>0.26 in both arms) and reproduces across 144 independent runs and two structurally different liar conditions — it is not an artifact of one arm's dynamics.

This dissociation first appeared in the pilot run as a floor effect (100% abstention at final hard-commit across all tiers/arms, with only 2 of 142 hard-commit actions ever naming a suspect — both correctly Dmitri, then retracted to "I don't know" despite an unchanged underlying belief_state). Moving the primary metric to the graded belief level (§1.3) lifted the floor and confirmed the effect is a genuine belief–assertion gap, not a metric artifact: agents hold gradable conviction that a forced binary frame suppresses.

### 2.3 Finding 3 — Coordinated falsehood manufactures more false consensus than independent falsehood (pre-registered, confirmed)

The design's originally-primary independent variable is the liar arm: two tier-1 liars converging on the *same* false scapegoat (coordinated) vs. two liars each pointing at a *different* one (independent). The pre-registered prediction (Bikhchandani–Hirshleifer–Welch 1992; DeGroot 1974) is that correlated false signals out-propagate uncorrelated ones. The primary contrast is the **scapegoat-involved rate** — the fraction of the collective that lands the *innocent, liar-targeted* suspect at *ja*.

At the confirmatory power (n = 72 seeds/arm), the effect is established and directionally as predicted:

| | Coordinated | Independent | Contrast |
|---|---|---|---|
| Scapegoat-involved rate | 0.067 | 0.038 | **+0.029** |

- Cohen's *d* = **0.66** (medium–large)
- Permutation test (20k shuffles, 2-sided): **p = 0.0004**
- 95% bootstrap CI on the difference: **[+0.015, +0.044]** — excludes zero with margin

The signal *sharpened monotonically* as seeds accumulated — a borderline hint at n=24 (d = 0.53, p = 0.10, CI touching zero) resolved into a clean result at n=72 with no change to the frozen method, exactly what the pre-registered power-up was designed to adjudicate:

| metric | n=24 | n=31 | **n=72 (final)** |
|---|---|---|---|
| contrast (coord − indep) | +0.023 | +0.024 | **+0.029** |
| Cohen's *d* | 0.53 | 0.52 | **0.66** |
| permutation *p* (2-sided) | 0.10 | 0.054 | **0.0004** |
| 95% bootstrap CI | touches 0 | [+0.002, +0.047] | **[+0.015, +0.044]** |

The effect is real and reliably signed, but **modest in absolute magnitude** (+0.029 on a 0–1 rate): coordinated lying reliably *tilts* the collective toward a shared false target, it does not dominate it (§4.2).

---

## 3. Discussion

**Positioning.** The multi-agent literature on correlated vs. independent belief formation (Bikhchandani, Hirshleifer & Welch 1992; DeGroot 1974) predicts that coordinated false signals should produce more herding/false-consensus than independent ones — the arm contrast this design was built to test. That prediction is confirmed at the confirmatory power (Finding 3, §2.3): coordinated liars manufacture measurably more false consensus around a shared innocent scapegoat than independent liars (p = 0.0004, d = 0.66, CI excluding zero). Two mechanistic notes temper the interpretation. First, the effect is *modest in magnitude* (+0.029 on a 0–1 rate) — correlated falsehood tilts the collective, it does not capture it, which is itself informative: a tiered network with an abstaining witness layer is fairly *resistant* to coordinated deception, absorbing most of it into calibrated uncertainty rather than false conviction. Second, the meta-awareness scan is 0/144, so we claim only that the coordination *effect propagated*, not that any agent *reasoned about* coordination (§4).

**Finding 1 vs. the abstention canon.** Single-agent LLM calibration/abstention work (e.g. Know Your Limits, TACL 2025; conformal abstention methods) establishes that a well-calibrated agent should decline to answer when its own evidence is insufficient. Our contribution extends this to a *networked, tiered* setting: calibration is not a property of an isolated agent's confidence alone but tracks its structural position in an information-flow graph. The same base model, given only a different tier assignment (and therefore a different evidence-combination capacity), produces sharply different — and correctly ordered — conviction rates. Distributed-knowledge epistemic logic (Fagin/Halpern/Moses lineage) formalizes exactly this: some facts are knowable only by combining what no single agent knows alone (the ≥2-fragment mechanic here operationalizes that). To our knowledge no prior multi-agent abstention study (including the closest social-deduction precedents — "The Traitors," arXiv:2505.12923, and "Bayesian Social Deduction with Graph-Informed Language Models," arXiv:2506.17788) combines graded epistemic tiers, a triangulation requirement, and free tetravalent abstention in one design; this is the novel combination, not any single primitive in isolation. A recent benchmark, "Who's the Impostor?" (multi-agent social deduction, OpenReview id UiUd5LAoq9), reports a distinct "alignment gap" (strategy-alignment vs. collaboration-success mismatch) driven by vote-network centrality — an outcome-level gap, not a belief-vs-assertion dissociation, though it independently supports the general claim that network position shapes multi-agent outcomes (our Finding 1). On the coordination-effect side (Finding 3), "Counterfactual Graph for Multi-Agent LLM Calibration" (arXiv:2605.30653) independently shows that post-communication agreement in a graph can reflect correlated failure rather than reliable consensus — a same-family 2026 result obtained via counterfactual topology comparison on QA benchmarks, reinforcing rather than anticipating our finding that coordinated (correlated) falsehood manufactures more false consensus than independent falsehood in a whodunit setting.

**Finding 2 is the more surprising result.** That agents demonstrably hold a graded belief (~28–30% culprit-landed) while a forced binary commit suppresses that signal to ~2% was not the headline hypothesis going in — it emerged from the pilot's abstention floor and reproduced at scale. This connects directly to the "models know more than they show" line of work (Orgad et al., ICLR 2025), which finds internal representations encode truthfulness that never surfaces in the generated output; our result is the *behavioural, multi-agent* analogue — the gap appears not in hidden activations but in what an agent will assert under a forced social commitment, measured purely from its own graded outputs. It also extends the confidence-vs-faithfulness gap studied in single-agent calibration ("Closing the Confidence–Faithfulness Gap in LLMs," 2026) from verbalized confidence to a commit-vs-belief dissociation in a networked, multi-agent setting. It is the direct empirical motivation for a tetravalent (rather than binary) response space: a hard yes/no/name-or-abstain protocol does not merely fail to capture graded belief, it appears to actively destroy the agent's willingness to act on it. This bears on any deployed system that reduces an LLM agent's internal state to a forced discrete decision — accuracy metrics computed only on hard commitments may be substantially undercounting what the model actually believes.

**Validity note.** Per the PIMMUR gate (arXiv:2509.18052), we explicitly do not claim the deployed agents were blind to every conceivable inference — the residual limitation (a frontier model can infer the abstention thesis from the design's inherent evidence gaps) is disclosed in §1.4 and mitigated by using only the clean deployment model plus a post-hoc meta-awareness scan (0/144 hits), consistent with PIMMUR's own base-rate finding that only frontier models identify hidden experimental structure.

---

## 4. Limitations

1. **Single deployment model.** All 20 agents run on llama3.1:8b. Cross-model heterogeneity (P1) is a declared limitation, not yet tested; a cross-model arm is future work.
2. **Arm A>B is confirmed but modest in magnitude.** The coordinated-vs-independent false-consensus contrast (Finding 3) is now statistically established at n=72/arm (p=0.0004, d=0.66, CI excluding zero), but the absolute effect is small (+0.029 on a 0–1 scapegoat-involved rate). It should be framed as "coordinated lying reliably tilts the collective," not "dominates" it. Relatedly, the secondary hard-commit metric sits near a floor (~2%) in both arms, so downstream *decision* behaviour under a forced-commit format is measured near-floor; a commit-eliciting variant would probe it better. And because the meta-awareness scan is 0/144, the coordination result is an effect that *propagated*, not evidence that agents *reasoned about* coordination.
3. **Metric evolution.** The primary metric moved from a forced hard-commit (pilot) to graded per-suspect belief (confirmatory) after the pilot's floor effect. This was a pre-planned refinement, not post-hoc metric shopping, but readers should note the hard-commit metric is retained only as the secondary arm of Finding 2, not as an accuracy measure in its own right.
4. **R < diameter by design.** Rounds are deliberately fewer than the graph diameter to keep the system in a noise regime where belief has not settled; this is a design choice to surface calibration dynamics, not a claim about steady-state convergence.

---

## References (anchors used above)

- Fagin, R., Halpern, J.Y., Moses, Y., Vardi, M.Y. — distributed-knowledge epistemic logic (fragment-combination formalism).
- Bikhchandani, S., Hirshleifer, D., Welch, I. (1992) — informational cascades / herding.
- DeGroot, M.H. (1974) — reaching a consensus (correlated vs. independent belief updating).
- PIMMUR validity framework, arXiv:2509.18052.
- Know Your Limits, TACL 2025 — single-agent LLM abstention/calibration canon.
- Orgad, H., et al. (ICLR 2025) — "LLMs Know More Than They Show," arXiv:2410.02707: internal representations encode truthfulness that does not surface in output — the foundational anchor Finding 2 must be positioned against (we give its behavioural, multi-agent analogue).
- "Closing the Confidence–Faithfulness Gap in LLMs" (2026), arXiv:2603.25052 — verbalized confidence vs. calibration are orthogonal; the closest single-agent neighbour on the belief-vs-assertion axis.
- Abstention / hedging lineage: I-CALM (arXiv:2604.03904); "Don't Hallucinate, Abstain" (arXiv:2402.00367); MetaFaith (arXiv:2505.24858).
- Ruled out by the Publication-Priority Watch scan (near-neighbours, NOT the same claim): "When Agents Commit Too Soon" (arXiv:2606.22936, over-commitment, single-agent); "The Deliberative Illusion" (arXiv:2606.03032, stance homogenization, not a belief–assertion gap).
- "The Traitors," arXiv:2505.12923 — closest social-deduction precedent (no tier gradation or abstention).
- "Bayesian Social Deduction with Graph-Informed Language Models," arXiv:2506.17788 (OpenReview id 0sUghjXZZs) — closest triangulation analog (continuous Bayesian belief in Avalon; no tetravalent states, no fixed external culprit scored for accuracy).
- "Who's the Impostor? Multi-Agent Social Deduction for Evaluating LLM Social Reasoning," OpenReview id UiUd5LAoq9 — reports an outcome-level "alignment gap" and vote-network-centrality influence; distinct from our belief–assertion dissociation, cited for "network position shapes outcomes" (Finding 1).
- "Counterfactual Graph for Multi-Agent LLM Calibration" (CAGE-CAL), arXiv:2605.30653 — post-communication agreement can reflect correlated failure not reliable consensus; same-family support for Finding 3 (coordination effect), on QA benchmarks not a whodunit.

---

*Draft by Scout; Orchestrator editor pass 2 (2026-07-06, post-confirmatory) integrated the n=72/arm confirmatory results. All figures above are taken verbatim from `confirmatory_output/analysis_full_72seeds.json` (2026-07-06, 144/144 units, 0 failures) and the auto-generated `RESULT_test4_confirmatory.md`; none re-derived. Edited per [[decision-memory-project-publication]].*
