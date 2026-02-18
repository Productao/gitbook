---
description: Filtering positions and sorting columns in Directory
hidden: false
---

# Filtering & Sorting

Master filtering and sorting to quickly find insights, identify outliers, and organize data in Directory.

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

> **[Screenshot placeholder: Directory table showing column header with ascending arrow indicator and sorted data]**

---

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

> **[Screenshot placeholder: Directory table with multiple sort indicators showing primary, secondary, and tertiary sorts on Department, Pay Grade, and Salary columns]**

---

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

### Sorting Tips

1. **Sort works across all pages** - Not just the current page, but entire dataset
2. **Combine with filters** - Filter first, then sort the subset
3. **Multi-column sort for precision** - Group, then sub-sort within groups
4. **Clear sort between tasks** - Click header 3 times to reset
5. **Use sorting to find anomalies** - High/low values often reveal interesting patterns

---

## Filtering

Apply filters to show only positions matching specific criteria.

### Basic Filtering

**How to filter:**
1. Click the **Filter** icon (funnel symbol)
2. Select an attribute (Department, Location, Pay Grade, etc.)
3. Choose which values to include (check boxes)
4. Click **Apply**

> **[Screenshot placeholder: Filter dialog showing attribute selection dropdown and checkbox list of values to include with Apply button]**

**Active filters appear:**
- As tags/chips above the table
- Showing which filters are active
- With X to remove individual filters

> **[Screenshot placeholder: Directory table with active filter tags/chips displayed above the table showing "Department = Engineering" and "Location = San Francisco" with X buttons to remove]**

---

### Multiple Filters

Combine filters to narrow results:
- Multiple filters use **AND logic** (all conditions must be true)
- Example: Department = Engineering AND Location = San Francisco AND Pay Grade = 12

**How to add multiple filters:**
1. Apply first filter
2. Click Filter icon again
3. Add second filter
4. Repeat as needed

> **[Screenshot placeholder: Directory with three active filter tags showing combined filters (Department = Engineering, Location = San Francisco, Pay Grade = 12) and filtered results below]**

---

### Clearing Filters

**Remove all filters:**
- Click Filter icon
- Click "Clear All" button

**Remove specific filter:**
- Click the X on the filter tag/chip above the table

---

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

---

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

### Filter Tips

1. **Filter before sorting** - Narrow data first, then sort for analysis
2. **Remember filters persist** - Active filters carry between Directory and Org Chart views
3. **Clear filters between tasks** - Start fresh for each new analysis
4. **Check active filters** - If data looks unexpected, check filter tags above table
5. **Combine filters strategically** - Use AND logic to create precise subsets

---

## Search

Find specific positions or people quickly.

**How to search:**
1. Use the search box at top of Directory
2. Type name, title, or any attribute value
3. Matching rows highlight automatically
4. Press Enter or click to navigate

> **[Screenshot placeholder: Directory search box at top with example search term "Senior Engineer" entered and matching rows highlighted in the table below]**

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

## Combining Filter, Sort, and Search

The most powerful analysis comes from combining all three:

### Example 1: Analyze Department Compensation

**Steps:**
1. **Filter:** Department = Engineering
2. **Sort:** Salary (high→low)
3. **Search:** (optional) Search for specific title like "Senior"
4. **Result:** See Engineering pay distribution, highest to lowest

> **[Screenshot placeholder: Directory showing Engineering department filter applied, Salary column sorted high to low with descending arrow, displaying compensation analysis view]**

**Export:** Create targeted compensation report

---

### Example 2: Find Compression Opportunities

**Steps:**
1. **Filter:** Direct SOC = 1-2 (low spans)
2. **Filter:** Pay Grade > 12 (senior levels)
3. **Sort:** Layer (low→high)
4. **Result:** Senior managers with low spans at shallow layers

**Action:** Identify restructuring opportunities

---

### Example 3: Create Contact List

**Steps:**
1. **Filter:** Department + Location (e.g., Engineering in San Francisco)
2. **Sort:** Name (A→Z)
3. **Customize columns:** Name, Email, Manager, Phone
4. **Export:** Download CSV for distribution

---

### Example 4: Identify Vacant Positions

**Steps:**
1. **Filter:** Employee Name = (empty)
2. **Sort:** Department (A→Z)
3. **Result:** All vacant positions grouped by department

**Export:** Send list to HR for recruitment planning

---

### Example 5: Compare Pay by Title

**Steps:**
1. **Filter:** Job Title = "Software Engineer"
2. **Sort:** Salary (high→low)
3. **Result:** Compare pay across departments/locations

**Action:** Identify pay equity issues

---

## Best Practices

1. **Filter before sorting** - Narrow data first, then sort for analysis
2. **Use multi-column sort** - Get precise ordering (e.g., Dept → Grade → Salary)
3. **Clear filters between tasks** - Start fresh for each analysis
4. **Sort to find anomalies** - High/low values reveal interesting patterns
5. **Combine filter + sort + export** - Create targeted reports efficiently
6. **Check active filters** - If data looks wrong, check filter tags
7. **Remember filters carry over** - Active filters affect org chart and directory views

---

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

---

## Troubleshooting

**Problem:** Can't find expected positions in Directory.
- **Solution:** Check active filters. Clear all filters and try again.

**Problem:** Sort doesn't seem to work correctly.
- **Solution:** Remove existing sort first (click header 3 times), then re-sort. Check if filters are affecting results.

**Problem:** Filter options are missing expected values.
- **Solution:** Values only appear if they exist in the data. Check if data was imported correctly.

**Problem:** Search returns no results.
- **Solution:** Search only works on visible (filtered) rows. Clear filters and try search again.

---

## Next Steps

- Explore [Column Customization](columns-customization.md) to show relevant attributes
- Learn about [Bulk Operations](bulk-operations.md) for mass edits in scenarios
- Master [Exporting](exporting.md) to create custom reports
- Try [Navigation & Access](navigation.md) to switch between views

