---
description: Using effective dates for phased changes
icon: calendar-days
---

# Time-Based Planning

## Time-Based Planning

Use date fields to model organizational changes that occur at specific future points, creating accurate time-phased forecasts.

## Core Date Fields

**Hire Date** - When a new position starts (person joins or vacancy is filled). The position appears in Forecast headcount and cost from this date forward.

**Termination Date** - When a person leaves or a position is eliminated. The position no longer appears in headcount after this date and costs are removed from projections.

**Effective Date** - When a change to an existing position takes effect (transfer, reorg, attribute change). The position appears in its "before" state until the effective date, then in its "after" state from that date forward.

### When to Use Each

| Scenario                                                         | Use              |
| ---------------------------------------------------------------- | ---------------- |
| New hire or filling a vacancy                                    | Hire Date        |
| Layoff, RIF, position elimination                                | Termination Date |
| Internal transfer or reorg (same person, new department/manager) | Effective Date   |
| Phased department move (e.g., Q3 effective)                      | Effective Date   |
| Salary increase effective next year                              | Effective Date   |

**Key distinction:** Effective dates preserve position continuity — the same position just changes attributes. Hire and termination dates show positions being created and eliminated.

## How Effective Dates Work in Forecast

When you change a position's department with an effective date of July 1, 2026:

* **In the org chart** - shows the "after" state (new department)
* **In Forecast before July 1** - position counts in the original department
* **In Forecast from July 1 onward** - position counts in the new department

**Show Changes view:** Before the effective date → 0 change; from the effective date → +1 in new department, -1 in old department.

**Example:**

| Department             | Q1 2026 | Q2 2026 | Q3 2026 | Q4 2026 |
| ---------------------- | ------- | ------- | ------- | ------- |
| Network Operations     | 25      | 25      | 20      | 20      |
| Operations & Logistics | 30      | 30      | 35      | 35      |

This shows 5 positions moved in Q3 2026.

## Phased Reorganizations

Set different effective dates on different positions within the same scenario:

* Teams moving in Q2 → effective date April 1, 2026
* Teams moving in Q3 → effective date July 1, 2026
* Teams moving in Q4 → effective date October 1, 2026

Forecast shows the gradual transition, letting budget owners see exactly when departmental headcount and costs shift.

## New Positions

For positions created in a scenario (no "before" state), effective dates control when the position appears in Forecast. The position only ever appears in its assigned department, starting from the effective date.

## Common Questions

**What if I don't set an effective date?**

The change is treated as immediate — it appears in the "after" state for all Forecast time periods.

**Can I set different effective dates on different positions in the same scenario?**

Yes — this is the standard approach for phased reorgs.

**How far can I forecast?**

Up to 5 years from the current date.

**Do effective dates work for all field types?**

Yes — department, location, manager, title, salary, and any custom fields.

**If I move someone with an effective date, do they appear in their old department in the org chart?** No — the org chart always shows the "after" state. Use **Show Before** to see the original state. Forecast is where you see the time-phased view.

## Related Articles

* [Forecast Overview](../forecast/overview.md)
* [Creating and Managing Scenarios](creating-scenarios.md)
* [Scenario Tracking & Analysis](/broken/pages/BweIAu0kM4eCKuYXwrHV)
