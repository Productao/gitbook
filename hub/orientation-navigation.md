---
description: Finding your way around Workforce Hub
icon: compass
---

# Workforce Hub Orientation & Navigation

The Workforce Hub provides powerful analytics and visualizations to help you understand your organization's structure, composition, and health. This guide will help you navigate the interface and make the most of Hub analytics.

---

## Workforce Hub Interface Overview

When you access the Workforce Hub, the interface consists of several key areas:

**Chart Selection Bar**: Choose which analytics chart to view

**Configuration Controls**: Configure chart dimensions, metrics, and filters

**Main Visualization Area**: Displays the selected chart with your data

**Before/After/Changes Toggle**: Control what state you're analyzing (when in a scenario)

> **[Screenshot placeholder: Full Workforce Hub interface with labeled areas - chart selector, configuration controls, main chart area]**

---

## Accessing Workforce Hub

### From Main Org

1. Navigate to your Main Org
2. Click the view dropdown at the top (defaults to "Org Chart")
3. Select "Workforce Hub"
4. Hub opens showing current state analytics

### From a Scenario

1. Open any scenario
2. Click the view dropdown at the top
3. Select "Workforce Hub"
4. Hub opens showing scenario analytics with Before/After/Changes toggle

> **[Screenshot placeholder: View dropdown showing Org Chart, Directory, Forecast, Workforce Hub options with Workforce Hub highlighted]**

---

## Chart Selection

The Hub provides multiple chart types for different analytical needs:

### Available Charts

**Layers & Spans Chart**
- Visualizes organizational layers and span of control
- Shows distribution of direct reports by layer
- Identifies managers with unhealthy spans

**Headcount Distribution Chart**
- Shows headcount across any dimension
- Proportional visualization of team sizes
- Interactive drill-down capabilities

**Headcount Heatmap Chart**
- Cross-tabulation of two dimensions
- Color intensity indicates concentration
- Identifies gaps and imbalances

> **[Screenshot placeholder: Chart selector dropdown showing Layers & Spans, Headcount Distribution, Headcount Heatmap options]**

### Switching Between Charts

**Method 1:** Use the chart selector dropdown at top
- Click dropdown
- Select desired chart
- Chart loads with last-used configuration

**Method 2:** Use keyboard navigation
- Press `/` for quick navigation
- Type chart name
- Select from results

---

## Configuring Charts

Each chart has configuration controls to customize what you're analyzing:

### Dimension Selection

**X-Axis / Primary Dimension:**
- Department
- Location
- Country
- Job Level
- Employee Type
- Custom attributes

**Y-Axis / Secondary Dimension (for Heatmap):**
- Same options as X-axis
- Creates cross-tabulation view

> **[Screenshot placeholder: Dimension selector dropdowns showing options]**

### Metric Selection

**For applicable charts:**
- **Headcount**: Count of positions
- **Cost**: Total compensation
- **Average Salary**: Mean compensation
- **Span of Control**: Direct report counts

Toggle between metrics to analyze different aspects.

### Filter Controls

**Apply filters to focus analysis:**
- Department filter (show only specific departments)
- Location filter
- Job Level filter
- Employee Type filter
- Custom attribute filters

**Multiple filters:**
- Combine filters for precise analysis
- Filters use AND logic
- Clear all filters with one click

> **[Screenshot placeholder: Filter panel with multiple filters applied]**

---

## Chart Interactions

### Layers & Spans Chart

**Interactions:**
- **Hover**: See detailed statistics for each layer/span combination
- **Click bubble**: Drill into positions with that span at that layer
- **Color coding**: Red = unhealthy spans, green = healthy spans
- **Size**: Bubble size indicates number of positions

**What to look for:**
- Large red bubbles (many managers with unhealthy spans)
- Very tall charts (many organizational layers)
- Clusters of narrow spans (potential for flattening)

> **[Screenshot placeholder: Layers & Spans chart with hover tooltip showing details]**

### Headcount Distribution Chart

**Interactions:**
- **Hover**: See headcount and percentage
- **Click segment**: Filter to that segment
- **Proportional sizing**: Larger boxes = more headcount
- **Color coding**: Can represent different metrics

**What to look for:**
- Imbalanced distribution
- Unexpectedly small or large segments
- Trends over time (compare Before vs After)

> **[Screenshot placeholder: Headcount Distribution chart showing department distribution]**

### Headcount Heatmap Chart

**Interactions:**
- **Hover cell**: See exact headcount
- **Click cell**: Drill into positions
- **Color intensity**: Darker = higher concentration
- **Empty cells**: Gaps in organizational coverage

**What to look for:**
- Gaps (empty cells) indicating missing coverage
- Heavy concentrations (very dark cells)
- Balanced distribution across cells
- Succession planning gaps (few at senior levels)

> **[Screenshot placeholder: Headcount Heatmap showing Department x Job Level with color intensity]**

---

## Before, After, and Changes Views

When viewing Hub from a scenario, use the toggle to analyze impact:

### Show Before

View analytics based on **Main Org** (current state).

**Use to:**
- Establish baseline metrics
- Understand current organizational health
- Identify problems to solve

### Show After

View analytics with **all scenario changes applied** (proposed state).

**Use to:**
- See impact of proposed changes
- Validate scenario improves metrics
- Check for new issues created

### Show Changes

View the **delta** between Before and After.

**Use to:**
- Highlight specific improvements or regressions
- Communicate impact to stakeholders
- Focus on what's actually changing

> **[Screenshot placeholder: Before/After/Changes toggle with Show Changes selected]**

---

## Chart Customization Settings

Click the **gear icon** to access advanced chart settings:

### Display Options

**Numbers vs Percentages:**
- Toggle between absolute counts and percentages
- Useful for comparing different-sized organizations

**Sort order:**
- Ascending, descending, or alphabetical
- Apply to rows or columns

**Chart type:**
- Bar chart, bubble chart, treemap (chart-dependent)

### Axis Configuration

**Reverse axes:**
- Swap X and Y axes for different perspective
- Useful for readability with many categories

**Group by:**
- Secondary grouping within primary dimension
- Creates nested or stacked visualizations

> **[Screenshot placeholder: Chart settings panel showing display and axis options]**

---

## Exporting Hub Analytics

Export charts for use in presentations and reports:

### Export Options

**Image export:**
- PNG format
- High resolution for presentations
- Includes current filters and configuration

**Data export:**
- CSV format for further analysis
- Excel format with formatting
- Includes underlying data points

**PDF export:**
- Multi-chart reports
- Formatted for printing
- Professional appearance

> **[Screenshot placeholder: Export menu showing PNG, CSV, Excel, PDF options]**

### Export Workflow

1. Configure chart to desired state
2. Apply filters if needed
3. Click export button (top right)
4. Select format
5. Download file

---

## Common Hub Navigation Scenarios

### "I want to see span of control distribution"

1. Access Workforce Hub
2. Select "Layers & Spans Chart"
3. Review bubble chart showing spans by layer
4. Look for red bubbles (unhealthy spans)
5. Click bubbles to drill into specific managers

### "I want to see headcount by department"

1. Access Workforce Hub
2. Select "Headcount Distribution Chart"
3. Set dimension to "Department"
4. Review proportional distribution
5. Hover for exact headcount numbers

### "I want to see if we have leadership gaps"

1. Access Workforce Hub
2. Select "Headcount Heatmap Chart"
3. Set X-axis to "Department"
4. Set Y-axis to "Job Level"
5. Look for empty cells at senior levels (gaps)

### "I want to compare current vs proposed org health"

1. Open a scenario
2. Switch to Workforce Hub
3. Select desired chart
4. Toggle "Show Before" → see current state
5. Toggle "Show After" → see proposed state
6. Toggle "Show Changes" → see delta

### "I want to export span of control analysis"

1. Configure Layers & Spans chart
2. Apply any needed filters
3. Click export button
4. Select PNG for presentation or CSV for analysis
5. Download and use in reports

---

## Tips for Effective Hub Usage

### Start with Overview Charts

- Begin with Headcount Distribution to understand composition
- Move to Layers & Spans to analyze structure
- Use Heatmap for deep-dive analysis

### Use Filters to Focus

- Don't try to analyze the entire org at once
- Filter to specific departments or segments
- Drill down progressively

### Leverage Before/After Comparisons

- Always check "Show Before" to establish baseline
- Review "Show After" to see impact
- Use "Show Changes" to communicate

### Export Key Visuals

- Export charts before major milestones
- Create audit trail of organizational evolution
- Share visuals with stakeholders who don't have Agentnoon access

### Combine with Other Views

- Use Hub for analysis
- Use Org Chart for visualization
- Use Directory for data detail
- Use Forecast for timing

---

## Related Articles

- [Workforce Hub Overview](overview.md)
- [Layers & Spans Chart](layers-spans-chart.md)
- [Headcount Distribution Chart](headcount-distribution-chart.md)
- [Headcount Heatmap Chart](headcount-heatmap-chart.md)
- [Scenario Workforce Hub](../scenarios/scenario-workforce-hub.md)
