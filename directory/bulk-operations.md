---
description: Selecting multiple positions and performing bulk edits in Scenario Directory
icon: pen-to-square
---

# Bulk Operations

Bulk operations in Directory let you select multiple positions and apply changes simultaneously. Available in Scenario Directory only — not in Main Org Directory (view-only).

## Selecting Positions

* **Single** — Click a row to select it
* **Multiple** — Check the checkboxes in the first column
* **All visible** — Check the header checkbox — selects all rows matching current filters only (not hidden rows). Always filter to your intended subset before using Select All.
* **Range** — `Shift+click` to select a range of rows

## Bulk Edit Actions

After selecting positions, click **Bulk Edit** to apply changes:

* **Department, Location, Pay Grade, Manager, custom fields** — Change the value for all selected positions simultaneously
* **Salary adjustments** — Apply a flat amount or percentage increase to all selected positions
* **Close positions** — Mark multiple positions as closed (RIF reason); tracked in the OpEx Panel as cost savings

<figure><img src="../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

A preview shows which positions will change and their old/new values — review before confirming.

## Common Workflows

**Move a team to a new manager** — Filter by Manager = \[old manager] > Select All > Bulk Edit > Manager > \[new manager]

**Apply merit increases by pay grade** — Filter by Pay Grade = 10 > Select All > Bulk Edit > Salary > +3% > repeat for other grades

**Close positions for RIF** — Filter by department + criteria > select target positions > Bulk Close > RIF reason > verify cost impact in OpEx Panel

**Relocate a remote team** — Filter to Department + Location = Remote > Select All > Bulk Edit > Location > \[office city]

## Change Tracking

All bulk changes are tracked in the OpEx Panel — change type, old and new values, and timestamp. Review there after applying bulk edits to verify the expected impact.

## Troubleshooting

<table><thead><tr><th width="336.53125">Problem</th><th>Solution</th></tr></thead><tbody><tr><td>No checkboxes / Bulk Edit button missing</td><td>Must be in Scenario Directory — Main Org Directory is view-only</td></tr><tr><td>Select All doesn't select everyone</td><td>Only selects visible (filtered) rows — clear filters to expand selection</td></tr><tr><td>Bulk edit applied wrong changes</td><td>Use Undo immediately, or restore from a scenario duplicate made before the operation</td></tr><tr><td>Changes not in OpEx Panel</td><td>Refresh the tracker panel; verify changes were applied by reviewing positions individually</td></tr></tbody></table>

## Related Articles

* [Scenario Directory](../scenarios/directory.md)
* [Filtering & Sorting](filtering-sorting.md)
