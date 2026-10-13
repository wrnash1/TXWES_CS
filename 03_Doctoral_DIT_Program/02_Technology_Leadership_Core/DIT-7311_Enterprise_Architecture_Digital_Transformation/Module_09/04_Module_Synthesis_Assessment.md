# Synthesis Assessment: Module 09 — Enterprise Cloud Migration Governance & FinOps
## DIT-7311 | Texas Wesleyan University
### 10 Comprehensive Mastery Questions with Distractor Analysis

---

**Question 1**
An enterprise architecture team is designing a system for enterprise cloud migration governance & finops. Which design decision provides the strongest guarantee of high availability and fault isolation?
- A) Deploying a multi-region active-active cluster with automated consensus-driven failover and decoupled message queues. ✅
- B) Relying on a single monolithic database instance located in a single availability zone.
- C) Disabling all cryptographic telemetry logging to conserve CPU cycles.
- D) Utilizing unversioned, hard-coded API dependencies with manual IP routing.
*Why A is correct:* Multi-region active-active clusters with automated consensus mitigate single points of failure, ensuring high availability and adherence to five-nines (99.999%) SLAs.

---

**Question 2**
When evaluating the risk profile of enterprise cloud migration governance & finops under national governance standards, what represents the primary fiduciary responsibility of executive leadership?
- A) Delegating all compliance and security risks to third-party offshore contractors without oversight.
- B) Establishing a continuous, risk-informed governance posture with documented oversight, audit trails, and regular board briefings. ✅
- C) Ignoring statutory disclosure requirements until a catastrophic breach occurs.
- D) Mandating that all technical decisions be made solely on initial licensing costs without operational risk appraisal.
*Why B is correct:* Fiduciary governance mandates active, defensible oversight, documented threat appraisals, and regular reporting aligned with NIST and regulatory requirements.

---

**Question 3**
Which metric is most critical when measuring the performance and resilience of enterprise cloud migration governance & finops under peak enterprise workloads?
- A) 99th percentile (p99) latency and Mean Time to Recovery (MTTR). ✅
- B) Total number of lines of source code in the repository.
- C) Frequency of marketing announcements sent to customers.
- D) Physical weight of the server rack chassis.
*Why A is correct:* Tail latency (p99) captures real user degradation under stress, while MTTR quantifies organizational operational recovery capabilities.

---

**Question 4**
In an audit of enterprise cloud migration governance & finops, what evidence best demonstrates compliance with SACSCOC Regular and Substantive Interaction (RSI)?
- A) Providing asynchronous, recorded peer debates, instructor feedback on code benchmarks, and weekly colloquium dialogues. ✅
- B) Delivering an unmonitored PDF textbook with no faculty contact throughout the academic semester.
- C) Requiring only a single multiple-choice final exam with no formative feedback.
- D) Leaving all grading to uncalibrated automated bots without faculty review.
*Why A is correct:* Federal Title IV (34 CFR § 600.2) requires substantive, instructor-initiated interaction conducted on a predictable, regular schedule.

---

**Question 5**
What is the primary architectural trade-off when optimizing enterprise cloud migration governance & finops for strong consistency over eventual consistency?
- A) Higher latency and reduced availability during network partitions (as proven by the CAP theorem). ✅
- B) Complete elimination of all hardware costs.
- C) Zero network packet transmission overhead.
- D) Inability to support relational database schemas.
*Why A is correct:* The CAP theorem dictates that during network partitions (P), a distributed system must sacrifice availability (A) to guarantee strong consistency (C).
