---
description: Understanding data structure and custom fields
---

# Fields and Attributes

Fields are the data points that define your organization in Agentnoon — things like Job Title, Department, Salary, and Location. They appear on cards, in the directory, in analytics charts, and in exports.

## Minimum Required Data

**Absolute minimum:**

* Position ID or Employee ID
* Manager Position ID or Manager Employee ID
* Position Name

**Recommended for greater functionality:**

* Job Title, Department, Manager, Location, Name, Employee ID, Start Date, Email

## Position Fields vs People Fields

> **\[Screenshot placeholder: Fields settings showing position fields and people fields grouped separately]**

**Position fields** are tied to roles and persist even when vacant: Example position fields include:

* Job Title, Department, Pay Grade, Location, Reports To

**People fields** are tied to individuals and removed when someone leaves. Example people fields include:

* Employee Name, Employee ID, Start Date, Email, Performance Rating

This separation lets you plan with positions independently of the people who fill them.

Note, that while Salary may be a position level field in some contexts, Agentnoon treats the mapped Salary field as a People field by default. **Attaching or detaching people from positions will result in their salary coming along.**

## Groups

Fields are organized into **groups** (e.g., Compensation, Contact Info, Job Details). Groups appear as sections in the edit panel when you click on a position, making it easier to find related fields. Admins can create and manage groups in Settings > Fields.&#x20;

## Calculated Fields (FX)

Some fields are computed automatically by Agentnoon and marked with **FX**:

* **Span of Control** — Number of direct reports
* **Total Organization Size** — Everyone under a manager (direct + indirect)
* **Layer** — Distance from the CEO
* **Average SOC** — Average span across the organization

These update in real time as the org structure changes.

## Where Fields Appear

* **Cards** — Configure which fields display via **Card Content** in the toolbar
* **Directory** — Add, remove, and reorder columns
* **Workforce Hub** — Fields power the axes and breakdowns of every chart
* **Filters** — Filter by any field value across the application
* **Highlighting** — Color-code cards by any field
* **Exports** — Include any field in CSV, Excel, or PowerPoint exports

## Admin Configuration

Admins can add custom fields, set data types (text, number, date, dropdown), define restricted dropdown values for data consistency, and control field visibility by access group. See [Fields and Attributes Management](../settings/overview.md).
