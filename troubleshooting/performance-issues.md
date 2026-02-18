---
description: Addressing slow performance and loading problems
icon: gauge-high
hidden: false
---

# Performance Issues

Common solutions for slow loading, browser freezing, timeouts, and performance optimization for large organizations.

## General Performance Issues

### Application Loading Slowly

**Problem:** Agentnoon takes a long time to load or respond to clicks

**Cause:** Browser cache bloat, too many tabs open, slow internet, or large dataset

**Solution:**
1. Clear browser cache (see [Troubleshooting Overview](overview.md))
2. Close unnecessary browser tabs and windows
3. Restart browser completely
4. Check internet speed:
   - Minimum: 5 Mbps download
   - Recommended: 25+ Mbps download
   - Test at fast.com or speedtest.net
5. Disable browser extensions temporarily (especially ad blockers)
6. Close other applications using internet (video streaming, downloads)
7. Try different browser (Chrome recommended)
8. Restart computer if issue persists

> **[Screenshot placeholder: Browser task manager (Shift+Esc in Chrome) showing Agentnoon tab using 850MB memory with "High" memory usage indicator]**

---

### Slow Initial Load After Login

**Problem:** First page load after login takes 30+ seconds

**Cause:** Large organization data loading, expired cache, or network latency

**Solution:**
1. Wait for initial load to complete (30-60 seconds is normal for orgs >5,000 employees)
2. Once loaded, subsequent navigation will be faster
3. Don't refresh page during initial load
4. For future sessions:
   - Keep Agentnoon tab open (don't close browser)
   - Use browser bookmarks instead of searching for URL
   - Stay logged in to avoid re-loading data
5. If initial load consistently >2 minutes:
   - Check internet connection speed
   - Try wired connection instead of WiFi
   - Contact support if persists

---

### Page Freezes or Becomes Unresponsive

**Problem:** Page stops responding, can't click anything, browser shows "Page Unresponsive"

**Cause:** Browser out of memory, large operation processing, or browser extension conflict

**Solution:**
1. Wait 30 seconds - operation may still be processing
2. Check browser task manager (Shift+Esc in Chrome) for memory usage
3. Close other tabs to free memory
4. If frozen >1 minute:
   - Close and reopen browser
   - Clear cache before reopening
5. For recurring freezes:
   - Disable browser extensions
   - Increase browser memory allocation (Advanced settings)
   - Use different browser
   - Close other applications
6. Avoid these actions that can cause freezes:
   - Opening org chart with >1,000 direct reports expanded
   - Bulk selecting >500 positions at once
   - Exporting >10,000 records at once

---

## Org Chart Performance Issues

### Org Chart Taking Long to Render

**Problem:** Org chart view loads slowly or doesn't render fully

**Cause:** Large organization, too many positions visible, or complex hierarchy

**Solution:**
1. Use filters to narrow view:
   - Filter by department
   - Filter by layer (show only top 3 layers)
   - Filter by location
2. Collapse sections you don't need to view:
   - Click collapse icon on position cards
   - Focus on area you're working on
3. Switch to Directory view (list format) instead of org chart:
   - Faster for large organizations
   - Still allows filtering and sorting
4. Zoom level optimization:
   - Zoom out to see structure (faster)
   - Zoom in only when editing specific positions
5. Use search to find specific positions instead of browsing entire org
6. For very large orgs (>10,000 employees):
   - Work in department-specific views
   - Use Directory view primarily
   - Use org chart only for specific sections

> **[Screenshot placeholder: Org chart with layer filter applied showing "Showing layers 0-3 only (487 positions visible, 2,350 hidden)" with filter controls]**

---

### Drag-and-Drop is Laggy

**Problem:** Dragging positions feels slow or stutters

**Cause:** Large org chart rendered, browser performance, or graphics issue

**Solution:**
1. Collapse sections not actively being edited
2. Filter to smaller view before dragging
3. Zoom to comfortable level (not too far out)
4. Close other browser tabs
5. Disable browser animations (browser settings)
6. Alternative method: Use "Change Manager" dropdown instead of drag-and-drop
   - Right-click position → Change Manager
   - Select from dropdown (faster than dragging)
7. For bulk moves: Use Bulk Operations instead of individual drag-and-drop

---

### Expand/Collapse Actions are Slow

**Problem:** Clicking expand icon takes several seconds to show direct reports

**Cause:** Position has many direct reports (>50), or large org structure below

**Solution:**
1. Wait for expansion to complete (may take 5-10 seconds for large teams)
2. Use Directory view for positions with many direct reports
3. Filter before expanding:
   - Filter by layer first
   - Then expand to see smaller subset
4. For positions with >100 direct reports:
   - Use Directory view exclusively
   - Filter by manager to see their team
5. Avoid expanding entire org chart at once
6. Collapse sections after viewing (to improve performance elsewhere)

---

## Scenario Performance Issues

### Scenario Operations Timing Out

**Problem:** Creating or editing scenarios results in timeout errors

**Cause:** Large scenario (>5,000 positions), complex calculations, or network issue

**Solution:**
1. Wait longer for operation to complete (up to 2 minutes)
2. Break large changes into smaller operations:
   - Instead of 100 additions at once, do 25 at a time
   - Save frequently between operations
3. Avoid making too many changes before saving
4. Check internet connection stability
5. For large bulk operations:
   - Use partial upload instead of manual edits
   - Upload CSV with changes (faster)
6. Close Change Tracker panel while editing (reduces load)
7. If timeouts persist:
   - Try during off-peak hours (early morning)
   - Contact support for assistance

---

### Scenario Comparison is Very Slow

**Problem:** Comparing two scenarios takes a long time to load

**Cause:** Scenarios have many differences, large dataset, or complex comparison

**Solution:**
1. Wait for comparison to complete (can take 30-60 seconds)
2. Reduce comparison scope:
   - Filter to specific department before comparing
   - Compare one section at a time
3. Export both scenarios to CSV and compare in Excel (faster for large data)
4. Use "Summary" comparison view instead of detailed view
5. Close other browser tabs during comparison
6. For very large scenarios:
   - Focus on Change Tracker summaries instead of full comparison
   - Use filtered exports for analysis

---

## Directory and Filter Performance

### Directory View Slow to Load

**Problem:** Switching to Directory view or applying filters is slow

**Cause:** Large number of records, complex filters, or calculations

**Solution:**
1. Wait for initial load (10-20 seconds for large orgs)
2. Apply filters to reduce dataset:
   - Start with department or location filter
   - Then add additional filters
3. Limit visible columns:
   - Hide unnecessary columns (fewer columns = faster)
4. Sort by simple fields (Name, Title) not calculated fields (SOC, Cost)
5. Use search instead of scrolling through entire directory
6. For exports: Apply filters before exporting (reduces file size)

---

### Filters Taking Long to Apply

**Problem:** Applying filter takes several seconds to update view

**Cause:** Complex filter logic, large dataset, or calculated field filters

**Solution:**
1. Apply simple filters first (Department, Location)
2. Then add complex filters (salary ranges, SOC)
3. Use "Apply" button instead of auto-apply (if available)
4. Avoid filtering on calculated fields when possible
5. Clear unnecessary filters to improve performance
6. Save frequently-used filter combinations as views
7. Wait for each filter to apply before adding next one

---

## Export Performance Issues

### Large Export Timing Out

**Problem:** Export fails or times out when exporting large datasets

**Cause:** Too many records or columns in export

**Solution:**
1. Apply filters to reduce export size:
   - Export one department at a time
   - Export by location or division
2. Remove unnecessary columns before exporting:
   - Uncheck columns you don't need
   - Export only essential fields
3. Break export into multiple smaller files:
   - Export Q1-Q2 data, then Q3-Q4
   - Export departments separately, combine in Excel
4. Use CSV format instead of Excel (faster for large data)
5. Close other browser tabs during export
6. Try during off-peak hours (early morning)
7. For very large exports (>50,000 rows):
   - Contact support for bulk export assistance

**See also:** [Export & Integration Issues](export-integration-issues.md)

---

### PowerPoint Export Very Slow

**Problem:** PowerPoint export takes several minutes or times out

**Cause:** Large org chart, many positions, or high-resolution graphics

**Solution:**
1. Filter org chart before exporting:
   - Export only top 3-4 layers
   - Export specific department, not entire org
2. Collapse sections you don't need in export
3. Reduce card content (fewer fields = smaller file)
4. Use image export instead (faster than PowerPoint)
5. For large exports:
   - Export in sections
   - Combine slides manually in PowerPoint
6. Alternative: Export to CSV and create charts in PowerPoint manually

---

## Browser-Specific Performance Issues

### Chrome Running Slowly

**Problem:** Chrome specifically has performance issues with Agentnoon

**Cause:** Chrome memory usage, extensions, or outdated version

**Solution:**
1. Update Chrome to latest version
2. Clear Chrome cache and cookies
3. Disable extensions:
   - Type chrome://extensions in address bar
   - Disable extensions one by one to find culprit
4. Check Chrome task manager (Shift+Esc):
   - Close tabs using excessive memory
5. Increase Chrome memory:
   - Close other applications
   - Restart Chrome
6. Reset Chrome settings:
   - Settings → Advanced → Reset settings
7. If Chrome still slow: Try Edge or Firefox

---

### Browser Crashing

**Problem:** Browser crashes completely when using Agentnoon

**Cause:** Out of memory, corrupted cache, or incompatible extension

**Solution:**
1. Clear browser cache completely
2. Disable all browser extensions
3. Update browser to latest version
4. Increase available RAM:
   - Close other applications
   - Restart computer
   - Upgrade RAM if computer has <8GB
5. Try different browser to isolate issue
6. Check browser crash logs (varies by browser)
7. If crashes persist:
   - Reinstall browser
   - Contact support with crash logs

---

## Network and Connectivity Performance

### Slow Connection / High Latency

**Problem:** Agentnoon feels laggy, actions take seconds to register

**Cause:** Slow internet connection, high latency, or network congestion

**Solution:**
1. Test internet speed:
   - Minimum required: 5 Mbps download, 1 Mbps upload
   - Recommended: 25+ Mbps download, 5 Mbps upload
2. Use wired connection instead of WiFi:
   - Ethernet cable reduces latency
3. Move closer to WiFi router
4. Disconnect other devices from network
5. Close applications using bandwidth (streaming, downloads)
6. Contact IT if on corporate network:
   - Request QoS prioritization for Agentnoon
7. Try different network (mobile hotspot) to test
8. Schedule large operations during off-peak hours

---

### VPN Slowing Down Performance

**Problem:** Agentnoon slower when connected to corporate VPN

**Cause:** VPN routing adds latency, or VPN throttling

**Solution:**
1. Test without VPN (if allowed):
   - Disconnect VPN temporarily
   - Note performance difference
2. If faster without VPN:
   - Request IT configure split-tunneling for Agentnoon
   - Or add Agentnoon to VPN bypass list
3. Use VPN with closest server location
4. Switch VPN protocol (OpenVPN, IKEv2, etc.)
5. If VPN required: Plan large operations for off-VPN times
6. Contact IT for VPN optimization

---

## Hardware Limitations

### Computer Running Slowly

**Problem:** Entire computer slow, not just Agentnoon

**Cause:** Insufficient RAM, old CPU, or too many applications running

**Solution:**
1. Close unnecessary applications
2. Restart computer
3. Check system requirements:
   - Minimum: 8GB RAM, 4-core CPU
   - Recommended: 16GB RAM, modern CPU
4. Upgrade hardware if below minimum
5. Check for malware or background processes
6. Free up disk space (>20% free recommended)
7. Use task manager to identify resource hogs

---

### Running on Older Computer

**Problem:** Agentnoon slow on older laptop or desktop

**Cause:** Hardware doesn't meet modern web application requirements

**Solution:**
1. Close all other applications when using Agentnoon
2. Use Directory view instead of org chart (less graphics intensive)
3. Apply filters to reduce data displayed
4. Avoid bulk operations on old hardware
5. Consider:
   - Adding RAM (8GB minimum, 16GB recommended)
   - Using different computer for Agentnoon
   - Using cloud desktop or virtual machine
6. Focus on essential tasks, minimize multitasking

---

## Working with Large Organizations (10,000+ Employees)

### General Best Practices for Large Orgs

**Problem:** Organization has >10,000 employees and everything feels slow

**Cause:** Large dataset inherently takes longer to process

**Solution:**
1. **Always use filters:**
   - Never view entire org at once
   - Filter by department, location, or layer
   - Work in sections
2. **Prefer Directory view over Org Chart:**
   - Directory view handles large data better
   - Use org chart only for specific sections
3. **Save frequently:**
   - Don't make 100 changes before saving
   - Save every 10-20 changes
4. **Use search instead of browsing:**
   - Search for specific positions or people
   - Don't scroll through entire directory
5. **Break bulk operations into batches:**
   - 50-100 positions at a time
   - Not 1,000+ at once
6. **Schedule large operations during off-peak hours:**
   - Early morning or late evening
   - Coordinate with team to avoid conflicts
7. **Use exports and imports for bulk changes:**
   - Partial upload is faster than manual edits
8. **Upgrade internet connection:**
   - 50+ Mbps recommended for large orgs

---

### Forecast View Slow for Large Org

**Problem:** Forecast module extremely slow with large organization

**Cause:** Calculating projections for 10,000+ employees across 5 years

**Solution:**
1. Filter before using Forecast:
   - View one department at a time
   - Filter to specific locations
2. Use yearly view instead of monthly (fewer data points)
3. Limit monetary fields displayed (salary only, not all pay components)
4. Export to CSV for detailed analysis in Excel
5. Close Change Tracker during Forecast navigation
6. Allow initial load to complete (1-2 minutes)
7. Avoid switching views frequently (stay in Forecast once loaded)

---

## When Performance is Unusable

**Contact support if:**
- Performance doesn't improve after trying all solutions
- Application consistently times out
- Browser crashes repeatedly
- Specific operations never complete
- Performance degraded suddenly (was fine before)

**Include in support request:**
- Organization size (number of employees)
- Browser version and operating system
- Internet speed (speedtest.net results)
- Computer specs (RAM, CPU)
- Specific actions that are slow
- Screenshots of browser console errors (F12 → Console)
- Network environment (corporate, VPN, home WiFi)

**Contact:** support@agentnoon.com

---

## Optimization Checklist

Before each Agentnoon session, optimize performance:

- [ ] Clear browser cache (once per week)
- [ ] Close unnecessary browser tabs
- [ ] Close other applications
- [ ] Check internet speed (25+ Mbps recommended)
- [ ] Use Chrome or Edge (latest version)
- [ ] Disable ad blockers and privacy extensions
- [ ] Use wired connection if available
- [ ] Apply filters before viewing large datasets
- [ ] Use Directory view for large org navigation
- [ ] Save work frequently during edits
- [ ] Plan large operations during off-peak hours

---

## Next Steps

- Return to [Troubleshooting Overview](overview.md)
- See [Export & Integration Issues](export-integration-issues.md) for export performance
- Review [Scenario Issues](scenario-issues.md) for scenario-specific performance
- Check [Data Issues](data-issues.md) for upload performance
- Contact [Support](../start-here/support-self-help.md) for persistent issues
