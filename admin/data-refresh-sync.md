---
description: Keeping Agentnoon synchronized with your HRIS data
icon: refresh
hidden: false
---

# Data Refresh & Sync

Keeping your Agentnoon data current is critical for accurate workforce planning. This guide covers how to refresh your Main Org data—either manually via CSV upload or automatically through live data integrations.

## What is a Data Refresh?

A **data refresh** updates your Main Org with the latest employee and position data from your source system (HRIS, payroll system, or other HR database).

**When you refresh data:**
- Main Org is updated with current organizational structure
- New employees appear
- Terminated employees are removed or marked as inactive
- Changes to salaries, titles, departments, and other fields are reflected
- Scenarios are NOT automatically updated (see Scenario Refresh section below)

**Two types of data refresh:**
1. **Manual refresh:** Upload a new CSV file to replace or update Main Org data
2. **Automated sync:** Live integration pulls data from your HRIS on a schedule

---

## Manual Data Refresh via CSV Upload

Manual CSV uploads give you full control over when and what data is updated.

### When to Use Manual Refresh
- You don't have a live data integration set up
- You want to perform one-time updates
- You're making corrections to data before uploading
- You're testing new fields or data structures
- Your HRIS doesn't support live integrations

### Full Data Upload

A **full data upload** replaces all data in your Main Org.

**Step 1: Prepare Your CSV File**
1. Export latest employee/position data from your HRIS
2. Ensure CSV matches Agentnoon's expected format
3. Verify all required fields are present (Employee ID, Name, Manager, Department, etc.)
4. Check for data quality issues (missing values, formatting errors)

**Step 2: Upload to Agentnoon**
1. Go to **Main Org**
2. Open the **taskbar** (left side)
3. Click **Data Management**
4. Select **"Upload Full Data"** or **"Bulk Data Import"**
5. Choose your CSV file
6. Map columns to Agentnoon fields (if first-time upload)
7. Review validation results
8. Confirm upload

**Step 3: Verify Data**
1. After upload completes, navigate through Main Org
2. Check that new employees appear
3. Verify terminated employees are no longer visible (or marked as terminated)
4. Spot-check salary changes, title updates, and department moves
5. Review org chart structure for accuracy

**Important:** Full data uploads replace your entire Main Org. Any data NOT in the CSV will be removed.

### Partial Data Upload

A **partial data upload** updates specific fields without replacing all data.

**When to use:**
- Update salaries for annual raises
- Change departments for a subset of employees
- Add new custom field values
- Correct errors in specific fields

**Step 1: Prepare Your Partial CSV**
1. Include only the fields you want to update
2. **Always include Employee ID** (required to match records)
3. Include only the rows for employees you're updating

**Example partial CSV:**
```
Employee ID, Salary, Title
12345, 150000, Senior Engineer
67890, 120000, Product Manager
```

**Step 2: Upload**
1. Go to Main Org → Data Management
2. Select **"Partial Data Upload"**
3. Choose your CSV file
4. Map columns to fields
5. Agentnoon updates only those fields for those employees

**Important:** Partial uploads do NOT remove data. They only add or modify existing records.

---

## Automated Data Sync (Live Integrations)

Live data integrations automatically sync your HRIS data to Agentnoon on a schedule.

### Available Integration Methods

**1. SFTP Integration**
- Agentnoon connects to your SFTP server
- Your HRIS exports CSV files to the SFTP location
- Agentnoon pulls the latest CSV at scheduled intervals
- **Best for:** Organizations with existing data pipelines

**2. Workday Integration**
- Direct API connection to Workday
- Pulls employee data automatically
- **Best for:** Workday customers

**3. REST API Integration**
- Push data to Agentnoon via REST API
- Your systems send data to Agentnoon endpoints
- **Best for:** Custom integrations and data transformation pipelines

**See also:** [Live Data Integration Overview](../live-data-integration/what-is-a-live-data-integration.md)

### Setting Up a Live Integration

**Admins only:**
1. Go to **Settings**
2. Navigate to **Data Management** or **API Keys and Documentation**
3. Select your integration method (SFTP, Workday, REST API)
4. Follow setup wizard:
   - Provide connection details (SFTP credentials, API keys, etc.)
   - Map fields from your HRIS to Agentnoon fields
   - Set sync frequency (hourly, daily, weekly)
   - Test connection
5. Save configuration
6. Monitor first sync to ensure data flows correctly

**Typical sync frequencies:**
- **Hourly:** Real-time workforce data (rare, usually unnecessary)
- **Daily:** Common for fast-moving organizations with frequent changes
- **Weekly:** Standard for most organizations
- **Monthly:** Budget-constrained or stable workforces

**Recommendation:** Weekly sync on Monday mornings ensures data is fresh for planning activities.

### Monitoring Live Sync Status

**Check sync health:**
1. Go to **Settings → Data Management**
2. View **Integration Status** or **Sync Logs**
3. Check last sync time and status (success/failure)
4. Review error logs if sync failed

**Healthy sync indicators:**
- Last sync completed within expected timeframe
- No error messages
- Record count matches expected size from HRIS
- Spot-check: Recent hires appear, recent terminations removed

**Unhealthy sync indicators:**
- Sync failed or hasn't run in several days
- Error logs show connection issues, authentication failures, or data validation errors
- Record count is significantly different from HRIS
- Known recent changes (new hire, termination) not reflected in Main Org

---

## What Happens During a Data Refresh

### The Refresh Process

**When data is refreshed (manual or automated):**
1. **Validation:** Agentnoon validates incoming data for required fields, data types, format errors
2. **Error check:** Any validation errors are flagged (see Data Error Checklist)
3. **Matching:** Agentnoon matches incoming records to existing records using Employee ID
4. **Updates:** Changed fields are updated (salary, title, department, etc.)
5. **Additions:** New employees appear in Main Org
6. **Removals:** Employees no longer in the data are removed (or marked inactive, depending on configuration)
7. **Recalculation:** Metrics (SOC, cost, IC count, etc.) are recalculated
8. **Org chart rebuild:** Reporting relationships and hierarchy are reconstructed

**Time to complete:** Usually 5-15 minutes for organizations with <5,000 employees. Larger organizations may take longer.

### Impact on Users

**During a refresh:**
- Users may see a "Data refresh in progress" banner
- Org chart and directory views may be temporarily unavailable
- Scenarios remain accessible (they're not affected by Main Org refreshes)

**After a refresh:**
- Users see updated Main Org data immediately
- Filters, views, and highlights re-apply to new data
- Custom fields and formulas recalculate

---

## Scenario Refresh: Updating Scenarios with New Main Org Data

**Key principle:** When Main Org data is refreshed, scenarios are NOT automatically updated.

### Why Scenarios Don't Auto-Update
Scenarios are snapshots of your org at the time they were created. If Main Org changes (new hire, termination, salary change), scenarios remain unchanged by default.

**This preserves:**
- Your planned changes (you don't want new hires auto-added to your RIF scenario)
- Historical accuracy (you can compare scenario to Main Org at that point in time)
- Approval integrity (approved scenarios shouldn't change unexpectedly)

### When You Need Scenario Refresh
**Scenario refresh** updates a scenario to include recent Main Org changes.

**Use scenario refresh when:**
- You created a scenario 2 months ago, and you want to incorporate recent hires before submitting for approval
- A major organizational change happened (acquisition, divestiture), and you need to update your long-term planning scenario
- You want to rebase your scenario on the current Main Org state

**How to refresh a scenario:**
1. Open the scenario you want to refresh
2. Go to **Data Management** (in scenario taskbar)
3. Click **"Refresh Scenario"** or **"Sync with Main Org"**
4. Agentnoon shows a preview of what will change:
   - New employees from Main Org that aren't in the scenario
   - Employees in the scenario who no longer exist in Main Org
   - Field changes (salary updates, title changes, etc.)
5. Review changes carefully
6. Confirm refresh

**After refresh:**
- Scenario now includes latest Main Org data
- **Your scenario changes are preserved** (additions, closures, moves you made)
- New baseline = current Main Org + your scenario modifications

**Warning:** Scenario refresh can be complex if many changes occurred. Review carefully to avoid losing your work.

**Current status:** Scenario refresh is still in development. Check with Agentnoon support for availability.

---

## Handling Data Conflicts and Errors

### Common Data Validation Errors

When uploading data, you may encounter validation errors:

**Missing Required Fields:**
- **Error:** "Employee ID missing for row 47"
- **Fix:** Ensure every row has an Employee ID

**Invalid Data Types:**
- **Error:** "Salary must be numeric, found 'N/A' for Employee 12345"
- **Fix:** Replace non-numeric values with valid numbers or leave blank

**Broken Reporting Relationships:**
- **Error:** "Manager ID 99999 not found in dataset"
- **Fix:** Ensure manager exists in the CSV or correct the Manager ID

**Duplicate Employee IDs:**
- **Error:** "Employee ID 12345 appears twice"
- **Fix:** Deduplicate your data before uploading

**See also:** [Data Error Checklist](../data-import/data-error-checklist.md) for comprehensive troubleshooting.

### Resolving Sync Failures

**If an automated sync fails:**

**Step 1: Check error logs**
1. Go to Settings → Data Management → Sync Logs
2. Identify error message

**Step 2: Common fixes**
- **Authentication failure:** Re-enter API credentials or SFTP password
- **Connection timeout:** Check firewall rules, verify SFTP server is accessible
- **Data validation error:** Fix source data in your HRIS, wait for next sync
- **Field mapping issue:** Update field mappings in integration settings

**Step 3: Test connection**
1. Use "Test Connection" button in integration settings
2. Verify connection succeeds
3. Manually trigger a sync to confirm resolution

**Step 4: Contact support if needed**
If errors persist, contact Agentnoon support with:
- Error logs
- Sync timestamp
- Recent changes to HRIS configuration

---

## Best Practices for Data Refresh

### Timing Your Refreshes

**Manual CSV uploads:**
- **Weekly:** Monday mornings (fresh data for the week)
- **Bi-weekly:** After payroll runs (incorporates recent hires, terminations)
- **Monthly:** After month-end close (for stable workforces)
- **Ad-hoc:** Before major planning sessions, board meetings, budget reviews

**Automated sync schedules:**
- **Daily sync:** Run overnight (2am-4am) to avoid disrupting users
- **Weekly sync:** Sunday nights or Monday mornings
- **Post-payroll sync:** Schedule sync for 24 hours after payroll close

### Pre-Refresh Checklist

Before uploading data:
- ✅ Verify data is latest export from HRIS
- ✅ Check for data quality issues (missing values, formatting errors)
- ✅ Ensure all required fields are present
- ✅ Test with a small sample first (if unsure)
- ✅ Notify users if refresh will disrupt work (large organizations)

### Post-Refresh Checklist

After uploading data:
- ✅ Verify upload completed successfully
- ✅ Spot-check recent hires appear
- ✅ Verify recent terminations are removed
- ✅ Review org chart for unexpected changes
- ✅ Check key metrics (total headcount, total cost, SOC) for reasonableness
- ✅ Test key filters and views to ensure they still work

### Data Governance

**Protect sensitive data:**
- Only admins should have data upload permissions
- Use secure SFTP connections (not unencrypted FTP)
- Rotate API keys regularly
- Monitor sync logs for unauthorized access attempts

**Maintain data accuracy:**
- Single source of truth: HRIS → Agentnoon (not manual edits in Agentnoon)
- Regularly audit Main Org vs. HRIS for discrepancies
- Document field mappings for consistency
- Train admins on proper CSV formatting

---

## Troubleshooting Common Sync Issues

**"Data hasn't synced in 3 days"**
- Check if integration is still configured (Settings → Data Management)
- Review sync logs for error messages
- Test connection to HRIS or SFTP server
- Verify HRIS export is running on schedule

**"New hire from yesterday isn't showing in Agentnoon"**
- Check if HRIS has exported the new hire yet
- Verify sync has run since the hire was added
- Check if new hire passed data validation (no missing required fields)
- If using manual upload, ensure you've uploaded the latest CSV

**"Terminated employee still appears in Agentnoon"**
- Verify termination was processed in HRIS
- Check if HRIS export includes terminated employees or filters them out
- If filtered out, wait for next sync (employee will disappear)
- If still in export, check if there's a "Status" or "Active" field that needs updating

**"Org chart is broken after data refresh"**
- Likely caused by invalid manager IDs or broken reporting relationships
- Go to Main Org → Taskbar → Data Management (admin only)
- Look for "Broken Hierarchy" indicator (orange link icon)
- Click to view positions with invalid managers
- Fix in HRIS, re-upload, or manually correct in Agentnoon

**"Sync is taking hours to complete"**
- Normal for very large organizations (>10,000 employees)
- If unusually slow, contact Agentnoon support
- Consider reducing sync frequency to minimize disruption

---

## Next Steps

- **[Data Import Requirements](../data-import/data-requirements.md)** - CSV formatting and required fields
- **[Data Error Checklist](../data-import/data-error-checklist.md)** - Troubleshoot validation errors
- **[Live Data Integration Overview](../live-data-integration/what-is-a-live-data-integration.md)** - Set up automated sync
- **[Admin Overview](overview.md)** - Full admin responsibilities
- **[Partial Data Upload](../data-import/partial-data-upload.md)** - Update specific fields only
