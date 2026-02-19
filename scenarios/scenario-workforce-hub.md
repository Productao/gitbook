---
description: Using Workforce Hub analytics within scenarios
icon: chart-mixed
---

# Scenario Workforce Hub

The Scenario Workforce Hub provides powerful analytics and visualizations to help you analyze the composition, structure, and distribution of your workforce within a scenario. Use the Hub to understand span of control, identify organizational patterns, and validate your scenario changes with data-driven insights.

## Overview

When you switch to Workforce Hub view within a scenario, you gain access to specialized charts and analytics that help you understand the impact of your organizational changes. The Hub is particularly valuable for analyzing reporting structures, identifying imbalances, and ensuring your scenario creates a healthy organizational design.

> **[Screenshot placeholder: Scenario with Workforce Hub selected from dropdown, showing span of control layers chart]**

**Key capabilities:**
- Analyze span of control and reporting layers
- Visualize headcount distribution across dimensions
- Identify organizational imbalances and outliers
- Validate scenario changes with data insights
- Compare current state vs proposed changes
- Export analytics for reporting and presentations

## Accessing Scenario Workforce Hub

To access the Workforce Hub view within a scenario:

1. Open any scenario
2. Click the view dropdown at the top (default shows "Directory")
3. Select "Workforce Hub"
4. The view switches to show available analytics charts

> **[Screenshot placeholder: View dropdown menu showing Directory, Forecast, and Workforce Hub options with Workforce Hub highlighted]**

The Workforce Hub is available in all scenarios and automatically reflects your scenario changes.

## Available Charts and Analytics

The Workforce Hub provides several specialized chart types:

### Layers & Spans Chart

**Purpose:** Visualize reporting layers and span of control across your organization

This chart shows:
- How many organizational layers exist (distance from top executive)
- How many direct reports each manager has (span of control)
- Where spans are too narrow (micromanagement risk) or too wide (lack of support)

> **[Screenshot placeholder: Layers & Spans chart showing org layers 0-7 with varying bubble sizes representing span of control]**

**Use cases:**
- Identify where your reorganization increases or decreases layers
- Validate that reporting structures are balanced
- Find managers with unsustainable spans after scenario changes

**Learn more:** [Layers & Spans Chart](../hub/layers-spans-chart.md)

### Headcount Distribution Chart

**Purpose:** Visualize how headcount is distributed across any organizational dimension

This chart shows:
- Distribution across departments, locations, job levels, or any custom field
- Proportional sizing to identify largest vs smallest groups
- Interactive filtering to drill into specific segments

> **[Screenshot placeholder: Headcount Distribution chart showing department distribution with proportional boxes]**

**Use cases:**
- See how departmental headcount changes in your scenario
- Validate that your scenario achieves intended distribution goals
- Identify if changes create imbalanced team sizes

**Learn more:** [Headcount Distribution Chart](../hub/headcount-distribution-chart.md)

### Headcount Heatmap Chart

**Purpose:** Visualize headcount across two dimensions simultaneously

This chart shows:
- Intersection of two attributes (e.g., Department x Job Level)
- Color intensity indicates headcount concentration
- Identify gaps or concentrations in your organizational design

> **[Screenshot placeholder: Headcount Heatmap showing Department (rows) vs Job Level (columns) with color-coded cells]**

**Use cases:**
- Analyze seniority distribution across departments after scenario changes
- Identify succession planning gaps
- Validate diversity distribution across organizational segments

**Learn more:** [Headcount Heatmap Chart](../hub/headcount-heatmap-chart.md)

## Understanding Before, After, and Changes in Workforce Hub

The Workforce Hub works seamlessly with the Before/After/Changes toggle:

### Show Before

Displays analytics based on your **Main Org** (current reality, before scenario changes).

**When to use:**
- Establish baseline metrics (current span of control, current distribution)
- Identify problems in the current state you want to solve
- Compare against proposed scenario changes

> **[Screenshot placeholder: Layers & Spans chart in "Show Before" mode showing current org structure]**

### Show After

Displays analytics with **all scenario changes applied** (proposed future state).

**When to use:**
- See the impact of your proposed changes on org structure
- Validate that changes achieve intended improvements
- Identify new issues your scenario might create

> **[Screenshot placeholder: Layers & Spans chart in "Show After" mode showing modified org structure]**

### Show Changes

Displays the **delta** between Before and After (improvements or regressions).

**When to use:**
- Highlight exactly what metrics are improving or worsening
- Show span of control increases/decreases
- Communicate analytical impact to stakeholders

> **[Screenshot placeholder: Headcount Distribution chart in "Show Changes" mode showing +/- by department]**

## Practical Use Cases

### Validating Span of Control in a Reorganization

**Goal:** Ensure your reorganization creates healthy reporting structures

**Approach:**
1. Open your reorganization scenario
2. Switch to Workforce Hub > Layers & Spans Chart
3. Toggle to "Show Before" to see current spans
4. Toggle to "Show After" to see proposed spans
5. Identify managers with extreme spans (too narrow or too wide)
6. Return to Directory view and adjust reporting relationships
7. Validate changes in Hub again

**Result:** A reorganization with balanced, sustainable reporting structures.

> **[Screenshot placeholder: Side-by-side comparison of Layers & Spans in Before vs After mode]**

### Analyzing Departmental Balance

**Goal:** Ensure departments have appropriate headcount after changes

**Approach:**
1. Open your scenario
2. Switch to Workforce Hub > Headcount Distribution Chart
3. Select "Department" as the dimension
4. Toggle "Show Changes" to see departmental increases/decreases
5. Validate that changes align with strategic goals

**Result:** Clear visibility into how your scenario rebalances the organization.

### Identifying Succession Planning Gaps

**Goal:** Ensure adequate talent pipeline at each level

**Approach:**
1. Open your scenario
2. Switch to Workforce Hub > Headcount Heatmap
3. Set X-axis to "Job Level" and Y-axis to "Department"
4. Toggle "Show After" to see proposed distribution
5. Identify departments with gaps at specific levels
6. Add positions or internal transfers to fill gaps

**Result:** A workforce plan with strong succession readiness.

> **[Screenshot placeholder: Headcount Heatmap showing gaps at senior levels in specific departments]**

## Exporting Hub Analytics

You can export Hub charts for use in presentations and reports:

1. Configure the chart to the view you want (Before/After/Changes)
2. Select the appropriate dimensions and filters
3. Click the export button (typically top-right of chart)
4. Choose image format (PNG, PDF) or data export (CSV, Excel)
5. Use exported visuals in stakeholder presentations

> **[Screenshot placeholder: Export button on Workforce Hub chart with format options]**

**Export use cases:**
- Include org structure analysis in business cases
- Share span of control metrics with leadership
- Add distribution charts to planning presentations
- Provide data to HR analytics teams

## Tips for Effective Hub Usage

**Use Hub early in scenario planning**
- Check Hub analytics BEFORE making changes to identify current problems
- Use insights to guide which changes to make
- Validate with Hub AFTER changes to ensure improvements

**Combine Hub with Forecast**
- Use Hub to analyze structure and composition
- Use Forecast to analyze timing and phasing
- Together they provide complete scenario validation

**Leverage Show Changes mode**
- This is the most powerful view for communicating impact
- Clearly shows what's improving vs degrading
- Makes it easy to justify scenario decisions

**Compare scenarios using Hub**
- Open Scenario A, check Hub metrics
- Open Scenario B, check the same Hub metrics
- Choose the scenario with better organizational health

**Filter to focus analysis**
- Use Hub filters to analyze specific segments
- Example: Filter to "Engineering" department to see just that area
- Drill into problem areas identified in high-level views

## Common Questions

**Why do Hub charts look the same in Before and After mode?**

If you haven't made changes that affect the dimensions being analyzed, the charts will appear identical. For example, if you only changed salaries and you're viewing a Department distribution chart, headcount by department won't change. Try toggling to Cost metrics or analyzing different dimensions.

**Can I customize which Hub charts are available?**

The available charts are configured by your Agentnoon administrator. If you need additional chart types or custom analytics, contact your admin or Agentnoon support.

**Do Hub analytics work with effective dates?**

Hub analytics show the final state of your scenario (the "After" view), not time-phased views. For time-phased analysis, use Forecast view. Hub shows "what the org looks like" after changes, Forecast shows "when changes take effect."

**Can I filter Hub charts to specific departments or locations?**

Yes. Most Hub charts have filtering capabilities. Use the filter controls to narrow your analysis to specific segments of the organization.

**How do I know if a span of control is "good" or "bad"?**

General guidelines:
- **1-3 direct reports**: May indicate narrow span, potential for flattening
- **4-8 direct reports**: Generally healthy span for most roles
- **9-15 direct reports**: High span, manageable for senior leaders or operationally-focused roles
- **15+ direct reports**: Very high span, may indicate lack of support structure

Context matters - sales leaders might have higher spans, while technical leaders might have lower spans.

---

## Related Articles

- [Workforce Hub Overview](../hub/overview.md) - Hub at the Main Org level
- [Layers & Spans Chart](../hub/layers-spans-chart.md)
- [Headcount Distribution Chart](../hub/headcount-distribution-chart.md)
- [Headcount Heatmap Chart](../hub/headcount-heatmap-chart.md)
- [Scenario Forecast](scenario-forecast.md)
- [Creating Scenarios](creating-scenarios.md)
