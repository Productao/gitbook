---
description: Guide to using the Headcount Heatmap chart
---

# 🗺️ Headcount Heatmap Chart

The Headcount Heatmap shows workforce distribution across two dimensions simultaneously — revealing structural depth and patterns that are invisible in single-dimension views.

## What It Shows

* **X-axis (columns):** Primary grouping — Department, KLT Area, Location, Job Function
* **Y-axis (rows):** Hierarchical dimension — Layers (most useful), Pay Grade, Level
* **Cell color intensity:** Darker = more headcount in that intersection
* **Cell values:** Exact headcount numbers

**Recommended setup:** X-axis = Department (or KLT Area), Y-axis = Layers.

## How to Read It

**Layer depth** — Count how many rows have data per column — this is how many layers that department has. Consistent depth across departments indicates standardized structure; outlier columns indicate structural variation.

**Concentration points** — Dense cells show where most people are. Small populations at high layers (e.g., 2 people in Layer 9) are potential efficiency flags — are those senior positions adding value?

**Structural anomalies to flag:**

* One department with 9+ layers when others have 6 — why so many?
* Very small populations (1–3 people) at high layer numbers
* Missing middle layers (structural gaps)
* Highly inconsistent patterns across comparable departments

**Healthy patterns** — 5–6 consistent layers across departments, concentration in middle layers (3–5), minimal populations at extreme layers.

## Common Use Cases

**Analyze chain length:** Set Departments × Layers, count rows per column, identify which departments have unusually long reporting chains, investigate why.

**Compare business units:** Look for departments with different patterns from peers; consistent patterns = standardized structure; variation warrants investigation.

**Pre/post-reorg comparison:** View heatmap in Main Org (current state), screenshot, then open the scenario to see how proposed changes reduce layers or redistribute headcount.

## Interactive Features

**Show table** — Click to reveal position-level breakdown for any cell (who is in that layer-department combination). Also exportable.

**Filters** — Apply filters to focus on specific layers only (e.g., Layers 1–4 for leadership analysis) or specific departments.

**Export** — PNG for presentations, PowerPoint for editable charts, CSV for quantitative analysis in Excel.

## Troubleshooting

| Problem                          | Solution                                                                                  |
| -------------------------------- | ----------------------------------------------------------------------------------------- |
| Chart looks empty                | Check filters; verify X/Y axes are configured; confirm recent data upload                 |
| Too many layers showing          | May be legitimate or a data issue; filter to Layers 1–6 to reduce noise                   |
| Numbers don't match expectations | Check scope filters; verify access permissions; confirm effective date range in scenarios |

## Related Resources

* [Layers and Spans of Control Chart](layers-spans-chart.md)
* [Headcount Distribution Chart](headcount-distribution-chart.md)
* [Hub Overview](overview.md)
* [Planning a Reorganization](../use-case-tutorials/planning-reorganization.md)
