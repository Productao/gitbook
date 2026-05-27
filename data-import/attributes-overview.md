---
description: Understanding attribute types and how to manage them
icon: input-text
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/FQHYLeH687WAkUobefnf/data-import/attributes-overview
---

# Attributes Overview

### Overview

This guide explains what attributes are in Agentnoon, the different types, and how to edit and manage them. Attributes help structure and analyze organizational data within the platform.

### Types of Attributes

#### 1. Imported Attributes

* These are data fields uploaded into Agentnoon (e.g., **Name, Job Title, Location**).
* Once imported, attributes can be:
  * Used for **filtering** and **displaying** on the org chart.
  * **Analyzed** in workforce hub and reporting.
  * **Grouped** for segmentation and insights.

#### 2. Calculated Attributes

* These are system-generated attributes based on existing data.
* Examples include:
  * **Layers** (depth in the hierarchy).
  * **Spans of Control** (number of direct reports).
  * **Rollups** (aggregated metrics for teams).
* These are useful for **org design analysis** and **structural insights**.

<figure><img src="../.gitbook/assets/image (77).png" alt=""><figcaption></figcaption></figure>

#### 3. State Attributes

* These are fields that must be filled when changing the state of an employee within a scenario - such as adding a new hire, closing a position, or assigning a backfill.
* For example, When a user clicks the **+ Add Role** to add a new hire, they’ll be prompted to fill out required fields such as:
  * Role
  * Office Location
  * Start Date
* State attributes help standardize planning workflows by prompting users to enter essential information during structural changes.

<figure><img src="../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

### Editing and Managing Global Attributes

#### 1. Adding New Attributes

You can create new attributes from **Data Management > Attributes & Formulas**

#### 2. Steps to Add or Edit Attributes

1. Navigate to **Data Management → Attributes & Formulas**.
2. Click **Add New Attribute** to create a new field.
3. Modify an existing attribute:
   * Rename it for clarity.
   * Adjust its type (**text, number, monetary, date, array etc.**).
4. Save changes to apply them across the org chart or scenario.

### Multiple Values (Array Fields)

You can store multiple values in a single field (for example, Skills, Certifications, or Clients) and use them in filters across the product.

#### How it works

When a field is set to Array type, values separated by commas are treated as individual items.

Example:

Analytics, AI, Account Management

Will be treated as:

* Analytics
* AI
* Account Management

These values will appear separately in filters instead of one combined string.

#### Setup

1. Import your field like a normal custom field
   * Example: Skills = Analytics, QA, Management
2. Go to Settings → Fields (Attributes & Formulas)
3. Edit the field
4. Change type from Text → Array
5. Save

#### Using Array Fields in Filters

* Each value appears as a separate, unique option
* Selecting a value returns all records that contain that value<br>

For multiple selections:

* Any of → matches at least one value
* All of → matches all selected values

#### Where this applies

Array fields work in:

* Filters (Org Chart, Workforce Hub, etc.)
* Highlighting and analytics
* Any place where filters are supported

#### Notes

* Values must be separated by commas
* Each value appears only once in filters (no duplicates)
* In card content and exports, values remain comma-separated

<figure><img src="../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>
