---
description: Introduction to directory and table views
---

# 📋 Directory Overview

The Directory module is your dedicated table view for analyzing organizational data. While org charts visualize hierarchy, Directory provides a spreadsheet-style interface for sorting, filtering, and exporting position and people data.

> **\[Screenshot placeholder: Directory view showing position table with multiple columns (Name, Title, Department, Manager, Salary)]**

## Directory vs Org Chart

| Feature                  | Directory              | Org Chart                   |
| ------------------------ | ---------------------- | --------------------------- |
| Format                   | Table (rows/columns)   | Visual hierarchy            |
| Best for                 | Data analysis          | Understanding relationships |
| Sorting                  | ✅ Yes                  | ❌ No                        |
| Multiple columns visible | ✅ Many at once         | ⚠️ Limited (card space)     |
| See reporting structure  | ⚠️ Manager column only | ✅ Visual lines              |
| Export                   | CSV lists              | JPEG, PowerPoint, CSV       |
| Find outliers            | ✅ Easy (sort high/low) | ⚠️ Manual search            |

## When to Use Directory

* **Analyze data:** Sort by salary, tenure, pay grade — find highest/lowest values and outliers
* **Create exports:** Department rosters, contact lists, filtered position lists
* **Multi-column comparison:** View many attributes simultaneously
* **Quick lookups:** Find all managers in a location, identify vacant positions
* **Bulk operations (scenarios only):** Select and edit multiple positions at once

## Directory Capabilities

| Feature                     | Learn More                                              |
| --------------------------- | ------------------------------------------------------- |
| Orientation & Navigation    | [Navigation & Access](navigation.md)                    |
| Filtering & Sorting         | [Filtering & Sorting](filtering-sorting.md)             |
| Column Customization        | [Column Customization](columns-customization.md)        |
| Bulk Operations (scenarios) | [Bulk Operations](bulk-operations.md)                   |
| Exporting Data              | [Exporting Data from Directory](exporting-reporting.md) |

## Common Workflows

**Find highest-paid positions:** Sort Salary column high to low.

**Export department roster:** Filter to Department = Engineering > show Name, Title, Email, Manager > Export CSV.

**Identify vacant positions:** Filter Employee Name = (empty) > sort by Department > review or export.

**Analyze pay equity:** Filter to Job Title = "Software Engineer" > sort by Salary > compare across departments.

**Find compression opportunities:** Filter to Direct SOC = 1–2 > sort by Pay Grade (high to low).

## Best Practices

1. **Use Directory for data analysis** — Table format is better for sorting and comparing numbers
2. **Use Org Chart for relationships** — Visual format is better for understanding hierarchy
3. **Filter before exporting** — Don't export everything; narrow to what you need
4. **Customize columns for your task** — Show only relevant attributes
5. **Remember filters carry over** — Active filters affect org chart and directory views

> **\[Screenshot placeholder: Switching between Org Chart and Directory views using the view dropdown]**
