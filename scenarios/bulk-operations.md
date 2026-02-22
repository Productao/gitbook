---
description: Editing multiple positions at once
hidden: false
---

# Bulk Operations

Make the same change to many positions at once instead of editing one by one.

## Three Ways to Select Multiple Positions

**Org chart multi-select** — Hold Cmd (Mac) or Ctrl (Windows) and click position cards. Best for cherry-picking specific visible positions (up to ~20).

**Select Team** — Hover over a manager > **⋮** > **Select Team** — selects the manager + all direct reports. Best for acting on an entire team.

**Directory selection** — Switch to Directory view, apply filters to narrow down positions, then click the header checkbox to select all filtered rows. Best for large-scale operations (50+ positions) or cross-departmental selections.

> Always review the selection count and list in the bulk edit panel before applying.

## Bulk Actions

Once positions are selected, the bulk edit panel opens on the right:

**Edit Attributes** — Change department, location, job function, pay grade, or any custom field for all selected positions simultaneously.

> Salary is typically not bulk-editable — it requires individual consideration.

**Change Manager** — Reassign all selected positions to report to a different manager. Use this for consolidating teams or restructuring after a manager departure.

**Close Positions (Bulk RIF)** — Mark multiple positions as closed (Layoff/RIF or Exit/Voluntary). Tracks cost savings in OpEx Panel and preserves history. Use Close, not Delete, for real org reductions.

**Detach Employees** — Remove employees from multiple positions, leaving positions vacant and employees available for reassignment.

**Move to Bench** — Remove employees from the org chart entirely and place them on the bench. Difference: Detach keeps positions filled-but-vacant; Move to Bench removes employees from the structure.

**Duplicate** — Create multiple copies of a position (works best for single-position duplication). Duplicate first, then bulk edit the copies to customize specialties or attributes.

## Common Workflows

**Reorganize a whole team:** Directory > Filter by Manager = "Name" > select all > Change Manager to new lead.

**Model a department budget cut:** Directory > Filter by department + pay grade > select target positions > Close Positions > Layoff (RIF) > verify savings in OpEx Panel.

**Standardize job titles:** Org chart > Cmd/Ctrl+click inconsistently-titled positions > Edit Attributes > Job Title > new standard value.

**Scale a team:** Duplicate one position (e.g., 10x "Software Engineer") > select all copies > Edit Attributes to customize specialties or locations.

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Multi-select (org chart) | Cmd/Ctrl+click |
| Quick-select while hovering | X key |
| Select all (Directory) | Cmd/Ctrl+A |
| Deselect all | Esc |

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Can't multi-select in org chart | Hold Cmd/Ctrl while clicking; or use Directory view |
| Bulk edit panel won't open | Select at least 2 positions |
| Some positions didn't change | Those may have field restrictions; check Activity Log |
| Wrong positions selected | Use Undo (Cmd/Ctrl+Z) immediately, or check Activity Log to revert |
| Directory selected too many | Refine filters, or manually deselect rows before applying |

## Related Articles

- [Scenario Directory](directory.md)
- [Making Position Changes](making-position-changes.md)
- [Time-Based Planning](time-based-planning.md)
