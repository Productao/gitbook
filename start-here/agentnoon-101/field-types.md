---
description: Understanding the types of fields you can bring into Agentnoon
icon: objects-align-left
---

# Field Types

### Attribute Types in Agentnoon

Attributes are the fields that define your organization in Agentnoon - things like Job Title, Department, Salary, Start Date, Location, and Skills. These fields can appear on cards, in filters, in Workforce Hub, and in Forecast depending on the type you assign to them.

All extra attributes are brought into Agentnoon through the custom fields section during import. This includes text, number, monetary, array, and date fields.

### How to import attributes

When uploading data, map your required core fields first, such as Position ID, Manager ID, Position Name, and Salary if needed. Any additional columns should be imported as custom fields.

Examples:

* Department → custom field
* Performance Score → custom field
* Bonus → custom field
* Skills → custom field
* Start Date → custom field

After import, go to Attributes & Formulas and assign the correct type to each field.

### Text

Use Text for general labels or categories.

Examples:

* Department
* Location
* Business Unit
* Employment Type

Example import:

* Column: Department
* Sample values: Finance, Marketing, Operations
* Type: Text

Text fields are mainly used for display, grouping, filtering, and chart breakdowns.

### Number

Use Number for numeric values that are not currency.

Examples:

* Performance Score
* FTE
* Open Roles
* Tenure in Years
* Span Target

Example import:

* Column: Performance Score
* Sample values: 3.5, 4.2, 5
* Type: Number

Number fields can be used inside formulas.

Examples:

* Performance Score \* 10
* FTE + Open Roles
* ifElse(Performance Score >= 4, 1, 0)

Use Number when the value is numeric and should be used in calculations, but is not a money field.

### Monetary

Use Monetary for financial values.

Examples:

* Salary
* Bonus
* Allowance
* Benefits
* Total Compensation

Example import:

* Column: Bonus
* Sample values: 5000, 12000, 25000
* Type: Monetary

Monetary fields can also be used inside formulas.

Examples:

* Salary + Bonus
* Salary \* 0.1
* Salary + Bonus + Benefits

Monetary fields can also be used inside Forecast. This is useful when customers want to track cost over time using more than one pay component.

Examples in Forecast:

* Salary only
* Salary + Bonus
* Salary + Allowance + Benefits

Use Monetary when the field represents money and should behave like a financial field in the product.

### Array

Use Array when one field contains multiple values.

Examples:

* Skills → Analytics, QA, Design
* Certifications → CPA, CFA
* Tools → Excel, SQL, Tableau
* Languages → English, Arabic, French

Example import:

* Column: Skills
* Sample value: Analytics, QA, Design
* Import as custom field first
* Then go to Attributes & Formulas
* Change type from Text to Array

Once a field is set to Array, Agentnoon splits the comma-separated values into individual items inside filters.

Example:

Analytics, QA, Design

Appears in filters as:

* Analytics
* QA
* Design

This makes it possible to filter by one or more values inside the same field.

### Date

Use Date for any field that stores a date.

Examples:

* Birth Date
* Promotion Date

Example import:

* Column: Promotion Date
* Sample values: 2024-01-15, 2023-09-01
* Type: Date

Date fields behave differently in filters. Instead of showing fixed dropdown values, Agentnoon converts them into a range filter.

Example:

* Promotion Date from January 1, 2024 to December 31, 2024
* Termination Date before March 31, 2025

Use Date when users need to filter by time periods instead of exact text values.

### Summary

* Text = labels and categories
* Number = numeric values for calculations
* Monetary = money values used in formulas and Forecast
* Array = multiple comma-separated values in one field
* Date = date values that become range filters

Choosing the right attribute type helps Agentnoon handle the field correctly across cards, filters, formulas, Hub, and Forecast.

<figure><img src="../../.gitbook/assets/Screenshot 2026-04-14 at 2.50.47 PM.png" alt=""><figcaption></figcaption></figure>
