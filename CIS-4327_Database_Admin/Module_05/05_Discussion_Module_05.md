# Discussion Forum: Module 05 — Bigtable: Wide-Column NoSQL at Scale

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

---

### Overview

This discussion connects Bigtable's data model and design constraints to real-world engineering decisions. Read all three scenarios and post your initial response to the one that most closely matches your professional background or academic focus. Reply to at least two classmates.

---

### Scenario A — IoT Platform Row Key Redesign

A smart building management company stores temperature, humidity, CO2, and occupancy readings from 50,000 sensors across 200 office buildings. They currently use a Bigtable table with the row key format `buildingId#sensorId#timestamp` where timestamp is a Unix epoch integer in ascending order. The engineering team reports that write throughput degrades during business hours even though the Bigtable cluster has 10 nodes. Key Visualizer confirms writes are concentrating at the high end of the row key space.

For your initial post, address all of the following.

Identify the specific component of the current row key design that causes the hotspot, explaining the mechanism at the tablet level. Propose a corrected row key design that eliminates the hotspot while still allowing efficient per-sensor time-range scans. Describe whether the order of components in your proposed key (building, sensor, timestamp) matters for the primary range scan access pattern and explain why. Identify one trade-off your proposed key design introduces compared to the original format. Your post should be 175–225 words using correct Bigtable terminology.

---

### Scenario B — Bigtable vs. BigQuery for Analytics

A retail chain collects point-of-sale transaction records from 3,000 stores, generating 2 billion records per year. The data science team wants to run nightly batch analytics to identify sales trends, compute store rankings, and build customer purchase history models. The operations team wants real-time dashboards showing current store transaction rates updated every 10 seconds. A junior engineer recommends using Cloud Bigtable for both use cases because it handles large data volumes.

For your initial post, address all of the following.

Explain why Bigtable is appropriate for the real-time dashboard use case and not appropriate for the nightly batch analytics use case — focus on the data access pattern differences, not just the data volume. Identify which GCP service would be more appropriate for the nightly analytics and explain the specific SQL capabilities it provides that Bigtable lacks. Describe a two-service architecture (one for real-time, one for analytics) and explain how data would flow between the two services to serve both use cases. Identify one operational challenge of maintaining the two-service architecture. Your post should be 175–225 words using correct terminology from Module 05.

---

### Scenario C — Column Family Design Debate

A fintech startup is designing a Bigtable schema for a user financial profile table. One engineer proposes creating 15 column families: one for each type of user data (cf_name, cf_address, cf_income, cf_credit_score, cf_accounts, cf_transactions, cf_risk_flags, cf_kyc_status, cf_preferences, cf_notifications, cf_login_history, cf_devices, cf_api_keys, cf_referrals, cf_support_tickets). Another engineer argues this design is wrong and proposes two column families: cf_profile (demographic and status data) and cf_activity (behavioral and transactional data).

For your initial post, address all of the following.

Explain why the 15-family design violates Bigtable's column family design guidelines and what specific performance or operational problems it may cause. Evaluate the two-family design: does it correctly apply the grouping-by-access-pattern principle, and which attributes would you put in each family? Identify one attribute category from the 15-family list that you might want in its own separate family and justify why, based on access pattern or GC policy requirements. Explain what the terms "column family" and "column qualifier" mean in Bigtable and how they differ from "column" in a relational database. Your post should be 175–225 words using correct Bigtable terminology from Module 05.

---

### Peer Response Guidelines

Reply to at least two classmates across any scenario. Each reply must be at least 50 words and add technical value — an alternative design, a trade-off they did not consider, a specific Bigtable behavior that modifies their recommendation, or a substantive follow-up question.

---

### Discussion Rubric — 10 Points Total

Initial post — 6 points.

- 5 to 6 points: Addresses all required prompt elements with technical accuracy, correct Bigtable terminology, and clear reasoning. Meets the 175–225 word count.
- 3 to 4 points: Addresses most elements but omits one required item or uses imprecise terminology.
- 0 to 2 points: Initial post is missing, substantially incomplete, or contains significant errors about Bigtable behavior.

Peer responses — 4 points.

- 4 points: Two substantive replies of at least 50 words each that contribute technical content.
- 2 points: Only one qualifying reply, or both replies are superficial.
- 0 points: No peer responses by the deadline.

---

### Due Dates

Initial post: Wednesday at 11:59 PM

Peer responses: Sunday at 11:59 PM

Professor Nash reads every post. Posts that connect the lab hotspot analysis to the discussion scenarios will be recognized in class.

---

Reference: cloud.google.com/learn
