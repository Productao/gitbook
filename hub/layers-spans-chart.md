---
description: Detailed guide to using the Layers and Spans of Control chart
---

# Layers and Spans of Control Chart

### Overview

The **Layers and Spans of Control** chart is one of the most powerful analytics tools in Agentnoon for identifying organizational efficiency opportunities. It provides a matrix view that shows how many managers fall into different span of control (SOC) groupings across various organizational layers or departments.

This chart gives you an immediate bird's-eye view of where spans might be too narrow (indicating potential compression or inefficiency) or too wide (indicating potential overload), making it essential for organizational design analysis and budget planning conversations.

### What This Chart Shows

The chart displays a **matrix breakdown** of managers organized by:

* **X-axis (columns)**: Span of Control groupings (e.g., 1-2, 3-5, 6-9, 10-15)
* **Y-axis (rows)**: Your chosen dimension (e.g., layers, departments, KLT areas)
* **Cell values**: Count of managers in each combination

**Example interpretation**: "In the Growth organization, there are 114 managers with a span of control between 1-2, with most of them in layers 5 and 6."

### When to Use This Chart

This chart is particularly valuable for:

* **SOC-led discovery** - Identifying managers with unusually high or low spans
* **Structural efficiency analysis** - Finding compression or organizational bottlenecks
* **Budget planning conversations** - Showing span distribution to budget owners
* **Comparative analysis** - Comparing span patterns across different departments
* **Leadership compression identification** - Finding senior leaders with minimal direct reports
* **Organizational rationalization** - Supporting decisions about flattening or restructuring

### Configuring the Chart

#### Setting Up Span Groupings

The chart allows you to customize span of control groupings to match your analysis needs:

1. Click the **settings gear icon** (top-right)
2. Add or modify span groupings:
   * **0-0**: Individual contributors (ICs) - useful for seeing IC count, but often excluded for manager-focused analysis
   * **1-2**: Very narrow spans (potential compression)
   * **3-5**: Common grouping for small teams
   * **6-9**: Mid-range spans
   * **10-15**: Larger spans
   * **16-25**: Very wide spans
   * **26-40**: Extremely wide spans
   * **41+**: Outlier spans

3. **Recommended configuration for manager analysis**:
   * Exclude 0-0 grouping (removes ICs from view)
   * Include: 1-2, 3-5, 6-9, 10-15, 16-25, 26-40, 41+
   * Adjust ranges based on your organization's typical spans

4. **Pro tip**: After adding groupings, use drag-and-drop to reorder them logically from smallest to largest

#### Configuring the Y-Axis

Choose what dimension to analyze spans across:

* **Layers** (default) - Shows span distribution by organizational level
* **Department** - Compares spans across different departments
* **KLT Area** - Analyzes spans by business unit or KLT area
* **Pay Grade** - Identifies span patterns at different compensation levels
* **Location/Region** - Compares spans across geographic areas

#### Applying Filters

Focus your analysis on specific populations:

* Filter by **KLT member** or **KLT area** to analyze one organization at a time
* Filter by **location**, **department**, or any custom field
* **Important**: Analyze one organization at a time for clearest insights

### How to Interpret the Data

#### Identifying Low Spans (1-2 Range)

When you see high numbers in the 1-2 span columns:

* **Potential compression** - Leaders reporting to leaders with minimal teams
* **Possible inefficiency** - Multiple management layers for small teams
* **Context matters** - Some situations legitimately require 1:1 relationships (e.g., VP of Strategy under CEO)

**Example from transcript**: "In the Growth organization, there are 114 managers with SOC 1-2, mostly in layers 5 and 6. Depending on context, this could indicate opportunities for flattening or consolidation."

#### Identifying High Spans (16-25+ Range)

When you see managers in very high span ranges:

* **Potential overload** - Manager may need support or additional leadership
* **Could be appropriate** - High standardization and process maturity may support wide spans
* **Context-dependent** - Nature of work, team distribution, and experience all matter

**Considerations for high spans**:
* Level of standardization in the work
* Process maturity of the team
* Workforce complexity and geographic distribution
* Manager experience and capability
* Nature of the work (transactional vs. strategic)

#### Layer Distribution Patterns

Look for patterns in how spans distribute across layers:

* **Top-heavy indicators**: Many narrow spans at senior levels (layers 1-3)
* **Compression at bottom**: Many narrow spans at lower levels (layers 5-6)
* **Balanced distribution**: Mix of spans across all layers appropriate to work type

#### Comparative Analysis

When analyzing multiple departments:

1. Apply filter for first department/area
2. Note the span distribution pattern
3. Switch filter to second department/area
4. Compare patterns - are some areas more compressed than others?
5. Identify best practices or problem areas

### Common Use Cases

#### Use Case 1: SOC-Led Discovery for Budget Planning

**Goal**: Identify efficiency opportunities before budget conversations

**Workflow**:
1. Navigate to Workforce Hub
2. Select Layers and Spans of Control chart
3. Configure span groupings (exclude 0-0, include 1-2 through 41+)
4. Filter to specific KLT area or department
5. Look for high concentrations in 1-2 span range
6. Note layers where this occurs most
7. Navigate to org chart to investigate specific positions
8. Document findings for budget owner conversations

#### Use Case 2: Identifying Leadership Compression

**Goal**: Find senior leaders with minimal direct reports

**Workflow**:
1. Configure Y-axis to show **Pay Grades** or **Layers**
2. Focus on senior levels (top 3-4 layers or pay grades)
3. Look for managers in the 1-2 span columns at these levels
4. Export table view to see specific positions
5. Navigate to org chart to understand context
6. Consider whether reporting relationships could be simplified

#### Use Case 3: Cross-Department Comparison

**Goal**: Compare organizational efficiency across departments

**Workflow**:
1. Start with no filters to see total organization
2. Document overall patterns
3. Apply filter for Department A
4. Take screenshot or note distribution
5. Switch filter to Department B
6. Compare patterns - which department has more narrow spans?
7. Identify if one department's structure could inform others

### Advanced Analysis Techniques

#### Breaking Down Narrow Spans Further

For detailed analysis of narrow spans:

1. Modify groupings to separate: **1-1**, **2-2**, **3-3**
2. This shows exactly how many managers have 1, 2, or 3 direct reports
3. Helps quantify the scope of compression issues

**Example configuration**: 1-1, 2-2, 3-3, 4-7, 8-10, 11-25

#### Combining with Org Chart Analysis

After identifying patterns in the Hub:

1. Note specific layer/span combinations of concern
2. Navigate to the org chart
3. Use **Spotlight** feature with "Average Immediate SOC" rule
4. Set range to match what you found (e.g., 1-2)
5. Expand to level 2 or 3 for broader view
6. Click through specific managers to understand context
7. Look for patterns like VP reporting to VP relationships

### Interactive Features

#### Show Table Function

Click **Show table** to reveal:
* Exact counts for each span/layer combination
* Position-level breakdown showing who's included
* Ability to export detailed data to CSV

#### Chart Elements

* **Clickable cells** - Some chart versions allow clicking to filter
* **Color coding** - Darker colors typically indicate higher concentrations
* **Hover details** - Hover over cells to see exact counts

### Export Options

#### PNG Export
* Quick visual snapshot for presentations
* Includes current filters and configuration

#### PowerPoint Export
* Generates actual chart element (not just image)
* Can be edited and customized in PowerPoint
* Perfect for copying into budget presentation decks

#### CSV Export
* Detailed data table with all positions
* Includes all attributes for further analysis
* Use for deeper quantitative analysis in Excel

### Settings and Customization

Access the settings gear icon to adjust:

* **Span groupings** - Add, remove, or modify ranges
* **Y-axis order** - Change how rows are sorted
* **X-axis order** - Adjust span grouping sequence (use drag-and-drop)
* **Display options** - Toggle between counts and percentages (chart-dependent)

### Strategic Insights from This Chart

#### Efficiency Opportunities

Look for:
* **High concentration in 1-2 spans** - Potential to flatten structure
* **Many narrow spans at senior levels** - Compression reducing efficiency
* **Inconsistent patterns across departments** - Opportunity for standardization

#### Organizational Health Indicators

* **Balanced distribution** - Mix of spans appropriate to organizational context
* **Few outliers** - Most managers within reasonable span ranges
* **Consistent patterns** - Similar structures across comparable departments

#### Questions This Chart Helps Answer

* Where do we have the most managers with narrow spans?
* Which layers or departments show signs of compression?
* Are there managers with spans so wide they may need support?
* How does our span distribution compare across business units?
* Where are the best opportunities for organizational efficiency?

### Best Practices

1. **Start broad, then narrow**: Begin with full organization view, then filter
2. **Exclude ICs when focusing on managers**: Remove 0-0 grouping for manager analysis
3. **Analyze one organization at a time**: Clearer patterns emerge with focused scope
4. **Consider context always**: Numbers need business context to be actionable
5. **Combine with org chart investigation**: Use Hub for patterns, org chart for specifics
6. **Document your configuration**: Save screenshots of useful span grouping setups
7. **Export for reference**: Create PowerPoint slides for ongoing discussions

### Workflow Example: Complete SOC Analysis

**Scenario**: Budget planning for Commercial NA organization

1. **Setup**:
   * Navigate to Workforce Hub
   * Select Layers and Spans of Control chart
   * Configure span groupings: 1-2, 3-5, 6-9, 10-15, 16-25, 26-40
   * Filter: KLT Area = "Commercial NA"

2. **Initial Analysis**:
   * Observe: 114 managers in 1-2 span range
   * Note: Concentration in layers 5-6
   * Notice: Few managers in very high span ranges

3. **Detailed Investigation**:
   * Navigate to org chart (filter persists)
   * Clear filters temporarily to see full context
   * Use Spotlight: "Direct Span of Control" = 1-2
   * Expand to level 2 layout
   * Identify specific VP-to-VP reporting relationships

4. **Documentation**:
   * Export chart as PowerPoint
   * Take notes on specific positions of concern
   * Screenshot org chart examples showing compression
   * Prepare recommendations for budget owner

5. **Follow-up**:
   * Return to Hub to verify patterns after scenario modeling
   * Compare before/after span distributions
   * Document efficiency impact of proposed changes

### Visual Guide

> **[Screenshot placeholder: Layers and Spans of Control chart showing matrix with span groupings on X-axis and layers on Y-axis]**

> **[Screenshot placeholder: Settings panel showing span grouping configuration with ranges being added]**

> **[Screenshot placeholder: Chart filtered to one department showing concentration in 1-2 span range]**

> **[Screenshot placeholder: Show table view revealing position-level details behind the chart]**

> **[Screenshot placeholder: Export options panel showing PNG, PowerPoint, and CSV options]**

### Related Resources

* [Headcount Heatmap](headcount-heatmap-chart.md) - Visualize layer depth across departments
* [Headcount Distribution](headcount-distribution-chart.md) - Analyze workforce counts by dimension
* [Chart Navigation](chart-navigation.md) - General Hub navigation and controls
* [Conducting Span of Control Analysis](../use-case-tutorials/span-of-control-analysis.md) - Complete tutorial
