# Prior-Art Deep Pass (OpenReview-native) — Test 4 Paper
## "Graded Epistemic Access and the Belief–Assertion Gap in Multi-Agent Help-Seeking"

**Trigger:** Nadi requested a deeper, OpenReview-native pass before any publication decision, per the draft's own flag ("a deeper OpenReview-native pass is recommended before submission"). Builds on and does not repeat the earlier scan (`2026-07-06_priorart_belief-assertion-dissociation.md`).

**Scope this pass:** OpenReview direct search (ICLR/NeurIPS/ICML/COLM submissions+reviews, incl. rejected/under-review), ACL Anthology, and a targeted hunt for any paper *combining* more than one of the three claimed primitives (tetravalent belief, tiered epistemic access + abstention, networked belief-vs-assertion gap).

---

## VERDICT: GREEN, with one required citation fix (not a novelty issue — an accuracy issue)

No paper found — on OpenReview, ACL Anthology, or elsewhere indexed as of 2026-07-06 — combines more than one of the three claimed primitives:
1. Empirical tetravalent (Belnap-4-shaped: yes/no/maybe/maybe-not) belief in real LLM agents.
2. Tiered epistemic access (structurally-limited single-fragment witnesses vs. triangulating relay) with abstention as a first-class, uniformly-available response.
3. A *networked* (not single-agent) belief-vs-assertion gap measured against a fixed external ground truth.

Every neighbour found — old or new — matches at most **one** of these three, confirming the draft's central novelty claim ("novel on the combination, not any single primitive"). This holds after direct OpenReview querying, which is the gap the first scan admitted (arXiv-recency bias only).

**One thing changed and must be fixed before submission:** the draft's citation of **"You Can't Fool Us," arXiv:2605.17353**, is mischaracterized (see below) — not a novelty problem, a citation-accuracy problem that a reviewer or the paper's own authors could catch.

---

## Re-verification of the must-distinguish neighbours (OpenReview-native check)

| Neighbour | OpenReview status | Verdict on characterization |
|---|---|---|
| **Bayesian Social Deduction with Graph-Informed LMs**, arXiv:2506.17788 | Confirmed on OpenReview: [openreview.net/forum?id=0sUghjXZZs](https://openreview.net/forum?id=0sUghjXZZs) | Characterization holds — continuous Bayesian belief updating in Avalon, no tetravalent states, no fixed external culprit scored for accuracy. Correctly cited as closest *triangulation* analog. |
| **"The Traitors,"** arXiv:2505.12923 | Confirmed on OpenReview: [openreview.net/forum?id=1YjrWLAXJr](https://openreview.net/forum?id=1YjrWLAXJr) | Characterization holds — deception/trust simulation, no tier gradation, no abstention mechanic. |
| **Orgad et al., "LLMs Know More Than They Show,"** ICLR 2025 / arXiv:2410.02707 | Confirmed on OpenReview: [openreview.net/forum?id=KRnsX5Em3W](https://openreview.net/forum?id=KRnsX5Em3W); ICLR 2025 proceedings page: [proceedings.iclr.cc/paper_files/paper/2025/hash/a712d461e57201efe35d429a6f1731c1-Abstract-Conference.html](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a712d461e57201efe35d429a6f1731c1-Abstract-Conference.html) | Characterization holds — single-agent, internal-representation-vs-output discrepancy, mechanistic (hidden states), not multi-agent/behavioral. Correctly positioned as Finding 2's foundational anchor. |
| **"Closing the Confidence–Faithfulness Gap,"** arXiv:2603.25052 | No dedicated OpenReview forum found this pass (appears arXiv-only/journal-track as of 2026-07-06); abstract independently verified via arXiv: [arxiv.org/abs/2603.25052](https://arxiv.org/abs/2603.25052) | Characterization holds — single-agent, mechanistic (linear probes + CAA steering), verbalized confidence orthogonal to calibration, "Reasoning Contamination Effect." Correctly cited as closest single-agent neighbour. |
| **arXiv:2607.02507**, "What LLM Agents Say When No One Is Watching" | **No OpenReview trace found** (searched directly; submitted July 2, 2026 — too recent for any indexed conference review cycle, or under anonymous review not surfaced by non-authenticated search) | Characterization holds — audience/social-pressure-driven public/private divergence in debate, no ground-truth culprit, no tetravalent states, no triangulation-tiering. Still the closest neighbour found in either scan; still needs the distinguishing paragraph the first scan specified. |
| **"You Can't Fool Us,"** arXiv:2605.17353 | Verified verbatim abstract directly via arXiv: [arxiv.org/abs/2605.17353](https://arxiv.org/abs/2605.17353) | **MISCHARACTERIZED in the current draft.** See flag below. |

### Citation-accuracy flag: "You Can't Fool Us" (arXiv:2605.17353)

The draft cites this (References + §3 Discussion) as **"closest tiered-exposure precedent (2 tiers, no abstention)."** The actual, verbatim abstract is:

> "Misinformation resilience is a dynamic community process... We study this process with an LLM-based agent simulation that constructs synthetic communities along two theoretically motivated dimensions: Actively Open-minded Thinking (AOT)... and Political Ideology (PI)... higher AOT improves both resistance to misinformation uptake and recovery... Intervention experiments further show that persuasion and fact checking better support post-peak correction..."

This paper is about **misinformation resilience in AOT/political-ideology-structured communities**, not tiered information exposure, and does not mention abstention. There is no tier structure at all in the actual paper — the "2 tiers, no abstention" description does not match. This looks like either (a) a mix-up with a different, similarly-named or similarly-numbered paper, or (b) a stale/garbled note from an earlier scan that got carried into the draft uncorrected. I could not locate any other paper matching "tiered exposure, 2 tiers, no abstention, misinformation/deception" under this or an adjacent arXiv ID this pass.

**Action needed before submission:** either (1) find and substitute the actually-intended tiered-exposure paper, or (2) drop this citation and rely on "The Traitors" + Bayesian Social Deduction as the social-deduction neighbours, which are independently verified correct. Recommend (2) unless the original scan can recover what paper was actually meant.

---

## New neighbours found this pass (none collide; all distinguishable)

1. **"Who's the Impostor? Multi-Agent Social Deduction for Evaluating LLM Social Reasoning"** — OpenReview: [openreview.net/forum?id=UiUd5LAoq9](https://openreview.net/forum?id=UiUd5LAoq9). 4-player hidden-word game across 90,720 games/9 models/5 modes; defines an "alignment gap" = difference between *strategy alignment* and *collaboration success* (a game-theoretic outcome gap), and finds vote-network centrality predicts influence. **How we differ:** their "alignment gap" is not a belief-vs-assertion dissociation — it's a strategy-vs-outcome mismatch. No tetravalent belief states, no fragmented/tiered epistemic access, no forced-commit-vs-graded-belief measurement. The vote-centrality finding is a nice adjacent-literature citation for "network position matters" (Claim 1) but doesn't test triangulation-driven calibrated abstention.

2. **BEDA: "Belief Estimation as Probabilistic Constraints for Performing Strategic Dialogue Acts"** — arXiv:2512.24885. Estimates an agent's belief *about its interlocutor* to condition dialogue-act generation (adversarial/alignment acts) in Keeper-Burglar, Mutual Friends, CaSiNo settings. **How we differ:** belief here is instrumental (used to act strategically toward another agent), not a graded self-report measured against a forced hard-commit; no tiered epistemic-access network; task-success metric, not calibration/abstention metric.

3. **"Counterfactual Graph for Multi-Agent LLM Calibration" (CAGE-CAL)** — arXiv:2605.30653. Shows that post-communication agent agreement in a graph can reflect *correlated failure* rather than reliable consensus, and calibrates confidence via a counterfactual no-communication graph comparison. **How we differ:** this is the closest 2026 neighbour to our Claim 3 territory (communication topology → false consensus / miscalibration) — worth adding as a citation reinforcing the coordination-effect literature — but it operates on QA-benchmark vote-share/topology selection, not a whodunit with liars, no tetravalent states, no belief-vs-assertion gap. Recommend citing alongside Bikhchandani/DeGroot in §3.

4. **"Social Dynamics as Critical Vulnerabilities that Undermine Objective Decision-Making in LLM Collectives"** — ACL 2026 ([aclanthology.org/2026.acl-long.1756](https://aclanthology.org/2026.acl-long.1756/)), arXiv:2604.06091. A single representative agent's decision is swayed by peer social pressure (conformity, perceived expertise, dominant-speaker effect, rhetorical persuasion). **How we differ:** single agent under peer pressure, not a networked tiered-access system; no tetravalent belief; no forced-commit-vs-belief measurement. Adjacent background for the "pressure-driven divergence" contrast already drawn against arXiv:2607.02507 in the draft — could be added to the same distinguishing paragraph as a second pressure-driven example.

5. **"Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement"** — arXiv:2606.27409. Pure theory/spectral-graph paper (grounded Laplacian, inverse-golden-ratio instability threshold) modeling belief-cascade stability under delayed verification. **How we differ:** formal dynamical-systems model, no empirical LLM agents at all, no ground-truth whodunit, no tetravalent states. Genre mismatch, not a collision; not necessary to cite.

6. **"Every Response Counts: Quantifying Uncertainty of LLM-based Multi-Agent Systems through Tensor Decomposition" (MATU)** — ACL 2026 ([aclanthology.org/2026.acl-long.737](https://aclanthology.org/2026.acl-long.737.pdf)), arXiv:2604.08708. Tensor-decomposition uncertainty quantification over multi-step reasoning trajectories in task-solving MAS. **How we differ:** a UQ *method* paper for task-accuracy pipelines, not a social-epistemics/whodunit study; no tetravalent belief, no tiered access, no forced-commit gap. Not necessary to cite.

7. **"When Planning Fails Despite Correct Execution: On Epistemic Calibration for LLM-Based Multi-Agent Systems"** — arXiv:2605.23414. Epistemic miscalibration in *plan feasibility judgment* (EPC-AW framework). **How we differ:** planning-feasibility domain, not belief-vs-assertion or social deduction; no relevance to any of our three claims beyond sharing the word "epistemic calibration." Not necessary to cite.

None of 1–7 combines more than one of the three primitives. None is a collision.

---

## Ready-to-paste Related Work distinguishing paragraph (drop-in addition/replacement)

Insert into §3 Discussion, after the existing "Finding 1 vs. the abstention canon" paragraph, or fold the "You Can't Fool Us" fix directly into the existing sentence:

> To our knowledge no prior multi-agent abstention study (including the closest social-deduction precedents — "The Traitors," arXiv:2505.12923, and "Bayesian Social Deduction with Graph-Informed Language Models," arXiv:2506.17788) combines graded epistemic tiers, a triangulation requirement, and free tetravalent abstention in one design; this is the novel combination, not any single primitive in isolation. A recent benchmark, "Who's the Impostor?" (multi-agent social deduction, OpenReview id UiUd5LAoq9), reports a distinct "alignment gap" (strategy-alignment vs. collaboration-success mismatch) driven by vote-network centrality — an outcome-level gap, not a belief-vs-assertion dissociation, though it independently supports the general claim that network position shapes multi-agent outcomes (our Finding 1). On the coordination-effect side (Finding 3), "Counterfactual Graph for Multi-Agent LLM Calibration" (arXiv:2605.30653) independently shows that post-communication agreement in a graph can reflect correlated failure rather than reliable consensus — a same-family 2026 result obtained via counterfactual topology comparison on QA benchmarks, reinforcing rather than anticipating our finding that coordinated (correlated) falsehood manufactures more false consensus than independent falsehood in a whodunit setting.

**Also recommend:** remove or replace the "You Can't Fool Us," arXiv:2605.17353 citation — verified this pass to not match its claimed characterization ("2 tiers, no abstention"); the actual paper is about misinformation resilience via AOT/political-ideology traits, with no tier structure and no abstention mechanic. If no correct tiered-exposure paper can be recovered, drop the citation and rely on "The Traitors" + Bayesian Social Deduction, both independently re-verified this pass.

---

## Residual coverage gaps (explicit, do not overstate certainty)

1. **No native OpenReview API/account access** — searches were Google-indexed `site:openreview.net` web queries, not OpenReview's own search/API. Anonymous double-blind submissions under generic titles, or very recent submissions not yet Google-indexed, could be invisible to this method. This is a real gap for "under-review, not-yet-public" papers specifically.
2. **No native Google Scholar access** (unchanged from the first scan) — arXiv/web-indexed search remains the substitute.
3. **No dedicated COLM 2026 proceedings sweep** — general ACL/OpenReview queries surfaced ACL 2026 and ICLR 2026 hits but did not specifically crawl COLM's own site or program; a COLM-specific pass is not done.
4. **NeurIPS 2026** is still pre-proceedings (December 2026 conference) — anything under review there is not indexed publicly by design; cannot be checked by this method at all until decisions/proceedings post.
5. **Workshop coverage is incidental, not systematic** — one AAAI-2026-bridge workshop (WMAC) surfaced by chance; no targeted sweep of NeurIPS/ICML/ICLR 2026 workshop tracks on multi-agent deception/social-epistemics was performed.
6. **Session rate-limited twice by the local circuit breaker** (WebSearch tripped at >8 calls/60s), capping total distinct queries this pass to roughly 20; this is a tooling constraint, not a claim that all reasonable phrasings were exhausted. If Nadi wants a fully exhaustive sweep, budget for a second, more paced pass.
7. **Search window** = whatever is indexed as of 2026-07-06; anything published in the days immediately before or after this date may not yet be surfaced.

---

## Bottom line for Nadi

GREEN stands. The three-way combination is still unmatched anywhere I could search, including OpenReview directly. The one real action item is fixing the "You Can't Fool Us" citation — that's a correctness fix a careful reviewer (or co-author) would flag, independent of novelty. Everything else found this pass is citable-but-distinguishable background, already covered by the drop-in paragraph above.
