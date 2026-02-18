---
description: >-
  Auto-mapping automatically maps attributes using configurable rules to ensure
  consistency and reduce manual work.
---

# Automapping

### Setting Up Auto-Mapping

Auto-mapping rules are configured within **Settings**.

<figure><img src="../.gitbook/assets/image (44).png" alt="" width="563"><figcaption></figcaption></figure>

To create an auto-mapping rule:

1. Navigate to **Settings**.
2. Create a new rule and provide a name and description.

<p align="center"> <img src="../.gitbook/assets/Screenshot 2026-01-30 at 11.48.11 AM.png" alt=""></p>

3. Upload a CSV file containing the mapping logic.
4. Click on Create Rule.

Once the file is uploaded, the system guides you through configuring how the mapping should be applied.

<figure><img src="../.gitbook/assets/Screenshot 2026-01-30 at 12.01.03 PM.png" alt="" width="563"><figcaption></figcaption></figure>

### Configuring the Mapping Logic

After uploading the CSV:

1. Select the column(s) that will act as the **independant attribute(s)** (e.g. National Department).
2. The remaining columns will be treated as **dependant attributes** (e.g. Location and International Department), that are automatically populated when a source value is selected or updated.

<figure><img src="../.gitbook/assets/Screenshot 2026-01-30 at 12.04.56 PM.png" alt="" width="563"><figcaption></figcaption></figure>

#### Example

If a source value is selected (e.g., a locally defined attribute), one or more standardized values are automatically populated based on the configured mapping.

Once confirmed, the auto-mapping rule becomes active and is applied consistently across the organization.

### Modifying Existing Records

When an existing record is updated:

* Changing the source attribute automatically updates the mapped target attributes according to the rule.

This is particularly helpful when regional or team-specific terminology differs from standardized or global definitions.

### Creating New Records

When creating a new record:

1. Define the record and its position within the structure.
2. Assign a source attribute (e.g.: National Department)

<figure><img src="../.gitbook/assets/Screenshot 2026-01-30 at 12.10.41 PM.png" alt="" width="210"><figcaption></figcaption></figure>

3. The relevant target attributes are automatically populated based on the active auto-mapping rule.

This ensures new data aligns with organizational standards from the outset, without requiring additional manual steps.
