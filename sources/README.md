# Independent study selection — 17 September 2026

This review follows the [initial portability reading](../2026-09-17-experience-portability/README.md)
and the user's request to create at least two further ancillary studies. It
selects [procedural-memory migration](../../notes/EXPERIENCE_PORTABILITY.md#selection-after-the-methods-review)
and [acquired correction lineage](../../notes/CORRECTION_LINEAGE.md).
These are bounded comparisons, not certified gaps in the literature. All paper
outcomes below are author-reported; no published experiment was reproduced.

## What the closest methods change

**P77 — [Agent KB, 2507.06229v5](https://arxiv.org/html/2507.06229v5).**
Read §§3.3, 4.3 and Appendices C/D. Feedback-conditioned refinement and a
plan-similarity gate already provide selective experience use. Similarity is
not task correctness. The cost analysis separates one-time ingestion from
marginal use; ingestion is not simply absent. **Answers** generic selective
sharing; **narrows** the candidate to decisions for a changed recipient. The
pinned static inspection below supplies an implementation donor, not evidence
that its gate identifies harmful inherited guidance.

**P78 — [CONTRAMEM, 2608.22533v1](https://arxiv.org/html/2608.22533v1).**
Read Methodology, matched-budget comparisons and Appendix A.7. Cross-model
trajectory contrasts produce function/skill cards; an unchanged bank is tested
on an unseen recipient. Same-trajectory-budget controls and construction/use
accounting already exist, although verifier tokens are omitted when unavailable.
GAIA ability labels assist retrieval. **Answers** generic unseen-recipient
transfer and **redirects** the comparison toward the added value of paying for
recipient-specific adaptation over a competent unchanged bank.

**P79 — [Agent Memory Distillation, 2608.07169v1](https://arxiv.org/html/2608.07169v1).**
Read §§3.2–3.3 and Discussion. Successful teacher trajectories yield hierarchical
workflow/subtask memories, with reactive function-level lookup. Stronger teachers
do not uniformly make better memories for a student; adaptive teacher selection
is proposed. **Narrows** a recipient comparison and supplies a construction donor.
The inspected passages do not establish a paid decision to retain, adapt or
retire a fixed bank after migration.

**P80 — [MemCollab, 2603.23234v2](https://arxiv.org/html/2603.23234v2).**
Read §§2.1–2.3, 3.2/Table 2, Appendices D.4/E. The shared bank is explicitly
model-aware: selection uses target-model participation in labeled memory pairs.
Construction and inference costs receive separate treatment. **Answers** generic
recipient-aware sharing. A recipient absent from those histories needs a
competent fallback, not an artificially empty comparator. Version 1 was an
initial discovery read; metadata checking led to this version-2 assessment.
Do not carry a model-agnostic interpretation into the proposed study.

**P81 — [MemoRepair, 2605.07242v1](https://arxiv.org/html/2605.07242v1).**
Read §2, §3 metrics/baselines and §3.4. Influence closure, withdrawal and repair
operate on supplied provenance; random edge-deletion robustness is already
tested. The reported task diagnostic is a formula over affected artifacts,
rather than executed complete tasks. Repair cost excludes the withdrawal
barrier and does not establish lifetime provenance cost. **Answers** cascade
repair and simple missing-edge demonstrations; **redirects** the new question
to acquired dependencies, complete behavior and the cost of recording them.

**P82 — [Dependency-Guided Rollback, 2608.10502v1](https://arxiv.org/html/2608.10502v1).**
Read §§3.1–3.3, §4 metrics and appendix schema/recurrence definitions. Diagnosed
faults and runtime-emitted typed edges support selective rollback/replay;
inferring missing semantic edges from natural-language logs is outside scope.
Recovery uses answer oracles; recurrence repeats the final query among successful
recoveries. **Answers** graph-directed recovery, while **narrowing** a new test
to acquiring useful lineage and later fresh tasks. It does not undo irreversible
external effects.

**P83 — [StateAuditor, 2608.01619v1](https://arxiv.org/html/2608.01619v1).**
Read §§3–4, 6.1, 6.3 and 7. Draft auditing and source-grounded transition checks
provide a strong correction alternative. A newer citation alone does not prove
semantic supersession. Full-history independent-query results differ from a
joint-probe upper bound; external results qualify the mechanism's generality.
**Narrows** the retained-lineage comparison: allow competent query-time auditing
and source reconstruction instead of comparing only with blind stale retrieval.

**P84 — [Does Your Agent's Memory Survive a Model Upgrade?, 2609.05339v1](https://arxiv.org/html/2609.05339v1).**
Read §§2–3.2 and Appendices C–E. Fixed histories separate writers, readers and
embedders. Own-store baselines, raw-history repair and a 20-probe forecast already
address migration. Cost-to-recovery selects among evaluated methods/budgets;
conditional recovery costs are not an online policy. **Answers** generic model
upgrade and cheap migration forecasting. **Redirects** our candidate from
factual store repair to the useful choice of inherited procedural guidance,
with calibration costs and fresh complete tasks.

**P37 revisited — [StateMem, 2608.19652v1](https://arxiv.org/html/2608.19652v1).**
Deepened §§5.2–5.3, 6.2 and Appendix H. Dependencies are extracted during
ingestion; propagation marks rechecking rather than automatic supersession.
Overpropagation can hurt, and encoding is substantial. **Answers** generic
acquired dependency tracking. **Narrows** the question to whether its lifetime
decision value beats reconstructing dependencies when a correction actually
arrives. No local outcomes or earlier paper numbering are changed.

## Static implementation boundary

Inspected [Agent-KB](https://github.com/OPPO-PersonalAI/Agent-KB) at
`588d6694e743a981179f2e11b47ca3a668e2f1ac`. The
[artifact manifest](artifact-inspection.json) records exact files, reading ranges
and hashes. The GAIA service exposes stored plans/experiences through hybrid
retrieval. The SWE refinement helper uses the task and student output, but needs
supplied paths and data. These paths are plausible donors for bounded development;
they do not validate a complete migration experiment or audit the paper's gate.
No imports, dependency installation, service startup or model calls were made.
This revision is not verified as the paper's experimental revision. Other new
papers received methods reading only; no author implementation was inspected.

## Discovery scope and leads

The two cached discovery responses cover the first 25 results each, ordered by
submission date: memory with transfer/migration/compatibility, and memory with
provenance/rollback/retraction/dependency. Four subsequent ID requests verified
selected metadata. [retrieval.json](retrieval.json) records all six requests,
timestamps, User-Agent and SHA-256 hashes. Requests used one connection and
were spaced at least three seconds apart. Versioned primary HTML supplied the
passages above. Supplementary web searches pursued cross-model procedural
memory, selective repair and model-upgrade repair. The last search found P84,
which the bounded broad pass had missed; it materially narrowed selection.

Metadata/abstract screening only: Portable Agent Memory `2605.11032v1`
(transport protocol), ChronoMem `2607.27773v2` (versioned memory), AgentZeroMemory
`2608.29606v1`, and PLACEMEM `2607.04089v1` (systems proposal). Other entries in
the discovery XML are search results, not inspected methods. None establishes
a deployed decision rule through its title or abstract. The provenance-survey
lead `2606.04990` received web discovery only and supplies no claim here.

## Selection and feasibility

The first study concerns an **agent change with evidence held fixed**. It must
beat strong unchanged inheritance or justify its adaptation through complete
behavior and paid recipient experience. The second concerns an **evidence
correction with the recipient held fixed**. It must acquire useful dependency
information, rather than receive the evaluator's graph, and beat reconstruction
from the same source archive. These questions can proceed independently of each
other and the active retained-implementation comparison.

Both permit small controlled workloads and fixed-weight model calls. Methods
and bounded feasibility work belong to the ancillary investigators. No serving
capability, gradient access, acquisition success or empirical advantage was
tested in preparation. Public answers, a strong simple alternative or a concrete
resource limitation can close a bounded phase without a new mechanism winning.
