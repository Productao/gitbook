---
description: Understanding organizational health metrics
hidden: false
---

# Org Metrics & Insights

Agentnoon automatically calculates powerful organizational metrics to help you understand your org structure, identify opportunities, and make data-driven decisions. These calculated fields (marked "FX") update in real-time as your org changes.

## What Are Calculated Metrics?

Calculated metrics are fields that Agentnoon computes automatically based on your org structure. You don't need to manually enter or update these values - they're always current and accurate.

**Where to find them:**
- Org chart cards (via Card Content settings)
- Directory View columns
- Workforce Hub charts
- Exports and reports

**How to identify them:** Look for the "FX" label next to the field name, indicating it's a formula-based calculation.

---

## Span of Control (SOC) Metrics

Span of Control metrics help you understand management load and organizational efficiency. Agentnoon provides four SOC calculations:

### Quick Reference Table

The following table provides a detailed breakdown of each Span of Control (SoC) metric, including its legacy name, calculation method, and practical use cases.

<table><thead><tr><th width="220.8046875">SoC metric</th><th width="135.51953125">Legacy name</th><th width="165.734375">How its calculated</th><th>Why you would want to use this metric</th></tr></thead><tbody><tr><td><p>Direct Span of Control</p><p><em>i.e. The number of employees who report directly to a manager.</em></p></td><td>Direct Span of Control</td><td>Number of direct reports</td><td>To determine a manager's <strong>immediate supervisory burden</strong>, and day-to-day people-management capacity. </td></tr><tr><td><p>Average Direct Manager Span of Control</p><p><em>i.e. Average of the direct SOC values for the managers who report to the focal manager.</em></p></td><td>Average (Immediate) SOC</td><td>(Sum of direct SOC values of direct-report managers) ÷ (Number of those managers)</td><td>To determine the average load of a leader's <strong>direct reports who are managers</strong>.</td></tr><tr><td><p>Average Hierarchical Span of Control</p><p><em>i.e. Average of the direct SOC values for all managers in the focal manager's hierarchy (all levels below, not including the focal manager).</em></p></td><td>Average (Total) SOC</td><td>(Sum of direct SOC values of all managers in hierarchy including focal) ÷ (Number of those managers)</td><td>To determine the <strong>overall  managerial load under an individual leader.</strong></td></tr><tr><td><p><strong>(NEW)</strong> Average Managerial Span of Control</p><p><em>i.e. Average of the direct SOC values for all managers in the hierarchy, including the focal manager.</em></p></td><td>None</td><td>(Sum of direct SOC values of all managers in hierarchy including focal) ÷ (Number of managers <strong>including</strong> <strong>focal</strong>)</td><td>To determine the <strong>average number of direct reports across all managers in a hierarchy</strong> (including the owner of the hierarchy).</td></tr></tbody></table>

---

### 1. Direct Span of Control

**What it measures:** The number of employees who report directly to a manager.

**How it's calculated:** Count of direct reports

**When to use it:**
- Determine a manager's immediate supervisory burden
- Assess day-to-day people-management capacity
- Identify managers who may be overburdened or under-utilized

**Example:** If Alice has 8 people reporting directly to her, her Direct SOC = 8

**Industry benchmarks:**
- Optimal range: 5-9 direct reports for most roles
- Executive level: 5-7 direct reports
- Frontline managers: 7-15 direct reports (depending on role complexity)

---

### 2. Average Direct Manager Span of Control
(formerly "Average Immediate SOC")

**What it measures:** Average Direct SOC of the managers who report directly to a focal manager.

**How it's calculated:**
```
(Sum of Direct SOC values of direct-report managers) ÷ (Number of those managers)
```

**When to use it:**
- Determine the average load of a leader's direct reports who are managers
- Assess whether your management layer has balanced workloads
- Identify inconsistencies in team structures

**Example:**
- Alice's direct reports include 3 managers:
  - Bob (Direct SOC = 6)
  - Carol (Direct SOC = 4)
  - David (Direct SOC = 8)
- Alice's Average Direct Manager SOC = (6 + 4 + 8) ÷ 3 = 6

---

### 3. Average Hierarchical Span of Control
(formerly "Average Total SOC")

**What it measures:** Average Direct SOC of all managers in the hierarchy below the focal manager (not including the focal manager).

**How it's calculated:**
```
(Sum of Direct SOC values of all managers below focal) ÷ (Number of those managers)
```

**When to use it:**
- Determine the overall managerial load under an individual leader
- Understand management density across the entire org under a leader
- Compare efficiency across different divisions or departments

**Example:**
- Alice leads an organization with 10 managers below her
- Sum of all their Direct SOC values = 60
- Alice's Average Hierarchical SOC = 60 ÷ 10 = 6

---

### 4. Average Managerial Span of Control (NEW)

**What it measures:** Average Direct SOC of all managers in the hierarchy, **including** the focal manager.

**How it's calculated:**
```
(Sum of Direct SOC values of all managers including focal) ÷ (Number of managers including focal)
```

**When to use it:**
- Determine the average number of direct reports across all managers in a hierarchy
- Get a complete picture including the focal manager's own load
- Benchmark entire org units against industry standards

**Example:**
- Alice's Direct SOC = 8
- Her 10 direct-report managers' combined SOC = 60
- Alice's Average Managerial SOC = (8 + 60) ÷ 11 = 6.18

---

## Other Key Metrics

### Total Organization Size

**What it measures:** Total number of positions under a manager (direct + indirect reports).

**When to use it:**
- Understand the full scope of a leader's responsibility
- Compare organization sizes across departments
- Identify growth or reduction opportunities

**Example:** Alice has 8 direct reports, who collectively have 45 direct reports. Alice's Total Org Size = 8 + 45 = 53

---

### Layer / Level

**What it measures:** Distance from the CEO/top of the organization.

**How it's calculated:**
- CEO = Layer 1
- CEO's direct reports = Layer 2
- Their direct reports = Layer 3
- And so on...

**When to use it:**
- Analyze org depth
- Identify unnecessarily deep reporting chains
- Compare layers across departments

**Industry benchmarks:**
- Small companies (< 500): 4-5 layers
- Mid-size companies (500-5000): 5-7 layers
- Large companies (5000+): 6-9 layers

**Red flags:** More than 8-10 layers suggests potential inefficiency

---

## Using Metrics for Analysis

### Finding Compression

Compression occurs when managers have very few direct reports (1-2), often indicating potential organizational inefficiency.

**How to identify:**
1. Go to Workforce Hub → Span of Control Distribution
2. Look for high counts in the "1-2" direct reports column
3. Filter by pay grade to find senior leaders with low SOC
4. Use Spotlight in Main Org to visualize specific positions

**When compression is acceptable:**
- New teams still ramping up
- Specialized technical leaders with IC responsibilities
- Interim structures during reorganizations

---

### Analyzing Org Depth

Deep hierarchies (many layers) can slow decision-making and communication.

**How to analyze:**
1. Go to Workforce Hub → Headcount Heatmap
2. Set X-axis = Department, Y-axis = Layer
3. Look for departments with unusually deep structures
4. Compare against industry benchmarks

**Questions to ask:**
- Why does Department A have 8 layers while Department B has 5?
- Are there opportunities to flatten the structure?
- Do deep chains add value or create bottlenecks?

---

### Identifying High-Span Managers

Very high spans (16+) may indicate overburdened managers or well-functioning, low-complexity teams.

**How to identify:**
1. Go to Main Org
2. Use Spotlight → Direct SOC → 16-25
3. Review each highlighted position for context

**Context matters:**
- High span for standardized, repetitive work (e.g., call center) may be fine
- High span for complex, strategic work may indicate need for additional management support

---

## Adding Metrics to Your View

### On Org Chart Cards

1. Click **Card Content** in the toolbar
2. Scroll to calculated metrics (marked "FX")
3. Check the metrics you want to display:
   - Direct Span of Control
   - Average Direct Manager SOC
   - Average Hierarchical SOC
   - Average Managerial SOC
   - Total Organization Size
   - Layer
4. Drag to reorder
5. Changes apply immediately

**Pro tip:** Don't add too many metrics at once. Cards become cluttered. Add only what you need for your current analysis.

---

### In Directory View

1. Go to Directory View
2. Click column settings
3. Add calculated metric columns
4. Sort by metrics to find outliers

**Common sorts:**
- Direct SOC (high to low) - Find largest teams
- Layer (shallow to deep) - Understand org depth
- Total Org Size (high to low) - Identify biggest org units

---

### In Workforce Hub

Calculated metrics power many Hub charts:

- **Layers and Spans of Control** - Uses Layer + Direct SOC
- **Span of Control Distribution** - Uses Direct SOC + Layer
- **Headcount Heatmap** - Can display by Layer

**How to use:**
1. Go to Workforce Hub
2. Select a chart
3. Configure axes using calculated metrics
4. Apply filters to focus analysis

---

## Best Practices

1. **Use metrics for discovery, not decisions** - Metrics identify opportunities; context determines action
2. **Benchmark against your industry** - Tech companies vs manufacturing vs retail have different norms
3. **Combine multiple metrics** - Don't rely on Direct SOC alone; consider Total Org Size, Layer, and business context
4. **Track trends over time** - Compare metrics across org snapshots to see changes
5. **Communicate the "why"** - When presenting metrics, explain why they matter and what they indicate

---

## Common Red Flags

⚠️ **Watch for these patterns:**

- **> 30% of managers with Direct SOC of 1-2** - Potential compression
- **Direct SOC > 20 without clear justification** - May indicate overburdened managers
- **Inconsistent spans across similar roles** - Why does Manager A have 3 reports while Manager B has 15?
- **> 8 layers in companies < 5000 employees** - Potentially inefficient hierarchy
- **High Average Hierarchical SOC with low Direct SOC** - Potential middle management compression

---

## When to Take Action

Prioritize investigation and potential changes when:

1. Metrics are outside optimal range **AND**
2. There's no clear business justification **AND**
3. It's causing operational issues:
   - Decision delays
   - Communication bottlenecks
   - Manager burnout or dissatisfaction
   - Employee engagement issues

**Remember:** Metrics are indicators, not mandates. Always consider context before making organizational changes.

---

## Next Steps

Now that you understand org metrics:
- Try the [Span of Control Analysis](../use-case-tutorials/span-of-control-analysis.md) tutorial
- Explore [Workforce Hub](../start-here/workforce-hub-fundamentals.md) to visualize metrics
- Create a [Scenario](../scenarios/creating-scenarios.md) to model improvements
- Read the detailed [Span of Control Metrics](../org-chart/span-of-control-metrics.md) reference

