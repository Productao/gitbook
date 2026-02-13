---
description: Introduction to directory and table views
icon: table-list
hidden: false
---

# Directory Overview

The Directory module is your dedicated table view for analyzing organizational data. While org charts visualize hierarchy, Directory provides a spreadsheet-style interface for sorting, filtering, and exporting position and people data.

## What is Directory?

Directory is Agentnoon's table-based view of your organization. It displays all positions and people as rows in a table, with attributes as columns - similar to Excel or Google Sheets.

**Key characteristics:**
- **Table format** - Rows and columns instead of visual hierarchy
- **Sortable** - Click any column header to sort
- **Filterable** - Show only positions matching criteria
- **Exportable** - Download filtered lists as CSV
- **Customizable** - Choose which columns to display
- **Accessible from anywhere** - Standalone module or accessed from Main Org/Scenarios

## Directory vs Org Chart

| Feature | Directory | Org Chart |
|---------|-----------|-----------|
| Format | Table (rows/columns) | Visual hierarchy |
| Best for | Data analysis | Understanding relationships |
| Sorting | ✅ Yes | ❌ No |
| Multiple columns visible | ✅ Many at once | ⚠️ Limited (card space) |
| See reporting structure | ⚠️ Manager column only | ✅ Visual lines |
| Export | CSV lists | JPEG, PowerPoint, CSV |
| Find outliers | ✅ Easy (sort high/low) | ⚠️ Manual search |

## When to Use Directory

Use Directory when you need to:

### 1. Analyze Data in Table Format
- Sort by salary, tenure, pay grade, etc.
- Find highest/lowest values
- Compare attributes across positions
- Identify outliers and anomalies

### 2. Create Lists and Exports
- Export department rosters
- Generate contact lists
- Create filtered position lists
- Download data for Excel analysis

### 3. Multi-Column Comparison
- View many attributes simultaneously
- Compare positions side-by-side
- Analyze relationships between fields

### 4. Quick Lookups
- Find all positions in a pay grade
- List all managers in a location
- Identify vacant positions
- Search by any attribute

### 5. Bulk Operations (in Scenarios)
- Select multiple positions
- Apply bulk edits
- Filter and mass-update

## Accessing Directory

**Three ways to access Directory:**

### 1. From Homepage
- Click **Directory** in the top navigation
- Press keyboard shortcut **5**

### 2. From Main Org or Scenarios
- Click the **Directory/Table** icon in the left toolbar
- Toggle between org chart and table view

### 3. From Workforce Hub
- Some charts have "View in Directory" links
- Click to see the underlying data in table format

## Directory Modes

Directory works in different contexts:

### Main Org Directory (View-Only)
- View current org data
- Sort and filter
- Export lists
- Cannot edit positions

### Scenario Directory (Editable)
- All Main Org capabilities PLUS:
- Edit position attributes
- Bulk select and edit multiple positions
- Add or close positions
- See change tracking

### Forecast Directory
- View forecasted headcount
- Analyze planned positions by quarter
- Export forecast data

## Key Features

### Sortable Columns
Click any column header to sort:
- Once: Ascending (A→Z, low→high)
- Twice: Descending (Z→A, high→low)
- Three times: Remove sort

**Multi-column sorting:**
- Hold Shift and click multiple headers
- Sort by Department, then by Salary, then by Title

### Filterable Rows
Apply filters to show only specific positions:
- Click Filter icon
- Select attribute and values
- Multiple filters combine with AND logic
- Clear filters to reset

### Customizable Columns
Choose which attributes to display:
- Click column settings (gear icon)
- Check/uncheck columns
- Drag headers to reorder
- Resize columns by dragging borders

### Search
Find positions quickly:
- Use search box to find names, titles, or values
- Matching rows highlight
- Click to select

### Export
Download filtered data:
- Export to CSV for Excel
- All visible columns included
- Only filtered rows included
- Custom templates available (admin-configured)

## Common Workflows

### Find Highest-Paid Positions
1. Go to Directory
2. Sort Salary column (high to low)
3. Review top positions

### Export Department Roster
1. Filter to Department = Engineering
2. Customize columns (Name, Title, Email, Manager)
3. Export to CSV

### Identify Vacant Positions
1. Filter to Employee Name = (empty)
2. Sort by Department
3. Review or export list

### Analyze Pay Equity
1. Filter to Job Title = "Software Engineer"
2. Sort by Salary
3. Compare ranges across departments or locations

### Find Compression Opportunities
1. Filter to Direct SOC = 1-2
2. Sort by Pay Grade (high to low)
3. Identify senior managers with low spans

## Directory in Different Modules

### Main Org Directory
- View-only current org data
- Sort, filter, search, export
- Cannot make changes

### Scenario Directory
- Editable copy of org data
- Make changes to model scenarios
- Bulk edit multiple positions
- See change tracker impact

### Forecast Directory
- View forecasted positions
- Filter by quarter or year
- Export forecast data
- Cannot edit (forecast is aggregate planning)

## Best Practices

1. **Use Directory for data analysis** - Table format is better for sorting and comparing
2. **Use Org Chart for relationships** - Visual format is better for understanding hierarchy
3. **Filter before exporting** - Don't export everything; narrow to what you need
4. **Customize columns for your task** - Show only relevant attributes
5. **Save common views** - Create presets for frequently-used column configurations
6. **Sort to find outliers** - Highest/lowest values, newest/oldest, etc.
7. **Remember filters carry over** - Active filters affect org chart and directory views

## Limitations (Main Org Directory)

- **View-only** - Cannot edit positions in Main Org Directory
- **No visual hierarchy** - Must use org chart to see reporting structure
- **Limited bulk actions** - Cannot select and edit multiple positions in Main Org

**To make changes:** Create a Scenario. Scenario Directory is fully editable.

## Next Steps

- Learn about [Directory Features](features.md) in detail
- Explore [Exporting & Reporting](exporting-reporting.md) options
- Compare with [Main Org Directory View](../main-org/directory-view.md)
- Try the [Scenario Directory](../scenarios/directory.md) for editing capabilities
