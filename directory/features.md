---
description: Sorting, filtering, and customizing directory views
icon: sliders
hidden: false
---

# Directory Features

Directory provides powerful tools for analyzing organizational data in table format. Master these features to quickly find insights, create custom views, and export exactly the data you need.

## Sorting

Sort data by any column to find outliers, compare values, or organize data logically.

### Basic Sorting

**How to sort:**
1. Click a column header once → Sort ascending (A→Z, 0→9, low→high)
2. Click again → Sort descending (Z→A, 9→0, high→low)
3. Click a third time → Remove sort (return to default order)

**Visual indicators:**
- Ascending arrow ↑ appears in column header
- Descending arrow ↓ appears in column header
- No arrow = no sort applied

### Multi-Column Sorting

Sort by multiple columns simultaneously:

1. Click first column header to set primary sort
2. Hold **Shift** and click second column header for secondary sort
3. Hold **Shift** and click third column for tertiary sort

**Example:**
- Primary sort: Department (A→Z)
- Secondary sort: Pay Grade (high→low)
- Tertiary sort: Salary (high→low)

**Result:** Positions grouped by department, then by pay grade within each department, then by salary within each pay grade.

### Common Sorting Use Cases

**Find highest/lowest values:**
- Salary (high→low) - Identify top earners
- Tenure (oldest→newest) - Find most tenured employees
- Direct SOC (high→low) - Find managers with most direct reports
- Layer (shallow→deep) - See organizational depth

**Alphabetical organization:**
- Department (A→Z) - Group positions by department
- Job Title (A→Z) - See all roles alphabetically
- Manager Name (A→Z) - Group by reporting manager

**Chronological sorting:**
- Start Date (newest→oldest) - Find recent hires
- Start Date (oldest→newest) - Identify long-tenured employees

---

## Filtering

Apply filters to show only positions matching specific criteria.

### Basic Filtering

**How to filter:**
1. Click the **Filter** icon (funnel symbol)
2. Select an attribute (Department, Location, Pay Grade, etc.)
3. Choose which values to include (check boxes)
4. Click **Apply**

**Active filters appear:**
- As tags/chips above the table
- Showing which filters are active
- With X to remove individual filters

### Multiple Filters

Combine filters to narrow results:
- Multiple filters use AND logic (all conditions must be true)
- Example: Department = Engineering AND Location = San Francisco AND Pay Grade = 12

**How to add multiple filters:**
1. Apply first filter
2. Click Filter icon again
3. Add second filter
4. Repeat as needed

### Clearing Filters

**Remove all filters:**
- Click Filter icon
- Click "Clear All" button

**Remove specific filter:**
- Click the X on the filter tag/chip above the table

### Advanced Filtering

**Filter by calculated fields:**
- Direct SOC = 1-2 (find managers with low spans)
- Layer = 6+ (find deep org positions)
- Total Org Size > 50 (find leaders with large orgs)

**Filter by empty/null values:**
- Employee Name = (empty) - Find vacant positions
- Email = (empty) - Find positions missing contact info

**Filter by date ranges:**
- Start Date = Last 6 months
- Start Date > 2020-01-01

### Filter Use Cases

**Department analysis:**
- Filter to one department
- Sort by salary to analyze pay distribution
- Export for department-specific reports

**Location analysis:**
- Filter to specific office or region
- Analyze headcount distribution
- Create location-specific rosters

**Pay grade analysis:**
- Filter to specific pay grade
- Compare job titles within grade
- Identify compression opportunities

**Vacancy identification:**
- Filter to Employee Name = (empty)
- Sort by department
- Export list of open positions

---

## Column Customization

Control which columns appear and how they're organized.

### Show/Hide Columns

**How to customize:**
1. Click the **column settings** icon (gear or three dots)
2. Check/uncheck columns to show/hide
3. Changes apply immediately

**Common column configurations:**

**Basic view:**
- Name, Title, Department, Manager

**Compensation view:**
- Name, Title, Department, Salary, Pay Grade

**Contact list view:**
- Name, Email, Manager, Location

**Span of control analysis:**
- Name, Title, Direct SOC, Total Org Size, Layer

**Org structure view:**
- Name, Title, Manager, Department, Layer

### Reorder Columns

Change column order:
- Drag column headers left or right
- Drop in desired position
- New order persists during session

### Resize Columns

Adjust column width:
- Drag the border between column headers
- Double-click border to auto-fit to content
- Make columns wider to see full text
- Make columns narrower to fit more on screen

### Column Presets

Save column configurations for reuse:
1. Configure columns for specific task
2. Save as preset (if feature available)
3. Quickly switch between saved configurations

---

## Search

Find specific positions or people quickly.

**How to search:**
1. Use the search box at top of Directory
2. Type name, title, or any attribute value
3. Matching rows highlight automatically
4. Press Enter or click to navigate

**Search tips:**
- Search works across all visible columns
- Partial matches work (e.g., "Eng" finds "Engineering")
- Case-insensitive
- Search respects active filters (searches only visible rows)

**Search use cases:**
- Find person by name
- Locate positions by title keyword
- Search for specific values (department name, location, etc.)

---

## Selection

Select rows for bulk operations (in Scenario Directory only).

### Single Selection
- Click a row to select it
- Selected row highlights
- Click again to deselect

### Multiple Selection
- Check checkboxes in first column
- Select multiple positions at once
- Use for bulk operations

### Select All
- Check the header checkbox
- Selects all rows matching current filters
- Useful for bulk edits on filtered subset

---

## Pagination

Navigate large datasets:

**Pagination controls:**
- Rows per page (25, 50, 100, 500)
- Page navigation (1, 2, 3... Next, Previous)
- Total row count displayed

**Tips:**
- Increase rows per page to see more data at once
- Use filters to reduce total rows before viewing
- Sorting works across all pages, not just current page

---

## Linking to Org Chart

Switch between table and visual views:

**From Directory to Org Chart:**
- Click the org chart icon next to a position
- Navigates to that position in org chart view
- Preserves filters and context

**From Org Chart to Directory:**
- Click the Directory/Table icon in toolbar
- Switches to table view
- Same positions visible

---

## Keyboard Shortcuts

Speed up navigation:

- **Cmd/Ctrl + F** - Open search
- **Esc** - Clear selection or close panels
- **5** - Jump to Directory module from anywhere
- **1** - Return to org chart view

---

## Best Practices

1. **Filter before sorting** - Narrow data first, then sort for analysis
2. **Use multi-column sort** - Get precise ordering (e.g., Dept → Grade → Salary)
3. **Save common column configs** - Don't reconfigure repeatedly
4. **Clear filters between tasks** - Start fresh for each analysis
5. **Sort to find anomalies** - High/low values reveal interesting patterns
6. **Combine filter + sort + export** - Create targeted reports efficiently

---

## Common Workflows

### Analyze Department Compensation
1. Filter to Department = Engineering
2. Sort by Salary (high→low)
3. Review pay distribution
4. Export for further analysis

### Find Compression Opportunities
1. Filter to Direct SOC = 1-2
2. Filter to Pay Grade > 12
3. Sort by Layer
4. Review senior managers with low spans

### Create Contact List
1. Filter to Department + Location
2. Show columns: Name, Email, Manager, Phone
3. Sort by Name (A→Z)
4. Export to CSV

### Identify Vacant Positions
1. Filter to Employee Name = (empty)
2. Sort by Department
3. Export list for HR

### Compare Pay by Title
1. Filter to specific Job Title
2. Sort by Salary
3. Compare across departments/locations

---

## Next Steps

- Learn about [Exporting & Reporting](exporting-reporting.md) from Directory
- Explore [Scenario Directory](../scenarios/directory.md) for bulk editing
- See [Directory Overview](overview.md) for when to use Directory vs Org Chart
- Try the [Main Org Directory View](../main-org/directory-view.md)
