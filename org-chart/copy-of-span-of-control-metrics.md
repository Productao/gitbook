---
description: Understanding Span of Control metrics and their calculations in Agentnoon
hidden: true
---

# Copy of Span of Control Metrics

### Summary of all Span of Control related metrics

There are 4 SOC-related metrics available to use in Agentnoon's orgchart. You can find them in the **Orgchart > Card Content**.

<div align="left"><figure><img src="../.gitbook/assets/Screenshot 2025-12-15 at 5.44.30 PM.png" alt="" width="375"><figcaption></figcaption></figure></div>

<figure><img src="../.gitbook/assets/Screenshot 2025-12-15 at 5.59.51 PM.png" alt=""><figcaption></figcaption></figure>

### **1.** Direct Span of Control

The number of employees who report directly to a manager.

#### Calculation:

`Number of direct reports`

#### Why would you want to use this metric:

To determine a manager’s immediate supervisory burden, and day-to-day people-management capacity.

### **2.** Average Direct Manager Span of Control

Average of the direct SOC values for the managers who report to the focal manager.

#### Calculation:

`(Sum of direct SOC values of direct-report managers) ÷ (Number of those managers)`

#### Why would you want to use this metric:

To determine the average load of a leader’s direct reports who are managers.

### **3.** Average Hierarchical Span of Control

Average of the direct SOC values for all managers in the focal manager’s hierarchy (all levels below, not including the focal manager).

#### Calculation:

`(Sum of direct SOC values of all managers in hierarchy including focal) ÷ (Number of those managers)`

#### Why would you want to use this metric:

To determine the overall managerial load under an individual leader.

### **4.** Average Managerial Span of Control

Average of the direct SOC values for all managers in the hierarchy, including the focal manager.

#### Calculation:

`(Sum of direct SOC values of all managers in hierarchy including focal) ÷ (Number of managers including focal)`&#x20;

#### Why would you want to use this metric:

To determine the average number of direct reports across all managers in a hierarchy (including the owner of the hierarchy).

### Example: Calculating All SOC Metrics

Here is a complete example calculating all the metrics for one focal manager:

<figure><img src="../.gitbook/assets/Screenshot 2025-12-18 at 3.59.06 PM.png" alt=""><figcaption></figcaption></figure>
