---
description: Agentnoon terminology and definitions
hidden: false
---

# Glossary

A comprehensive reference of Agentnoon terminology, workforce planning concepts, and common abbreviations.

---

## A

### Access Groups
Permissions configuration that controls which employees/positions a user can see based on field values (department, location, etc.). Admins create access groups to restrict data visibility.

**Example:** "Engineering Team" access group shows only Engineering department employees.

**Learn more:** [Access Groups](../access-control/access-groups.md)

### Admin
A user with elevated permissions to configure Agentnoon, manage users, upload data, and control system settings. Admins have access to Settings, Data Management, and user configuration features.

**Learn more:** [Admin Overview](../admin/overview.md)

### Aggregator
In Forecast, the field used to group rows (e.g., Department, Location, Employee Type). Determines how data is summarized in the forecast table.

**Example:** Aggregating by Department shows one row per department with total headcount/cost.

**Learn more:** [Forecast Overview](../forecast/overview.md)

### Approval Flow
Multi-stage review process where scenarios are submitted for approval by designated approvers (Level 0-3). Ensures workforce planning changes are reviewed before implementation.

**Learn more:** [Configuring Approval Flows](../admin/configuring-approval-flows.md)

### Approval History
Log of all approval/rejection actions on a scenario, including timestamps, approver names, and reasons for rejection.

### Attributes
See **Fields and Attributes**

### Auto Mapping
Automatically populates dependent fields when you select certain values. Example: select Pay Grade + Job Family → salary auto-populates from rate card.

**Learn more:** [Auto Mapping](../settings/automapping.md)

### Attrition
The rate at which employees leave the organization (voluntary or involuntary). Modeled in Agentnoon by closing positions or setting termination dates.

---

## B

### Before/After/Changes
Three scenario view modes: **Before** = Main Org baseline, **After** = scenario final state, **Changes** = delta.

**Learn more:** [Forecast Navigation](../forecast/navigation.md)

### Bench, The
Positions without a manager assigned. Used as a holding area during reorganizations or before final placement.

### Broken Hierarchy
Error state where a position's manager doesn't exist or reporting relationships form an invalid loop. Indicated by an orange link icon in the toolbar.

**Fix:** Assign valid managers or escalate broken positions to org roots.

### Budget (Scenario Budget)
Target savings or spending amount set when creating a scenario. The OpEx Panel tracks progress toward this budget.

**Learn more:** [Budget Planning & Tracking](../forecast/budget-planning-tracking.md)

### Bulk Operations
Actions performed on multiple positions simultaneously (e.g., bulk close, bulk edit). Available in Directory view by selecting multiple rows.

**Learn more:** [Bulk Operations](../scenarios/bulk-operations.md)

---

## C

### Card
Visual representation of a position in org chart view. Shows position details (title, name, salary, department, etc.) and employee details (if filled).

**Learn more:** [Key Concepts - Cards](../start-here/concepts.md)

### Card Content
Toolbar tool that lets you customize which fields appear on position cards. Control what information is visible in org chart view.

**Learn more:** [Main Org Toolbar](../main-org/toolbar.md)

### OpEx Panel
Panel showing all modifications in a scenario: additions (green), reductions (red), modifications (blue), with net cost and headcount impact.

**Also called:** OpEx Panel, Scenario Impacts and Changes

**Learn more:** [Scenario Tracking & Analysis](../scenarios/tracking-analysis.md)

### Compensation (Total Compensation)
Sum of all pay components (salary, bonus, stock, allowances). In Agentnoon, total compensation = base salary + any additional monetary fields configured.

### CSV (Comma-Separated Values)
File format used for data uploads. A spreadsheet exported as a .csv file with columns representing fields and rows representing positions/employees.

**Learn more:** [Data Requirements](../data-import/data-requirements.md)

---

## D

### Data Management
Admin-only feature for uploading CSV files, configuring live integrations, and managing data refresh. Accessible via Main Org toolbar → Data Management button.

**Learn more:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

### Data Refresh
Process of updating Main Org with latest employee/position data from your HRIS. Can be manual (CSV upload) or automated (live integration).

**Learn more:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

### DEI (Diversity, Equity & Inclusion)
Employee demographic fields used for analyzing workforce diversity (gender, ethnicity, disability status, etc.). Custom fields in Agentnoon.

### Department
Organizational unit grouping (e.g., Engineering, Sales, Marketing). Common aggregator for reporting and forecasting.

### Directory
Spreadsheet-style table view of positions/employees. Alternative to org chart view. Useful for filtering, sorting, and bulk operations.

**Learn more:** [Directory Overview](../directory/overview.md)

### Direct Reports
Positions reporting directly to a manager (not indirect reports). A manager with 5 direct reports has a SOC of 5.

---

## E

### Effective Date
Date when a change takes effect in Forecast projections. Used to phase organizational changes over time.

**Learn more:** [Time-Based Planning](../scenarios/time-based-planning.md)

### Employee
A person filling a position. Employee-specific details (name, hire date, performance rating) are tracked separately from position details (title, salary, department).

**Learn more:** [Position vs Headcount Management](../best-practices/position-vs-headcount.md)

### Employee Field
Field that describes the person in a position (e.g., employee name, hire date, performance rating), not the position itself. Appears in white section of position cards.

### Export
Download data from Agentnoon in various formats: CSV (for Excel), PowerPoint (for presentations), or Image (PNG/JPEG).

**Learn more:** [Forecast Reports & Exports](../forecast/reports-exports.md)

---

## F

### Field
Data attribute for positions or employees (e.g., Salary, Department, Title, Location). Fields can be standard (built-in) or custom (user-created).

**Learn more:** [Fields and Attributes Management](../settings/fields.md)

### Field Duplication
Setting that controls whether a field's value copies when duplicating a position in scenarios. Useful for copying position attributes but not employee-specific details.

**Learn more:** [Field Duplication](../settings/field-duplication.md)

### Filter
Toolbar tool to narrow down visible positions based on field values (e.g., show only Engineering dept, only San Francisco location).

**Logic:** AND between categories, OR within categories.

**Learn more:** [Main Org Toolbar](../main-org/toolbar.md)

### Forecast
Agentnoon module for viewing workforce data over time. Provides pivot table-style visualization of headcount and cost projections (monthly, quarterly, yearly).

**Key principle:** Forecast is view-only (visualization), not for making changes.

**Learn more:** [Forecast Overview](../forecast/overview.md)

### Formula
Calculated field based on other fields (e.g., Fully Loaded Cost = Salary + Benefits + Taxes).

**Learn more:** [Formulas](../data-import/formulas.md)

### FTE (Full-Time Equivalent)
Measure of employee workload. 1.0 FTE = full-time, 0.5 FTE = half-time. Used to calculate total workforce capacity.

### Full Org Scenario
Scenario that copies your entire Main Org. Use for company-wide planning (annual hiring plans, budget cuts, reorgs).

**Learn more:** [Creating Scenarios](../scenarios/creating-scenarios.md)

---

## H

### Headcount
Number of employees (people filling positions). Headcount ≠ position count: you may have 100 positions but only 85 filled (15 vacancies).

**Learn more:** [Position vs Headcount Management](../best-practices/position-vs-headcount.md)

### Highlight
Toolbar tool to color-code position cards by field values (e.g., highlight by Department → each dept gets a different color).

**Learn more:** [Main Org Toolbar](../main-org/toolbar.md)

### Hire Date
Date when a future position starts. Controls when the position appears in Forecast projections.

**Learn more:** [Building Headcount Forecasts](../forecast/building-headcount-forecasts.md)

### HRIS (Human Resources Information System)
Source system for employee data (Workday, BambooHR, ADP, etc.). Agentnoon imports data from your HRIS.

---

## I

### IC (Individual Contributor)
Employee without direct reports. Not a manager.

**Metric:** IC Count = total employees minus managers.

### Integration (Live Integration)
Automated connection between your HRIS and Agentnoon. Syncs data automatically on a schedule (hourly, daily, weekly).

**Types:** SFTP, Workday, REST API

**Learn more:** [Data Refresh & Sync](../admin/data-refresh-sync.md)

---

## L

### Layers
Number of management levels between CEO and frontline employees. More layers = taller org; fewer = flatter. Example: 5 layers = CEO → VP → Director → Manager → IC.

### Level 0/1/2/3 Approvers
Four-tier approval system:
- **Level 0:** Scenario-specific first approver
- **Level 1:** Global first approver (all scenarios)
- **Level 2:** Global second approver (all scenarios)
- **Level 3:** Scenario-specific final approver

**Learn more:** [Configuring Approval Flows](../admin/configuring-approval-flows.md)

### Live Integration
See **Integration**

### Lock Scenarios Upon Submission
Setting that prevents scenario editing after submission for approval. Ensures approvers review a stable version.

**Learn more:** [Configuring Approval Flows](../admin/configuring-approval-flows.md)

---

## M

### Main Org
Your current organizational structure. View-only—reflects real data from your HRIS. Cannot be edited directly (create scenarios to model changes).

**Learn more:** [Main Org Overview](../main-org/overview.md)

### Manager
Employee with one or more direct reports.

**Metric:** Manager Count = employees with at least 1 direct report.

### Mandatory Field
Field that must be filled when creating a new position. Configured by admins in field settings.

### Metrics
System-calculated values displayed throughout Agentnoon (SOC, manager count, IC count, total cost, etc.).

**Learn more:** [Org Metrics & Insights](../main-org/metrics-insights.md)

### Monetary Field
Pay component field (Salary, Bonus, Stock, Allowances). Can be displayed as separate columns in Forecast.

---

## N

### New Org Scenario
Scenario starting from scratch (no positions copied from Main Org). Use for modeling brand-new teams or business units.

**Learn more:** [Creating Scenarios](../scenarios/creating-scenarios.md)

---

## O

### Open Position
Position without an assigned employee (vacancy). Contributes to position count but not headcount.

**Also called:** Vacant position

### OpEx Panel
Side panel showing scenario budget, cost/headcount impact, and list of changes. Used to submit scenarios for approval.

**Full name:** Operating Expense Panel, also called "Scenario Impacts and Changes"

**Learn more:** [Budget Planning & Tracking](../forecast/budget-planning-tracking.md)

### Org Chart
Visual hierarchy view of your organization showing reporting relationships. Default view in Agentnoon.

**Learn more:** [Main Org Overview](../main-org/overview.md)

---

## P

### Partial Data Upload
CSV upload that updates specific fields without replacing all data. Must include Employee ID to match records.

**Learn more:** [Partial Data Upload](../data-import/partial-data-upload.md)

### Partial Org Scenario
Scenario that copies only a specific part of Main Org (e.g., just Engineering dept). Use for department-specific planning.

**Learn more:** [Creating Scenarios](../scenarios/creating-scenarios.md)

### Pay Grade
Compensation level or band (e.g., Grade 10, Grade 11). Often used with rate cards to auto-populate salaries.

### Position
A role with defined structure and budget (title, department, salary, manager). Position = the role; Employee = the person filling it.

**Learn more:** [Position vs Headcount Management](../best-practices/position-vs-headcount.md)

### Position Field
Field that describes the position itself (e.g., Title, Salary, Department), not the employee. Appears in colored section of position cards.

---

## R

### Rate Card
Compensation reference table that auto-populates salaries for new positions based on criteria (pay grade, job family, location).

**Learn more:** [Rate Cards / Compensation Bands](../settings/compensation-cards.md)

### Reporting Relationship
Defines who reports to whom, creating the hierarchy in org charts.

### RIF (Reduction in Force)
Layoffs or workforce reduction. In Agentnoon, modeled by closing positions in scenarios.

### Row Aggregator
See **Aggregator**

---

## S

### Salary
Base annual compensation. Primary field for workforce cost calculations. Does not include bonuses, stock, or other pay components (unless configured as additional monetary fields).

### Scenario
Sandbox workspace for modeling organizational changes. Scenarios don't affect Main Org—they're for testing "what-if" alternatives.

**Types:** Full Org, Partial Org, New Org

**Learn more:** [Scenarios Overview](../scenarios/overview.md)

### Scenario Refresh
Feature (in development) to update a scenario with recent Main Org changes. Preserves scenario modifications while incorporating new data.

**Learn more:** [Scenario Refresh](../scenarios/refresh.md)

### SFTP (Secure File Transfer Protocol)
Method for live data integration. Your HRIS exports CSV files to SFTP server, Agentnoon pulls them automatically.

**Learn more:** [Importing Data via SFTP](../live-data-integration/available-data-integration-methods/importing-data-via-sftp.md)

### Show Before/After/Changes
See **Before/After/Changes**

### SOC (Span of Control)
Number of direct reports a manager has. Healthy range: 5–10 (context-dependent).

**Learn more:** [Key Concepts - Span of Control](../start-here/concepts.md)

### Spotlight
Toolbar tool for conditional formatting. Highlights positions matching specific rules (e.g., SOC > 10, salary > $200K).

**Learn more:** [Main Org Toolbar](../main-org/toolbar.md)

### SSO (Single Sign-On)
Authentication method using company identity provider (Okta, Azure AD, Google). Users log in with company credentials.

**Learn more:** [Single Sign-On (SSO)](../authentication-and-identity-security/single-sign-on-sso/README.md)

---

## T

### Toolbar
Left sidebar with tools for navigating and analyzing org data (Search, Filter, Highlight, Card Content, Views, Export, etc.).

**Learn more:** [Main Org Toolbar](../main-org/toolbar.md)

### Termination Date
Date when an employee leaves or position is closed. Controls when the position disappears from Forecast projections.

### Time Period
In Forecast, the column granularity: Monthly, Quarterly, or Yearly. Determines how cost/headcount data is displayed over time.

**Learn more:** [Forecast Navigation](../forecast/navigation.md)

---

## V

### Vacant Position
See **Open Position**

### View
Saved configuration of filters, highlights, and card content for quick reloading.

**Learn more:** [Main Org Toolbar](../main-org/toolbar.md)

---

## W

### Workforce Hub
Analytics module with pre-built charts and visualizations (headcount by department, cost distribution, SOC analysis, etc.).

**Learn more:** [Chart Navigation](../hub/chart-navigation.md)

### Workforce Planning
Strategic process of designing organizational structure, planning hiring, and forecasting workforce costs. Agentnoon's primary use case.

**Workforce Planning vs. Talent Management:** Planning focuses on positions and structure; talent management focuses on individual employees and performance.

---

## Common Abbreviations

- **CSV** - Comma-Separated Values (file format)
- **DEI** - Diversity, Equity & Inclusion
- **FTE** - Full-Time Equivalent
- **HRIS** - Human Resources Information System
- **IC** - Individual Contributor
- **MFA** - Multi-Factor Authentication
- **OpEx** - Operating Expense
- **RIF** - Reduction in Force
- **SFTP** - Secure File Transfer Protocol
- **SOC** - Span of Control
- **SSO** - Single Sign-On

---

## Industry Workforce Planning Terms

### Budget Variance
Difference between planned (forecasted) workforce cost and actual workforce cost.

### Burden Rate
Multiplier applied to salary to account for benefits, taxes, and overhead (e.g., 1.3x burden rate means total cost = salary × 1.3).

### Compression
Situation where pay gaps between levels are too small (e.g., ICs making more than their managers). Indicates compensation structure issues.

### FP&A (Financial Planning & Analysis)
Finance function responsible for budgeting, forecasting, and financial modeling. Often collaborates with HR on workforce planning.

### Fully Loaded Cost
Total cost of an employee including salary, benefits, taxes, overhead, and other expenses. May be 1.3-1.5x base salary.

### Org Design (Organizational Design)
Process of structuring an organization to align with business strategy. Includes defining teams, reporting relationships, and layers.

### Strategic Workforce Planning
Long-term planning (3-5 years) of workforce needs aligned with business strategy. Focuses on what roles are needed, when, and at what cost.

### Talent Management
Operational management of individual employees (recruiting, performance, development, retention). Complements strategic workforce planning.

---
