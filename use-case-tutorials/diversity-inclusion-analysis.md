---
description: Analyzing diversity metrics and planning inclusive workforce changes
hidden: false
---

# Diversity & Inclusion Analysis

Learn how to analyze diversity, equity, and inclusion (DEI) metrics in Agentnoon and model workforce changes that improve representation and equity across your organization.

## What is DEI Analysis?

Diversity & Inclusion Analysis in Agentnoon enables you to:
- **Track representation** across demographic dimensions
- **Identify gaps** in leadership and critical roles
- **Model diverse hiring** and promotion scenarios
- **Project DEI improvements** over time
- **Monitor pay equity** across demographic groups
- **Report on progress** toward DEI goals

## Prerequisites

Before performing DEI analysis, you must:

### 1. Upload DEI Data Fields

DEI analysis requires demographic data to be included in your Agentnoon data upload. Common fields include:
- **Gender** (Woman, Man, Non-binary, Prefer not to disclose)
- **Ethnicity/Race** (using your organization's categories)
- **LGBTQ+ Status** (if collected with consent)
- **Disability Status** (if collected with consent)
- **Veteran Status** (for US organizations)
- **Age/Generation** (Calculated from birth year)
- **Combined categories** (e.g., "BIPOC", "Underrepresented Minorities")

### 2. Configure Fields in Agentnoon

Work with your Agentnoon administrator to:
1. Add DEI fields via **Data Management > Fields and Attributes**
2. Ensure fields are marked as **Employee Fields** (not position fields)
3. Configure appropriate visibility and access controls
4. Consider creating **aggregate fields** (e.g., "BIPOC" combining multiple ethnicity values)

### 3. Privacy and Compliance

Important considerations:
- ⚠️ **Obtain consent** before collecting sensitive demographic data
- ⚠️ **Comply with local laws** (GDPR, EEOC, PIPEDA, etc.)
- ⚠️ **Limit access** to DEI data to authorized personnel only
- ⚠️ **Aggregate reporting** to prevent identification of individuals
- ⚠️ Never report on groups smaller than 5 people
- ⚠️ Allow "Prefer not to disclose" options

## Step 1: Analyze Current State in Workforce Hub

Workforce Hub is your primary tool for DEI analysis and reporting.

### Access Workforce Hub

1. Navigate to your **Main Org**
2. Click the view dropdown (default shows "Org Chart")
3. Select **Workforce Hub**

### Create DEI Breakdown Charts

**To analyze representation by demographic dimension:**

1. Click **+ Add Chart** in Workforce Hub
2. Select chart type:
   - **Bar Chart** - Compare representation across departments/levels
   - **Pie Chart** - Show overall composition percentages
   - **Table** - Detailed breakdown with multiple dimensions
3. Configure the chart:
   - **Rows**: Select your dimension (e.g., Department, Job Level, Location)
   - **Columns**: Select your DEI field (e.g., Gender, Ethnicity)
   - **Values**: Choose Headcount or Percentage
4. Click **Apply**

**Example Use Cases:**

- **Leadership representation**: Aggregate by "Job Level" and break down by "Gender" or "Ethnicity"
- **Departmental diversity**: Aggregate by "Department" and show "Ethnicity" composition
- **Location diversity**: Compare "Office Location" representation across "Gender"

### Use Filters for Focused Analysis

Narrow your analysis to specific populations:

1. Click **Filter** in the taskbar
2. Select filter criteria:
   - **BIPOC** = Yes (to analyze BIPOC population only)
   - **Gender** = Woman (to analyze women's representation)
   - **Job Level** = Executive, Senior Manager (to analyze leadership)
3. Apply multiple filters to see intersectional data
4. View filtered results in Workforce Hub charts

**Pro tip:** Save filtered views for recurring DEI reports!

## Step 2: Identify Representation Gaps

### Common Patterns to Look For

#### Leadership Pipeline Issues
- **Low representation** at higher job levels
- **Drop-off points** where underrepresented groups decrease
- **Missing from succession plans** for critical roles

#### Departmental Segregation
- Certain departments **significantly less diverse** than others
- **Technical roles** underrepresenting women or BIPOC employees
- **Administrative roles** overrepresenting certain groups (potential bias indicator)

#### Pay Inequity
- **Salary disparities** for comparable roles across demographic groups
- Different **pay progression rates** for underrepresented groups

### Using Spotlight for Gap Analysis

Find specific areas needing attention:

1. Go to **Main Org**
2. Click **Spotlight** in the taskbar
3. Select **Fields** tab
4. Choose your DEI field (e.g., "Gender")
5. Select the group to highlight (e.g., "Woman")
6. Click **Apply**

Now you can visually see representation across the org chart! Blue-highlighted cards show your selected demographic.

### Export Data for Deeper Analysis

Export Workforce Hub data for detailed analysis:

1. In Workforce Hub, click the **Export** button
2. Choose **CSV** format
3. Open in Excel/Google Sheets for:
   - Percentage calculations
   - Year-over-year comparisons
   - Statistical significance testing
   - Visualization creation

## Step 3: Set DEI Goals and Targets

Before modeling changes, establish clear objectives:

### Example DEI Goals

- **Representation targets**: "Increase women in engineering roles from 25% to 40% by 2027"
- **Leadership parity**: "Achieve leadership team composition reflecting overall workforce by 2026"
- **Pay equity**: "Eliminate statistically significant pay gaps by demographic group"
- **Pipeline goals**: "Ensure succession plans include diverse candidates for all VP+ roles"

### Document Your Baseline

Using current Workforce Hub data:
1. Record current representation percentages by level and department
2. Note specific gaps and disparities
3. Calculate required changes to meet targets
4. Determine realistic timeline

## Step 4: Model Diverse Hiring Scenarios

Use scenarios to plan and visualize DEI improvements.

### Create a DEI Scenario

1. Click **+ Create Scenario**
2. Name it descriptively: "2026 Diverse Hiring Plan"
3. Add description: "Model impact of targeted diverse recruitment"
4. Click **Create**

### Add Diverse Positions

**For new positions:**

1. Navigate to the department/team
2. Click **+ Add Position**
3. Fill in role details (title, level, salary)
4. **Important**: Set the hire date in the future
5. In the employee fields section:
   - Set DEI fields to reflect your hiring goals
   - Example: If targeting women in engineering, set "Gender" = "Woman"
6. Click **Create Position**

Repeat this for all planned diverse hires.

### Model Diverse Promotions

**To promote underrepresented employees:**

1. Find the employee card in the scenario
2. Click **Edit Position**
3. Change **Job Level** and/or **Job Title**
4. Update **Salary** per your compensation structure
5. Set **Effective Date** for when promotion takes effect
6. Click **Save**

### Track Scenario Impact

View how your changes affect overall diversity:

1. Open the **OpEx Panel** (Scenario Impacts and Changes)
2. Review headcount changes by level and department
3. Navigate to **Workforce Hub** within the scenario
4. Recreate your DEI charts to see the "after" state
5. Compare representation percentages

## Step 5: Project DEI Improvements in Forecast

The Forecast view shows how diversity will change over time with your planned hires and promotions.

### Access Forecast View

1. In your DEI scenario, click the view dropdown
2. Select **Forecast**

### Configure Forecast for DEI Analysis

1. **Aggregator dropdown**: Select how to group data
   - Choose **Gender**, **Ethnicity**, or other DEI fields
   - Or choose **Department** or **Job Level** to see changes by org segment
2. **Headcount/Cost toggle**: Select **Headcount**
3. **Time period**: Choose **Quarterly** or **Yearly**
4. **Year selector**: Pick which years to view (up to 5 years forward)

### Interpret Forecast Results

The forecast table shows:
- **Rows**: Your selected dimension (Gender, Department, etc.)
- **Columns**: Future time periods
- **Values**: Headcount in each category over time

**Example**: If aggregating by Gender with quarterly view:
- You'll see how women's headcount grows each quarter
- You can track when you'll reach representation targets
- Easily spot if hiring pace is too slow or aggressive

### Use Filters with Forecast

Combine filters for intersectional forecasting:

1. Click **Filter** in the taskbar
2. Select criteria: e.g., "Job Level" = "Manager, Senior Manager"
3. Return to Forecast view
4. Now you see DEI changes in leadership specifically

This helps answer: "When will we reach gender parity in leadership?"

## Step 6: Analyze Pay Equity

Use Workforce Hub to identify and address pay disparities.

### Compare Compensation by Demographics

1. In **Workforce Hub**, create a new chart
2. **Chart type**: Table
3. **Rows**: Gender or Ethnicity
4. **Columns**: Job Level or Job Title
5. **Values**: Average Salary
6. Click **Apply**

Look for:
- **Significant differences** in average salary for the same role
- Patterns suggesting **systemic pay inequity**

### Model Pay Equity Adjustments

In a scenario:

1. Identify underpaid employees from your analysis
2. For each affected employee:
   - Click **Edit Position**
   - Adjust **Salary** to market/equity level
   - Set **Effective Date** for adjustment
   - Add note: "Pay equity adjustment"
3. Track total cost in the OpEx Panel
4. Use this to budget for equity adjustments

## Step 7: Model Succession Planning for Diversity

Ensure diverse representation in leadership pipeline.

### Identify Succession Candidates

1. Use **Spotlight** to highlight high-performers from underrepresented groups
2. Apply filters:
   - Performance rating = High
   - Tenure = 2+ years
   - Gender/Ethnicity = Target demographics
3. Review highlighted candidates for leadership potential

### Create Succession Scenario

1. Create a scenario: "Diverse Leadership Succession 2026"
2. For retiring/departing leaders:
   - Set **Termination Date** on the current executive
3. For succession candidates:
   - Click **Edit Position**
   - Promote to the leadership role
   - Set **Effective Date** matching the departure
4. Use **Shortlist** feature to compare multiple candidates

### Visualize Leadership Changes

1. Go to **Workforce Hub** in the scenario
2. Create chart: Job Level (Executive+) by Gender/Ethnicity
3. Compare before/after representation
4. Adjust succession plans to meet diversity goals

## Step 8: Create DEI Reports and Dashboards

### Save Views for Recurring Reporting

1. Configure your DEI charts in Workforce Hub
2. Set relevant filters
3. Click **Views** in taskbar
4. Click **Save Current View**
5. Name it: "Monthly DEI Dashboard"

Now you can load this view anytime for consistent reporting!

### Export DEI Reports

**For executive presentations:**

1. Go to **Main Org** or your DEI scenario
2. Configure view with DEI highlights/filters
3. Click **Export** > **PowerPoint**
4. Automatically generates slides with org structure and diversity highlighting

**For detailed analysis:**

1. In **Workforce Hub**, configure DEI charts
2. Click **Export** > **CSV**
3. Use for detailed reporting, graphing, or compliance documentation

### Before/After Comparisons

Show impact of DEI initiatives:

1. Open your DEI scenario
2. Use the **Before/After/Changes** dropdown
3. Select **Changes** view
4. Export or screenshot to show anticipated improvements

## Best Practices

### Data Collection and Ethics

✅ **DO:**
- Obtain explicit consent before collecting demographic data
- Offer "prefer not to disclose" options for all fields
- Explain how data will be used and protected
- Limit access to aggregated, anonymized reports
- Comply with all applicable privacy laws
- Regularly audit who has access to DEI data

❌ **DON'T:**
- Report on groups of fewer than 5 people
- Share individual demographic data without consent
- Make hiring/promotion decisions solely based on demographics
- Assume demographics from names or appearance

### Analysis and Action

✅ **DO:**
- Look for **patterns**, not isolated cases
- Consider **intersectionality** (e.g., women of color face unique barriers)
- Investigate **root causes** of representation gaps
- Set **realistic, time-bound** improvement goals
- Track **leading indicators** (pipeline, offers, retention)
- Celebrate progress while acknowledging ongoing work

❌ **DON'T:**
- Draw conclusions from small sample sizes
- Ignore context (e.g., location demographics, industry norms)
- Set quotas without addressing systemic barriers
- Focus only on representation (also address inclusion, equity, belonging)

### Scenario Modeling

✅ **DO:**
- Model **multiple pathways** to DEI goals (hiring, promotion, retention)
- Test **realistic hiring volumes** based on pipeline
- Consider **retention risk** for underrepresented groups
- Include **succession planning** in DEI scenarios
- Share scenarios with DEI leaders and ERGs for input

❌ **DON'T:**
- Model aggressive hiring without addressing retention
- Ignore promotion equity (focus only on new hires)
- Forget to model compensation equity improvements
- Create scenarios without stakeholder buy-in

### Reporting and Transparency

✅ **DO:**
- Share **aggregated** DEI metrics with the organization
- Report **progress and setbacks** honestly
- Contextualize data with **qualitative insights**
- Tie DEI metrics to **business outcomes**
- Update reports **regularly** (quarterly or monthly)

❌ **DON'T:**
- Share reports that could identify individuals
- Cherry-pick positive metrics while hiding challenges
- Report metrics without action plans
- Treat DEI as a one-time initiative

## Common Use Cases

### Use Case 1: Quarterly DEI Board Report

**Goal**: Report to board on diversity progress

**Workflow**:
1. Open **Workforce Hub** in Main Org
2. Load saved view: "Board DEI Dashboard"
3. Review key charts:
   - Overall company composition (pie chart)
   - Leadership representation by level (bar chart)
   - Department diversity (table)
4. Compare to prior quarter (export from both)
5. Export to PowerPoint for board deck

**Frequency**: Quarterly

---

### Use Case 2: Building 2026 Diverse Hiring Plan

**Goal**: Model realistic path to 40% women in engineering by end of 2026

**Workflow**:
1. Analyze current state in Workforce Hub (baseline: 25% women)
2. Calculate needed change: +15 percentage points
3. Create scenario: "2026 Women in Eng Plan"
4. Add positions:
   - Q1 2026: Add 5 women engineers (with future hire dates)
   - Q2 2026: Add 5 women engineers
   - Q3 2026: Add 3 women engineers, promote 2 women to senior
   - Q4 2026: Add 2 women engineers, promote 1 to lead
5. Go to **Forecast** view, aggregate by Gender, filter to Engineering
6. Verify trajectory reaches 40% by Q4 2026
7. Share scenario with Engineering leadership for approval

---

### Use Case 3: Pay Equity Audit and Adjustment

**Goal**: Identify and close gender pay gaps

**Workflow**:
1. In **Workforce Hub**, create table: Gender x Job Level, value = Avg Salary
2. Identify roles with >5% salary difference by gender
3. Export to CSV, calculate statistical significance
4. Create scenario: "2026 Pay Equity Adjustments"
5. For underpaid women (or other groups):
   - Edit position, increase salary to equity level
   - Set effective date (e.g., March 1, 2026)
6. Review total cost in OpEx Panel
7. Get approval and budget allocation
8. Implement via data upload when effective date arrives

---

### Use Case 4: Diverse Leadership Succession

**Goal**: Ensure next VP of Product comes from underrepresented background

**Workflow**:
1. Create scenario: "VP Product Succession - Diverse Candidate"
2. Set termination date on current VP (e.g., June 30, 2026)
3. Use Spotlight to identify high-potential diverse candidates:
   - Filter: Performance = High, Job Level = Director/Senior Director
   - Spotlight: Ethnicity = BIPOC or Gender = Woman
4. Shortlist 3 diverse candidates
5. Model each promotion:
   - Create separate scenario for each candidate
   - Promote candidate, set effective date July 1, 2026
   - Model backfills for their vacated role
6. Compare scenarios for cost and organizational impact
7. Share with CEO and board for input

---

### Use Case 5: Intersectional Analysis (Women of Color in Leadership)

**Goal**: Understand representation of women of color specifically

**Workflow**:
1. Ensure you have combined field: "Women of Color" (Admin creates via Fields & Attributes)
2. In **Workforce Hub**, create chart:
   - Bar chart: Job Level (rows) x Women of Color % (values)
3. Apply filter: Job Level = Manager+
4. Identify drop-off: Strong representation at Manager, drops at Senior Manager
5. Create scenario: "WoC Leadership Pipeline 2026"
6. Model:
   - Promote 3 women of color from Manager to Senior Manager
   - Hire 2 women of color Senior Managers externally
   - Add to succession plans for 2 VP roles
7. Return to Forecast view, verify improvement trajectory
8. Partner with ERG on mentorship and sponsorship programs

## Privacy and Compliance Considerations

### Legal Requirements

Different jurisdictions have different rules:

**United States (EEOC)**
- Employers with 100+ employees must file EEO-1 report
- DEI data collection is permitted for affirmative action
- Cannot use protected characteristics for discriminatory decisions

**European Union (GDPR)**
- Demographic data is "sensitive personal data"
- Requires explicit consent and strong justification
- Must allow opt-out and data deletion

**Canada (PIPEDA, AODA)**
- Consent required for demographic data collection
- Disability data has additional protections
- Provincial laws may have additional requirements

**Consult your legal team** before implementing DEI tracking.

### Agentnoon Access Controls

Work with your admin to:
- **Restrict access** to DEI fields to HR and DEI team only
- Use **field visibility settings** to hide DEI data from managers
- Create **default views** for executives that show only aggregated data
- Set up **separate user roles** for DEI analysts vs. general users

### Anonymization Best Practices

- Never report on groups smaller than **5 people**
- Use **percentage ranges** instead of exact numbers when groups are small
- **Combine categories** when intersectional analysis creates tiny groups
- **Exclude from reports** any data that could identify individuals

## Troubleshooting

### "I don't see DEI fields in my data"

**Solution**: DEI fields must be uploaded in your employee data file
- Work with your admin to add columns to your CSV upload
- Fields must be added via **Data Management > Fields and Attributes**
- Mark fields as "Employee Fields" not "Position Fields"

### "Can I model demographic changes over time?"

**Yes!** Use effective dates and hire dates:
- New hires: Set future **hire dates** on new positions with demographic data
- Promotions: Set **effective dates** when editing existing employees
- View changes over time in **Forecast** view

### "The forecast isn't showing my DEI improvements"

**Check**:
- Are hire dates set on new positions?
- Are effective dates set on promotions/changes?
- Have you selected the DEI field in the Forecast aggregator dropdown?
- Are you looking at the right time period (year selector)?

### "I can't aggregate by demographic field in Workforce Hub"

**Solution**: Ensure the field is properly configured
- Field must exist in **Fields and Attributes**
- Field must not be hidden
- Try refreshing your data upload

### "Our DEI data is incomplete (many 'prefer not to disclose')"

This is common and expected:
- Report on both known data and response rates
- Note limitations in analysis
- Focus on patterns in available data
- Consider voluntary demographic surveys to increase data completeness
- Never pressure employees to disclose

## Next Steps

After completing DEI analysis:

1. **Share findings** with leadership and DEI stakeholders
2. **Create action plans** based on identified gaps
3. **Get approval** for diverse hiring and promotion scenarios
4. **Implement changes** via recruiting, development, and succession planning
5. **Track progress** with recurring Workforce Hub reports
6. **Iterate and improve** based on outcomes

## Related Resources

- **[Workforce Hub Charts](../workforce-hub/creating-charts.md)** - Detailed guide to creating DEI analytics
- **[Scenario Creation](../scenarios/creating-scenarios.md)** - Model diverse hiring and promotions
- **[Forecast View](../forecast/forecast-overview.md)** - Project diversity improvements over time
- **[Succession Planning](succession-planning.md)** - Ensure diverse leadership pipeline
- **[Compensation Planning](compensation-planning.md)** - Address pay equity gaps
- **[Fields and Attributes](../admin/fields-attributes.md)** - Configure DEI data fields (Admin)

## Visual Guide

> **[Screenshot placeholder: Workforce Hub showing diversity breakdown by department and job level with bar charts and pie charts]**

> **[Screenshot placeholder: Org chart using Spotlight to highlight underrepresented demographics across the organization]**

> **[Screenshot placeholder: Forecast view showing increasing diversity over time with quarterly projections]**

> **[Screenshot placeholder: Before/After comparison in Workforce Hub showing improved leadership representation after modeling diverse promotions]**

> **[Screenshot placeholder: Pay equity analysis table showing average salary by gender and job level for equity audit]**
