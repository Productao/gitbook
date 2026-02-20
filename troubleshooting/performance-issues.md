---
description: Addressing slow performance and loading problems
hidden: false
---

# Performance Issues

Common solutions for slow loading, browser freezing, timeouts, and performance optimization for large organizations.

## General Slowness

**Application loading slowly or page freezes**
- Clear browser cache; close unnecessary tabs and other applications
- Minimum: 5 Mbps download; recommended: 25+ Mbps
- Disable browser extensions (especially ad blockers); try Chrome (recommended) or Edge
- Restart the browser; restart the computer if needed

**Slow initial load after login**
- 30–60 seconds is normal for orgs >5,000 employees — don't refresh during initial load
- If consistently >2 minutes: test internet speed, try a wired connection, contact support

**Page freezes / "Page Unresponsive"**
- Wait 30 seconds — a large operation may still be processing
- Check Chrome task manager (Shift+Esc) for memory usage; close other tabs
- Avoid: opening org chart with >1,000 expanded reports, bulk-selecting >500 positions at once, exporting >10,000 records at once

## Org Chart Performance

**Org chart slow to render**
- Filter by department, layer (top 3 layers), or location before opening the org chart
- Collapse sections you don't need; switch to Directory view for navigation
- For orgs >10,000: use Directory view primarily; use org chart only for specific sections

**Drag-and-drop is laggy**
- Collapse sections not being edited; filter to a smaller view; close other tabs
- Alternative: Right-click > Change Manager (faster than dragging)
- For bulk moves: use Bulk Operations

**Expand/collapse actions are slow**
- Normal: 5–10 seconds for positions with >50 reports
- Use Directory view + filter by Manager for large teams instead of expanding in org chart

## Scenario Performance

**Scenario operations timing out**
- Break large changes into smaller batches (25 at a time, not 100+); save frequently
- For large bulk changes: use partial upload (CSV) instead of manual edits
- Try during off-peak hours; contact support if timeouts persist

**Scenario comparison is slow**
- Wait 30–60 seconds; filter to a specific department before comparing
- For large datasets: export both scenarios to CSV and compare in Excel

## Directory and Filter Performance

**Directory view or filters slow to load**
- Apply simple filters first (department, location), then add complex ones
- Hide unnecessary columns (fewer columns = faster); sort by simple fields (Name, Title) not calculated fields (SOC, Cost)
- Save frequently-used filter combinations as views

## Export Performance

**Large export timing out**
- Apply filters to reduce export size; export one department or date range at a time
- Use CSV format (faster than Excel); close other tabs during export
- For >50,000 rows: contact support for bulk export assistance

**PowerPoint export slow**
- Filter to top 3–4 layers or a specific department before exporting
- Reduce card content fields; export in sections and combine manually

## Browser-Specific Issues

**Chrome slow or crashing**
- Update Chrome; clear cache and cookies; check chrome://extensions and disable one by one
- Reset Chrome settings (Settings > Advanced > Reset) if needed; try Edge or Firefox

**General browser crash**
- Clear cache; disable all extensions; restart computer (need 8GB+ RAM recommended)
- Reinstall browser if crashes persist; contact support with crash logs

## Network and VPN

**Slow connection / high latency**
- Minimum: 5/1 Mbps; recommended: 25+/5 Mbps; use wired (Ethernet) over WiFi
- Close bandwidth-heavy apps (streaming, downloads); schedule large operations off-peak

**VPN slowing performance**
- Test without VPN to confirm it's the cause
- Ask IT to configure split-tunneling (bypass VPN) for agentnoon.com

## Large Organizations (10,000+ Employees)

- Always filter before viewing — never load the full org at once
- Use Directory view as primary navigation; reserve org chart for specific sections
- Save every 10–20 changes; use partial upload for bulk changes
- Break bulk operations into batches of 50–100; schedule large operations off-peak
- Recommended: 50+ Mbps internet; 16GB RAM

## When to Contact Support

Contact support@agentnoon.com if performance doesn't improve after trying solutions, the application consistently times out, or a browser crashes repeatedly.

Include: org size, browser version, OS, internet speed, computer specs, specific slow actions, and browser console errors (F12 > Console).
