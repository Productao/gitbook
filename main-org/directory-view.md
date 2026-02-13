---
description: Table view of organizational data
icon: list
hidden: false
---

# Directory View

Directory View is your spreadsheet-style table for viewing, sorting, filtering, and exporting organizational data. While the org chart shows visual hierarchy, Directory View lets you analyze data in rows and columns.

## What is Directory View?

Directory View displays all positions and people in your org as a table, similar to Excel or Google Sheets. Each row represents a position or employee, and each column represents an attribute (Name, Title, Department, Salary, etc.).

**When to use Directory View:**
- Sort data by any column (e.g., salary high-to-low)
- Filter to find specific positions quickly
- Export lists to CSV for Excel analysis
- View many attributes at once without cluttering org chart cards
- Analyze data that's easier to see in table format

**When to use Org Chart View:**
- Visualize reporting relationships
- Understand org structure and hierarchy
- Present to stakeholders
- Navigate teams visually

---

## Accessing Directory View

**From Main Org:**
1. Click the **Directory** icon in the left toolbar (table/grid symbol)
2. Or press keyboard shortcut **5** from anywhere

**From Homepage:**
- Click **Directory** in the top navigation

---

## Directory View Interface

### Columns

Each column represents an attribute in your org:

**Standard columns:**
- Name
- Job Title
- Department
- Manager
- Location
- Pay Grade
- Salary

**Custom columns:**
- Any fields your admin has configured
- Calculated fields (SOC, Total Org Size, Layer)

### Customizing Columns

**Add/remove columns:**
1. Click the column settings icon (gear or three dots)
2. Check/uncheck columns to show/hide
3. Changes apply immediately

**Reorder columns:**
- Drag column headers to rearrange

**Resize columns:**
- Drag the column border to adjust width

---

## Sorting

Sort data by any column:

1. Click a column header to sort ascending
2. Click again to sort descending
3. Click a third time to remove sort

**Multi-column sorting:**
- Hold Shift and click multiple column headers
- Data sorts by first column, then second, then third, etc.

**Common sorts:**
- Salary (high to low)
- Department (alphabetical)
- Start Date (newest to oldest)
- Layer (shallowest to deepest)

---

## Filtering

Apply filters to show only specific rows:

1. Click the **Filter** icon
2. Select an attribute (Department, Location, Pay Grade, etc.)
3. Choose values to include
4. Click **Apply**

**Multiple filters:**
- Add multiple filters to narrow results
- Filters combine with AND logic (all conditions must be true)

**Clear filters:**
- Click Filter → Clear All

**Pro tip:** Filters in Directory View are the same as filters in Org Chart View. Changing filters in one affects the other.

---

## Search

Find specific positions or people:

1. Use the search box at the top of Directory View
2. Type a name, title, or attribute value
3. Matching rows highlight
4. Click a row to select it

---

## Selecting Rows

Click a row to select it:
- Selected row highlights
- Click the position's name to open details
- Click the org chart icon to navigate to that position in org chart view

**Bulk selection:**
- Check the checkbox column to select multiple rows
- Select all rows matching current filters
- Export selected rows

---

## Exporting from Directory View

Export filtered data to CSV for Excel analysis:

1. Apply filters to show only the data you want
2. Click the **Export** button
3. Choose **CSV**
4. Download the file

**What gets exported:**
- All visible columns
- All rows matching current filters
- Raw data (no formulas or formatting)

**Custom export templates (Admin):**
- Admins can configure standard export templates
- Pre-defined column orders and selections
- Available from the Export menu

---

## Linking Between Directory and Org Chart

Directory View and Org Chart View are two views of the same data:

**From Directory to Org Chart:**
- Click the org chart icon next to a position
- Navigates to that position in org chart view

**From Org Chart to Directory:**
- Click the Directory icon in the toolbar
- Current filters and selections carry over

---

## Common Use Cases

### Find Highest-Paid Positions
1. Go to Directory View
2. Sort by Salary column (high to low)
3. Review top positions

### Export Engineering Department List
1. Filter to Department = Engineering
2. Customize columns (Name, Title, Location, Salary)
3. Export to CSV

### Find All Positions in a Pay Grade
1. Filter to Pay Grade = 14
2. Sort by Department
3. Review list or export

### Analyze Managers with Low SOC
1. Filter to Span of Control = 1-2
2. Sort by Layer
3. Identify compression opportunities

### Create a Contact List
1. Filter to specific department or location
2. Show columns: Name, Email, Manager
3. Export to CSV

---

## Directory View vs Org Chart View

| Feature | Directory View | Org Chart View |
|---------|----------------|----------------|
| Format | Table (rows/columns) | Visual hierarchy |
| Sorting | ✅ Yes | ❌ No |
| Filter | ✅ Yes | ✅ Yes |
| Search | ✅ Yes | ✅ Yes |
| Export | CSV | JPEG, PowerPoint, CSV |
| View many attributes | ✅ Easy | ⚠️ Clutters cards |
| See reporting structure | ⚠️ Column only | ✅ Visual |
| Bulk selection | ✅ Yes | ⚠️ Limited |
| Edit positions | ❌ No (in Main Org) | ❌ No (in Main Org) |

---

## Best Practices

1. **Use Directory for data analysis** - Sorting and filtering are easier in table format
2. **Use Org Chart for relationships** - Visualize reporting structure
3. **Customize columns for your needs** - Don't show everything; focus on relevant attributes
4. **Filter before exporting** - Export only the data you need
5. **Remember filters carry over** - Filters apply to both Directory and Org Chart views
6. **Sort to find outliers** - Highest/lowest salary, longest tenure, etc.

---

## Tips and Tricks

- **Double-click column border** - Auto-resize column to fit content
- **Shift + click column headers** - Sort by multiple columns
- **Use search for quick lookups** - Faster than scrolling through long lists
- **Export with filters** - Create custom lists by filtering first
- **Link back to org chart** - Click positions to see visual context

---

## Limitations

Directory View in Main Org is view-only:

- Cannot edit position attributes
- Cannot add or delete positions
- Cannot move people between positions
- Cannot bulk edit multiple positions

**To make changes:** Create a Scenario. Scenarios have editable Directory Views where you can make bulk changes.

---

## Keyboard Shortcuts

- **5** - Jump to Directory View
- **1** - Return to Org Chart View
- **Cmd/Ctrl + F** - Open search
- **Esc** - Clear selection or close dialogs

---

## Troubleshooting

**Problem:** I don't see all my positions.
- **Solution:** Check active filters. Click Filter → Clear All.

**Problem:** Columns are missing.
- **Solution:** Click column settings and check the columns you want to see.

**Problem:** Data looks different than Org Chart.
- **Solution:** Verify filters are the same. Filters apply to both views.

**Problem:** Export doesn't include all data.
- **Solution:** Check that all desired columns are visible before exporting.

---

## Next Steps

- Compare with full [Directory module](../directory/overview.md) documentation
- Learn about [Exporting & Reporting](../directory/exporting-reporting.md)
- Explore [Org Metrics & Insights](metrics-insights.md) for calculated fields
- Create a [Scenario](../scenarios/creating-scenarios.md) for editable Directory View
