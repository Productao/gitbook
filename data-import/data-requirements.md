---
description: Basic data field requirements to get started
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/FQHYLeH687WAkUobefnf/data-import/data-requirements
---

# Data Requirements

### Overview

This guide explains the essential fields required to set up data in Agentnoon, along with additional custom fields for advanced functionality.

### Three Required Fields

1. **Position ID**: A unique identifier for each position (can be a number or letter, as long as it's unique).
2. **Manager’s Position ID**: Defines reporting relationships by linking a position to its manager.
   * Example: If Ali's Position ID is `1` and Shayan's Position ID is `2`, and Shayan reports to Ali, then Shayan’s **Manager’s Position ID** is `1`.
3. **Job Title**: The title assigned to each position (e.g., CEO, Head of Product) to display on the org chart.

**Example Data Template:** [https://docs.google.com/spreadsheets/d/1CYUSEkljMDEMadGuJU50PnKyBhuaQe0rfh-PxWhhnMc/edit?gid=0#gid=0](https://docs.google.com/spreadsheets/d/1CYUSEkljMDEMadGuJU50PnKyBhuaQe0rfh-PxWhhnMc/edit?gid=0#gid=0)

### Custom Fields

* You can import unlimited custom fields, such as:
  * **Department**
  * **Name**
  * **Location**
  * **Employment Status**
  * **Start Dates and End Dates** (useful for tracking hires and planned terminations)

### Employee vs. Position Fields

* For advanced functionality (e.g., talent selection, reassigning employees between positions), you need to distinguish between:
  * **Position Fields** (attributes tied to a role, not a specific person)
  * **Employee Fields** (attributes tied to an individual, such as personal details)
* This distinction is managed in the **data import mechanism**, covered in a separate guide.

By setting up these fields correctly, you ensure accurate org visualization and enable more advanced workforce planning capabilities.
