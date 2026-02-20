---
description: Filtering positions and sorting columns in Directory
hidden: false
---

# Filtering & Sorting

## Sorting

Click a column header to sort ascending (↑); click again to sort descending (↓); click a third time to remove the sort.

**Multi-column sort:** Click first header for primary sort, then Shift+click additional headers for secondary/tertiary sort. Example: Department (A→Z) → Pay Grade (high→low) → Salary (high→low).

## Filtering

1. Click the **Filter** icon
2. Select an attribute (Department, Location, Pay Grade, etc.)
3. Choose values to include
4. Click **Apply**

Active filters appear as tags above the table. Multiple filters use **AND logic** — all conditions must be true. Click the X on any tag to remove it; use Clear All to reset.

**Filter by calculated fields:** Direct SOC = 1–2 (low spans), Layer = 6+ (deep org), Total Org Size > 50 (large orgs).

**Filter by empty values:** Employee Name = (empty) finds vacant positions.

**Important:** Active filters persist across Directory and Org Chart views. Always check for active filters if data looks unexpected.

## Search

Type in the search box to find positions by name, title, or any attribute. Partial matches work; case-insensitive. Search only works on currently filtered (visible) rows.

## Common Workflows

**Analyze department compensation:** Filter = Department > Sort = Salary (high→low) > Export CSV.

**Find compression:** Filter = Direct SOC = 1–2 AND Pay Grade > 12 > Sort = Layer (low→high).

**Vacancy list for recruiting:** Filter = Employee Name = (empty) > Sort = Department (A→Z) > Export CSV.

**Pay equity check:** Filter = Job Title = "Software Engineer" > Sort = Salary (high→low) to compare across departments/locations.

**Find recent hires:** Sort = Start Date (newest→oldest).

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Can't find expected positions | Check active filters; clear all and search again |
| Sort not working | Remove existing sort (click header 3×), then re-sort |
| Filter options missing a value | That value doesn't exist in the data; check import |
| Search returns no results | Search only scans filtered rows; clear filters and retry |

## Related Articles

- [Column Customization](columns-customization.md)
- [Bulk Operations](bulk-operations.md)
- [Exporting](exporting.md)
