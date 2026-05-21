# Quiz: Module 08 - Business Intelligence Tools – Power BI and Tableau
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
A sales director wants a single screen showing live KPI tiles for revenue, units sold, and return rate — updated every hour — so she can monitor performance throughout the day without running a new report each time. What type of BI output best meets this need?
*   A) A paginated report with detailed transaction rows exported to PDF.
*   B) An interactive dashboard displaying real-time KPI tiles that refresh automatically.
*   C) A flat CSV extract sent to her inbox each morning.
*   D) A data dictionary documenting the definitions of each metric.
*   **Correct Answer:** B) An interactive dashboard displaying real-time KPI tiles that refresh automatically.
*   **Distractor Analysis:**
    *   *Why correct:* A dashboard is designed for real-time or near-real-time monitoring of key metrics on a single screen. The director's need — "monitor performance throughout the day" — is the canonical dashboard use case.
    *   A) A paginated PDF report is for detailed historical analysis, not live monitoring. C) A CSV extract is a static snapshot, not a live display. D) A data dictionary documents metadata, not operational metrics.

---

**Question 2**
In business intelligence, which of the following most accurately defines a **data connector**?
*   A) A formula-based computation inside a BI tool that aggregates raw data into a derived metric — such as total revenue or profit margin — evaluated dynamically based on the active filter context.
*   B) A driver or interface that allows a BI tool to read data from a specific external system, such as a database, a cloud storage service, or an API endpoint.
*   C) A visual component on a dashboard that lets users select a value from a dropdown or slider to dynamically filter all charts on the page.
*   D) A schema design pattern in which a central fact table is joined to multiple surrounding dimension tables to support fast analytical queries.
*   **Correct Answer:** B) A driver or interface that allows a BI tool to read data from a specific external system, such as a database, a cloud storage service, or an API endpoint.
*   **Distractor Analysis:**
    *   *Why B is correct:* A data connector is the mechanism that establishes the link between the BI tool and the data source. Without a connector, the tool cannot ingest or query the data.
    *   *Why A is incorrect:* This describes a calculated measure or calculated field — a formula evaluated at query time, not a connection mechanism.
    *   *Why C is incorrect:* This describes a slicer or filter control — a UI element for interactive filtering, not a data ingestion component.
    *   *Why D is incorrect:* This describes a star schema — a data modeling pattern, not a connection mechanism.

---

**Question 3**
A BI analyst is building a Power BI dashboard connected to a hospital database that updates every 10 minutes with new patient admission data. The hospital needs the dashboard to always reflect the most current data without manual refreshes. Which connection mode is most appropriate?
*   A) Import mode, because it caches a full snapshot of the data in Power BI for fast performance.
*   B) DirectQuery mode, because it sends live queries to the source database each time a visual loads, always reflecting current data.
*   C) Export mode, because it writes the data to a CSV file that Power BI reads at startup.
*   D) Snapshot mode, because it takes a point-in-time copy of the database and stores it locally.
*   **Correct Answer:** B) DirectQuery mode, because it sends live queries to the source database each time a visual loads, always reflecting current data.
*   **Distractor Analysis:**
    *   *Why B is correct:* DirectQuery bypasses caching and queries the live source on every interaction, ensuring the dashboard always shows the latest data. This matches the hospital's requirement for up-to-the-minute accuracy.
    *   *Why A is incorrect:* Import mode creates a static snapshot that is only as fresh as the last scheduled refresh. With data changing every 10 minutes, an import-mode cache would frequently be stale.
    *   *Why C is incorrect:* "Export mode" is not a Power BI connection mode. Exporting to CSV and re-reading it would not provide live updates.
    *   *Why D is incorrect:* "Snapshot mode" is not a standard Power BI connection mode. The term describes what Import mode does, but the answer is framed incorrectly and does not address the live-data requirement.

---

**Question 4**
An analyst builds a Tableau dashboard showing quarterly sales. When a user clicks a bar in the "Sales by Region" chart, the "Sales by Product" chart on the same dashboard automatically filters to show only that region's products. What BI feature is being used?
*   A) Data blending — combining data from two different sources into a single view.
*   B) Cross-filtering (dashboard actions) — clicking one visual passes a filter context to other visuals on the same dashboard.
*   C) Drill-through — navigating from a summary page to a separate detailed report page.
*   D) Calculated field — a formula that derives a new metric from existing columns in the data source.
*   **Correct Answer:** B) Cross-filtering (dashboard actions) — clicking one visual passes a filter context to other visuals on the same dashboard.
*   **Distractor Analysis:**
    *   *Why B is correct:* Cross-filtering (called dashboard actions in Tableau, cross-report filtering or interactions in Power BI) allows a selection in one chart to act as a filter for other charts on the same canvas. This is the standard mechanism for building interactive dashboards.
    *   *Why A is incorrect:* Data blending combines data from multiple sources at the row level. It is a data preparation technique, not an interaction behavior between two charts.
    *   *Why C is incorrect:* Drill-through navigates to a separate, more detailed page or report. The scenario describes both charts on the same dashboard, not navigation to another page.
    *   *Why D is incorrect:* A calculated field is a formula for deriving a metric. It has nothing to do with the interactive filtering behavior between charts.

---

**Question 5**
A BI developer creates a measure in Power BI: `Profit Margin = DIVIDE([Total Profit], [Total Revenue])`. When a slicer is set to "Electronics," the measure shows 18%. When the slicer is cleared, it shows 22%. What explains this behavior?
*   A) The measure formula contains an error that causes it to calculate incorrectly when no filter is applied.
*   B) Measures in Power BI are evaluated dynamically based on the current filter context, so the result changes as slicers and filters change.
*   C) The measure is recalculating because the underlying database was updated between the two slicer states.
*   D) Power BI rounds calculated fields differently depending on the number of rows returned by the active filter.
*   **Correct Answer:** B) Measures in Power BI are evaluated dynamically based on the current filter context, so the result changes as slicers and filters change.
*   **Distractor Analysis:**
    *   *Why B is correct:* This is the defining behavior of a BI measure — it aggregates only the data that passes through the active filter context. "Electronics" filters to a subset with an 18% margin; the full dataset yields 22%. This is expected and correct behavior.
    *   *Why A is incorrect:* Different results for different filter states is not an error — it is the intended behavior of a dynamic measure. An actual formula error would produce a consistent error or null value, not contextually different numbers.
    *   *Why C is incorrect:* The scenario describes two slicer states in the same session, not two different query times. The database update explanation does not apply to instantaneous slicer changes.
    *   *Why D is incorrect:* Power BI does not apply different rounding logic based on row count. The difference in results is driven by filter context, not a rounding implementation detail.
