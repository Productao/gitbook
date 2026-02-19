---
description: Guide to using the Headcount Distribution chart
---

# Headcount Distribution Chart

### Overview

The **Headcount Distribution** chart is a fundamental analytics tool that shows how your workforce is distributed across different organizational dimensions. It provides clear, immediate visibility into headcount counts or percentages across layers, departments, locations, or any other attribute in your organization.

This chart is particularly useful for understanding workforce composition, identifying imbalances, and communicating headcount allocation to stakeholders during budget planning and organizational review conversations.

### What This Chart Shows

The chart displays workforce distribution using:

* **X-axis**: The dimension you're analyzing (e.g., layers, departments, locations)
* **Y-axis**: Headcount count or percentage
* **Bars or visualization elements**: Each represents a category with corresponding headcount

**Example**: "Layer 5 contains 45% of the organization's total headcount" or "The Growth organization has 612 total people"

> **[Screenshot placeholder: Headcount Distribution by layers showing pyramid shape with percentages]**

### When to Use This Chart

Use the Headcount Distribution chart when you need to:

* **Understand workforce composition** - See how headcount is allocated across dimensions
* **Identify organizational imbalances** - Spot top-heavy or bottom-heavy structures
* **Compare department sizes** - Quickly see relative team sizes
* **Track changes over time** - Monitor how distribution shifts (in scenarios)
* **Prepare leadership presentations** - Show clear headcount breakdowns
* **Support budget conversations** - Demonstrate current workforce allocation
* **Analyze organizational shape** - Understand pyramid structure

### Configuring the Chart

#### Selecting the X-Axis Dimension

Choose what dimension to analyze headcount across:

* **Layers** - See distribution by organizational level (most common)
* **Pay Grade** - Understand compensation level distribution
* **Department** - Compare headcount across departments
* **KLT Area** - View business unit sizes
* **Location/City** - Analyze geographic distribution
* **Job Function** - See functional area headcount
* **Any custom field** - Use organization-specific attributes

**To change the X-axis**:
1. Use the second dropdown in the chart navigation
2. Select your desired dimension
3. Chart updates automatically

#### Choosing Display Mode

Toggle between display modes using the settings gear icon:

* **Numbers (Count)** - Shows absolute headcount numbers
  * Best for: Actual workforce size, budget calculations
  * Example: "Layer 5 has 287 people"

* **Percentages (Distribution)** - Shows relative proportions
  * Best for: Understanding composition, comparing across organizations
  * Example: "Layer 5 represents 32% of total headcount"

#### Sorting Options

Control how the data is ordered:

* **Ascending** - Smallest to largest (left to right)
* **Descending** - Largest to smallest (left to right)
* **Natural order** - Layer 1, 2, 3... or alphabetical for text dimensions
* **Custom** - Manual reordering (in some configurations)

**Access sorting**: Click the settings gear icon → adjust Y-axis or X-axis order

> **[Screenshot placeholder: Toggle between numbers and percentages in settings panel]**

> **[Screenshot placeholder: Sorted distribution showing ascending vs descending order]**

### How to Interpret the Data

#### Analyzing by Layers

When X-axis = Layers, the chart reveals organizational shape:

* **Bottom-heavy (pyramid)**: More people at lower layers
  * Common in manufacturing, retail, operations-heavy orgs
  * Example: 60% at layers 5-6, 20% at layers 3-4, 10% at layers 1-2

* **Top-heavy (inverted pyramid)**: More people at senior layers
  * May indicate compression or excess management layers
  * Example: 40% at layers 1-3, 35% at layer 4, 25% at layers 5-6

* **Balanced (diamond)**: Concentration in middle layers
  * Common in professional services, knowledge work
  * Example: 15% at senior, 60% in middle, 25% at junior layers

#### Comparing Across Departments

When X-axis = Department or KLT Area:

* Quickly see relative team sizes
* Identify largest and smallest organizations
* Support resource allocation discussions
* Verify expected department sizes

**Example**: "Commercial NA: 450, Growth: 612, R&D: 234"

> **[Screenshot placeholder: Headcount Distribution by department showing relative team sizes]**

#### Distribution Patterns to Note

* **Sudden drops or spikes** - May indicate data issues or real structural patterns
* **Missing layers** - Gaps in organizational hierarchy
* **Extremely small groups** - Teams that may be unsustainable
* **Dominant categories** - Where most workforce is concentrated

### Common Use Cases

#### Use Case 1: Understanding Organizational Shape

**Goal**: Determine if the organization is top-heavy, bottom-heavy, or balanced

**Workflow**:
1. Navigate to Headcount Distribution chart
2. Set X-axis to **Layers**
3. View in **percentage mode** for clear proportions
4. Sort in **natural order** (Layer 1, 2, 3...)
5. Analyze the shape:
   * Is it pyramid (bottom-heavy)?
   * Is it inverted (top-heavy)?
   * Is it diamond (balanced)?
6. Compare against industry norms or best practices

#### Use Case 2: Comparing Department Sizes

**Goal**: Understand relative team sizes for resource allocation

**Workflow**:
1. Set X-axis to **Department** or **KLT Area**
2. View in **numbers mode** for actual headcount
3. Sort **descending** to see largest to smallest
4. Note the distribution
5. Export as PowerPoint for budget discussions
6. Use **show table** to see position-level details

#### Use Case 3: Geographic Distribution Analysis

**Goal**: Understand workforce distribution across locations

**Workflow**:
1. Set X-axis to **Work City** or **Work Country**
2. Choose **percentage mode** to see proportions
3. Sort **descending** to identify major hubs
4. Filter by department to see location distribution per team
5. Document findings for real estate or expansion planning

#### Use Case 4: Pay Grade Distribution

**Goal**: Understand compensation level distribution

**Workflow**:
1. Set X-axis to **Pay Grade**
2. View in **percentage mode**
3. Sort in **natural order** (lowest to highest grade)
4. Look for:
   * Concentration at certain grades
   * Gaps in progression
   * Top-heavy compensation patterns
5. Cross-reference with layers for compression analysis

### Advanced Analysis Techniques

#### Layered Filtering

Combine filters for deeper insights:

1. **Filter by department** → See headcount distribution within that department only
2. **Filter by location** → Analyze distribution for a specific geography
3. **Filter by multiple attributes** → Narrow focus to specific population

**Example**: Filter to "Growth + North America + Layer 4-6" to see mid-level distribution in that scope

#### Time-Based Comparison

Compare distribution across different time periods or scenarios:

1. View distribution in **Main Org** (current state)
2. Note the pattern
3. Switch to a **Scenario** with planned changes
4. View same distribution chart
5. Compare before/after to see impact of changes

#### Combining with Other Charts

For comprehensive analysis:

1. Start with **Headcount Distribution** by layers (understand shape)
2. Switch to **Headcount Heatmap** (see layer × department)
3. Then view **Layers and Spans** (understand management structure)
4. Finally use **Org Chart** to investigate specific areas

### Interactive Features

#### Show Table Function

Click **Show table** to reveal:
* Position-by-position breakdown
* All attributes for each position in view
* Exact counts for each category
* Exportable data for further analysis

> **[Screenshot placeholder: Show table view revealing position-level breakdown]**

#### Filtering from Chart

* Click on specific bars or elements (chart-specific)
* May filter down to that subset
* Use to quickly drill into specific categories

### Export Options

#### PNG Export
* Quick visual for presentations
* Includes current configuration and filters
* Good for executive summaries

#### PowerPoint Export
* Generates editable chart in PowerPoint
* Maintains data structure
* Can be customized further in PPT
* Best for formal presentations

#### CSV Export
* Detailed position-level data
* All attributes included
* Use for quantitative analysis in Excel
* Good for detailed workforce planning

### Settings and Customization

Access the settings gear icon to adjust:

* **Display mode** - Toggle between numbers and percentages
* **Sort order** - Change ascending/descending or natural order
* **Color schemes** - Adjust visual appearance (if available)
* **Label formatting** - Show/hide data labels on chart

### Strategic Insights from This Chart

#### Organizational Health Indicators

* **Balanced pyramid** - Sustainable structure with appropriate ratio of leaders to ICs
* **Too top-heavy** - May indicate excess management, compression, or efficiency opportunities
* **Too bottom-heavy** - May indicate need for leadership capacity or structure

#### Budget Implications

* **Large concentrations** - Where most cost and headcount are allocated
* **Small populations** - May be unsustainable or under-resourced
* **Unexpected patterns** - Areas needing strategic review

#### Questions This Chart Helps Answer

* How many people are in each layer of the organization?
* What percentage of our workforce is at senior vs. junior levels?
* How does headcount distribute across our business units?
* Where is our workforce concentrated geographically?
* Is our organization top-heavy or bottom-heavy?
* How does our distribution compare to planned state?

### Best Practices

1. **Start with layers** - Most fundamental view of organizational structure
2. **Use percentages for comparison** - Easier to compare across different org sizes
3. **Use numbers for planning** - Actual headcount needed for budget calculations
4. **Sort thoughtfully** - Natural order for hierarchical data, descending for comparisons
5. **Filter systematically** - Analyze one organization or dimension at a time
6. **Export early** - Capture snapshots for before/after comparisons
7. **Combine with context** - Numbers need business context to be meaningful
8. **Check filters** - Verify you're viewing the expected population

### Workflow Example: Complete Distribution Analysis

**Scenario**: Preparing for annual organizational review

1. **Overall Shape Analysis**:
   * Navigate to Headcount Distribution chart
   * Set X-axis to **Layers**
   * Toggle to **percentage mode**
   * Sort in natural order
   * Document: "Organization is 15% layers 1-3, 45% layer 4-5, 40% layer 6+"
   * Take screenshot

2. **Department Comparison**:
   * Change X-axis to **Department**
   * Switch to **numbers mode**
   * Sort descending
   * Note relative sizes
   * Export to PowerPoint

3. **Geographic Analysis**:
   * Change X-axis to **Work Country**
   * View percentages
   * Sort descending
   * Document major locations
   * Filter by each department to see location distribution per team

4. **Pay Grade Analysis**:
   * Change X-axis to **Pay Grade**
   * Percentage mode
   * Natural sort (low to high)
   * Look for patterns
   * Export CSV for detailed analysis

5. **Presentation Prep**:
   * Export key views as PowerPoint slides
   * Add to slide pack with annotations
   * Share with leadership team

### Common Patterns and What They Mean

#### Healthy Patterns

* **Pyramid by layers** - More ICs than managers, appropriate ratios
* **Even department distribution** - Balanced investment across functions
* **Clear geographic hubs** - Concentrated presence with strategic intent

#### Concerning Patterns

* **Inverted pyramid** - Too many managers relative to ICs
* **Extreme concentration** - Over 70% in one category (unless expected)
* **Tiny populations** - Groups too small to be sustainable (e.g., 2-3 people in a department)
* **Missing mid-levels** - Gaps in organizational layers

### Troubleshooting

#### Chart looks unexpected:
* **Check active filters** - May be scoped to subset
* **Verify data load** - Ensure recent data sync
* **Check dimension selection** - Confirm X-axis is set correctly

#### Numbers don't match expectations:
* **Review filter settings** - May exclude expected populations
* **Check date ranges** - In scenarios, verify effective dates
* **Verify access scope** - You may not have access to full organization

### Related Resources

* [Headcount Heatmap](headcount-heatmap-chart.md) - Two-dimensional distribution view
* [Layers and Spans of Control](layers-spans-chart.md) - Management structure analysis
* [Chart Navigation](chart-navigation.md) - General Hub controls and features
* [Hub Overview](overview.md) - Introduction to all Hub charts
