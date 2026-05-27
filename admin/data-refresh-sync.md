---
description: Keeping Agentnoon synchronized with your HRIS data
icon: rotate-exclamation
---

# Data Refresh & Sync

Keep your Main Org current by uploading fresh data manually or setting up automated sync with your HRIS.

## Manual CSV Refresh

**Full data upload** — Replaces all Main Org data. Use when you want a clean refresh from your HRIS.

1. Export latest data from HRIS
2. Main Org > Toolbar > **Data Management** > **Upload Full Data**
3. Choose CSV, map fields (first upload only), review validation, confirm
4. Spot-check: new hires appear, recent terminations removed, org chart intact

**Note:** Any record NOT in the CSV is removed from Main Org.

## Automated Sync (Live Integrations)

Three integration methods are available (Admin > Settings > Data Management):

* **SFTP** — Agentnoon connects to your SFTP server and pulls CSV files on a schedule
* **Workday** — Direct API integration for Workday customers
* **REST API** — Your systems push data to Agentnoon endpoints

**Recommended sync frequency:** Weekly (Sunday night or Monday morning). Daily is available for fast-moving organizations.

**Monitoring:** Settings > Data Management > Integration Status shows last sync time, success/failure status, and error logs.

**Healthy indicators:** Completed within expected timeframe; no errors; record count matches HRIS; recent hires and terminations reflected.

## What Happens During Refresh

1. Validation (required fields, data types, format)
2. Matching to existing records by Employee ID
3. Updates (changed fields), additions (new employees), removals (departed employees)
4. Org chart hierarchy reconstruction and metric recalculation

**Duration:** 5–15 minutes for <5,000 employees; larger orgs take longer.

**During refresh:** Users may see a "Data refresh in progress" banner; org chart may be temporarily unavailable. Scenarios remain accessible.

## Scenario Refresh

Main Org refreshes do NOT automatically update scenarios. Scenarios are snapshots that preserve your planned changes.

**When to refresh a scenario:** Your scenario is months old and you want to incorporate recent Main Org changes before submitting for approval.

1. Open the scenario > Data Management > **Refresh Scenario**
2. Review what will change (new employees, removed employees, field updates)
3. Confirm — your scenario changes are preserved; only the baseline updates

**Note:** Scenario refresh is in development. Contact support to confirm availability.

## Troubleshooting Common Issues

| Problem                           | Solution                                                                                                                                      |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| New hire not appearing            | Check if HRIS exported them; verify sync has run since hire was added; check for validation errors                                            |
| Terminated employee still showing | Verify HRIS processed termination; wait for next sync (will auto-remove); or upload corrected CSV. Contact support if the issue still exists. |
| Sync taking hours                 | Normal for >10,000 employees; contact support if unusually slow                                                                               |

**Full troubleshooting:** [Data Issues](../troubleshooting/data-issues.md)

## Related Resources

* [Data Import Requirements](../data-import/data-requirements.md)
* [Partial Data Upload](../scenarios/advanced-actions/partial-data-upload-1.md)
* [Live Data Integration Overview](../live-data-integration/what-is-a-live-data-integration.md)
* [Data Error Checklist](../data-import/data-error-checklist.md)
