# Graded Epistemic Access and the Belief–Assertion Gap in Multi-Agent Help-Seeking

*Twenty LLM agents, a networked whodunit, and a four-valued (yes / no / maybe / maybe-not)
response space — asking whether **abstention is the correct answer for an agent who structurally
cannot know**, whether **forcing a binary answer destroys a belief the agent privately holds**, and
whether **coordinated lying manufactures more false consensus than independent lying**.*

---

## 🙏 Origin & credit

This study belongs to the same tetravalent research line as
[`schrodinger-tetravalent-brain`](../schrodinger-tetravalent-brain) — the **yes / no / maybe / maybe-not**
(Belnap-4-shaped) reasoning idea sparked by **[FloatHeadPhysics](https://www.youtube.com/@FloatHeadPhysics)**
and the video *"I finally understood why the universe needs imaginary numbers."* The design that turns that
into a *maybe / maybe-not* system whose uncertainty forces collaboration, and the whodunit experiment testing
it, are Nadi's. The literature it stands on is credited in the paper's References (Belnap's four-valued logic;
Bikhchandani–Hirshleifer–Welch 1992 & DeGroot 1974 on correlated belief; Fagin/Halpern/Moses on distributed
knowledge; Orgad et al. ICLR 2025; the PIMMUR validity framework).

## What this is

### 📄 `essay/` — the paper
**Graded Epistemic Access and the Belief–Assertion Gap in Multi-Agent Help-Seeking**
(`tetravalent-help-seeking.html` — open in a browser; markdown in `REPORT.md`). Three findings, all confirmed
at n = 72 seeds/arm (144 runs, 0 failures):

1. **Conviction tracks the ability to triangulate.** The relay tier that can combine ≥2 witness fragments
   lands the true culprit most (0.65 / 0.57); single-fragment witnesses — who genuinely cannot know alone —
   correctly abstain (~0.91 can't-tell). Calibration is a property of *network position*, not isolated confidence.
2. **Belief and assertion dissociate.** Agents hold the culprit in graded belief ~28–30% of the time, but a
   forced hard-commit collapses that to ~2% (gap > 0.26, both arms). The direct empirical motivation for a
   first-class "maybe / maybe-not."
3. **Coordinated falsehood out-propagates independent falsehood** (pre-registered). Two liars converging on the
   same scapegoat manufacture more false consensus than two pointing independently: scapegoat-involved rate
   0.067 vs. 0.038; Cohen's *d* = 0.66; permutation *p* = 0.0004 (20k); 95% bootstrap CI [+0.015, +0.044],
   excluding zero. A real but **modest-magnitude** effect — the tiered, abstaining network is fairly *resistant*
   to coordinated deception.

### 🔬 `experiment/` — reproduce it
- `PREREG.md` — the frozen pre-registration (hypotheses, metrics, thresholds fixed before the run).
- `run_confirmatory.py`, `ground_truth.py`, `analyze_confirmatory.py` — the runnable harness and the external,
  never-circular grader.
- `RESULT_test4_confirmatory.md` — auto-generated results write-up.
- `data/analysis_full_72seeds.json` — the full aggregated statistics (per-tier, per-arm, all contrasts). The
  raw 144-unit per-agent trajectory dumps are large and kept with the project; available on request.
- Deployment: 20 agents on `llama3.1:8b` (local, $0). Single model is a declared limitation (see §4).

### 🔎 `research/` — prior-art dossiers
Two independent scans (`priorart_pass1_belief-assertion.md`, `priorart_pass2_openreview-native.md`), the second
an OpenReview-native deep pass. Verdict: **novel on the three-way combination**, not on any single primitive.

## Epistemic honesty

The paper carries a validity gate (PIMMUR, arXiv:2509.18052) cleared by an independent auditor, a post-hoc
meta-awareness scan (0/144 transcripts showed agents recognizing the setup), and an explicit limitations
section. The coordination effect is reported as *modest*, not dominant. Nothing here is overclaimed.

## Where this lives

- **GitHub (canonical, browsable):** https://github.com/nadiadatepe-eng/tetravalent-help-seeking
- **OSF (archive, DOI-capable):** https://osf.io/2scbp/ — a component of the tetravalent project
  [*From the Schrödinger Equation to a Tetravalent Synthetic Brain*](https://osf.io/h9xcr/).
  Note: on OSF, `PREREG.md` is posted as a **study protocol**, not an OSF-timestamped preregistration
  (the confirmatory data was already collected) — see the OSF component note.

## Status

Draft, editor-verified post-confirmatory (2026-07-06). Prior-art GREEN. Not yet submitted to a venue.

## License

MIT — see [`LICENSE`](LICENSE). © 2026 Nadi Adatepe.
