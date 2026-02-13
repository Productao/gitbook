---
icon: calculator
---

# Calculated Agentnoon Attributes

### Overview

Calculated fields in Agentnoon can be applied on top of an organizational chart to provide a dynamic, roll-up view of various metrics across different organizational units. These fields are designed to give you insights into costs, headcounts, reporting structures, and ratios that matter for effective organizational analysis and decision-making.

<figure><img src="../.gitbook/assets/Screenshot 2025-11-11 at 5.36.03 PM.png" alt=""><figcaption></figcaption></figure>

Calculated fields allow you to:

* **Aggregate Data:** Roll up information from individual positions to give an overall picture of a department or the entire organization.
* **Monitor Costs and Counts:** Track both individual contributor (IC) and manager-related costs and headcounts.
* **Analyze Reporting Structures:** Understand layers within the org chart and the span of control at various levels.

Below is a list of common calculated metrics along with a brief explanation of each.

### Common Calculated Metrics

| Metric                  | Definition                                                                                                                                                  | Usage / Note                                                                                                                                 |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| IC Cost                 | Total cost associated with all individual contributors (non-managerial staff) in an organization.                                                           | Useful for budgeting and comparing the investment in non-managerial personnel across departments.                                            |
| IC Count                | Total number of individual contributors in an organization.                                                                                                 | Helps in understanding the scale of the workforce excluding managerial roles.                                                                |
| Layers                  | The hierarchical level a position occupies within the organization (e.g., CEO is typically at Layer 1).                                                     | Provides clarity on the structure and depth of the org chart.                                                                                |
| Manager Cost            | Total cost associated with managerial positions.                                                                                                            | Used to assess the investment in leadership compared to the overall organization.                                                            |
| Manager Count           | The number of managers within an organization.                                                                                                              | Offers insights into the leadership density in different parts of the organization.                                                          |
| Manager Cost Ratio      | Proportion of the total organizational cost attributed to managers.                                                                                         | Helps identify how much of the org’s expenses are invested in management. The inverse (1 - Manager Cost Ratio) gives the IC cost proportion. |
| Manager to IC Ratio     | Ratio showing the number of managers per individual contributor (e.g., a 5:1 ratio means one manager for every five individual contributors).               | A key metric for assessing organizational efficiency and leadership distribution.                                                            |
| Rate Card               | Displays the attributes used to auto-populate salary details when a compensation or rate card is ingested.                                                  | Streamlines the process of applying standard salary metrics to positions, ensuring consistency across the organization.                      |
| Total Cost              | Sum of all costs (both individual contributors and managers) within a given part of the organization.                                                       | Provides a complete financial overview, aiding in comprehensive budgeting and financial planning.                                            |
| Total Count             | Overall headcount including both individual contributors and managers.                                                                                      | Useful for calculating per-employee metrics or evaluating the scale of a department.                                                         |
| Reporting Layers        | Number of layers below a specific person in the hierarchy (e.g., if the CEO is Layer 1 and there are 8 reporting layers, then the lowest layer is Layer 9). | Assists in understanding the depth of reporting and potential managerial span within the organization.                                       |
| Roll Up Span of Control | Average span of control per manager in a particular segment of the organization, including the leader’s span.                                               | A key indicator for assessing managerial effectiveness and the balance of organizational structure.                                          |
| Average Salary          | The average salary across all positions within the selected scope (includes both managers and individual contributors).                                     | Useful for benchmarking compensation trends and identifying outliers across teams or departments.                                            |
| Average Manager Salary  | The average salary of all managerial positions in the organization.                                                                                         | Helps evaluate leadership compensation and compare it against overall organizational costs.                                                  |
| Average IC Salary       | The average salary of all individual contributors (non-managerial staff).                                                                                   | Provides insight into compensation distribution for non-managerial roles, helping to assess pay equity and workforce cost structure.         |
| IC Cost Ratio           | The proportion of total workforce cost attributed to individual contributors.                                                                               | Useful for understanding how much of the organization’s investment goes into non-managerial roles relative to managers.                      |
| 1:1 Managers Ratio      | The proportion of managers who directly manage only one report.                                                                                             | Highlights potential inefficiencies or top-heavy structures, signaling where leadership layers may need to be reviewed.                      |

### How to Enable Calculated Fields

1. **Access the Org Chart:** Navigate to the section where your org chart is displayed and navigate to card content
2. **Select Metrics:** Choose the metrics you wish to display (e.g., IC Cost, Manager Count, etc.). Calculated metrics are marked with an <kbd>_fx_</kbd>
3. **Review Roll-Up Data:** Once enabled, the calculated fields will update the org chart with the aggregated values for the selected metrics.<br>

<figure><img src="../.gitbook/assets/Screenshot 2025-07-15 at 4.29.30 PM.png" alt="" width="375"><figcaption></figcaption></figure>

\
Agentnoon’s calculated fields offer a robust way to visualize and analyze organizational data directly on your org chart. Whether you need to manage budgets, assess team structure, or gain deeper insights into your organization’s makeup, these fields provide an essential toolset for modern organizational management.
