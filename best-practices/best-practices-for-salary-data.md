---
description: To ensure accurate compensation modeling, analytics, and reporting
---

# 💰 Best Practices for Salary Data

#### 1. Upload Each Component Separately

Break down salary data into its individual components:

* <mark style="color:green;">Base Salary</mark>
* <mark style="color:green;">Bonus</mark>
* <mark style="color:green;">Benefits</mark>
* <mark style="color:green;">Allowances</mark>
* <mark style="color:green;">Other Compensation</mark>

This allows Agentnoon to calculate total compensation and run cost modeling with flexibility.

#### 2. Use Consistent Field Naming

Ensure the field names used in the imported salary files exactly match the naming in your:

* Rate Cards

_Example:_ If your salary upload uses <mark style="color:green;">Base\_Salary</mark>, your rate card should not use <mark style="color:green;">BasePay</mark>—they must be the same.

#### 3. Support for Multiple Currencies

If your data spans multiple currencies:

* Include a <mark style="color:green;">Currency</mark> column (e.g., USD, EUR, NGN)
* Include a <mark style="color:green;">Salary\_Amount\_Local</mark> field

_(Optional)_ Add a <mark style="color:green;">Salary\_Amount\_USD</mark> field if conversion is pre-applied\
Agentnoon supports in-platform currency conversion, but clarity at upload helps validate totals.

#### 4. Normalize Units Across Fields

Ensure all monetary values are uploaded in the same unit (e.g., annual, monthly).\
Use a <mark style="color:green;">Frequency</mark> field to denote if values are:

* Annual
* Monthly
* Hourly

This enables fair comparisons and accurate forecasting.

#### 5. Avoid Free Text in Numeric Fields

Do not enter salary data as text with symbols (e.g., "$50,000").\
Use numeric values only (e.g., <mark style="color:green;">50000</mark>) with separate fields for currency or frequency.

#### 6. Validate Totals Before Upload

Sum each salary record to ensure:\
<mark style="color:green;">Total Compensation = Base + Bonus + Benefits + Allowances + Other</mark>\
This prevents mismatches in dashboards or when filtering for salary bands.

#### 7. Secure Sensitive Information

Ensure salary files are access-controlled and uploaded by authorized users only.
