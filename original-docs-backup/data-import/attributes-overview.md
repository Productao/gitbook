---
description: Understanding attribute types and how to manage them
icon: database
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

<div align="left"><figure><img src="../.gitbook/assets/Screenshot 2025-03-06 at 9.30.44 AM.png" alt="" width="375"><figcaption></figcaption></figure></div>

#### 3. State Attributes

* These are fields that must be filled when changing the state of an employee within a scenario - such as adding a new hire, marking an exit, or assigning a backfill.
* For example, When a user clicks the **+ Add Role** to add a new hire, they’ll be prompted to fill out required fields such as:
  * Role
  * Office Location
  * Start Date
*   State attributes help standardize planning workflows by prompting users to enter essential information during structural changes.<br>

    <figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

### Editing and Managing Global Attributes

#### 1. Adding New Attributes

You can create new attributes in two places:

1. **Main Org Chart** (for all users).
2. **Scenario-Specific** (for temporary analysis in a scenario).

#### 2. Steps to Add or Edit Attributes

1. Navigate to **Data Management → Attributes & Formulas**.
2. Click **Add New Attribute** to create a new field.
3. Modify an existing attribute:
   * Rename it for clarity.
   * Adjust its type (**text, number, monetary, date, etc.**).
4. Save changes to apply them across the org chart or scenario.

<figure><img src="../.gitbook/assets/Screenshot 2025-03-06 at 9.31.12 AM.png" alt=""><figcaption></figcaption></figure>

### Scenario-Specific Attributes

* Attributes can be **scenario-specific**, meaning they only apply within that particular scenario.
* This is useful for **temporary categorization** or **testing new data fields** without affecting the global dataset.

<figure><img src="../.gitbook/assets/Screenshot 2025-03-06 at 9.31.36 AM.png" alt=""><figcaption></figcaption></figure>

By understanding and managing attributes effectively, you can **customize data views, improve reporting accuracy, and enhance workforce planning** in Agentnoon.
