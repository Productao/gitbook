---
description: Table view in scenarios with change highlighting
---

# 🔍 Scenario Directory

The Scenario Directory is a spreadsheet-style table of all positions with change highlighting, bulk selection, and export. Unlike Main Org Directory (view-only), Scenario Directory lets you select, bulk edit, and export changed data.

Access it: click the Directory icon in the toolbar, select it from the Org Chart dropdown, or press **2**.

## Scenario-Specific Columns

In addition to standard fields (Name, Title, Department, Manager, Salary), Scenario Directory shows:

* **Scenario Status** — Addition, Reduction, Modification, or None
* **Effective Date** — When the change takes effect

Enable these via the column selector (gear icon). Showing Scenario Status is recommended when reviewing scenarios.

## Change Highlighting

Rows are color-coded:

* **Green** — Added position
* **Red** — Closed/RIF'd position
* **Blue** — Modified position
* **White** — No change from Main Org

## Filtering for Changes

Use filters to focus on specific change types:

* **Scenario Status = Select All + Unselect "(blanks)"** — Review all new positions before submitting

Common combinations: `Department = "Engineering" AND Scenario Status = "RIF"` (all RIF'ed Engineering positions); `Scenario Status = Select All + Unselect "(blanks)"` (all changes only, for export to Finance).

## Bulk Selection and Editing

Scenario Directory supports mass selection for bulk actions:

* **Click checkbox** to select individual rows
* **Click header checkbox** to select all visible (filtered) rows
* **Shift+click** to select a range

Once selected, the bulk edit panel opens. Available actions: Edit Attributes, Change Manager, Close Positions, Detach Employees, Move to Bench, Export Selection.

**Learn more:** [Bulk Operations](bulk-operations.md)

## Exporting from Directory

1. Set filters and visible columns as desired
2. Click **Export** > choose format (CSV, Excel) and scope (all/filtered/selected)
3. Export includes all visible columns: change indicators, before/after values, cost impact, effective dates

## Troubleshooting

| Problem                                | Solution                                                                                                                |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Change Type column missing             | Click column settings > check "Change Type"                                                                             |
| Seeing all positions, not just changes | Filter: Change Type ≠ "No Change"                                                                                       |
| Bulk selection not working             | Confirm you're in a Scenario (Main Org Directory is view-only)                                                          |
| Color-coding not showing               | Refresh the page                                                                                                        |
| Can't edit in Directory                | Confirm that you are in a scenario. Select positions > use bulk edit panel, or click a position to open the edit panel. |

## Related Articles

* [Bulk Operations](bulk-operations.md)
* [Scenario Tracking & Analysis](/broken/pages/BweIAu0kM4eCKuYXwrHV)
* [Scenario Exporting](exporting.md)
