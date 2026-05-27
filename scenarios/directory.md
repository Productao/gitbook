---
description: Table view in scenarios with change highlighting
icon: magnifying-glass
---

# Scenario Directory

The Scenario Directory is a spreadsheet-style table of all positions with change highlighting, bulk selection, and export. Unlike the Main Org Directory (view-only), Scenario Directory lets you select, bulk edit, and export changed data.

**How to Access:** Click the Directory icon in the toolbar, select it from the Org Chart dropdown, or press `2`.

<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

## Filtering for Changes

Use filters to focus on specific change types:

* **Change Type = Addition** — Review all new positions before submitting
* **Change Type = Reduction** — Audit all RIFs
* **Change Type = Modification** — See what was edited and at what cost

**Common combinations:**

`Department = "Engineering" AND Change Type = "Addition"` (all new Engineering hires); `Change Type ≠ "No Change"` (all changes only, for export to Finance).

## Bulk Selection and Editing

Scenario Directory supports mass selection for bulk actions:

* **Click checkbox** to select individual rows
* **Click header checkbox** to select all visible (filtered) rows
* **Shift+click** to select a range

Once selected, the bulk edit panel opens. Available actions: Edit Attributes, Change Manager, Close Positions, Detach Employees, Move to Bench, Export Selection.

**Learn more:** [Bulk Operations](bulk-operations.md)

## Exporting from Directory

1. Set filters and visible columns as desired
2. Click **Export** > choose file (CSV, Comparison CSV) and scope (all/selected fields)
3. Export includes all visible columns: change indicators, before/after values, cost impact, effective dates

## Troubleshooting

| Problem                        | Solution                                                                                                                |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| Scenario status column missing | Click column settings > check "Scenario status"                                                                         |
| Bulk selection not working     | Confirm you're in a Scenario (Main Org Directory is view-only)                                                          |
| Color-coding not showing       | Refresh the page                                                                                                        |
| Can't edit in Directory        | Confirm that you are in a scenario. Select positions > use bulk edit panel, or click a position to open the edit panel. |

## Related Articles

* [Bulk Operations](bulk-operations.md)
* [Scenario Exporting](exporting.md)
