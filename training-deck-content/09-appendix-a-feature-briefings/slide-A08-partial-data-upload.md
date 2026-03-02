# Slide A8 — Partial Data Upload

## Title
Partial Data Upload

## Lead-line
Update specific records without replacing the entire dataset — surgical updates for targeted changes.

## What Is It?
Partial Data Upload lets you update specific positions or employees in Main Org or a scenario by uploading a CSV with only the records and fields you want to change. Unlike a full data upload (which replaces everything), partial upload adds or updates individual records.

## How to Set It Up
Prepare a CSV file with:
- A **unique identifier** column: Employee ID or Position ID (must match existing records)
- A **Manager ID** column (required only for new positions — needed to place them in the hierarchy)
- Only the **fields you want to update** — you don't need to include every column

## How to Use It
1. Go to **Data Management** → **Partial Upload**
2. Choose the file type and upload your CSV
3. **Map fields:** The system auto-detects columns. Select the unique identifier. Adjust any field mappings as needed.
4. Click **Upload** → the system matches records by identifier
5. **Results:** Existing records update with the new values. New records (with IDs not found in the system) are added. Changed cards are marked with an **orange edit icon** for easy identification.

## Common Use Cases
- Updating salary data for a specific group after a compensation review
- Adding acquired company data into a scenario for M&A planning
- Correcting specific data fields without doing a full re-import
- Adding new positions to Main Org that came through outside of the normal HRIS sync

## Screenshot / Visual
The Partial Upload mapping dialog showing field matching between the CSV columns and Agentnoon fields.

## Speaker Notes
Partial upload is a targeted tool — use it when you need to update 10 records, not 10,000. For large-scale data refreshes, use the full data upload or an automated integration. The unique identifier is critical: the system uses Employee ID or Position ID to find existing records and update them. If an ID doesn't match, it's treated as a new record and added. Always double-check your CSV before uploading to avoid creating duplicate positions.
