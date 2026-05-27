---
description: Understanding data structure and custom fields
icon: objects-align-left
---

# Fields and Attributes

In Agentnoon, fields and attributes mean the same thing. They are the data points that define your organization, such as Job Title, Department, Salary, Location, Start Date, and Skills. This section explains the minimum data needed to build your org, the main attribute types used in Agentnoon, how custom fields are imported, and how fields behave across cards, filters, formulas, Workforce Hub, Forecast, and exports.

Fields appear on cards, in the directory, in analytics charts, in filters, and in exports.

### Attribute Types

All extra attributes are imported through Custom Fields. After uploading your data, go to Attributes & Formulas and assign the right type to each field.

#### **Text**

Use Text for labels and categories. Examples: Job Title, Department, Location, Business Unit.&#x20;

Import the column as a custom field and keep the type as Text.

#### **Number**

Use Number for non-currency values. Examples: Performance Score, FTE, Open Roles, Span Target.&#x20;

Import the column as a custom field, set the type to Number, and use it in formulas like FTE + Open Roles or Performance Score \* 10.

#### **Monetary**

Use Monetary for money fields. Examples: Salary, Bonus, Benefits, Allowance, Total Compensation. Import the column as a custom field, set the type to Monetary, and use it in formulas like Salary + Bonus.&#x20;

Monetary fields can also be used in Forecast and in the Stacked Headcount Cost chart in Workforce Hub.

#### **Array**

Use Array when one field contains multiple values. Examples: Skills = Analytics, QA, Design; Certifications = CPA, CFA; Tools = Excel, SQL, Tableau.&#x20;

Import the column as a custom field with comma-separated values, then change the type from Text to Array so filters split the values into separate unique options.

#### **Date**

Use Date for time-based fields. Examples: Start Date, End Date, Hire Date, Termination Date. Import the column as a custom field, set the type to Date, and Agentnoon will treat it as a range filter instead of a normal dropdown.

### **Position Fields vs People Fields**

Position fields are tied to roles and persist even when vacant. Example position fields include: Job Title, Department, Pay Grade, Location, Reports To.

People fields are tied to individuals and removed when someone leaves. Example people fields include: Employee Name, Employee ID, Start Date, Email, Performance Rating.

This separation lets you plan with positions independently of the people who fill them.

Note that while Salary may be a position-level field in some contexts, Agentnoon treats the mapped Salary field as a People field by default. Attaching or detaching people from positions will result in their salary coming along.

### Groups

Fields are organized into groups such as Compensation, Contact Info, and Job Details. Groups appear as sections in the edit panel when you click on a position, making it easier to find related fields. Admins can create and manage groups in Settings > Fields.

### Calculated Fields (FX)

Some fields are computed automatically by Agentnoon and marked with FX:

* Span of Control — Number of direct reports
* Total Organization Size — Everyone under a manager (direct + indirect)
* Layer — Distance from the CEO
* Average SOC — Average span across the organization

These update in real time as the org structure changes.

### Where Fields Appear

* Cards — Configure which fields display via Card Content in the toolbar
* Directory — Add, remove, and reorder columns
* Workforce Hub — Fields power the axes and breakdowns of charts
* Filters — Filter by any field value across the product
* Highlighting — Color-code cards by any field
* Exports — Include any field in CSV, Excel, or PowerPoint exports

### Admin Configuration

Admins can add custom fields, set data types such as text, number, date, monetary, or array, define restricted dropdown values for consistency, and control field visibility by access group. See [Fields and Attributes Management](../settings/overview.md).

#### Minimum Required Data (Data Upload)

Fields required for data upload

**Absolute minimum:**

* Position ID or Employee ID
* Manager Position ID or Manager Employee ID
* Position Name

**Recommended for greater functionality:**

* Job Title, Department, Manager, Location, Name, Employee ID, Start Date, Total Compensation.

<figure><img src="../.gitbook/assets/Screenshot 2026-02-27 at 1.55.20 AM.png" alt=""><figcaption></figcaption></figure>
