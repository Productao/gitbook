---
description: Detailed guide to using the Layers and Spans of Control chart
icon: layer-group
---

# Layers and Spans of Control Chart

The Layers and Spans of Control chart is a matrix showing how many managers fall into different span-of-control ranges across layers or departments. It immediately surfaces where spans are too narrow (compression) or too wide (overload).

## What It Shows

* **X-axis (columns)** — Span of control groupings (e.g., 1–2, 3–5, 6–9, 10–15, 16–25)
* **Y-axis (rows)** — Layers, Department, KLT Area, Pay Grade, or Location
* **Cell values** — Count of managers in each combination

**Example:** "In Growth, 114 managers have SOC 1–2, concentrated at layers 5 and 6."

## Configuration

**Span groupings (gear icon)** — Customize ranges to match your needs. Recommended settings: exclude 0–0 (ICs), include 1–2, 3–5, 6–9, 10–15, 16–25, 26–40. Drag to reorder from smallest to largest.

**Y-axis** — Layers (default) for layer-by-layer analysis; Department or KLT Area for cross-functional comparison; Pay Grade for compensation level analysis.

**Filters** — Apply a KLT area or department filter to analyze one org at a time — clearer patterns emerge with a focused scope.

## Interpreting the Data

**High concentrations in 1–2 span columns** — Potential compression — leaders managing minimal teams. Some 1:1 relationships are legitimate (e.g., VP of Strategy under CEO), but many indicate structural inefficiency.

**High spans (16–25+)** — Potential overload — evaluate based on work type, standardization, and manager experience. Not always problematic.

**Layer distribution patterns:**

* Many narrow spans at senior levels (layers 1–3) — top-heavy, senior leadership compression
* Many narrow spans at lower levels (layers 5–6) — compression in the execution layer
* Balanced distribution — healthy structure

## Common Use Cases

**Budget planning** — Configure chart > filter to one KLT area > identify high concentrations in the 1–2 range > note layers of concern > navigate to org chart with Spotlight (Direct SOC = 1–2) to investigate specifics.

**Leadership compression** — Set Y-axis to Pay Grade > focus on senior levels > look for narrow spans at top pay grades > use **Show Table** to see specific positions.

**Cross-department comparison** — Filter to Dept A, note the pattern, screenshot; switch to Dept B and compare — which has more narrow spans? Which structure could inform the other?

## Interactive Features

**Show Table** — Click to see the position-level breakdown behind each cell: exact lists, all attributes, and exportable data.

**Clickable cells** — Click a cell to drill in and filter to that span/layer combination.

## Export

PNG for presentations, PowerPoint for editable charts (recommended for budget decks), CSV (via **Show Table**) for quantitative analysis.

## Troubleshooting

| Problem                         | Solution                                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- |
| Too many rows (too many layers) | Filter to specific layers or a smaller org scope                                        |
| Numbers seem wrong              | Verify active filters; check if the 0–0 grouping is included (inflates counts with ICs) |
| Can't see narrow spans clearly  | Break down further: 1–1, 2–2, 3–3 groupings for more granularity                        |

## Related Resources

* [Headcount Heatmap Chart](headcount-heatmap-chart.md)
* [Headcount Distribution Chart](headcount-distribution-chart.md)
* [Hub Overview](overview.md)
* [Span of Control Analysis Tutorial](../use-case-tutorials/span-of-control-analysis.md)
