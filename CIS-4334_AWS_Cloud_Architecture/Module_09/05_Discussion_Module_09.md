# Discussion Forum: Module 09 — AWS Databases

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

**Instructions:** Choose ONE of the three scenarios below. Write an initial post of 175–225 words responding to the scenario. Then write a substantive reply (75–100 words) to at least one classmate who chose a different scenario. Use specific AWS service names and feature names in your response.

---

## Scenario A — The Database Migration Decision

A mid-size e-commerce company runs their entire product catalog, customer orders, and user accounts on a single on-premises Oracle RAC database. They are migrating to AWS and the CTO asks the architecture team to evaluate whether to lift-and-shift to RDS Oracle or redesign using purpose-built AWS database services.

Analyze this migration decision. Consider whether a single-database approach remains appropriate in AWS or whether specific workloads should be separated into purpose-built databases. For each major data type (product catalog, customer orders, user accounts), identify which AWS database service — if any — would serve it better than a monolithic Oracle database, and explain your reasoning. Address the trade-offs of the redesign approach versus lift-and-shift in terms of migration complexity, ongoing operational cost, and scalability.

---

## Scenario B — Caching Strategy Debate

A high-traffic news website has an Aurora MySQL database with three read replicas, but it is still experiencing read latency spikes of 50–100ms during breaking news events when millions of users request the same article simultaneously. The team is debating between two approaches: adding more Aurora read replicas versus deploying ElastiCache Redis in front of the database.

Evaluate both approaches. For each approach, describe how it addresses the latency problem, at what scale it is the right choice, and what its limitations are. Then recommend one approach for this specific scenario and justify your recommendation. Consider the nature of the data (news articles change infrequently once published), the traffic pattern (spikes for the same content), and the team's operational complexity budget.

---

## Scenario C — Multi-Region Database Architecture

A gaming company wants to launch a global multiplayer game where players in North America, Europe, and Asia-Pacific each need low-latency access to player profile data. Players can update their own profile (username, stats, preferences) from any region. Players from different regions occasionally interact, so profile data must eventually be consistent across all regions. The company considered using three separate Aurora clusters — one per region — but is concerned about keeping them synchronized.

Evaluate the three-Aurora-cluster approach and explain its limitations. Describe the AWS database service and feature that better solves this problem natively. Explain how write conflicts are handled when a player updates their profile in two regions simultaneously. Address the question of whether eventual consistency is acceptable for this use case or whether it is a problem.

---

## Peer Response Instructions

After posting your initial response, read your classmates' posts and reply to at least one person who chose a different scenario than you. Your reply should:

- Identify one point in their response you agree with and explain why
- Identify one consideration they may have missed or could strengthen
- Ask a follow-up question that extends the discussion

---

## 10-Point Grading Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| Technical Accuracy | 3 | Database service names, features, and behaviors described correctly |
| Depth of Analysis | 2 | Response addresses trade-offs, not just lists features |
| Word Count (Initial) | 1 | Initial post is between 175 and 225 words |
| Use of Module Concepts | 2 | Response explicitly references concepts from Module 09 video and reading guide |
| Peer Reply Quality | 2 | Reply is substantive (75–100 words), identifies a specific point, and asks a meaningful follow-up question |
| **Total** | **10** | |

---

**Professor Nash Note:** Scenario B is the one that trips up even experienced engineers. The instinct when a database is slow is to scale the database — add more replicas, provision more capacity. But for a specific traffic pattern where millions of users are requesting the same content simultaneously, the architectural insight is that a caching layer collapses those millions of identical database queries into a tiny number of cache misses. Understanding when to scale the database versus when to cache in front of it is a fundamental architectural judgment that you will exercise throughout your career. Push yourself to be quantitative: think about what the cache hit ratio would be for this workload and what that means for database load.

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
