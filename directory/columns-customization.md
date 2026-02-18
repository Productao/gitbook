---
description: Customizing visible columns, reordering, and resizing in Directory
hidden: false
---

# Column Customization

Control which columns appear in Directory and how they're organized to create custom views for different tasks.

## Show/Hide Columns

Choose which attributes to display in your Directory view.

### How to Customize Columns

**Steps:**
1. Click the **column settings** icon (gear or three dots)
2. Check/uncheck columns to show/hide
3. Changes apply immediately

**Tips:**
- Only show columns relevant to your current task
- Fewer columns = easier to scan and compare
- More columns = more comprehensive view

---

### Common Column Configurations

**Basic view:**
- Name
- Title
- Department
- Manager

**Use case:** Quick reference, org structure overview

---

**Compensation view:**
- Name
- Title
- Department
- Salary
- Pay Grade

**Use case:** Compensation analysis, pay equity review

---

**Contact list view:**
- Name
- Email
- Manager
- Location
- Phone (if available)

**Use case:** Creating rosters, email lists, contact sheets

---

**Span of control analysis:**
- Name
- Title
- Direct SOC
- Total Org Size
- Layer

**Use case:** Identifying compression, analyzing org structure

---

**Org structure view:**
- Name
- Title
- Manager
- Department
- Layer

**Use case:** Understanding reporting relationships, hierarchy depth

---

**Vacancy tracking:**
- Position Title
- Department
- Manager
- Employee Name (shows empty for vacancies)
- Start Date

**Use case:** Identifying open positions, recruitment planning

---

## Reorder Columns

Change the order in which columns appear.

### How to Reorder

**Method:**
- Drag column headers left or right
- Drop in desired position
- New order persists during session

**Tips:**
- Put most important columns on the left
- Group related columns together (e.g., all compensation fields)
- Place identifying info (Name, Title) first

---

### Strategic Column Ordering

**Left to right priority:**
1. **Identifying info** - Name, Title, Employee ID
2. **Grouping attributes** - Department, Location, Manager
3. **Analysis fields** - Salary, Pay Grade, Metrics
4. **Secondary info** - Start Date, Email, Phone

**Example order for compensation analysis:**
- Name → Title → Department → Pay Grade → Salary → Location

**Example order for contact list:**
- Name → Email → Manager → Department → Location → Phone

---

## Resize Columns

Adjust column width for readability.

### How to Resize

**Manual resize:**
- Drag the border between column headers
- Make columns wider to see full text
- Make columns narrower to fit more on screen

**Auto-fit:**
- Double-click border between column headers
- Column auto-sizes to fit content

**Tips:**
- Auto-fit long text fields (Name, Title)
- Keep numeric fields narrow (Layer, SOC)
- Widen columns if text is truncated with "..."

---

## Column Presets

Save column configurations for reuse (if available in your Agentnoon instance).

### Creating Presets

**Steps:**
1. Configure columns for specific task
2. Click "Save as preset" (if feature available)
3. Name the preset (e.g., "Compensation Analysis", "Contact List")
4. Preset saved for quick access

### Using Presets

**Steps:**
1. Click presets dropdown
2. Select saved preset
3. Columns reconfigure automatically

**Common presets to create:**
- Compensation analysis
- Contact lists
- Span of control review
- Vacancy tracking
- Department rosters

---

## Column Types

Understanding different attribute types:

### Text Columns
- Name, Title, Department, Location
- Sort alphabetically (A→Z)
- Filter by value selection

### Numeric Columns
- Salary, Pay Grade, Direct SOC, Layer
- Sort by value (low→high, high→low)
- Filter by ranges or specific values

### Date Columns
- Start Date, Last Promotion Date
- Sort chronologically (oldest→newest, newest→oldest)
- Filter by date ranges

### Calculated Columns
- Direct SOC, Total Org Size, Layer, Tenure
- Computed by Agentnoon
- Cannot be edited directly
- Sort and filter like other columns

---

## Best Practices

1. **Create task-specific views** - Different column sets for different analyses
2. **Start with fewer columns** - Add more only if needed
3. **Put identifying info first** - Name and Title should be leftmost
4. **Group related columns** - Keep compensation fields together, contact info together
5. **Save presets** - Don't reconfigure repeatedly for common tasks
6. **Resize for readability** - Ensure all text is visible
7. **Remove noise** - Hide columns you're not using

---

## Common Workflows

### Set Up Compensation Analysis View

**Steps:**
1. Hide all columns
2. Show: Name, Title, Department, Pay Grade, Salary, Location
3. Reorder: Name → Title → Pay Grade → Salary → Department → Location
4. Resize Salary column to show full amounts
5. Save as preset: "Compensation Analysis"

**Use for:**
- Pay equity reviews
- Salary benchmarking
- Budget planning

---

### Create Contact List Export

**Steps:**
1. Show: Name, Email, Manager, Department, Location, Phone
2. Reorder: Name → Email → Manager → Department → Location → Phone
3. Resize Name and Email columns for readability
4. Filter to specific department or location
5. Export to CSV

**Use for:**
- Email distributions
- Department rosters
- Emergency contact lists

---

### Analyze Span of Control

**Steps:**
1. Show: Name, Title, Department, Layer, Direct SOC, Total Org Size
2. Reorder: Name → Title → Department → Direct SOC → Total Org Size → Layer
3. Sort by Direct SOC (high→low)
4. Identify high/low spans

**Use for:**
- Org design
- Compression analysis
- Restructuring planning

---

### Track Vacancies

**Steps:**
1. Show: Position Title, Department, Manager, Employee Name, Start Date
2. Filter to Employee Name = (empty)
3. Sort by Department
4. Export vacancy list

**Use for:**
- Recruitment planning
- Headcount tracking
- Budget allocation

---

## Customization by Directory Mode

### Main Org Directory
- All column customization features available
- Presets persist across sessions
- View-only (cannot edit position data)

### Scenario Directory
- Same customization features PLUS:
- Can see "Change" indicators on modified positions
- Bulk selection checkboxes appear in first column
- Edit capabilities available

### Forecast Directory
- Standard column customization
- Time-based columns (Quarter, Year) available
- Forecast-specific attributes visible

---

## Troubleshooting

**Problem:** Can't find a specific column.
- **Solution:** Click column settings, scroll through available columns, check the box to show it.

**Problem:** Column order resets when switching views.
- **Solution:** Column order may not persist between sessions. Save as preset to quickly restore preferred configuration.

**Problem:** Text is truncated with "..." in columns.
- **Solution:** Drag column border to make it wider, or double-click border to auto-fit.

**Problem:** Too many columns to fit on screen.
- **Solution:** Hide less important columns, or use horizontal scroll at bottom of table.

**Problem:** Lost track of which columns are visible.
- **Solution:** Click column settings to see full list with checkboxes indicating visibility.

---

## Next Steps

- Learn about [Filtering & Sorting](filtering-sorting.md) to narrow down data
- Try [Bulk Operations](bulk-operations.md) for mass edits in scenarios
- Master [Exporting](exporting.md) to create custom reports
- Explore [Navigation & Access](navigation.md) to switch between views

## Visual Guide

> **[Screenshot placeholder: Column customization menu showing checkboxes for show/hide]**

> **[Screenshot placeholder: Dragging column header to reorder columns]**

> **[Screenshot placeholder: Common column preset examples]**
