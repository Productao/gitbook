---
description: Accessing Directory and switching between views
hidden: false
---

# Navigation & Access

Learn how to access Directory, switch between table and org chart views, and navigate large datasets effectively.

## Accessing Directory

Directory can be accessed from multiple locations throughout Agentnoon:

### From Homepage
- Click **Directory** in the top navigation bar
- Press keyboard shortcut **5**
- Fastest way to access standalone Directory view

### From Main Org or Scenarios
- Click the **Directory/Table** icon in the left toolbar
- Toggle between org chart and table view
- Context remains (same filters, same scenario)
- View switches but data stays consistent

### From Workforce Hub
- Some charts include "View in Directory" links
- Click to see underlying data in table format
- Automatically filters to chart data subset
- Opens Directory with relevant positions

---

## Directory Modes

Directory works differently depending on where you access it from:

### Main Org Directory (View-Only)

**What you can do:**
- View current org data
- Sort by any column
- Filter positions
- Search for people or positions
- Export to CSV
- Customize visible columns

**What you cannot do:**
- Edit position attributes
- Make org changes
- Bulk edit multiple positions

**When to use:**
- Analyzing current organization
- Creating reports and exports
- Quick lookups and searches

---

### Scenario Directory (Editable)

**What you can do:**
- Everything in Main Org Directory PLUS:
- Edit position attributes
- Bulk select multiple positions
- Apply bulk edits
- Add or close positions
- See change tracking symbols
- Model "what-if" scenarios

**When to use:**
- Planning organizational changes
- Modeling reorganizations
- Testing different structures
- Preparing for hiring/budget planning

**Learn more:** [Scenario Directory](../scenarios/directory.md)

---

### Forecast Directory

**What you can do:**
- View forecasted headcount
- Analyze planned positions by quarter/year
- Filter by time period
- Export forecast data

**What you cannot do:**
- Edit positions (forecast is aggregate planning)
- Make individual position changes

**When to use:**
- Reviewing hiring plans
- Analyzing future headcount projections
- Validating forecast against scenarios

**Learn more:** [Forecast Overview](../forecast/overview.md)

---

## Switching Between Views

### From Directory to Org Chart

**Method 1: Toolbar icon**
1. Click the **Org Chart** icon in the left toolbar
2. View switches to visual hierarchy
3. Filters and selections persist

**Method 2: Position link**
1. Click the org chart icon next to a position name
2. Navigates to that specific position in org chart
3. Position becomes focal point
4. Preserves context

---

### From Org Chart to Directory

**Method:**
1. Click the **Directory/Table** icon in left toolbar
2. View switches to table format
3. Same positions visible
4. Filters remain active

**Tip:** Use keyboard shortcut **1** to return to org chart view from Directory.

---

## Navigating Large Datasets

### Pagination Controls

**Rows per page:**
- Options: 25, 50, 100, 500
- Select larger values to see more data at once
- Located at bottom of Directory table

**Page navigation:**
- Use Next/Previous buttons
- Or jump to specific page number (1, 2, 3...)
- Total row count displayed

**Tips:**
- Increase rows per page for smaller datasets (< 500 rows)
- Keep default (25-50) for very large orgs (1000+ positions)
- Use filters to reduce total rows before viewing

---

### Sorting Across Pages

**Important:** Sorting works across ALL pages, not just the current page.

**Example:**
- You have 500 positions across 10 pages (50 per page)
- Sort by Salary (high to low)
- Page 1 shows the 50 highest salaries across entire org
- Page 2 shows the next 50 highest salaries
- And so on...

---

### Filtering to Reduce Pages

**Strategy:**
1. Apply filters first to narrow data
2. Sort filtered results
3. Reduce pagination needs
4. Easier to analyze focused subset

**Example:**
- Start with 800 positions
- Filter to Department = Engineering
- Now viewing 150 positions (3 pages)
- Much easier to navigate and analyze

---

## Keyboard Shortcuts

Speed up navigation with these shortcuts:

| Shortcut | Action |
|----------|--------|
| **5** | Jump to Directory module from anywhere |
| **1** | Return to org chart view |
| **Cmd/Ctrl + F** | Open search box |
| **Esc** | Clear selection or close panels |

---

## Directory vs Org Chart

Understanding when to use each view:

| Use Directory When... | Use Org Chart When... |
|----------------------|----------------------|
| Analyzing data in table format | Understanding reporting structure |
| Sorting by attributes | Visualizing hierarchy |
| Comparing multiple columns | Seeing team relationships |
| Finding highest/lowest values | Navigating by manager |
| Creating filtered exports | Presenting to stakeholders |
| Need spreadsheet-like interface | Need visual representation |

**Best practice:** Switch between both views as needed. They complement each other.

---

## Common Navigation Workflows

### Start in Directory, Navigate to Org Chart

**Scenario:** Find highest-paid position, then see their team

**Steps:**
1. Open Directory
2. Sort by Salary (high to low)
3. Click org chart icon next to top position
4. View switches to org chart
5. Position is focal point with full team visible

---

### Start in Org Chart, Switch to Directory

**Scenario:** Viewing an Engineering team, want to export contact list

**Steps:**
1. In org chart, filter to Engineering department
2. Click Directory icon in toolbar
3. Directory opens with same Engineering filter
4. Customize columns (Name, Email, Manager)
5. Export to CSV

---

### Use Hub Chart to Open Directory

**Scenario:** See high-layer positions in Hub chart, want details

**Steps:**
1. View Layers and Spans chart in Hub
2. See positions at Layer 7+
3. Click "View in Directory"
4. Directory opens filtered to Layer 7+ positions
5. Sort by department or salary for further analysis

---

## Best Practices

1. **Use keyboard shortcuts** - Faster than clicking
2. **Filter before paginating** - Reduce total rows first
3. **Switch views freely** - Use both Directory and Org Chart
4. **Remember context persists** - Filters carry across views
5. **Start broad, narrow down** - Begin in Directory, filter to subset, switch to org chart for detail
6. **Increase rows per page for exports** - See more data before exporting

---

## Troubleshooting

**Problem:** Directory shows empty or unexpected data.
- **Solution:** Check active filters (may be hiding positions). Clear filters and try again.

**Problem:** Can't switch between Directory and Org Chart.
- **Solution:** Look for toolbar icons on left side of screen. May need to scroll up to see toolbar.

**Problem:** Pagination is slow or confusing.
- **Solution:** Apply filters to reduce total rows. Use search to find specific positions instead of paging through all rows.

**Problem:** Lost track of which mode (Main Org vs Scenario) I'm in.
- **Solution:** Check top-left corner for scenario name. If it says "Main Org" or no scenario name, you're in view-only mode.

---

## Next Steps

- Learn about [Filtering & Sorting](filtering-sorting.md) to narrow down data
- Explore [Column Customization](columns-customization.md) to show relevant attributes
- Try [Bulk Operations](bulk-operations.md) in Scenario Directory
- Understand [Exporting](exporting.md) to create reports

## Visual Guide

> **[Screenshot placeholder: Accessing Directory from homepage]**

> **[Screenshot placeholder: Switching between Org Chart and Directory views]**

> **[Screenshot placeholder: Directory pagination controls]**
