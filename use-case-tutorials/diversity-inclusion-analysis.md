---
description: Analyzing diversity metrics and planning inclusive workforce changes
icon: people-carry-box
---

# Diversity & Inclusion Analysis

Analyze DEI metrics in Agentnoon and model workforce changes that improve representation and equity.

## Prerequisites

**IMPORTANT:** DEI analysis requires demographic data fields (Gender, Ethnicity, etc.) in your employee data. Without this data, you cannot perform DEI analysis in Agentnoon.

**Setup (Admin):**

1. Add DEI columns to your HRIS export CSV (e.g., Gender, Ethnicity, Race, Disability Status)
2. Upload data via **Data Management > Import Data**
3. Go to **Data Management > Fields and Attributes** to configure field visibility
4. Restrict DEI field access to authorized personnel only

> **Privacy:** Obtain consent before collecting demographic data. Comply with applicable laws (GDPR, EEOC, PIPEDA). Never report on groups smaller than 5 people.

## Analyze Current State

**In Workforce Hub:**

1. Go to Main Org > switch view to **Workforce Hub**
2. Select a preconfigured chart from the dropdown (e.g., **Headcount Distribution Chart**)
3. Use the axis dropdowns to configure:
   * X-axis: Department, Job Level, or Location
   * Y-axis: Select your DEI field (Gender, Ethnicity, etc.)
   * Values: Headcount or Percentage
4. Apply filters for focused analysis (e.g., Job Level = Manager+ to see leadership pipeline)

**With Spotlight:**

1. Go to Main Org > **Spotlight** > Fields tab
2. Select a DEI field and value (e.g., Gender = Woman)
3. Matching positions highlight across the org chart

**Export for deeper analysis:** Workforce Hub > Export > CSV for year-over-year comparisons or statistical analysis in Excel.

## Common Gaps to Identify

* Low representation at higher job levels (leadership pipeline)
* Drop-off points where underrepresented groups decrease
* Departmental segregation (technical roles underrepresenting certain groups)
* Pay disparities for comparable roles across demographic groups

## Model DEI Improvements

**Create a DEI scenario:**

1. Click **+ Create Scenario**, name it (e.g., "2026 Diverse Hiring Plan")

**Add diverse hires:**

* Add Position > set DEI fields on the new position (e.g., Gender = Woman) > set a future hire date

**Model promotions:**

* Edit existing employee position > change Job Level and Salary > set Effective Date

**Track impact:** Open **Workforce Hub** within the scenario to see before/after representation changes.

## Project Changes Over Time

In your DEI scenario, switch to **Forecast** view:

1. Set Aggregator to your DEI field (Gender, Ethnicity)
2. Choose Quarterly or Yearly view
3. Apply filters (e.g., Job Level = Manager+) for leadership-specific projections

This shows when you'll reach representation targets.

## Pay Equity Analysis

1. In Workforce Hub, create a Table chart: Rows = Gender/Ethnicity, Columns = Job Level, Values = Average Salary
2. Identify roles with significant salary differences by demographic group
3. In a scenario, adjust salaries for underpaid employees and set effective dates
4. Review total cost in the **OpEx Panel** to budget for equity adjustments

## Save Views for Recurring Reporting

1. Configure DEI charts and filters in Workforce Hub
2. Click **Views > Save Current View**
3. Name it (e.g., "Monthly DEI Dashboard") to reload quickly for consistent reporting

**Export for presentations:** Export > PowerPoint (org chart with DEI highlights) or CSV (detailed compliance data).

## Related Resources

* [Workforce Hub Charts](../workforce-hub/creating-charts.md)
* [Scenario Creation](../scenarios/creating-scenarios.md)
* [Forecast View](../forecast/forecast-overview.md)
* [Fields and Attributes](../admin/fields-attributes.md)
