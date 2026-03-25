---
description: Add enrichment data on top of your automated integration
icon: laptop-binary
---

# Data Transformation Hub

The Data Transformation Hub lets admins add additional data on top of an existing automated integration.

This is useful when your main HRIS or automated source does not include all the data you want to analyze in Agentnoon. For example, you may want to enrich your workforce data with:

* Performance data
* Planning data
* Custom attributes
* Data exported from another system

This feature was introduced as part of the Data Transformation API and subsequent improvements to the enrichment workflow. Recent releases also added clearer enrich-and-import flows and support for enrichment data in import pipelines.

### What this Feature Does

Data Transformation Hub allows you to:

* Upload a CSV enrichment file
* Join it to your existing automated integration
* Add new columns to your Agentnoon dataset
* Keep those columns in sync going forward

Once configured, the enrichment step runs alongside your automated data flow, so you do not need to manually rebuild the full process every time.

### When to Use Enrichment Data <a href="#wopj02q3c8i6" id="wopj02q3c8i6"></a>

Use enrichment data when:

* Your automated integration is missing fields you need
* You want to combine HRIS data with another flat file
* You want to add custom attributes that do not exist in your main source
* You want to enrich workforce data using a shared unique identifier such as:
  * Employee ID
  * Position ID
  * Email
  * Another stable unique key

Example:\
&#x20;Your HRIS integration brings in core employee data, but you also want to add:

* New Performance
* New Data
* New Attribute

You can upload those extra columns in an enrichment file and merge them into your main dataset using Employee ID.

### Before You Start <a href="#lxb6okjbf75j" id="lxb6okjbf75j"></a>

Make sure you have:

* An automated integration already set up
* A CSV file containing the additional data
* A join column that exists in both datasets

Your enrichment file should include:

* One column that matches a unique field in your main data
* One or more new columns you want to add

Example:

<table data-header-hidden><thead><tr><th valign="top"></th><th valign="top"></th><th valign="top"></th><th valign="top"></th></tr></thead><tbody><tr><td valign="top">Employee ID</td><td valign="top">New Performance</td><td valign="top">New Data</td><td valign="top">New Attribute</td></tr><tr><td valign="top">1001</td><td valign="top">High Performer</td><td valign="top">A</td><td valign="top">Internal</td></tr><tr><td valign="top">1002</td><td valign="top">Solid Performer</td><td valign="top">B</td><td valign="top">External</td></tr></tbody></table>

### How to Add Enrichment Data <a href="#o5dbo4s4a887" id="o5dbo4s4a887"></a>

#### Step 1: Open Data Transformation Hub <a href="#gso6zhsq8r65" id="gso6zhsq8r65"></a>

1. Go to the Home page
2. Open Settings
3. Go to Data Management
4. Open Data Transformation Hub
5. Click Open Hub

#### Step 2: Start a New Enrichment Upload <a href="#xmcsdc5uf8hx" id="xmcsdc5uf8hx"></a>

1. Click Add or Update Enrichment Data
2. Upload your enrichment file
3. Make sure the file is in CSV format (UTF-8 Encoding)

#### Step 3: Choose the Merge Type <a href="#o9x6wpf52qds" id="o9x6wpf52qds"></a>

You will see merge options for how the enrichment file should be combined with your main data.

**Left Join to Main Data**

Recommended in most cases.

This keeps:

* All rows from your main dataset
* Matching rows from your enrichment file

Use this when you want to preserve your full organization while adding extra fields where matches exist.

**Enriching / common records only**

This only keeps records that exist in both datasets.

Use this only if you are sure your enrichment file contains the full population you want to work with. In most cases, Left Join to Main Data is the safer option.

#### Step 4: Select the join columns <a href="#lo1irk2a8zow" id="lo1irk2a8zow"></a>

Choose:

* The Main Data Join Column
* The Enrichment Join Column

These columns should contain the same identifier.

Examples:

* Employee ID ↔ Employee ID
* Position ID ↔ Position ID
* Email ↔ Email

Agentnoon will use these fields to match rows between your main data and your enrichment file.

#### Step 5: Review the Transformation <a href="#id-5hdxyfthlktq" id="id-5hdxyfthlktq"></a>

After mapping the join columns, click Next.

You’ll see a preview of:

* Your main dataset
* The enrichment file
* The new columns that will be added

Review the output carefully before processing.

#### Step 6: Process the Data <a href="#rw81tmbrl4ms" id="rw81tmbrl4ms"></a>

Click Process Data.

After processing:

* Download the processed file
* This file now includes your original data plus the new enrichment columns

#### Step 7: Upload the Processed Dataset Once <a href="#fysqcico550" id="fysqcico550"></a>

To make the new columns available in Agentnoon:

1. Go to Upload Entire Data Set
2. Choose the CSV upload option
3. Upload the processed file you just downloaded

On the mapping screen:

* Your previous mappings should remain saved
* Select the new fields you are bringing in
* Finish the upload

You only need to do this initial mapping once for new columns.

### What Happens After Setup <a href="#t0ib9mve4r39" id="t0ib9mve4r39"></a>

Once the enrichment file is configured and the new columns are mapped:

* The new fields become available in Agentnoon
* You can access them in places like card content and analysis views
* Your automated integration remains intact
* On future syncs, the enrichment logic continues to run automatically

This means you do not need to rebuild your setup every time your automated integration refreshes.

### Updating an existing enrichment file <a href="#hdkqbgjhky9o" id="hdkqbgjhky9o"></a>

If you want to update the values in your enrichment file later:

1. Return to Data Transformation Hub
2. Open Add or Update Enrichment Data
3. Upload the updated CSV
4. Process it again

If the column structure is unchanged:

* You usually do not need to remap the fields again
* The existing mapped fields will continue to work

If you add brand new columns:

* You will need to upload the processed dataset once again
* Then map the new fields in the CSV upload flow

### Best Practices <a href="#id-82ig3xa9g0e" id="id-82ig3xa9g0e"></a>

#### Use a Stable Join Key <a href="#jpn6bw4kud8" id="jpn6bw4kud8"></a>

Use a field that does not change often, such as:

* Employee ID
* Position ID

Avoid joining on fields like name where duplicates or formatting differences may exist.

#### Prefer Left Join to Main Data <a href="#iu91o6j0yrac" id="iu91o6j0yrac"></a>

This keeps your full org intact and prevents accidental loss of unmatched rows.

#### Keep enrichment files clean <a href="#id-5vqhakg4ansi" id="id-5vqhakg4ansi"></a>

Before upload:

* Remove duplicates
* Confirm identifiers match formatting in your main data
* ,ake sure CSV headers are final

#### Add only Useful Fields <a href="#id-8zk3jwhs6ajc" id="id-8zk3jwhs6ajc"></a>

Only bring in columns you plan to use in Agentnoon. This keeps your setup clean and easier to manage.

### Limitations <a href="#oge1xesw9zau" id="oge1xesw9zau"></a>

* Enrichment files must be uploaded in CSV format
* You need a matching join column in both datasets
* New columns must be mapped once before they become available in the product
* If your enrichment file does not contain all rows from your main data, using the wrong merge type can lead to incomplete output

### Common workflow example <a href="#lwcjiflmikh5" id="lwcjiflmikh5"></a>

#### Add Performance Data to an Automated Integration <a href="#id-6qg166v8zeoj" id="id-6qg166v8zeoj"></a>

1. Your HRIS integration already brings in workforce data
2. You export a flat file containing:
   1. Employee ID
   2. Performance
   3. Potential
3. You upload that flat file into Data Transformation Hub
4. You join on Employee ID
5. You process and upload the enriched dataset once
6. Performance and Potential now become available in Agentnoon
7. Future syncs continue using the same enrichment logic

### Troubleshooting <a href="#cffce2tafz9j" id="cffce2tafz9j"></a>

#### My new fields are not visible in Agentnoon <a href="#id-34mjfrw9rjo0" id="id-34mjfrw9rjo0"></a>

Check that:

* The processed dataset was uploaded
* The new columns were selected during CSV mapping
* The join column matched correctly

#### My data looks incomplete after processing <a href="#id-9z64t3jxnuju" id="id-9z64t3jxnuju"></a>

Check whether you selected:

* Left Join to Main Data instead of a common-records-only enrichment mode

#### My enrichment file updated, but values did not change <a href="#jsm812yfnsw2" id="jsm812yfnsw2"></a>

Re-upload the updated file through Data Transformation Hub and process it again.
