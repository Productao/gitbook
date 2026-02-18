---
description: Understanding Span of Control metrics and their calculations in Agentnoon
---

# Span of Control Metrics

### Summary of all Span of Control related metrics

There are 4 SOC-related metrics available to use in Agentnoon's orgchart. You can find them in the **Orgchart > Card Content**.

<div align="left"><figure><img src="../.gitbook/assets/Screenshot 2025-12-15 at 5.44.30 PM.png" alt="" width="375"><figcaption></figcaption></figure></div>

The following table provides a detailed breakdown of each Span of Control (SoC) metric, including its legacy name, calculation method, and practical use cases.

<table><thead><tr><th width="220.8046875">SoC metric</th><th width="135.51953125">Legacy name</th><th width="165.734375">How its calculated</th><th>Why you would want to use this metric</th></tr></thead><tbody><tr><td><p>Direct Span of Control</p><p><em>i.e. The number of employees who report directly to a manager.</em></p></td><td>Direct Span of Control</td><td>Number of direct reports</td><td>To determine a manager’s <strong>immediate supervisory burden</strong>, and day-to-day people-management capacity. </td></tr><tr><td><p>Average Direct Manager Span of Control</p><p><em>i.e. Average of the direct SOC values for the managers who report to the focal manager.</em></p></td><td>Average (Immediate) SOC</td><td>(Sum of direct SOC values of direct-report managers) ÷ (Number of those managers)</td><td>To determine the average load of a leader’s <strong>direct reports who are managers</strong>.</td></tr><tr><td><p>Average Hierarchical Span of Control</p><p><em>i.e. Average of the direct SOC values for all managers in the focal manager’s hierarchy (all levels below, not including the focal manager).</em></p></td><td>Average (Total) SOC</td><td>(Sum of direct SOC values of all managers in hierarchy including focal) ÷ (Number of those managers)</td><td>To determine the <strong>overall  managerial load under an individual leader.</strong></td></tr><tr><td><p><strong>(NEW)</strong> Average Managerial Span of Control</p><p><em>i.e. Average of the direct SOC values for all managers in the hierarchy, including the focal manager.</em></p></td><td>None</td><td>(Sum of direct SOC values of all managers in hierarchy including focal) ÷ (Number of managers <strong>including</strong> <strong>focal</strong>)</td><td>To determine the <strong>average number of direct reports across all managers in a hierarchy</strong> (including the owner of the hierarchy).</td></tr></tbody></table>

#### Example: Calculating All SOC Metrics

Here is a complete example calculating all the metrics for one focal manager:

<figure><img src="../.gitbook/assets/Screenshot 2025-12-18 at 3.59.06 PM.png" alt=""><figcaption></figcaption></figure>
