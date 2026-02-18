---
description: Guide to using the Headcount Heatmap chart
---

# Headcount Heatmap Chart

### Overview

The **Headcount Heatmap** chart provides a powerful two-dimensional visualization of how headcount is distributed across your organization. Unlike simple distribution charts, the heatmap allows you to see the intersection of two dimensions simultaneously—revealing patterns that might be hidden in single-dimension views.

This chart is particularly valuable for understanding organizational depth (layers), identifying structural patterns across departments, and spotting areas where chains of command may be unusually long or compressed.

### What This Chart Shows

The heatmap displays workforce distribution using:

* **X-axis (columns)**: First dimension (e.g., departments, KLT areas, locations)
* **Y-axis (rows)**: Second dimension (typically layers or levels)
* **Cell intensity/color**: Headcount concentration (darker = more people)
* **Cell values**: Exact headcount numbers in each intersection

**Example**: "The Growth organization has 45 people in Layer 5, while Commercial NA has 23 people in Layer 5"

### When to Use This Chart

Use the Headcount Heatmap when you need to:

* **Visualize organizational depth** - See how many layers exist in each department
* **Identify long chains** - Spot departments with more layers than others
* **Compare structural patterns** - Understand if departments are structured consistently
* **Find structural anomalies** - Identify departments with unusual layer distributions
* **Analyze layer consistency** - Determine if layer definitions are consistent across org
* **Support reorganization planning** - Visualize impact of structural changes
* **Identify compression points** - See where layers are densely populated

### Configuring the Chart

#### Setting the X-Axis

The X-axis typically represents your primary grouping dimension:

* **Department** - Compare structural depth across departments
* **KLT Area** - View business unit layer patterns
* **Entity** - Analyze by legal entity or company
* **Location/Region** - See geographic structural patterns
* **Job Function** - Compare functional area structures

**To set X-axis**: Use the second dropdown in the chart navigation bar

#### Setting the Y-Axis

The Y-axis typically represents the hierarchical dimension:

* **Layers** (most common) - Shows organizational levels
* **Pay Grade** - Visualizes compensation level distribution
* **Level** - Alternative to layers if your org uses different terminology
* **Manager Level** - Distance from top of organization

**To set Y-axis**: Use the third dropdown in the chart navigation bar

#### Recommended Configuration

For analyzing organizational chains and structure:

* **X-axis**: Department or KLT Area
* **Y-axis**: Layers
* **Result**: See how many organizational layers each department has

### How to Interpret the Data

#### Understanding Layer Depth

The heatmap immediately shows the hierarchical depth of each department:

* **Consistent depth** - All departments span similar number of layers (e.g., 6 layers each)
* **Varying depth** - Some departments have more layers than others
* **Outlier departments** - One department with 9 layers when others have 6

**What this means**:
* Organizations typically aim for consistent layer depth
* Extra layers can mean longer chains of command
* Extra layers can add friction and slow decision-making
* Some business context may justify additional layers

#### Identifying Concentration Points

Look for cells with high headcount numbers:

* **Dense cells** - Large numbers indicate where most people are located
* **Layer-department patterns** - Which layers are most populated in each department
* **Sparse cells** - Few people may indicate bottlenecks or unusual structures

**Example from transcript**: "It seems that these make sense. We've got one, two, three, four, five, six chains. Six layers in this organization in growth, which is quite consistent with every other group."

#### Analyzing Structural Consistency

Compare columns (departments) to see if they're structured similarly:

* **Aligned patterns** - Similar distributions suggest standardized structure
* **Different patterns** - May indicate different business needs or inconsistent organization
* **Missing layers** - Gaps in certain departments may be intentional or problematic

#### Spotting Anomalies

Look for unusual patterns that warrant investigation:

* **Single department with 9+ layers** - Why so many layers compared to others?
* **Very small populations at top layers** - "Why do we have 3 people in Layer 10?"
* **Empty middle layers** - Missing layer numbers may indicate structural gaps
* **Extreme concentration** - One cell with 80% of department headcount

**From transcript**: "Should we have a group that has nine layers to the organization, which is above average for the organization, that's something we might want to consider. Why do we have these? In this case, it's 14, but in another case, it might be three. Why do we have three people in layer 10 of this organization? Is that really necessary?"

### Common Use Cases

#### Use Case 1: Analyzing Organizational Chain Length

**Goal**: Understand how deep reporting chains are in each department

**Workflow**:
1. Navigate to Headcount Heatmap chart
2. Set X-axis to **Department** or **KLT Area**
3. Set Y-axis to **Layers**
4. Observe the vertical extent of each column
5. Count the number of layers in each department
6. Identify departments with more layers than others
7. Document: "Growth has 6 layers, Commercial NA has 6 layers, R&D has 7 layers"
8. Investigate why R&D has an extra layer

**Questions to ask**:
* Is the extra layer necessary?
* Does it add friction to decision-making?
* Are there only a few people in that extra layer?
* Should it be rationalized?

#### Use Case 2: Comparing Structural Patterns Across Business Units

**Goal**: Determine if business units are structured consistently

**Workflow**:
1. Configure X-axis: **KLT Area**
2. Configure Y-axis: **Layers**
3. Look across all columns
4. Note similarities and differences:
   * Do all areas span same number of layers?
   * Are populations distributed similarly?
   * Where do concentrations occur?
5. Take screenshot for leadership discussion
6. Export to PowerPoint for presentation

**Insights to look for**:
* **Consistency** - All areas have 6 layers with similar distribution
* **Variation** - One area has 8 layers while others have 6
* **Implications** - May indicate opportunity for standardization

#### Use Case 3: Identifying Small Populations at High Layers

**Goal**: Find potential inefficiencies where few people exist at senior layers

**Workflow**:
1. Set up heatmap: Departments × Layers
2. Focus on top rows (Layers 1-3)
3. Look for very small numbers (1-3 people)
4. Ask: "Why do we have 2 people in Layer 2 of this department?"
5. Click **Show table** to see specific positions
6. Navigate to org chart to investigate context
7. Consider if additional reporting layers are necessary

**Example**: Finding "3 people in Layer 10" suggests those positions may be:
* Creating unnecessary hierarchy
* Adding friction without value
* Candidates for flattening into Layer 9

#### Use Case 4: Pre- and Post-Reorganization Comparison

**Goal**: Visualize the impact of proposed structural changes

**Workflow**:
1. View heatmap in **Main Org** (current state)
2. Take screenshot or export
3. Document current layer depth per department
4. Switch to **Scenario** with proposed changes
5. View same heatmap configuration
6. Compare:
   * Did layer depth decrease in target departments?
   * Did headcount distribution become more balanced?
   * Were small high-layer populations eliminated?
7. Use in presentation to show before/after impact

### Advanced Analysis Techniques

#### Filtering for Focused Analysis

Apply filters to narrow focus:

* **Filter by senior layers only** - Focus on Layers 1-4 to analyze leadership structure
* **Filter by location** - See how one geography is structured
* **Filter by specific department** - Deep dive into one area

**Example**: Filter to "Layers 4-6" to analyze mid-management structure only

#### Switching Dimensions for Different Views

Try alternative dimension combinations:

* **Pay Grade × Department** - See compensation distribution across departments
* **Location × Layers** - Understand geographic-hierarchical patterns
* **Job Function × Pay Grade** - Analyze compensation by function

#### Cross-Chart Analysis

Combine heatmap with other charts for comprehensive understanding:

1. **Start with Heatmap** - Identify department with most layers
2. **Switch to Layers and Spans** - Analyze if that department also has span issues
3. **Go to Org Chart** - Investigate specific reporting chains
4. **Return to Heatmap** - Verify patterns after investigation

### Interactive Features

#### Show Table Function

Click **Show table** to reveal:
* Position-by-position breakdown for each cell
* Exact lists of who is in each layer-department combination
* All attributes for further analysis
* Exportable data

#### Color Intensity

* **Darker cells** - Higher headcount concentration
* **Lighter cells** - Lower headcount concentration
* **Empty/white cells** - No headcount in that combination
* Visual pattern recognition at a glance

#### Clickable Cells

* May allow clicking to filter (chart-specific)
* Can drill down to population in that cell
* Quick way to investigate specific combinations

### Export Options

#### PNG Export
* Visual snapshot of the heatmap
* Good for quick sharing and presentations
* Includes current filters and configuration

#### PowerPoint Export
* Generates editable chart element
* Can be further customized in PowerPoint
* Best for formal presentations
* Maintains data structure

#### CSV Export
* Detailed position-level data
* Shows all positions and their dimensions
* Use for quantitative analysis in Excel
* Good for detailed workforce planning

### Settings and Customization

Access the settings gear icon to adjust:

* **X-axis order** - Sort departments alphabetically or by size
* **Y-axis order** - Typically natural layer order (1, 2, 3...)
* **Color scaling** - Adjust intensity thresholds
* **Display values** - Show/hide numbers in cells
* **Legend options** - Customize color legend display

### Strategic Insights from This Chart

#### Organizational Efficiency Indicators

* **Fewer layers** - Generally more efficient, faster decision-making
* **Consistent depth** - Indicates intentional, standardized structure
* **Concentrated populations** - Shows where most workforce resides

#### Structural Red Flags

* **Outlier departments with extra layers** - May indicate over-structuring
* **Very small populations at high layers** - Potential inefficiency
* **Missing layers in middle** - Potential structural gaps
* **Extremely uneven patterns** - Suggests inconsistent organizational design

#### Questions This Chart Helps Answer

* How many layers does each department have?
* Are our departments structured consistently?
* Where do we have unusually long reporting chains?
* Which layers have the most headcount concentration?
* Are there small populations at high layers that may be inefficient?
* How does our structure compare across business units?
* What would a flatter organization look like?

### Best Practices

1. **Use layers as Y-axis** - Most intuitive for analyzing organizational depth
2. **Use department/KLT area as X-axis** - Best for comparing structural patterns
3. **Look for consistency** - Similar patterns across departments usually indicate good design
4. **Investigate outliers** - Departments with different patterns warrant deeper analysis
5. **Count the layers** - Literally count how many rows have data per column
6. **Consider context** - Some businesses legitimately need more layers than others
7. **Export for comparison** - Save snapshots when doing scenario planning
8. **Combine with org chart** - Use heatmap for patterns, org chart for specific investigation

### Workflow Example: Complete Layer Analysis

**Scenario**: Evaluating organizational structure for efficiency opportunities

1. **Initial Setup**:
   * Navigate to Headcount Heatmap
   * Set X-axis: **KLT Area**
   * Set Y-axis: **Layers**
   * Remove any filters to see full organization

2. **Overall Pattern Analysis**:
   * Observe all columns (departments)
   * Count layers per department:
     * Growth: 6 layers (Layers 1-6)
     * Commercial NA: 6 layers (Layers 1-6)
     * R&D: 7 layers (Layers 1-7)
     * Supply Chain: 8 layers (Layers 1-8)
   * Document: "Supply Chain has 2 more layers than most departments"

3. **Deep Dive into Outlier**:
   * Focus on Supply Chain column
   * Note which layers have small populations
   * Observe: "Layers 7-8 have only 4 people combined"
   * Click **Show table** to see specific positions
   * Take screenshot

4. **Context Investigation**:
   * Navigate to org chart
   * Filter to Supply Chain
   * Use Spotlight to find positions in Layers 7-8
   * Investigate: Are these necessary?
   * Document business context

5. **Recommendation Development**:
   * Determine if extra layers add value or friction
   * Consider if those 4 people could report at Layer 6 instead
   * Model in scenario if recommending change
   * Return to heatmap to show before/after

6. **Presentation Prep**:
   * Export heatmap as PowerPoint
   * Annotate with findings
   * Add org chart examples
   * Present recommendations to leadership

### Common Patterns and What They Mean

#### Healthy Patterns

* **Consistent 5-6 layers** across all departments
* **Concentration in middle layers** (Layers 3-5)
* **Minimal populations at extreme layers**
* **Similar distribution patterns** across comparable departments

#### Concerning Patterns

* **One department with 9+ layers** when others have 6
* **Small populations (1-3 people) at Layer 8+**
* **Missing middle layers** creating structural gaps
* **Extreme concentration** in single layer-department cell
* **Highly inconsistent patterns** suggesting ad-hoc structure

### Troubleshooting

#### Chart looks empty or sparse:
* **Check filters** - May be scoped too narrowly
* **Verify dimensions** - Ensure X and Y axes are set correctly
* **Check data** - Verify recent data upload

#### Too many layers showing:
* **Data issue** - May have incorrect layer assignments
* **Legitimate depth** - Some orgs truly have many layers
* **Filter to core layers** - Focus on Layers 1-6 if noise is an issue

#### Numbers don't match expectations:
* **Check scope** - Verify filters aren't excluding expected populations
* **Verify access** - You may only see subset you have access to
* **Check effective dates** - In scenarios, verify date ranges

### Visual Guide

> **[Screenshot placeholder: Headcount Heatmap showing departments on X-axis and layers on Y-axis with color intensity]**

> **[Screenshot placeholder: Heatmap showing one department with more layers than others (outlier department)]**

> **[Screenshot placeholder: Close-up of heatmap cells showing exact headcount numbers in each layer-department combination]**

> **[Screenshot placeholder: Show table view revealing position-level details for a specific cell]**

> **[Screenshot placeholder: Before/after comparison showing reduced layers after reorganization]**

### Related Resources

* [Layers and Spans of Control](layers-spans-chart.md) - Analyze management structure alongside layer depth
* [Headcount Distribution](headcount-distribution-chart.md) - Single-dimension distribution view
* [Chart Navigation](chart-navigation.md) - General Hub controls and features
* [Hub Overview](overview.md) - Introduction to all Hub charts
* [Planning a Reorganization](../use-case-tutorials/planning-reorganization.md) - Complete reorganization tutorial
