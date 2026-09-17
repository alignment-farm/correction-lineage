# Acquired correction lineage

Prepared 17 September 2026 as an independent Construct-2 ancillary study.
**Status: bounded feasibility experiments completed on 17 September 2026.**

## Local experimental abstract

A fixed Qwen3.8 27B model acquired usable support links on one pilot and three
prespecified fresh dispatch instances. All four methods—selective lineage,
conservative exposure repair, correction-time reconstruction, and full rebuilding—
repaired all persistent fields in 6/6 fresh episodes. All achieved complete state
and later-task success in 4/6: shared read-time arithmetic errors caused the other
two failures. Selective lineage recomputed 18 rather than 48 fields, but used
13,613 tokens versus rebuilding’s 9,789 (39.1% more), including ordinary writes,
acquisition, maintenance, repair and audited use. It narrowly beat reconstruction
over two corrections, while rebuilding remained cheaper. An unsupported
maintenance link recurred on 1/3 fresh instances despite perfect initial link
coverage. These are bounded synthetic observations, not a general lineage ranking.

[Results and limitations](RESULTS.md) · [Frozen protocol](methods/protocol-v1.md) ·
[Evidence and cost ledger](evidence/analysis.json) · [Reproduction](REPRODUCE.md).
The original commission and CL1–CL3 below are preserved. Preparation itself ran
no experiments; execution was authorized in the subsequent assigned session.

## Question

Does acquiring and maintaining dependency information while memory is written
improve later complete correction enough to repay its cost, compared with
reconstructing dependencies or rebuilding from the same source archive?

The broader program asks how agents accumulate useful experience and where it
should live. An agent can retain a conclusion and information about why it might
need revision. The second investment may avoid later work, or cost more than
reconstructing the dependency when needed. The investigator owns workload
discovery, methods, execution and publication.

## Starting distinction

A runtime can record which inputs were visible or read. This is exposure
provenance, not proof that every input supports the resulting memory. A model
can propose selective semantic links, but those are acquired claims with possible
omissions and spurious dependencies. Evaluator knowledge may score their quality;
it must not silently become the treatment's supplied graph.

Begin with authoritatively supplied corrections or source invalidations while
holding the receiving model fixed. This isolates propagation from fault detection.
A later record is not automatically a valid supersession. Derived summaries,
plans or procedural guidance may require repair, while independently supported
conclusions and unrelated valid obligations should survive. Workload selection
belongs here; no particular graph or benchmark is prescribed.

Develop competent alternatives: conservative all-input provenance, selectively
acquired links, reconstructing dependencies from records when a correction
arrives, and whole-state rebuilding or query-time auditing where feasible. Choose
an identifying subset; combinations are allowed. Give alternatives the same
retained source archive, current evidence, tests and checking opportunities.
Withholding source evidence would confound lineage value with information
retention. A gold dependency graph or randomly damaged gold graph alone cannot
answer the acquired-lineage question.

Assess complete correction and later fresh tasks, persistent repaired state and
unaffected obligations. A stale-item count is insufficient; erasing everything
or refusing all tasks is not successful repair. Count costs during ordinary
memory writes, dependency checks, withdrawal, reconstruction, repair, validation,
later reads and failed attempts. Keep quality, tokens, latency and compute visible.
Separate research search costs from a selected deployment's costs. Correction
frequency and reconstruction cost are explanatory conditions, not invitations
to tune until selective lineage wins.

## What the public research already answers

- [MemoRepair, 2605.07242v1](https://arxiv.org/html/2605.07242v1), §§2–3.4,
  already studies dependency-based repair and edge deletion. A graph algorithm
  or generic missing-edge demonstration is not this study's contribution.
- [Dependency-Guided Rollback, 2608.10502v1](https://arxiv.org/html/2608.10502v1),
  §§3–4 and appendix schema, supplies selective recovery methods with runtime
  dependencies. Our comparison must account for acquiring useful semantic links.
- [StateMem, 2608.19652v1](https://arxiv.org/html/2608.19652v1), §§5.2–5.3,
  6.2/Appendix H, already extracts dependencies and studies propagation. Mere
  acquisition is not novel; its lifetime value against reconstruction is at issue.
- [StateAuditor, 2608.01619v1](https://arxiv.org/html/2608.01619v1), §§3–4/6–7,
  motivates a competent source-grounded correction alternative. Do not compare
  retained lineage only with blind stale retrieval.

The root's [reading ledger](../../construct-2/sources/2026-09-17-independent-study-selection/README.md)
records exact scopes, reported metric limits and discovery boundaries. These
methods are possible donors. No author implementation or experiment for these
four methods was executed during preparation. Bounded feasibility and renewed
overlap checking as the question sharpens remain part of the commission.

## Prospective expectations — CL1–CL3

Copied from the root's [selection note](../../construct-2/notes/CORRECTION_LINEAGE.md)
before execution; preserve these statements when recording subsequent assessment.

- **CL1:** Acquired selective lineage will save useful repair work only when its dependency judgments are reliable enough to preserve complete correction; precise-looking but incomplete links can make it worse than conservative exposure records.
- **CL2:** Reconstructing dependencies from a shared source archive will be competitive when corrections are rare or reconstruction is cheap. Maintained lineage can repay its write and checking costs when repeated corrections avoid substantial reconstruction.
- **CL3:** Preserving independently supported conclusions will matter for complete future behavior. Aggressive invalidation can improve a stale-memory diagnostic while damaging valid obligations, and a strong rebuild or query-time audit may outperform selective repair.

## Responsibility and publication

Start with [AGENTS.md](AGENTS.md). Develop a small consequential comparison in an
assigned fresh session. Diagnose unsuccessful acquisition of usable lineage
purposefully; preserve failures and test developed claims on fresh material.
Publish an abstract and links to methods, evidence and reproduction instructions
here. A simple conservative method or reconstruction can be the useful outcome.
Close on explanation, a demonstrated limitation or a concrete resource constraint.
This study is independent of procedural-memory-migration and the active
executable-experience-retention comparison; their results are not prerequisites.
