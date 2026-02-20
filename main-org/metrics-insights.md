---
description: Understanding organizational health metrics
hidden: false
---

# Org Metrics & Insights

Agentnoon automatically calculates organizational metrics (marked "FX" for formula-based) that update in real-time. Find them on org chart cards (via Card Content), in Directory columns, in Workforce Hub charts, and in exports.

## Span of Control (SOC) Metrics

| Metric | Calculation | Use It For |
|--------|-------------|-----------|
| **Direct SOC** | Count of direct reports | Assessing manager's immediate supervisory load |
| **Average Direct Manager SOC** (formerly Avg Immediate SOC) | Avg Direct SOC of managers who report to this position | Assessing whether the next-level managers are balanced |
| **Average Hierarchical SOC** (formerly Avg Total SOC) | Avg Direct SOC of all managers in the hierarchy below (excluding focal) | Overall management density under a leader |
| **Average Managerial SOC** (new) | Avg Direct SOC of all managers including focal position | Average reports-per-manager across the full hierarchy |

**Direct SOC benchmarks:** Optimal: 5–9 for most roles; Executives: 5–7; Frontline managers: 7–15 (depends on role complexity).

## Other Key Metrics

**Total Organization Size** — All positions under a manager (direct + all indirect). Measures scope of responsibility.

**Layer / Level** — Distance from CEO (CEO = Layer 1, direct reports = Layer 2, etc.). Measures org depth.

**Layer benchmarks:** <500 employees: 4–5 layers; 500–5,000: 5–7; >5,000: 6–9. More than 8–10 layers suggests potential inefficiency.

## Using Metrics for Analysis

**Find compression (too-narrow spans):**
1. Workforce Hub > Layers and Spans chart > look for high counts in the 1–2 SOC column
2. Or: Main Org > Spotlight > Direct SOC = 1–2

**Find deep hierarchies:**
1. Workforce Hub > Headcount Heatmap > X = Department, Y = Layers
2. Compare depths across departments

**Find overburdened managers:**
- Spotlight > Direct SOC = 16–25; evaluate context before acting

## Adding Metrics to Views

**On org chart cards:** Card Content (taskbar) > scroll to FX metrics > check boxes. Don't add too many — cards become cluttered.

**In Directory:** Column settings > add calculated metric columns > sort high-to-low to find outliers.

**In Workforce Hub:** Metrics power the Layers & Spans and Heatmap charts automatically.

## Red Flags

- >30% of managers with Direct SOC of 1–2 → potential compression
- Direct SOC >20 without clear justification → potentially overburdened
- Inconsistent spans across similar roles → structural inconsistency
- >8 layers in a company <5,000 employees → potentially inefficient hierarchy

## Important Caveat

Metrics are indicators, not mandates. Investigate context before taking action. A Direct SOC of 2 may be appropriate for a senior architect with strategic responsibilities; a Direct SOC of 20 may be fine for a standardized call center team.

## Related Resources

- [Span of Control Analysis Tutorial](../use-case-tutorials/span-of-control-analysis.md)
- [Layers and Spans Chart](../hub/layers-spans-chart.md)
- [Workforce Hub Overview](../hub/overview.md)
