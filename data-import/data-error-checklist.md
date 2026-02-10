---
description: Common data errors to avoid when uploading data into Agentnoon
icon: list-check
---

# Data Error Checklist

### Overview

To ensure a smooth experience when uploading your CSV or Google Sheets files, follow this checklist. Completing each step will help prevent errors and ensure accurate data processing.

### Required Data Structure

* **Single Header Row**: Ensure all column headers are in the first row.
* **Unique Column Names**: No duplicate headers.
* **All Columns Have Headers**: No missing column names.
* **No Blank Columns**: Remove empty columns.
* **Date Format**: Use `YYYY-MM-DD` for consistency.
* **File Encoding**: Save the CSV in **UTF-8** encoding to avoid character issues.
* **Consistent Text Formatting**: Standardize capitalization and remove extra spaces.
* **No Special Characters**: Avoid symbols or emojis that may interfere with data processing.
* **Supported File Format**: Use **CSV (.csv)** or **Google Sheets format**.

### Mandatory Data Fields

* **Required Fields Completed**: Ensure all mandatory fields are filled.
* **Unique Employee IDs**: Each employee must have a distinct Employee ID.
* **Valid Manager IDs**: Manager IDs must correspond to existing Employee IDs.
* **No Self-Reporting**: An employee **cannot** be their own manager.
* **No Circular Reporting**: Ensure reporting structures do not loop back on themselves.
* **Manager Assignments**: All employees needing a manager must have one assigned.

### Data Validation

* **Field Dependencies**: Ensure fields like **cost center → department** follow required logic.
* **Data Type Consistency**:
  * Numeric fields contain only numbers.
  * Decimal values maintain a standard precision (e.g., two decimal places).
* **Currency Codes**:
  * Use standard three-letter currency codes (**USD, EUR, etc.**).
  * Ensure currency matches salary amounts consistently.
* **Consistent Department & Location Names**: Standardized naming for data integrity.
* **Data Completeness**: No empty mandatory fields (e.g., **Employee ID, Manager ID, Job Title**).
* **No Duplicate Records**: Remove any repeated employee entries.
* **Top-Level Managers**: If applicable, leave **Manager ID** blank or assign a valid value.
* **No Orphan Records**: Every **Manager ID** must correspond to an existing **Employee ID**.
* **Succession Plan Consistency:** Ensure successor fields are correctly mapped and valid employees are referenced.
* **Unauthorized Field Entries:** Monitor for unapproved additions to fields like Position Title, especially during scenario planning.
* **Circular Reporting:** Looks for reporting loops, like a manager reporting to someone who reports back to them directly or indirectly.

### Salary & Compensation

* **Salaries Are Valid**:
  * Salary values must be **positive numbers**.
  * Amounts must align with the assigned currency.
* **Salary Outliers:** Review compensation values for outliers compared to similar job families, grades, or levels.

### Date Validation

* **Correct Date Format**: Use `YYYY-MM-DD` format for all dates.
* **Logical Date Entries**: Ensure dates make sense (e.g., **Hire Date** is after **Birth Date**).

### Consistency & Clean Data Practices

* **Consistent Text Entries**: No typos or variations in naming conventions.
* **No Formulas in Cells**: Only raw data should be present, without embedded formulas or macros.
* **Proper Use of Special Characters**: Ensure correct handling of commas, quotes, or other characters in CSV files.

### Error Handling & Validation

Agentnoon automatically validates data upon upload. If errors are found:

* **Error Reports**: You can export a report of incorrect records for review.
* **Field Mapping Adjustments**: If there are mismatches, the system will prompt you to adjust mappings.

### Best Practices

* **Consistent Formatting**: Keep data structured correctly to avoid import errors.
* **Data Accuracy**: Review information for correctness before uploading.
* **Version Control**: Maintain copies of previous data files for tracking and rollback purposes.

By following this checklist, you ensure a seamless data upload process in Agentnoon.
