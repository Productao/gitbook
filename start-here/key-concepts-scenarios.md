---
description: Essential concepts for working with scenarios
icon: lightbulb
---

# Key Concepts for Scenarios

## What Is a Scenario?

An editable copy of your Main Org where you model future changes without affecting the current live data. Changes in scenarios are completely isolated from Main Org until you choose to implement them.

**Typical workflow:** Main Org (current state) → Create scenario → Model changes → Review impact → Submit for approval → Implement

## Change Types

**Addition (green outline)** — New position created; increases headcount and cost.

**Reduction (red outline)** — Existing position closed; decreases headcount and cost. Types: Layoff/RIF, Voluntary Exit, Elimination.

**Modification (icon only, no color)** — Changed attributes on existing position (title, salary, department, manager). May increase or decrease cost.

**No Change** — Position exists in both the Main Org and scenario; no attributes modified.

## Before / After / Changes Views

* **Show Before** — Main Org (current reality); your baseline
* **Show After** — All scenario changes applied; the proposed future state
* **Show Changes** — Delta only; shows +/- per department; best for communicating impact

## OpEx Panel (Scenario Changes & Impact)

The OpEx Panel is the side panel where you review all scenario changes and their impact. It shows headcount additions and reductions, net headcount change, net cost impact, and breakdown by department. You can toggle between cost and headcount views, and see changes grouped by effective date. The OpEx Panel is also where you submit scenarios for approval. See [Scenario Changes & Impact](../scenarios/opex-panel.md).

## Effective Dates

Date when a planned change takes effect. Set different dates on different changes in the same scenario to model phased rollouts. Forecast shows the time-phased impact. See [Time-Based Planning](../scenarios/time-based-planning.md).

## The Bench

Holding area for employees detached from positions but not yet placed elsewhere. Useful for modeling internal transfers: detach from Position A → assign to Position B. The bench is a planning construct only.

## Scenario Views

* **Org Chart** — Visual hierarchy; drag-and-drop; best for structural changes
* **Directory** — Table view; bulk operations; best for mass edits and filtering
* **Forecast** — Time-phased projections; headcount/cost by period
* **Workforce Hub** — Analytics charts (SOC, distribution, heatmap); before/after comparison

## Approval States

Draft (editable) → Submitted/Pending (locked) → Approved (locked) → Rejected (editable for revisions). Once approved, scenarios lock to preserve the approved state.

## Scenario Comparisons

Compare 2 scenarios side-by-side: cost, headcount, structure, org health metrics. Create Option A and Option B and use comparisons to choose the best approach for leadership. Comparisons must be started from the homepage.

## Projects (Optional)

Group related scenarios under a project for larger initiatives. Example: "2026 Restructuring" project containing Engineering Reorg, Sales Consolidation, and G\&A Cost Reduction scenarios.

## Related Articles

* [Scenarios Overview](../scenarios/overview.md)
* [Creating Scenarios](../scenarios/creating-scenarios.md)
* [Time-Based Planning](../scenarios/time-based-planning.md)
* [Scenario Comparisons](../scenarios/comparisons.md)
* [Scenario Approvals](../scenarios/approvals.md)
