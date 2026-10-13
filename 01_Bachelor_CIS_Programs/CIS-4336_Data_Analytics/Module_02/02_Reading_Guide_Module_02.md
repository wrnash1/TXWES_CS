# Reading Guide — Module 02: Data Collection and Data Sources

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4336 &BULL; DATA ANALYTICS & BUSINESS INTELLIGENCE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">freeCodeCamp / IBM &bull; CIS-4336 Module 02</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=r-uOLxNrNk8" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/r-uOLxNrNk8" title="Data Analytics with Python, Pandas & SQL Masterclass" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Data Analytics with Python, Pandas & SQL Masterclass</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->




**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 1 and Domain 2

---

## Overview

This reading guide covers data collection methods, database structures, and ETL processes that appear on the CompTIA Data+ exam. Work through all sections before attempting the lab or quiz.

---

## Section 1 — Core Vocabulary

| Term | Definition |
|---|---|
| Primary data | Data collected directly for the current analytical purpose |
| Secondary data | Data originally collected for a different purpose, reused for analysis |
| OLTP | Online Transaction Processing — operational systems optimized for fast writes and row-level access |
| OLAP | Online Analytical Processing — analytical systems optimized for fast reads across large data volumes |
| ETL | Extract, Transform, Load — the pipeline for moving data from source to analytical target |
| ELT | Extract, Load, Transform — variant where transformation occurs inside the target environment |
| Primary key | A column or set of columns that uniquely identifies each row in a table; cannot be null |
| Foreign key | A column that references the primary key of another table to enforce referential integrity |
| Schema | The structural definition of a database: its tables, columns, data types, and relationships |
| Star schema | OLAP design with a central fact table connected directly to dimension tables |
| Snowflake schema | OLAP design where dimension tables are further normalized into sub-dimension hierarchies |
| Data warehouse | A central analytical repository storing integrated historical data from multiple sources |
| Data mart | A subject-specific subset of a data warehouse |
| Data lake | A large-scale repository storing raw data in native format, including unstructured data |
| API | Application Programming Interface — a defined contract for programmatic data exchange |
| Referential integrity | The rule that every foreign key value must match an existing primary key value in the referenced table |
| Normalization | Organizing database tables to reduce data redundancy and improve update consistency |
| Denormalization | Combining normalized tables to optimize read performance for analytical queries |

---

## Section 2 — Primary vs. Secondary Data Comparison

| Characteristic | Primary Data | Secondary Data |
|---|---|---|
| Who collected it | The analyst or their organization, for this purpose | Another party, for a different original purpose |
| Cost | Higher — survey design, administration, tooling | Lower — often free or purchased at scale |
| Time to acquire | Longer | Faster |
| Relevance fit | High — designed for the specific question | Variable — may not perfectly match the question |
| Quality control | Full control | Limited — must evaluate source credibility |
| Examples | Custom survey, A/B experiment, new sensor deployment | Census records, CRM history, purchased demographic data |

---

## Section 3 — Data Collection Method Reference

| Method | Primary or Secondary | Structure | Volume | Key Risk |
|---|---|---|---|---|
| Survey / questionnaire | Primary | Mixed (structured + unstructured) | Small to medium | Response bias, low completion rates |
| Transactional capture | Secondary (from analyst view) | Structured | High | Schema complexity, data sprawl |
| IoT / sensor data | Primary or secondary | Semi-structured, time-series | Very high | Sensor drift, missing timestamps |
| Interview / focus group | Primary | Unstructured | Very small | Not statistically generalizable |
| Web scraping | Primary collection | Semi-structured to unstructured | Medium to high | Legal risk, layout changes break scrapers |
| REST API | Primary or secondary | Semi-structured (JSON/XML) | Variable | Rate limits, versioning breaks |
| Direct database query | Secondary | Structured | High | OLTP performance impact if queried directly |
| Purchased dataset | Secondary | Structured or semi-structured | Variable | Unknown collection methodology |

---

## Section 4 — OLTP vs. OLAP Reference

| Characteristic | OLTP | OLAP |
|---|---|---|
| Purpose | Record operational transactions | Support analytical queries |
| Optimization | Fast writes, row-level access | Fast reads, column aggregation |
| Schema design | Highly normalized (3NF typical) | Denormalized (star or snowflake) |
| Query type | Short, targeted — single records or small sets | Long, aggregate — millions of rows |
| Data freshness | Real-time or near-real-time | Periodic refresh (hourly, daily, weekly) |
| Data history | Current state or short history | Long historical record |
| Should analysts run heavy queries here? | No — degrades operational performance | Yes — designed for this workload |
| Examples | POS systems, ERP, CRM, banking cores | Redshift, BigQuery, Snowflake, Azure Synapse |

---

## Section 5 — Relational Database Concepts

### Primary and Foreign Keys

A primary key uniquely identifies each row in a table. Three rules apply:

- Values must be unique across all rows in the table
- Values cannot be null
- Each table has exactly one primary key (which may span multiple columns, forming a composite key)

A foreign key in one table references the primary key of another table. The referential integrity constraint requires every foreign key value to either match an existing primary key in the referenced table or be null.

### Schema Patterns Compared

| Schema Type | Structure | Join Complexity | Storage Use | Best For |
|---|---|---|---|---|
| Third Normal Form (3NF) | Highly normalized, many small tables | High (many joins required) | Efficient | OLTP operational systems |
| Star schema | Fact table with flat dimension tables | Low (one join per dimension) | Moderate | Simple, fast OLAP queries |
| Snowflake schema | Fact table with normalized dimension hierarchies | Medium (more joins) | More efficient than star | Complex dimensional hierarchies |

---

## Section 6 — ETL Pipeline Reference

| Stage | Key Activities | Common Tools | Common Issues |
|---|---|---|---|
| Extract | Pull data from source systems via queries, API calls, or file exports | Python, SQL, Talend, Informatica | Incomplete extraction, source system load, schema drift |
| Transform | Clean, normalize, join, aggregate, and compute derived fields | Python/pandas, dbt, Apache Spark | Null handling logic, type mismatches, business rule errors |
| Load | Write transformed data to the target analytical store | SQL COPY/INSERT, cloud storage APIs | Duplicate loading, failed transactions, index rebuild time |

### ELT vs. ETL Decision Guide

Use ETL when:

- The target system has limited compute power for transformation
- Raw data should not be stored in the target for compliance reasons
- The transformation logic is mature and unlikely to change

Use ELT when:

- The target is a modern cloud platform (Snowflake, BigQuery, Databricks)
- You want to preserve raw data for re-processing as business logic evolves
- Transformation complexity benefits from the target's SQL compute engine

---

## Section 7 — Data Quality Dimensions

| Dimension | Definition | Example Issue | Detection Method |
|---|---|---|---|
| Completeness | All expected records and fields are present | Missing customer address fields | Count nulls per column; compare to expected row count |
| Accuracy | Values reflect real-world truth | Sensor calibration drift producing wrong temperature readings | Cross-reference with validated reference values |
| Consistency | Same entity represented identically across systems | "USA" vs. "U.S.A." vs. "United States" in different tables | Standardization checks, fuzzy matching |
| Timeliness | Data is current enough for the use case | 24-hour-stale metrics displayed on a real-time dashboard | Freshness timestamp checks |
| Uniqueness | Each entity appears exactly once | Duplicate customer records from a CRM migration | Deduplication checks on identifier columns |
| Validity | Values conform to defined format and range rules | Age field containing -5 or 999 | Range constraints, format pattern checks |

---

## Section 8 — Data+ Exam Tips

1. **Primary vs. secondary identification.** The key signal: did the analyst's organization collect it directly for this purpose? Yes means primary. No — reusing data collected by others — means secondary.

2. **OLTP is never the right answer for heavy analytics.** Any exam choice suggesting aggregate analytical queries should run against an OLTP production database is incorrect. Heavy reads belong in a data warehouse.

3. **Star vs. snowflake schema.** Star schema: fact table connects directly to flat dimension tables. Snowflake schema: dimension tables are further normalized. The exam may show a diagram and ask you to name the pattern.

4. **ETL stage mapping.** Know which activities belong in each stage. Removing duplicates is Transform. Pulling data from source is Extract. Writing to the warehouse is Load.

5. **Foreign key = referential integrity.** When an exam scenario describes a foreign key value that references a non-existent primary key, the violation is a referential integrity violation.

6. **Data lake vs. data warehouse.** A warehouse stores processed, structured analytical data. A lake stores raw data in native format, including unstructured data. The exam tests this distinction frequently.

7. **API responses are semi-structured.** JSON from a REST API is semi-structured, not structured. The schema is implied by keys, not enforced by a relational constraint.

8. **Survey bias types.** Non-response bias (those who do not respond differ from those who do) and response bias (respondents answer how they think they should) are the two main survey quality risks on the exam.

---

## Section 9 — Study Checklist

- [ ] Memorize all vocabulary terms in Section 1
- [ ] Distinguish primary from secondary data for five different scenarios
- [ ] Reproduce the OLTP vs. OLAP comparison table from memory
- [ ] Explain star schema and snowflake schema with a diagram
- [ ] Describe all three ETL stages with concrete examples
- [ ] List all six data quality dimensions and their detection methods
- [ ] Review all eight exam tips
- [ ] Review official CompTIA Data+ objectives at comptia.org
- [ ] Review Professor Messer's free study materials at professormesser.com
- [ ] Complete Lab 02
- [ ] Complete Quiz 02

---


---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Reading Guide — Module 02: Data Collection and Data Sources** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Reading Guide — Module 02: Data Collection and Data Sources**, we decompose the execution lifecycle into sequential, verifiable stages:

```
[Phase 1: Ingestion & Validation] ──> [Phase 2: State Transformation] ──> [Phase 3: Verification & Persistence]
       │                                       │                                       │
       ▼                                       ▼                                       ▼
Input Sanitization, Schema              Algorithmic Execution,                  Cryptographic Hashing,
Validation & Boundary Checks             Concurrency Arbitration                 Write-Ahead Logging & Audit
```

1. **Ingestion & Boundary Verification:** Inputs entering the boundary of this architecture must undergo strict structural validation. In software systems, this prevents buffer overflows, injection vectors, and malformed state propagation. In enterprise and governance systems, this ensures data integrity before ledger entry.
2. **State Transformation & Concurrency Arbitration:** During execution, intermediate states must maintain transactional isolation. Whether managing distributed lock managers (DLM), thread synchronization, or multi-area routing convergence, race conditions must be mathematically eliminated using provable synchronization primitives.
3. **Commit, Persistence, and Telemetry:** Once state transitions execute successfully, atomic commits guarantee persistence across non-volatile memory or distributed journals. Comprehensive telemetry events are simultaneously emitted to structured observability pipelines.

---

## 4. Real-World Engineering Scenarios & Failure Mode Analysis

### Case Study: High-Impact Enterprise Failure Mode
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Reading Guide — Module 02: Data Collection and Data Sources**:

* **Incident Context:** During peak quarterly processing, an enterprise infrastructure stack running critical financial or operational workflows experienced cascading timeouts and data corruption.
* **Root Cause Diagnostics:** Technicians misconfigured operational parameters, ignoring queue saturation thresholds and bypassing circuit-breaker protections. When transient latency occurred on upstream dependencies, worker threads blocked indefinitely, leading to resource starvation, memory exhaustion, and silent data drops.
* **Remediation Architecture:**
  * Implemented an exponential backoff retry policy coupled with full jitter to eliminate thundering herd phenomena.
  * Deployed strict isolation boundaries (bulkheads) to restrict cascading failures to isolated tenant pools.
  * Enforced continuous automated telemetry alarms monitoring p99 latency, queue depth, and error budget exhaustion.

```python
# Production Architectural Invariant: Resilient Execution with Circuit Breaking
import time
import random

class ResilientExecutionGovernor:
    def __init__(self, failure_threshold=5, recovery_timeout=30):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF-OPEN

    def execute_with_guard(self, operation, *args, **kwargs):
        current_time = time.time()
        
        # Check Circuit State
        if self.state == "OPEN":
            if current_time - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF-OPEN"
            else:
                raise RuntimeError("CircuitBreakerOpen: Request rejected to preserve system invariants.")

        try:
            result = operation(*args, **kwargs)
            if self.state == "HALF-OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = current_time
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
            raise e
```

---

## 5. Critical Misconceptions & Certification Exam Traps

In both certification examinations (such as CompTIA, Cisco, AWS, Scrum.org) and doctoral defense committees, specific high-yield traps consistently cause students to fail. Review these critical distinctions:

| Common Student Misconception | Architectural Reality & Truth | Consequence of Misunderstanding |
|---|---|---|
| *"More resources or threads linearly scale performance."* | Amdahl's Law proves speedup is strictly capped by the sequential fraction of the task; thread contention adds lock overhead. | Costly infrastructure overprovisioning with degraded throughput. |
| *"Redundancy alone guarantees high availability."* | Unmonitored redundancy creates hidden common-mode failure points and split-brain states without quorum arbitration. | Catastrophic double-outages and corrupted ledger state. |
| *"Default vendor configurations are production-ready."* | Vendor defaults prioritize ease of setup over least privilege, hardened encryption, and tuned memory limits. | Severe security vulnerability exposure and predictable resource exhaustion. |
| *"Fast recovery is a substitute for data integrity."* | Recovering quickly with inconsistent or unverified state compounds operational damage beyond the initial downtime. | Long-term ledger corruption and regulatory audit failure. |

---

## 6. Formative Knowledge Synthesis & Applied Defense Prompts

To confirm mastery before proceeding to this module's laboratory exercises and synthesis quizzes, synthesize responses to the following peer-review prompts:

### Mastery Check 1: Invariant Analysis
> **Question:** In the context of **Reading Guide — Module 02: Data Collection and Data Sources**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**


## Additional Resources

- Official exam objectives: comptia.org (search "Data+ DA0-001 exam objectives")
- Professor Messer's free study guides: professormesser.com

## 9. Supplemental Resources

**1. Mode Analytics SQL Tutorial — Intermediate SQL**
<https://mode.com/sql-tutorial/introduction-to-sql>
A free, browser-based SQL course covering JOINs, GROUP BY, HAVING, and subqueries with real datasets. Directly reinforces the relational database and ETL concepts in this module.

**2. dbt (data build tool) — What is ELT? (Official Documentation)**
<https://docs.getdbt.com/terms/elt>
The team behind the most widely used ELT transformation tool explains the ELT pattern, its advantages over ETL, and when to use each. Practical and concise.

**3. Kimball Group — Star Schema in Depth**
<https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/>
Ralph Kimball's dimensional modeling techniques are the industry standard for data warehouse design. This page covers star schema, snowflake schema, fact tables, and dimension tables with authoritative depth.
