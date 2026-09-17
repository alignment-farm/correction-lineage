# Inspected method boundary

Pinned versions were inspected again on 17 September 2026. Local HTML hashes and
copied root-ledger provenance are in [manifest](../sources/manifest.json).

- [MemoRepair v1](https://arxiv.org/html/2605.07242v1), §§2–3.4: supplied
  influence edges determine withdrawal and reconstruction. We borrow repair
  scope, not the paper's min-cut selection or neural-skill experiments.
- [Dependency-Guided Rollback v1](https://arxiv.org/html/2608.10502v1), §§3.1–3.4:
  runtime typed dependencies and independent-support checks distinguish affected
  candidates from unsupported state. Our source links are inferred by the model.
- [StateMem v1](https://arxiv.org/html/2608.19652v1), §§5.1–5.3:
  dependency extraction during ingestion precedes deterministic recheck flags.
  Our separate acquisition and maintenance calls make those costs explicit.
- [StateAuditor v1](https://arxiv.org/html/2608.01619v1), §§3–4:
  source-grounded auditing motivates giving all arms competent archive checking.
  We supply authoritative corrections rather than testing transition discovery.

These are purpose-built experimental arms, not implementations or replications
of those named systems. No author code was executed. The copied
[reading ledger](../sources/README.md) labels paper outcomes as author reports.
Local findings concern only this small controlled workload and deployed model.
