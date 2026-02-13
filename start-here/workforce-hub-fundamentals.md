---
description: Introduction to workforce analytics and insights
icon: chart-pie
hidden: false
---

# Workforce Hub Fundamentals

Workforce Hub is Agentnoon's analytics engine, providing pre-built charts and insights to help you understand your organizational structure, identify opportunities, and make data-driven decisions.

## What is Workforce Hub?

Workforce Hub transforms your org data into visual analytics. Instead of manually analyzing spreadsheets, you get instant insights into:

- Span of control distribution
- Headcount by department, layer, or location
- Organizational depth and breadth
- Manager vs IC ratios
- Cost distribution

**Key concept:** Workforce Hub is for **analysis**, not editing. Use it to identify opportunities, then model solutions in Scenarios.

## When to Use Workforce Hub

Use Workforce Hub when you need to:

1. **Identify efficiency opportunities** - Find managers with low span of control or deep reporting chains
2. **Prepare for stakeholder meetings** - Generate charts for presentations
3. **Analyze org structure** - Understand distribution across layers, departments, locations
4. **Benchmark against best practices** - Compare your org to industry standards
5. **Export data for reports** - Download charts as PowerPoint slides, PNGs, or CSV tables

## Key Charts

### 1. Layers and Spans of Control

**What it shows:** Distribution of managers across organizational layers and span of control ranges.

**When to use it:**
- Identify compression (managers with 1-2 direct reports)
- Find overburdened managers (span > 15)
- Understand management density across layers

**Example insight:** "Layer 5 has 114 managers with 1-2 direct reports - potential opportunity to flatten structure."

### 2. Headcount Distribution

**What it shows:** Breakdown of headcount by layer, department, location, or any custom field.

**When to use it:**
- See headcount by department
- Compare distribution across regions
- Analyze workforce by pay grade or job function

**Example insight:** "Engineering represents 40% of total headcount, but only 25% of the budget."

### 3. Headcount Heatmap

**What it shows:** Two-dimensional visualization of headcount across any two attributes.

**When to use it:**
- Understand org depth (layers) by department
- Identify unusual reporting chains
- Spot anomalies in org structure

**Example insight:** "Growth department has 6 layers, while other departments have only 4 - why the difference?"

### 4. Span of Control Distribution

**What it shows:** Breakdown of managers vs individual contributors by layer, pay grade, or department.

**When to use it:**
- Identify senior leaders without direct reports
- Find compression at high pay grades
- Understand manager-to-IC ratio

**Example insight:** "14 managers and 61 ICs at Pay Grade 14 - is this the right ratio?"

## Chart Navigation

Every chart in Workforce Hub has consistent controls:

### Chart Selection
Use the dropdown in the top-left to switch between available charts.

### Axis Configuration
- **X-axis dropdown** - Choose the dimension for horizontal axis (Department, Layer, Location, etc.)
- **Y-axis dropdown** - Choose what to measure (Headcount, Cost, Manager Count, etc.)

### Filtering
Apply filters to focus on specific groups:

1. Click the **Filter** icon (usually top-right)
2. Select filter criteria (e.g., "Department = Engineering")
3. Multiple filters combine with AND logic
4. Clear filters to see full organization

**Important:** Filters carry over between charts and even between modules. Always check active filters if data looks unexpected.

### Chart Settings (Gear Icon)

Click the settings gear to customize:

- **Numbers vs Percentages** - Toggle display format
- **Axis ordering** - Sort by value, alphabetically, or custom order
- **Span of Control ranges** - Adjust groupings (e.g., 1-2, 3-9, 10-15)
- **Show/hide elements** - Toggle legends, labels, or gridlines

### Show Table View

Click **Show Table** to see the raw data behind any chart:

- View exact numbers
- See detailed breakdowns
- Export to CSV
- Click rows to drill into details

### Exporting Charts

Download charts in multiple formats:

1. Click the **Download** icon
2. Choose format:
   - **PNG** - Image file for emails or documents
   - **PowerPoint** - Editable chart element you can paste into presentations
   - **CSV** - Raw data table for Excel analysis

**Pro tip:** The PowerPoint export includes the actual chart object, not just an image. You can edit colors, labels, and formatting in PowerPoint.

## Interactive Features

Charts are interactive:

- **Click chart elements** to filter (e.g., click "Layer 5" bar to see only Layer 5 data)
- **Hover for details** - See exact numbers and percentages
- **Click legends** - Show/hide specific data series
- **Zoom and pan** - Navigate large datasets

## Typical Workflow

Here's how analysts commonly use Workforce Hub:

1. **Start with Layers & Spans of Control** - Get bird's eye view of org structure
2. **Apply filters** - Focus on specific department or division
3. **Identify patterns** - Look for compression, high spans, or anomalies
4. **Use Spotlight in Org Chart** - Find specific positions matching criteria
5. **Create Scenario** - Model potential solutions
6. **Return to Hub** - Generate charts to present proposed changes

## Common Use Cases

### Finding Compression
1. Go to **Span of Control Distribution**
2. Configure to show 0-0 (ICs) vs 1+ (Managers)
3. Break down by Pay Grade
4. Look for high-paid individuals with no direct reports

### Analyzing Org Depth
1. Go to **Headcount Heatmap**
2. Set X-axis = Department
3. Set Y-axis = Layer
4. Look for departments with unusually deep hierarchies

### Budget Analysis
1. Go to **Headcount Distribution**
2. Set Y-axis = Total Cost
3. Set X-axis = Department or Pay Grade
4. Compare cost distribution across groups

## Best Practices

1. **Check filters first** - If data looks wrong, verify no unexpected filters are active
2. **Use multiple charts** - Don't rely on just one view; cross-reference insights
3. **Export for presentations** - Download PowerPoint charts for stakeholder meetings
4. **Combine with Org Chart** - Use Hub for analysis, Org Chart for detailed exploration
5. **Create scenarios to test hypotheses** - When Hub reveals opportunities, model solutions in Scenarios

## Tips for Analysis

- **Look for outliers** - Unusually high or low values often indicate opportunities
- **Compare across dimensions** - Department A vs B, Region 1 vs 2, Layer 3 vs 4
- **Track over time** - If your org syncs regularly, compare current vs previous snapshots
- **Consider context** - A span of 20 might be fine for a call center, problematic for R&D leadership

## Next Steps

Now that you understand Workforce Hub:

- Try the [Conducting Span of Control Analysis](../use-case-tutorials/span-of-control-analysis.md) tutorial
- Learn about [Chart Navigation](../hub/chart-navigation.md) for detailed chart features
- Explore [Org Metrics & Insights](../main-org/metrics-insights.md) in Main Org
- Create [Scenarios](scenarios-fundamentals.md) to model changes based on Hub insights
