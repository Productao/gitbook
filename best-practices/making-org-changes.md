---
description: Best practices for organizational changes and restructuring
---

# Making Org Changes

Best practices for planning, testing, communicating, and implementing organizational changes using Agentnoon.

## Always Use Scenarios

Never make organizational changes directly in Main Org. Scenarios let you:

* Test changes and see full impact before committing
* Identify unintended consequences (broken hierarchies, SOC issues, budget overruns)
* Compare multiple approaches side-by-side
* Submit for formal approval with an audit trail
* Show before/after comparisons for stakeholder communication

## Planning Process

1. **Define the problem:** What are you solving? (e.g., "Sales team lacks capacity", "Engineering managers are overloaded")
2. **Set measurable goals:** (e.g., "Reduce average SOC to 7", "Cut workforce cost by $2M by Q3")
3. **Analyze the current state:** Use Workforce Hub (SOC distribution, cost by department), Spotlight (highlight problem areas), and the Directory export for deeper analysis
4. **Create a scenario:** Name it descriptively — "Q3 2026 Engineering Reorg" — and set a budget if applicable

## Testing Changes Before Committing

In your scenario, make the changes (add, close, move, modify positions), then verify:

* **OpEx Panel:** Net headcount and cost impact, with itemized additions/reductions/modifications
* **Org chart:** Reporting relationships are correct; no broken hierarchies (orange icon)
* **SOC metrics:** Add "Direct SOC" to Card Content to see spans on every card — aim for 5–10 reports per manager
* **Forecast:** Toggle Show Changes to see department-level headcount deltas over time

Iterate: if the plan creates new problems (overloaded managers, unexpected cost), create alternative scenarios and compare.

## Phasing Changes Over Time

Use effective dates to spread changes across phases and reduce disruption:

* Phase 1 (Q1): Add new manager positions
* Phase 2 (Q2): Reassign teams to new managers
* Phase 3 (Q3): Close redundant positions

In Forecast, monthly/quarterly view shows exactly when each change hits headcount and budget.

## Getting Approval

1. Open the **OpEx Panel** > **Configure Submission**
2. Write a justification: problem statement, approach, expected outcomes, risks
3. Submit through approval levels (Level 0–3 as configured)
4. If rejected, review feedback, revise, and resubmit

Pre-socialize with key approvers before formal submission to surface concerns early and increase approval likelihood.

## Communicating Changes

Use Agentnoon exports to support communication:

* **PowerPoint org charts:** Before/after visuals for executive and all-hands presentations
* **OpEx Panel CSV:** Summary of additions, reductions, moves with cost impact
* **Forecast export:** Timeline of when changes take effect by department

Lead with the "why" — employees respond better to rationale than to announcements of structure changes alone.

## Implementing After Approval

1. Communicate changes to affected employees with timeline and rationale
2. Execute in phases if phased: add new roles first, move teams, then close eliminated positions
3. Update Main Org via CSV upload or wait for next scheduled data sync
4. Monitor post-implementation: check SOC, gather manager/employee feedback, adjust if needed

## Related Resources

* [Planning a Reorganization](../use-case-tutorials/planning-reorganization.md)
* [Scenarios Overview](../scenarios/overview.md)
* [Configuring Approval Flows](../admin/configuring-approval-flows.md)
* [Position vs Headcount Management](position-vs-headcount.md)
