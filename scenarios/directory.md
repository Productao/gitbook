---
description: Table view in scenarios with change highlighting
hidden: false
---

# Scenario Directory

The Scenario Directory is a spreadsheet-style table of all positions with change highlighting, bulk selection, and export. Unlike Main Org Directory (view-only), Scenario Directory lets you select, bulk edit, and export changed data.

Access it: click the Directory icon in the taskbar, select it from the Org Chart dropdown, or press **5**.

## Scenario-Specific Columns

In addition to standard fields (Name, Title, Department, Manager, Salary), Scenario Directory shows:
- **Change Type** — Addition, Reduction, Modification, or None
- **Effective Date** — When the change takes effect
- **Cost Impact** — Dollar impact of the change
- **Before/After values** — Original and new values for modifications

Enable these via the column selector (gear icon). Showing Change Type and Cost Impact is recommended when reviewing scenarios.

## Change Highlighting

Rows are color-coded:
- **Green** — Added position
- **Red** — Closed/RIF'd position
- **Blue** — Modified position
- **White** — No change from Main Org

## Filtering for Changes

Use filters to focus on specific change types:
- **Change Type = Addition** — Review all new positions before submitting
- **Change Type = Reduction** — Audit all RIFs
- **Change Type = Modification** — See what was edited and at what cost
- **Effective Date range** — See all Q1 or Q2 changes

Common combinations: `Department = "Engineering" AND Change Type = "Addition"` (all new Engineering hires); `Change Type ≠ "No Change"` (all changes only, for export to Finance).

## Bulk Selection and Editing

Scenario Directory supports mass selection for bulk actions:
- **Click checkbox** to select individual rows
- **Click header checkbox** to select all visible (filtered) rows
- **Shift+click** to select a range

Once selected, the bulk edit panel opens. Available actions: Edit Attributes, Change Manager, Close Positions, Detach Employees, Move to Bench, Export Selection.

**Learn more:** [Bulk Operations](bulk-operations.md)

## Exporting from Directory

1. Set filters and visible columns as desired
2. Click **Export** > choose format (CSV, Excel) and scope (all/filtered/selected)
3. Export includes all visible columns: change indicators, before/after values, cost impact, effective dates

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Change Type column missing | Click column settings > check "Change Type" |
| Seeing all positions, not just changes | Filter: Change Type ≠ "No Change" |
| Bulk selection not working | Confirm you're in a Scenario (Main Org Directory is view-only) |
| Color-coding not showing | Refresh the page |
| Can't edit in Directory | Select positions > use bulk edit panel, or click a position to open the edit panel |

## Related Articles

- [Bulk Operations](bulk-operations.md)
- [Scenario Tracking & Analysis](tracking-analysis.md)
- [Scenario Exporting](exporting.md)
