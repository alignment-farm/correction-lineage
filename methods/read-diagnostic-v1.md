# Prospective read-time diagnostic v1

Recorded during the frozen fresh-v1 run, after observing event-1 errors on seeds
211 and 307. These outcomes remain unchanged. No main experiment prompt changes.

Observation: persistent unit_cost is correct, but later order totals correspond
to quantity times (unit_cost + handling). This is consistent with double-counting
handling, but outputs alone do not establish the internal mechanism. Original
wording says tariff plus handling, both per item, and defines unit_cost elsewhere.

Test two new parameter instances, seeds **523 and 631**, not selected from model
outcomes. Generate original memory with the model, then rebuild corrected memory
with the same archive and repair prompt as the original rebuild arm. Fork that
actual state into two read calls: original wording versus replacing the cost
sentence with `total_cost = quantity * (current tariff + per-item handling) =
quantity * memory.unit_cost when memory.unit_cost is correct. Do not add handling
again to unit_cost.` Everything else, including schema, archives, corrections,
quantities and model settings, is identical. Counterbalance order between seeds.
No gold state or dependencies go to the model. Four calls per seed, eight total.

Score all fields and orders using the original typed evaluator. Count all calls,
including failed writes or rebuilds; do not repair with truth or drop instances.
The prespecified directional expectation is fewer order-cost errors with explicit
wording. A successful contrast supports prompt sensitivity on new material, not a
universal causal explanation or evidence that original arms passed complete tasks.
Keep this exploratory diagnostic separate from deployment results and costs.
