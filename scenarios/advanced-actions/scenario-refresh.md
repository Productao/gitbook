---
description: Update an existing scenario with the latest Main Org data
icon: arrows-rotate
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
---

# Scenario Refresh

Scenario Refresh lets you update an older scenario with the latest data from your **Main Org** (or the latest synced HRIS data that is now reflected in Main Org).

This is useful when you created a scenario some time ago, but your Main Org has since changed and you want to bring those updates into the scenario without starting over.

With Scenario Refresh, you can control:

* **which position /** **people** get refreshed
* **which fields** get refreshed
* whether to **keep scenario values** or **overwrite with Main Org**
* whether to include **new joiners** that are now part of the scenario scope

Agentnoon also creates a **backup scenario automatically** before refresh is applied, so you can go back if needed.

## When to use Scenario Refresh

Use Scenario Refresh when:

* your scenario was created weeks or months ago
* Main Org has newer data than your scenario
* new fields have been added to Main Org
* new employees have joined and should be pulled into the scenario
* you want to update selected fields without recreating the scenario

Examples:

* new people joined the team after the scenario was created
* department, role, or manager data changed in Main Org
* new custom fields were added and now need to appear in the scenario
* you want the scenario to reflect the latest HRIS sync before continuing planning

### How to refresh a scenario

#### Step 1: Open the scenario

Go to the scenario you want to refresh.

#### Step 2: Open Data Management

From the left toolbar, click **Data Management**.

#### Step 3: Click Refresh Scenario

Select **Refresh Scenario**.

You’ll now see:

* **Main Org** on the left
* **Your scenario** on the right

This view helps you compare your current scenario against the latest main data.

<figure><img src="../../.gitbook/assets/Screenshot 2026-03-26 at 4.06.25 PM.png" alt=""><figcaption></figcaption></figure>

### Step 1 of refresh: Select people

In the first step, choose which people should be refreshed.

You can:

* select all people already in the scenario
* include newly joined people from Main Org
* search by:
  * name
  * role
  * department
* apply filters to narrow the list

This is especially useful if only part of the org has changed and you do not want to refresh the full scenario.

<figure><img src="../../.gitbook/assets/Screenshot 2026-03-26 at 4.07.38 PM.png" alt=""><figcaption></figcaption></figure>

### Step 2 of refresh: Select fields

Next, choose which fields should be refreshed.

You can:

* select specific fields only
* use **Select All** to refresh every available field

This includes:

* existing fields already present in the scenario
* **new fields that now exist in Main Org** but were not present when the scenario was created

Example:\
If Main Org now contains a field such as **Performance Review** or **New Attribute**, those fields will appear in the field list during refresh and can be added into the scenario.

<figure><img src="../../.gitbook/assets/Screenshot 2026-03-26 at 4.08.22 PM.png" alt=""><figcaption></figcaption></figure>

### Step 3 of refresh: Review conflicts and summary

Before confirming, Agentnoon shows a summary of what will change.

This includes:

* **Total headcount before vs. after**
* **Total compensation before vs. after**
* **Number of fields refreshed**
* **People with manager changes**
* **a preview of which fields and values are changing**

This is the review step where you can decide how to handle conflicts.

<figure><img src="../../.gitbook/assets/Screenshot 2026-03-26 at 4.08.58 PM.png" alt=""><figcaption></figcaption></figure>

### Keep Scenario Values vs. Overwrite with Main Org

For each field, you can choose:

#### Keep Scenario Values

Use this when you want to preserve edits already made inside the scenario.

#### Overwrite with Main Org

Use this when you want the scenario to take the latest value from Main Org.

Example:\
If your scenario already contains a custom value for `New Attribute`, but Main Org now has a newer value, you can decide whether to:

* keep the scenario’s version, or
* replace it with the latest Main Org value

<figure><img src="../../.gitbook/assets/Screenshot 2026-03-26 at 4.11.37 PM.png" alt=""><figcaption></figcaption></figure>

### Step 4: Confirm and Refresh

When you’re ready:

1. Click **Next**
2. Review the final summary
3. Click **Confirm and Refresh**

Before refresh is applied, Agentnoon automatically creates a **backup scenario** of your original version.

This gives you a recovery point in case you want to undo the refresh later.

<figure><img src="../../.gitbook/assets/Screenshot 2026-03-26 at 4.12.06 PM.png" alt=""><figcaption></figcaption></figure>

### What happens after refresh

Once refresh is complete:

* your scenario is updated with the selected Main Org data
* newly selected people are added into the scenario
* newly selected fields become available in the scenario
* the refreshed values are visible across the scenario views

You may also see a scenario status tag such as **Refreshed by…** for newly added people.

## Full Org vs. Partial Org scenarios

Scenario Refresh behaves slightly differently depending on how the scenario was created.

### Refreshing a Full Org scenario

In a Full Org scenario:

* you can refresh all current people in the scenario
* you can also bring in new joiners from Main Org
* you can select any relevant fields to refresh

This is the most flexible version of Scenario Refresh because the scenario already represents the full workforce scope.

### Refreshing a Partial Org scenario

In a Partial Org scenario, refresh is limited to the **original scenario scope**.

For example:

* if the scenario was created only for the **IT department**
* Scenario Refresh will only show:
  * people already in the IT scenario
  * new people who joined the IT department
* it will **not** show people from Engineering, Sales, or other departments outside the original scenario scope

This is intentional and keeps the partial scenario aligned to its original filter boundaries.

### Important limitation for Partial Org scenarios

If you want to bring in people from outside the original scenario scope, Scenario Refresh is **not** the right feature.

Best practice:

1. Create another scenario for that additional group
2. Use **Scenario Merging** to combine them

Example:\
If your current scenario is for IT only, and you now want to include new Engineering employees, create an Engineering scenario separately and merge it with the IT scenario.

### Common workflow example

#### Refresh an old scenario with new fields and new joiners

1. Open the old scenario
2. Go to **Data Management → Refresh Scenario**
3. Select all current people in the scenario
4. Select any new joiners from Main Org
5. Choose the fields to refresh
6. Review the summary
7. Decide which fields should:
   * keep scenario values, or
   * overwrite with Main Org
8. Confirm the refresh
9. Continue planning using the updated scenario

### Best practices

#### Refresh before major planning work

If your scenario is old, refresh it before making large changes so you are planning on the latest data.

#### Refresh only the fields you need

If you want to preserve certain scenario edits, avoid selecting fields unnecessarily.

#### Use conflict handling carefully

Only overwrite with Main Org when you are sure the latest source data should replace scenario edits.

#### Review new fields before confirming

If Main Org now includes new attributes, decide whether they should be added into the scenario during this refresh.

#### Use partial scenarios carefully

Remember that partial org refresh only pulls changes within the scenario’s original filter scope.

#### Rely on the backup

If you are unsure, proceed with refresh knowing a backup scenario is created automatically.

### Limitations

* Scenario Refresh only updates the scenario based on the latest **Main Org** data
* Partial org scenarios only refresh within their original scope
* If you want to include people outside that scope, create another scenario and merge it
* Refresh does not replace the need for Scenario Merging when combining broader workforce segments

## Related Articles

* [Scenario Approvals](../approvals.md)
* [Scenario Merging](../merging.md)
