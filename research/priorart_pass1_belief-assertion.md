# Prior-Art Re-Scan — Test 4 Belief↔Assertion Dissociation (Publication-Priority Watch, 2nd pass)

**Trigger:** Nadi green-lit event-triggered Publication-Priority Watch 2026-07-06. This is a targeted re-scan against 4 specific prior-art axes, building on the first scan run earlier the same day (recorded in Scout's `past-findings.md` / `project-scout-tech-watch-patrol.md`).

**Coverage caveat:** No native Google Scholar access; arXiv-indexed web search + direct arXiv/OpenReview fetch used as substitute. Search window: whatever is indexed as of 2026-07-06. One WebFetch summary (arXiv:2603.00142) was caught mid-scan producing a leading/confabulated answer that over-matched my prompt — verified independently against the real abstract and downgraded. Flagging this so the verdict below isn't taken as more certain than a same-day scan supports.

---

## Q1 — Belief vs. assertion / credence vs. stated-answer divergence

**Closest prior work:**
- **"LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations"** — arXiv:2410.02707 (Oct 2024). Internal hidden-state probes detect truthfulness the model's own output contradicts; ~40% average relative gap between internal and external "knowledge." [Link](https://arxiv.org/abs/2410.02707)
- **"Are LLM Decisions Faithful to Verbal Confidence?"** — Wang, Zhou, Devic, Fu, arXiv:2601.07767 (2026). Single-agent: verbalized confidence is only weakly coupled to the actual accept/reject decision the model then makes. [Link](https://arxiv.org/pdf/2601.07767)
- **"Revealing Economic Facts: LLMs Know More Than They Say"** — arXiv:2505.08662 (2025, Bank of England-adjacent authors). Hidden states yield better economic-variable estimates than the model's own text output. [Link](https://arxiv.org/html/2505.08662)
- **"Competing Biases underlie Overconfidence and Underconfidence in LLMs"** — Nature Machine Intelligence, 2026 (10.1038/s42256-026-01217-9). Choice-supportive bias vs. overweighting of contradictory advice; explains hedging/collapse dynamics under pressure. [Link](https://www.nature.com/articles/s42256-026-01217-9)
- **"A Survey on the Honesty of Large Language Models"** — arXiv:2409.18786. Umbrella survey framing the whole "models know more than they say" literature. [Link](https://arxiv.org/pdf/2409.18786)

**Verdict on this axis: PARTIALLY-ANTICIPATED, at the single-agent/mechanistic level only.** The general phenomenon — internal signal (hidden state, verbalized confidence, token-probability) diverges from external output/decision — is a well-established and actively growing 2024-2026 literature. **What is NOT anticipated:** (a) none of these operationalize the internal signal as a *graded four-valued belief* (yes/no/maybe/maybe-not) elicited via the same interface as the assertion, only as continuous scalars or probe classifiers; (b) none measure the gap against an external ground-truth *culprit* in a social/adversarial multi-agent whodunit — they measure factual QA or single-agent judgment tasks. **Must cite** as the established background literature a reviewer will expect ("models know more than they say" is not our coinage).

---

## Q2 — Multi-agent private belief ≠ public statement (cascades, conformity, herding)

**Closest prior work:**
- **"What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Debates"** — arXiv:2607.02507v1 (submitted **July 2, 2026** — very recent, likely post-dates or was missed by the first scan same day). 10 models, 3 scenarios; compares public utterances to off-the-record (OTR) private responses under identical conditions; divergence rises from a ~3% baseline to ~40% in alignment-inducing/social-pressure settings; OTR responses explicitly cite career-risk/relational pressure as the reason for public accommodation. **This is the single closest neighbor found in this entire scan and MUST be cited.** [Link](https://arxiv.org/html/2607.02507v1)
- **"Conformity Dynamics in LLM Multi-Agent Systems: The Roles of Topology and Self-Social Weighting"** — arXiv:2601.05606. Formalizes conformity-to-majority in LLM debate networks. [Link](https://arxiv.org/pdf/2601.05606)
- **"Bayesian Social Deduction with Graph-Informed Language Models"** — Rahimirad et al., arXiv:2506.17788 (June 2025). Avalon; maintains Bayesian probabilistic private beliefs over hidden roles, distinct from public statements; graph-based reasoning triangulates multiple dialogue fragments to update role conviction. Mechanistically the closest thing to our "triangulation → conviction" secondary finding, but belief representation is continuous-Bayesian, not tetravalent, and the game is Avalon (roles), not a whodunit with a single fixed external culprit. [Link](https://arxiv.org/pdf/2506.17788)
- Banerjee-style information-cascade framing and DeGroot-averaging analogies recur across this literature as the standard theoretical lens for why public statements diverge from private signal in sequential/social settings — expected background citation, not a direct hit.

**Verdict on this axis: YELLOW — closest neighbor exists and changes what must be written.** arXiv:2607.02507 reports a public/private gap of comparable *size* (their divergence reaches ~40%; ours is the mirror-image ~27pp collapse from ~29% true-belief-accuracy down to ~1.5-2% assertion-accuracy). But the **mechanism differs**: their divergence is driven by *social/audience pressure* (career risk, alignment-inducing context) in a debate setting with no external ground truth; ours is driven purely by *response-format* (forced binary commit-or-abstain vs. graded tetravalent state) in a whodunit with a fixed external culprit, and — per the brief — is stable across 2 arms and 31+ seeds regardless of social pressure manipulation. **The write-up must add a paragraph distinguishing:** (1) format-induced vs. pressure-induced divergence as two different causal routes to the same qualitative phenomenon, (2) measurement against objective ground-truth accuracy vs. stance/semantic divergence between two text samples, (3) that our tetravalent representation is what "graded belief" collapses from, which 2607.02507 does not use.

---

## Q3 — Graded/many-valued (Belnap-4/tetravalent) belief representations for LLM/agent help-seeking

**Closest prior work:**
- **"Four Imprints of Belnap's Useful Four-Valued Logic in Computer Science"** — arXiv:2503.20679 (2025). Survey of Belnap-Dunn logic's CS applications (databases, paraconsistent reasoning, hardware verification) — no LLM/agent application. [Link](https://arxiv.org/html/2503.20679v1)
- **"Two-Layered Logics for Probabilities and Belief Functions over Belnap-Dunn Logic"** — arXiv:2402.12953 (2024). Formal extension of Belnap-Dunn with graded belief functions — pure logic/math, no empirical agent study. [Link](https://arxiv.org/pdf/2402.12953)
- **"Reasoning with Belief Functions over Belnap-Dunn Logic"** — arXiv:2203.01060 / ScienceDirect (2023). Same family, formal only. [Link](https://arxiv.org/pdf/2203.01060)
- Belnap's original 1977 "A Useful Four-Valued Logic" — the canonical citation any reviewer will expect if we invoke Belnap-4/tetravalent framing at all. [Link](https://link.springer.com/chapter/10.1007/978-94-010-1161-7_2)

**Verdict on this axis: GREEN — no empirical LLM/agent precedent found.** The four-valued logic itself is 45+ years old and its formal extensions with graded belief functions are established (must cite Belnap 1977 + the two belief-function papers if the write-up invokes the formalism by name). But **nobody found applies Belnap-4/tetravalent states empirically to LLM agent belief, and nobody uses maybe/maybe-not as first-class states that gate or trigger help-seeking behavior.** This is the strongest and cleanest novelty axis in the whole finding — the tetravalent *framing device* itself, applied to a real multi-agent LLM experiment, appears unprecedented in the literature surfaced by this scan.

---

## Q4 — Distributed knowledge (Fagin/Halpern) empirically tested in LLM agents; triangulation predicts conviction

**Closest prior work:**
- **Fagin, Halpern, Moses, Vardi — "Reasoning about Knowledge"** (MIT Press, 1995) and **"What Can Machines Know? On the Properties of Knowledge in Distributed Systems"** (JACM). The foundational formalization of the distributed-knowledge operator D_G — **must cite** if the secondary triangulation finding is framed in this vocabulary at all. [Reference via Stanford Encyclopedia of Philosophy, Epistemic Logic entry](https://plato.stanford.edu/entries/logic-epistemic/)
- Dynamic-epistemic-logic LLM benchmarks (muddy children, Cheryl's birthday puzzles) test whether LLMs can *formally solve* distributed/common-knowledge puzzles — capability testing, not an interactive multi-agent whodunit generating the agents' own beliefs. Located via ScienceDirect ("Logical reasoning in evolving scenarios: Evaluating LLMs with dynamic epistemic logic puzzles"), not independently fetched/verified this pass — flag as unconfirmed detail.
- **Bayesian Social Deduction with Graph-Informed Language Models** — arXiv:2506.17788 (same paper as Q2). Closest *empirical* precedent for "combining information fragments across the group predicts belief/conviction" — but framed as Bayesian probability updating over a graph, not as Fagin/Halpern distributed knowledge, and Avalon has no single external fixed culprit to score accuracy against.
- **Checked and RULED OUT:** arXiv:2603.00142 ("Evaluating Theory of Mind and Internal Beliefs in LLM-Based Multi-Agent Systems," Kostka & Chudziak). A WebFetch summary initially reported this as matching our private-belief/public-assertion gap and triangulation result almost exactly — independent verification against the actual abstract showed this was a fetch-summary artifact (the tool over-fit to my leading prompt). The real paper is about Theory-of-Mind/BDI cognitive-architecture interplay with formal-logic verification for coordination performance, not a belief-assertion gap or triangulation-predicts-conviction result. Excluded from the verdict below; noted here as a caught false positive.

**Verdict on this axis: GREEN — no combined precedent found.** Distributed knowledge as formal theory (Fagin/Halpern) is 30+ years old and must be cited if invoked. Empirical LLM tests of *formal* distributed-knowledge puzzles exist but don't generate agent belief from role-play. The closest *empirical* multi-agent analog (2506.17788) tests a structurally similar idea (combining fragments → conviction) but via Bayesian probability in Avalon, not via tiered epistemic-access conditions (single-fragment witness vs. two-fragment triangulator) measured against a fixed external ground truth with calibrated near-100% correct abstention in the under-informed tier. **No paper found combining:** formal distributed-knowledge framing + empirical LLM multi-agent test + tiered access conditions + ground-truth-scored conviction/abstention.

---

## Overall novelty verdict

**GREEN, unchanged from the first scan, but with two required citation additions this second pass surfaced:**
1. **arXiv:2607.02507** ("What LLM Agents Say When No One Is Watching," July 2 2026) — closest neighbor found in either scan; must be cited with an explicit paragraph distinguishing format-induced vs. pressure-induced belief/assertion divergence, and ground-truth-scored accuracy vs. stance-divergence measurement.
2. **arXiv:2601.07767** ("Are LLM Decisions Faithful to Verbal Confidence?") — closest single-agent analog; cite as established background for the general "verbalized signal decoupled from behavior" phenomenon.

No paper combines all of: (a) multi-agent whodunit with fixed external ground truth, (b) a tetravalent graded belief state read out separately from a forced hard commit/abstain, (c) a measured belief→assertion collapse of this magnitude (+0.27), (d) tiered epistemic access where only two-fragment triangulation (not single-fragment witnessing) predicts conviction. Both core and secondary findings remain novel on the specific combination, not on any single ingredient in isolation — every ingredient in isolation has prior art and must be cited.

**Established literature to cite regardless of verdict:** Belnap (1977) four-valued logic; Fagin/Halpern/Moses/Vardi (1995) distributed knowledge; the "models know more than they say" cluster (2410.02707, 2505.08662, 2601.07767); Banerjee-style information cascades for the conformity/herding framing.

---

## Executive summary (5 lines)

1. **Verdict: GREEN, novel on the specific combination** — no single paper found that combines a whodunit ground-truth, tetravalent graded belief vs. forced-commit, a measured +0.27 collapse, and tiered-triangulation-predicts-conviction.
2. **Must-cite, closest neighbor:** arXiv:2607.02507 (July 2 2026) — same public/private divergence shape, different mechanism (social pressure vs. response format); write-up needs a distinguishing paragraph.
3. **Q1/Q2 (belief-assertion gap generally):** well-documented at single-agent level and in one very recent multi-agent debate paper — cite as background, not overlap.
4. **Q3 (tetravalent/Belnap-4 applied to LLM belief) is the cleanest novelty axis** — 45-year-old logic, zero empirical LLM/agent applications found.
5. **Q4 (distributed-knowledge triangulation) has a structurally similar but mechanistically distinct empirical precedent** (Bayesian Social Deduction, arXiv:2506.17788, Avalon) — cite, distinguish, proceed.
