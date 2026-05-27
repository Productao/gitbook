---
description: Editing multiple positions at once
icon: ball-pile
---

# Bulk Operations

Make the same change across multiple positions at once instead of editing one by one.

## Selecting Multiple Positions

| Method                     | How                                                                                                     | Best for                                                                |
| -------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Org chart multi-select** | Hold `Cmd` (Mac) or `Ctrl` (Windows) and click cards OR Hover over cards and press "x" on your keyboard | Cherry-picking specific visible positions (up to \~20)                  |
| **Select Team**            | Hover over a manager > ⋮ > Select Team                                                                  | Acting on an entire team                                                |
| **Directory selection**    | Switch to Directory, apply filters, click the header checkbox to select all filtered rows               | Large-scale operations (50+ positions) or cross-departmental selections |

Always review the selection count and list in the bulk edit panel before applying.

## Bulk Actions

Once positions are selected, the bulk edit panel opens on the right:

* **Edit Attributes** - Change department, location, job function, pay grade, or any custom field for all selected positions simultaneously. Note: salary is typically not bulk-editable and requires individual consideration.
* **Change Manager** - Reassign all selected positions to a different manager. Use for consolidating teams or restructuring after a manager departure.
* **Close Positions (Bulk RIF)** - Mark multiple positions as closed (Layoff/RIF or Exit/Voluntary). Tracks cost savings in the OpEx Panel and preserves history. Use Close, not Delete, for real org reductions.
* **Detach Employees** - Remove employees from multiple positions, leaving positions vacant and employees available for reassignment.
* **Move to Bench** - Remove employees from the org chart and place them on the bench. Note: Detach leaves positions vacant; Move to Bench removes employees from the structure entirely.
* **Duplicate** - Create multiple copies of a position. Duplicate first, then bulk edit the copies to customize attributes.

## Common Workflows

**Reorganize a whole team** - Directory > Filter by Manager = "Name" > select all > Change Manager to new lead.

**Model a department budget cut** - Directory > Filter by department + pay grade > select target positions > Close Positions > Layoff (RIF) > verify savings in OpEx Panel.

**Standardize job titles** - Org Chart > `Cmd/Ctrl+click` inconsistently-titled positions > Edit Attributes > Job Title > enter new standard value.

**Scale a team** - Duplicate one position (e.g., 10x "Software Engineer") > select all copies > Edit Attributes to customize specialties or locations.

## Keyboard Shortcuts

| Action                      | Shortcut            |
| --------------------------- | ------------------- |
| Multi-select (org chart)    | `Cmd/Ctrl+click`    |
| Quick-select while hovering | `X`                 |
| Select all (Directory)      | `select all button` |
| Deselect all                | `Esc`               |

## Troubleshooting

| Problem                         | Solution                                                             |
| ------------------------------- | -------------------------------------------------------------------- |
| Can't multi-select in org chart | Hold `Cmd/Ctrl` while clicking, or switch to Directory view          |
| Bulk edit panel won't open      | Select at least 2 positions                                          |
| Some positions didn't change    | Those positions may have field restrictions — check the Activity Log |
| Wrong positions selected        | Use Undo immediately from the Activity Log to revert                 |
| Directory selected too many     | Refine your filters, or manually deselect rows before applying       |

## Related Articles

* [Scenario Directory](directory.md)
* [Making Position Changes](making-position-changes.md)
* [Time-Based Planning](time-based-planning.md)
