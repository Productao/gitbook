---
description: Selecting multiple positions and performing bulk edits in Scenario Directory
hidden: false
---

# Bulk Operations (Directory)

Bulk operations in the Directory view let you select multiple positions and apply changes simultaneously. Available only in Scenario Directory — not in Main Org Directory (view-only).

## Selecting Positions

**Single:** Click a row to select it.

**Multiple:** Check checkboxes in the first column.

**All visible:** Check the header checkbox — selects all rows matching current filters only (not hidden rows). Always filter to your intended subset before using Select All.

**Range:** Shift+click to select a range of rows.

## Bulk Edit Actions

After selecting positions, click **Bulk Edit** to apply changes:

- **Department, Location, Pay Grade, Manager, custom fields:** Change the value for all selected positions simultaneously
- **Salary adjustments:** Apply a flat amount or percentage increase to all selected positions
- **Close positions:** Mark multiple positions as closed (RIF reason); tracked in OpEx Panel as cost savings

A preview shows which positions will change and their old/new values — review before confirming.

## Common Workflows

**Move team to new manager:** Filter by Manager = [old manager] > Select All > Bulk Edit > Manager > [new manager]

**Apply merit increases by pay grade:** Filter by Pay Grade = 10 > Select All > Bulk Edit > Salary > +3% > repeat for other grades

**Close positions for RIF:** Filter by department + criteria > select target positions > Bulk Close > RIF reason > verify cost impact in OpEx Panel

**Relocate remote team:** Filter to Department + Location = Remote > Select All > Bulk Edit > Location > [office city]

## Change Tracking

All bulk changes are tracked in the OpEx Panel panel — change type, old and new values, timestamp. Review there after applying bulk edits to verify expected impact.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No checkboxes / Bulk Edit button missing | Must be in Scenario Directory; Main Org Directory is view-only |
| Select All doesn't select everyone | Only selects visible (filtered) rows; clear filters to expand selection |
| Bulk edit applied wrong changes | Use scenario undo (Cmd/Ctrl+Z) immediately; or restore from scenario duplicate made before the operation |
| Changes not in OpEx Panel | Refresh the tracker panel; verify changes were applied by reviewing positions individually |

## Related Articles

- [Scenario Directory](../scenarios/directory.md)
- [Filtering & Sorting](filtering-sorting.md)
- [Scenario Tracking & Analysis](../scenarios/tracking-analysis.md)
