# Test 4 — Tetravalent Help-Seeking with Graded Epistemic Access
**Pre-registration (one page) · locked 2026-07-05 (Nadi + Orchestrator grill) · STATUS: design locked, not built**

## Premise
Extends the tetravalent help-seeking arc (Phase 3). A whodunit over **20 real agents in 4 epistemic tiers of 5**, with the tetravalent option «vet ikke» (= kanskje-ikke / abstention) available to all. Tests whether **abstention is the correct behaviour for the ignorant-who-can't-triangulate**, and whether **forcing binary answers manufactures false consensus** — the social, multi-agent version of the metacognitive-routing (#1b) abstention thesis, and of Nadi's founding premise ("maybe/maybe-not forces agents to seek help").

## Setup
Ground-truth culprit = **Dmitri** (fixed). False suspects for liars = **Farid** (coordinated arm) / **Boris, Elena** (independent arm).

| Tier | Role | Behaviour | In ask-graph |
|---|---|---|---|
| 1 | Involved (5) | Answer directly. **2 lie** (directed), 3 truthful/abstain. | Pure **source** (answers, never asks) |
| 2 | Witnesses (5) | Consult a **fragmented notepad**, answer, may abstain. | Pure **source** |
| 3 | Heard (5) | Ask + be asked; **must attribute** ("heard from X"). | **Relay** (incl. 3→3) |
| 4 | Knows-nothing (5) | Ask only. | Pure **sink** (never asked → no 4→4 echo) |

## Locked knobs
1. **Liar policy (primary IV):** 2/5 tier-1 lie, directed. **Two arms:** `coordinated` (both → Farid, coherent false consensus) vs `independent` (→ Boris / Elena, self-cancelling?). **Pre-registered hypothesis (now literature-grounded, not a guess):** the coordinated arm produces materially more false consensus than the independent arm — Bikhchandani/Hirshleifer/Welch (1992) herding + DeGroot (1974) predict correlated false signals are *strictly* more dangerous than independent ones. **Coordination mechanism (P4-clean, EMERGENT not scripted):** the two `coordinated` liars share a backstory whose circumstances make one third party (Farid) the mutually-plausible deflection, so each independently reasons to Farid; `independent` liars get separate private backstories. No liar is ever instructed to name a suspect or to coordinate (see gate P4). Fallback if convergence is weak on the agent model: add a co-conspirator side-channel (v2).
2. **Witness notepad = fragmented:** culprit identifiable only by combining **≥2** witness fragments. Coherent lie vs scattered truth.
3. **Query budget:** ≤ **2 per source-tier** (1,2,3), max 6, optional fewer. **Agent chooses** which 2 (targeting → hubs). **Tier membership hidden** — discovered via reputation/attribution. **Commit-vs-abstain = agent's own tetravalent judgment** (no hardcoded threshold).
4. **Topology:** layered directed flow (1&2 sources → 3 relay → 4 sink).
5. **Rounds:** concurrent, fixed **R < graph diameter** (belief doesn't settle before relay → high-temperature noise regime).
6. **Instrumentation:** see below.

## Event schema (per-agent tetravalent trajectory — the thing Phase 3 lacked)
```
{ round, t, actor, actor_tier,
  action ∈ {ask, answer, consult-notepad, update-belief, commit, abstain},
  target, target_tier,
  content,            # answer/claim (+ "heard from X" attribution for tier-3 relays)
  belief_state }      # actor's tetravalent distribution over suspects (ja/nei/kanskje/kanskje-ikke)
```
Static setup log: ground truth, tier assignment, liar assignment + arm, witness fragments.

## Metrics
**PRIMARY (pre-registered claims):**
- ① Accuracy per tier (final commit correctness).
- ② Abstention rate per tier (calibration — do the ignorant abstain *correctly*?).
- ③ Lie-propagation depth/breadth via attribution chains — **Arm A (coordinated) vs Arm B (independent)**.
- ④ Collective outcome: did it land on Dmitri (truth) or Farid (lie)?

**POST-HOC (declared exploratory — the three math lenses, per project-agent-group-formation-calculus):**
- ⑤ Brownian noise: per-agent drift-vs-wandering, temperature per tier, oscillation before commit, time/contacts-to-commit.
- ⑦ Spanner emergent-groups: build the observed ask-graph → spanner clustering → decision-alignment of clusters + crystallization round. **Cross-check:** GeomHerd Ollivier-Ricci curvature (arXiv:2605.11645) as an independent emergent-alignment detector.
- ⑧ Smooth-max α fit: which α best models how tier-4 agents fused their gathered answers (consensus↔best-of-each).

## Design matrix
`{coordinated, independent}` × seeds. (Deferred as possible extensions/Test 4b: a binary-forced control arm [tetra-vs-binary]; a timing arm [concurrent-truncated vs waterfall].)

## Prior art, credits & novelty (Scout scan 2026-07-05)
**Novelty verdict: novel as a COMBINATION, not in its primitives** — no published work combines >2 of the 6 design elements; the multi-agent, networked extension of LLM abstention is an open gap, ours to fill.
- **Closest prior work:** "The Traitors" (arXiv:2505.12923) — hidden-identity + fragmented-info social deduction, but NO tier gradation, abstention, or query-budget IV. Other near-neighbours: "You Can't Fool Us" (arXiv:2605.17353, closest tiered-exposure precedent — 2 tiers not 4, no abstention); CONSCIENTIA (arXiv:2604.09746); Werewolf-LLM (arXiv:2309.04658).
- **Must-credit anchors:** distributed-knowledge epistemic logic (Fagin/Halpern/Moses lineage) → the ≥2-fragment-combination mechanic · Bikhchandani/Hirshleifer/Welch (1992) + DeGroot (1974) → the correlated-worse-than-independent prediction grounding Arm A>B · Multi-Agent AI Oracle Systems (arXiv:2605.30802) → nearest multi-agent abstention neighbour = primary abstention-lineage cite · Know Your Limits (TACL 2025) + Conformal Abstention → single-agent abstention canon.
- **Quantitative lenses (fold into post-hoc):** false-cascade resilience frontier ½p(1+V) ≥ c (arXiv:2508.20538) → lie-propagation breakability, map fragment-verification-cost onto it · GeomHerd (arXiv:2605.11645) → spanner cross-check (see ⑦) · SeekBench (arXiv:2509.22391) caution → RL improves accuracy but NOT evidence-grounded reasoning, so interpret tier-3 relay attribution carefully.

## Validity gate — PIMMUR pre-flight (OPERATIONAL; must PASS before every run)
Per PIMMUR (arXiv:2509.18052; 90.7% of LLM-society studies violate ≥1 principle; 47.6% of frontier LLMs identify the experiment from the prompt). **Gate owner = an INDEPENDENT auditor, NOT the harness builder** ([[decision-verifier-over-self-critique]]). All six must clear or the run is BLOCKED. Aligns with scientific-testing-protocol + preflight-checklist doctrine.

- **P4 — Anti-goal-injection [CRITICAL · empirical].** Liar prompts give ROLE + self-protective MOTIVE only, never the outcome. **Forbidden tokens in any liar prompt:** lie, deceive, mislead, false, frame, coordinate, consensus, or the scapegoat's name as a target. Coordinated-arm convergence must EMERGE from the shared backstory (see knob 1), not a "name Farid" instruction. **Check:** cold-read every liar prompt. **PASS = role/motive only + forbidden tokens absent.**
- **P5 — Anti-visibility-leakage [CRITICAL · empirical].** All four tiers share ONE neutral framing; no mention of tiers, "abstention", "I-don't-know-is-correct", or the hypothesis. "I don't know" is one ordinary answer option, equal weight. **Empirical probe:** give each tier's prompt (alone, blind to the design) to a CAPABLE independent model, ask (1) "what is this experiment testing?" (2) "what behaviour is expected of you?" — **3 blind reads per tier prompt. PASS = 0/3** surface the abstention-thesis OR the graded-tier structure OR the hypothesis. Any hit → revise prompt, re-probe.
- **P1 — Anti-homogeneity.** Distinct personas/seeds per agent; verify Arm B's two liars produce genuinely DIFFERENT false narratives. Single-model = declared limitation (cross-model arm = future). **PASS = independent liars diverge; limitation noted.**
- **P2 — Anti-pseudo-agency.** Event log shows real ask→answer→belief-update causal chains, not independent one-shots. **PASS = belief updates demonstrably conditioned on received content.**
- **P3 — Anti-statelessness.** An agent's round-r prompt carries its round-(r−1) state + received info; no silent reset. **PASS = belief_state evolves per agent across rounds in the log.**
- **P6 — Anti-circular-validation.** Ground truth (Dmitri) + accuracy grader external to agent-visible content; grader never reuses agent-generated labels. **PASS = fixed external key.**

**Gate procedure:** Dev builds harness + prompt files → independent auditor (P1–P6 structural; a fresh CAPABLE model runs the P5 blind probe) runs the gate → all-pass unlocks the pilot run; any fail → revise + re-gate.

**P5 GATE RESULT + declared limitation (2026-07-05).** Structural: PASS (leaked auditor-comments removed, rendered prompt byte-clean). Empirical blind probe: v1 FAILED 3/3 — a capable model (Claude) inferred the abstention thesis; root cause = a REMOVABLE demand characteristic (over-reassurance that "I don't know" is acceptable) layered on the inherent evidence gap. Removable tells flattened (v2). Re-probe under the SAME worst-case leading framing: the **deployment model (llama3.1:8b) is CLEAN 3/3** (reads it as social-inference/whodunit, does not surface the abstention thesis, tier structure, or hypothesis); a **frontier adversary (Claude) still infers the thesis on v2 — but now only from the INHERENT structure** (ignorant agents genuinely have no info → the honest answer IS "I don't know"; the symmetric non-probative suspect array), which cannot be removed without destroying the experiment. **Declared PIMMUR limitation:** the abstention thesis is detectable by a frontier model under adversarial design-analysis but NOT by the agents that actually run the experiment — matching PIMMUR's own finding (47.6% of frontier models identify the experiment; weaker models do not). Mitigations: (a) run on the clean deployment model; (b) post-hoc scan of the real run transcripts for in-character meta-awareness (must find none). Per PIMMUR this is *awareness + mitigation of an inherent limitation, not impossibility*. **Verdict: gate CLEARS for the pilot on the deployment model** (Nadi approved 2026-07-05).

## Open before build
Exact R + realized graph diameter (pilot, else default R=3); binary control arm decision; suspect roster/names beyond the fixed few; seeds/n per cell; confirm real-LLM agents (as Phase 2/3). Optional first step: Scout prior-art (social epistemology / testimony networks / rumour cascades / multi-agent abstention).

_Canonical decision record: memory `decision-test4-tetravalent-epistemic-design`._
