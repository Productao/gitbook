---
description: Finding your way around Workforce Hub
icon: compass
---

# Workforce Hub Orientation & Navigation

## Accessing Workforce Hub

From Main Org or any scenario: click the view dropdown (defaults to "Org Chart") > select **Workforce Hub**.

From a scenario, the Before/After/Changes toggle is available to compare baseline vs. proposed state.

## Available Charts

**Layers & Spans Chart** — Bubble chart of span of control by management layer. Red bubbles = unhealthy spans; size = number of managers. Drill in by clicking a bubble.

**Headcount Distribution Chart** — Proportional view of headcount across any dimension (department, location, job level). Hover for exact numbers; click a segment to filter.

**Headcount Heatmap Chart** — Cross-tabulation of two dimensions with color intensity for concentration. Best for analyzing org depth and coverage gaps.

Switch charts via the chart selector dropdown at the top.

## Configuration Controls

Each chart has:

- **Primary dimension (X-axis):** Department, Location, Country, Job Level, Employee Type, custom attributes
- **Secondary dimension (Y-axis, Heatmap only):** Same options — creates cross-tab
- **Metric:** Headcount count, Cost, Average Salary, or Span of Control
- **Filters:** Department, Location, Job Level, Employee Type, custom fields (AND logic; clear all with one click)

Access advanced settings (sort order, percentages vs. counts, axis reversal) via the gear icon.

## Before / After / Changes (Scenarios Only)

When in a scenario:
- **Show Before** — baseline metrics (current Main Org state)
- **Show After** — proposed state with all scenario changes applied
- **Show Changes** — delta between before and after

Use Show Before to establish baseline, Show After to validate improvements, Show Changes to communicate impact to stakeholders.

## Exporting

Export button (top-right): PNG for presentations, PowerPoint for editable charts, CSV for analysis in Excel or BI tools.

For CSV: click **Show Table** first, then download.

## Common Workflows

**See SOC distribution:** Layers & Spans chart > look for red bubbles > click to drill into specific managers.

**See headcount by department:** Headcount Distribution > set dimension to Department.

**Find leadership coverage gaps:** Headcount Heatmap > X-axis = Department > Y-axis = Job Level > look for empty cells at senior levels.

**Compare org health before/after reorg:** Open scenario > Workforce Hub > select chart > toggle Before → After → Changes.

## Related Articles

- [Layers & Spans Chart](layers-spans-chart.md)
- [Headcount Distribution Chart](headcount-distribution-chart.md)
- [Headcount Heatmap Chart](headcount-heatmap-chart.md)
- [Hub Overview](overview.md)
