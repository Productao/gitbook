---
description: >-
  Partial uploads and scenario refreshes in Agentnoon let you update specific
  data without impacting the rest of your org or scenario structure
---

# Understanding Partial Uploads and Scenario Refreshes

### 1. What Happens During a Partial Upload?

#### **i. Existing Data** Preservation

When you perform a partial upload, you are **only updating the records included in your file**. All other employee data remains unchanged.

**Example:**

* You have 1,000 employees in your org.
* You upload a file with 50 employees to update their departments.
* **Result:** Only those 50 employees are updated. The remaining 950 keep all their existing details, including salary, title, manager, etc.

#### **ii. Smarter Manager Resolution**

Agentnoon intelligently updates reporting lines, even if the manager isn’t included in your upload.

**Example:**

* Sarah manages John, Lisa, Mike, Emma, and Tom.
* You upload a file that includes only John and Lisa. You change John’s manager to David.
* **Result:** Sarah’s team is automatically updated. She will now be shown as managing Lisa, Mike, Emma, and Tom (John is removed from her team).

### 2. What About Scenario-Specific Behavior?

#### i. Scenario Handling

Scenarios allow for flexible modeling of roles, even if the employee ID is the same.

**Example:**

* In the main org: Employee ID `EMP001` refers to one person only.
* In a scenario: `EMP001` could represent “John as a Manager” and “John as an Individual Contributor.”
* **Result:** When you update `EMP001` in a scenario, both roles are updated accordingly. In contrast, the main org would only allow one record per ID.

### Summary of Best Practices

* Use partial uploads when you want to make small, quick changes to specific records.
* Avoid relying on partial uploads to maintain data across full refresh cycles.
* Always ensure your custom field values are included in any full org data source if you want them preserved.
* Leverage scenario flexibility for experimenting with multiple role views using the same employee IDs.
