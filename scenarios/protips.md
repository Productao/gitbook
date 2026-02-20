---
description: Pro tips and best practices for effective scenario planning
icon: lightbulb
---

# Scenario Protips

## Naming and Organization

Use descriptive names: `"2026 Q1 Sales Reorg - West Coast"` not `"New Scenario"`. Include time period, purpose, scope, and version when iterating.

Create a consistent tagging system: time-based tags (Q1 2026), status tags (Draft/In Review/Approved), type tags (Hiring Plan/Reorg/Budget Cut).

## Backup Before Major Operations

Duplicate your scenario before: a scenario refresh, merging, large bulk operations, or wide sharing. In the scenario actions menu (⋮) > Duplicate Scenario. Name the backup with a date (e.g., "Plan - BACKUP 2026-02-18").

## Efficiency

**Keyboard shortcuts:** `3` = Org Chart, `5` = Directory, Cmd/Ctrl+K = search, Cmd/Ctrl+S = save, Cmd/Ctrl+Z = undo.

**Bulk operations:** Use Select Team to grab a manager + all direct reports. In Directory view, apply a filter and use the header checkbox to select all filtered rows. See [Bulk Operations](bulk-operations.md).

**Save filter views:** Save combinations like "Open Positions Only" or "Changed in This Scenario" to quickly return to focused views.

## Collaboration

Use Comments to explain changes, tag collaborators (@mention), and document assumptions. This is especially important for changes that might need justification during approval.

Give edit access only to active collaborators; use view-only for stakeholders who just need visibility.

## Quality Control

**Before finalizing:** Always switch to "Show Changes" mode to see the delta — don't just work in "Show After." Catch unintended modifications before submission.

**Validate in multiple views:**
- **Org Chart** — Does the structure look correct visually?
- **Directory** — Are all attributes consistent?
- **Forecast** — Is the timing accurate?
- **Workforce Hub** — Are span of control and layers healthy?

## Effective Dates: Don't Skip Them

Always set effective dates for time-specific changes. Without them, Forecast treats changes as immediate. See [Time-Based Planning](time-based-planning.md).

## Before Submitting for Approval

- [ ] Name is clear and descriptive
- [ ] Justification explains business rationale and expected outcomes
- [ ] All changes reviewed in "Show Changes" mode
- [ ] Cost impact and headcount delta match targets
- [ ] Effective dates are set correctly
- [ ] Key views exported for documentation

## Common Mistakes

**No effective dates on future changes** → Forecast shows wrong timing; costs hit budget in the wrong period.

**Working on months-old scenarios** → Baseline drifts from current Main Org. Create a new scenario or use Scenario Refresh.

**Edit access too broad** → Conflicting edits and unintended changes. Limit edit access; use view-only for most stakeholders.

**Only using "Show After" mode** → Misses unintended changes. Always review "Show Changes" before submitting.

## Related Articles

- [Creating Scenarios](creating-scenarios.md)
- [Time-Based Planning](time-based-planning.md)
- [Scenario Comparisons](comparisons.md)
- [Organizing Scenarios](management/organizing-scenarios.md)
