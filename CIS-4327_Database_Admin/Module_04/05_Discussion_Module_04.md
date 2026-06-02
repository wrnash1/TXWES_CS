# Discussion Forum: Module 04 — Cloud Spanner: Globally Distributed Databases

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

---

### Overview

This discussion connects Cloud Spanner's unique capabilities and design constraints to real-world architecture decisions. Read all three scenarios and post your initial response to the one that best matches your professional background or academic focus. Reply to at least two classmates.

---

### Scenario A — Global Gaming Platform

A mobile gaming company runs a multiplayer game with 10 million active users across North America, Asia, and Europe. The current database is a Cloud SQL for PostgreSQL instance in us-central1. Players in Asia report that leaderboard updates take 8–12 seconds to appear because data must travel from Asia to the US datacenter and back. Additionally, the team reports that during peak hours on Friday evenings, the Cloud SQL primary instance maxes out at 100% CPU and write transactions begin failing.

For your initial post, address all of the following.

Explain why Cloud SQL cannot solve both problems simultaneously — the latency problem and the write scalability problem — and what architectural limitation causes each. Identify the specific Cloud Spanner features that address each of the two problems. Describe the primary key strategy you would use for the leaderboard table, which will receive tens of thousands of writes per second from player score updates, and explain why the recommended strategy avoids hotspots. Identify one cost trade-off the company must accept when migrating from Cloud SQL to Cloud Spanner. Your post should be 175–225 words using correct Cloud Spanner terminology.

---

### Scenario B — Financial Services: Strong vs. Stale Reads

A global investment firm uses Cloud Spanner to store portfolio positions and trade confirmations. Two types of queries run against the same Spanner database: real-time trade execution queries that read account balances before approving a trade, and executive dashboard queries that display portfolio summaries refreshed every 30 seconds. The platform architect wants to optimize query latency without compromising data integrity for trade execution.

For your initial post, address all of the following.

Explain the difference between a strong read and a bounded staleness read in Cloud Spanner in terms of which replica serves the request and what consistency guarantee is provided. Identify which read mode is appropriate for the trade execution queries and which is appropriate for the executive dashboard queries, and justify each choice based on the data consistency requirements described. Explain what specific risk would occur if bounded staleness reads were used for trade execution queries. Identify one additional Spanner configuration decision (beyond read mode) that would improve latency for users in different regions. Your post should be 175–225 words using correct terminology from Module 04.

---

### Scenario C — Schema Migration: Sequential Keys to Spanner

An e-commerce company is migrating their order management system from Cloud SQL for MySQL to Cloud Spanner to support global expansion. The current MySQL schema uses AUTO_INCREMENT integer primary keys for all tables: orders, order_items, customers, and products. The migration team plans to import all data into Spanner using the same integer keys for simplicity.

For your initial post, address all of the following.

Explain what a Spanner write hotspot is and why importing data with sequential integer primary keys will cause hotspot behavior on the orders and order_items tables, which receive the highest insert rates. Propose a specific alternative primary key strategy for the orders table that eliminates the hotspot risk while still allowing efficient lookups by customer and date. Describe how the existing MySQL integer foreign key references (e.g., order_items.order_id referencing orders.order_id) need to be redesigned in the new Spanner schema. Identify one advantage and one disadvantage of using UUID primary keys in Cloud Spanner compared to sequential integers. Your post should be 175–225 words using correct terminology from Module 04.

---

### Peer Response Guidelines

Reply to at least two classmates across any scenario. Each reply must be at least 50 words and add technical value — an alternative design, a trade-off they did not mention, a specific Cloud Spanner behavior that modifies their recommendation, or a follow-up question that deepens the technical discussion.

---

### Discussion Rubric — 10 Points Total

Initial post — 6 points.

- 5 to 6 points: Addresses all required prompt elements with technical accuracy, correct Spanner terminology, and clear reasoning. Meets the 175–225 word count.
- 3 to 4 points: Addresses most elements but omits one required item or lacks technical precision.
- 0 to 2 points: Initial post is missing, substantially incomplete, or contains significant errors about Spanner behavior.

Peer responses — 4 points.

- 4 points: Two substantive replies of at least 50 words each that contribute technical content.
- 2 points: Only one qualifying reply, or both replies are superficial.
- 0 points: No peer responses by the deadline.

---

### Due Dates

Initial post: Wednesday at 11:59 PM

Peer responses: Sunday at 11:59 PM

Professor Nash reads every post. Posts that connect lab experience with the conceptual material will be recognized in class.

---

Reference: cloud.google.com/learn
