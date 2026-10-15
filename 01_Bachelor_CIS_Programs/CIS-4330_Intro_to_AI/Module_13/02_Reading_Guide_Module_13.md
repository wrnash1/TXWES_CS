# Reading Guide: Module 13 — Data Preparation and Feature Engineering

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Microsoft Learn / Stanford Online &bull; CIS-4330 Module 13</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLhQjrBD2T382Nz7z1AEXmioc27axa19Kv" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLhQjrBD2T382Nz7z1AEXmioc27axa19Kv" title="Artificial Intelligence Foundations & Machine Learning Principles" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Artificial Intelligence Foundations & Machine Learning Principles</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe machine learning concepts (20-25%)

---

## Overview

This reading guide covers data quality dimensions, data cleaning techniques, feature engineering methods, train-test splitting, data leakage, and Azure ML data preparation tools. These topics appear in AI-900 questions about machine learning pipelines and the conditions required for successful model training. Estimated reading time: 50–65 minutes.

---

## Section 1: Core Vocabulary

**Data preparation** — The process of cleaning, transforming, and structuring raw data into a form suitable for model training. Typically 60–80 percent of total ML project time.

**Feature** — A single measurable input variable used by a model to make predictions. Also called an attribute or predictor variable.

**Feature engineering** — The process of transforming raw data columns into features that express patterns more clearly for a model to learn from.

**Missing value** — A data record where a field contains no value. Strategies: deletion, imputation, or indicator encoding.

**Imputation** — Filling in missing values with a calculated substitute such as the column mean, median, mode, or a forward-filled value.

**Outlier** — A data value that falls far outside the typical range of the feature. May be a genuine rare event, a measurement error, or a data entry mistake.

**Normalization** — Scaling numeric features to a common range (commonly 0 to 1) using min-max scaling: (value minus min) divided by (max minus min).

**Standardization** — Scaling numeric features to have mean zero and standard deviation one using z-score scaling: (value minus mean) divided by standard deviation.

**One-hot encoding** — Creating a separate binary (0/1) column for each category value in a categorical variable. Appropriate for nominal categories with no natural order.

**Label encoding** — Assigning an integer to each category value (e.g., Low=1, Medium=2, High=3). Appropriate for ordinal categories with a natural order.

**Train-test split** — Dividing a labeled dataset into a training portion (used to fit the model) and a test portion (held out for final evaluation).

**Data leakage** — The inadvertent inclusion of information in training data that would not be available at prediction time in production, causing artificially high training performance that does not generalize.

**Cross-validation** — A technique that repeatedly splits the training data into different folds, trains and evaluates on each fold, and averages results to produce a more robust performance estimate.

**Data asset** — An Azure ML concept for registering and versioning a dataset so that training runs are reproducible and traceable to the exact input data used.

**Binning** — Converting a continuous numeric feature into discrete category ranges. Example: converting age values into age bands (18–25, 26–35, etc.).

---

## Section 2: Comparison Tables

### Table 1: Data Quality Dimensions

| Dimension | Definition | ML Impact if Violated | Detection Method |
|---|---|---|---|
| Completeness | All required values are present | Missing values force deletion or imputation; both reduce accuracy | Null count per column |
| Accuracy | Values correctly reflect real-world state | Model learns from incorrect signal; errors in labels corrupt all learning | Manual audit; label agreement checks |
| Representativeness | Training data reflects production distribution | Model performs poorly on segments not seen during training | Distribution comparison: train vs production |
| Relevance | Features are predictive and appropriate | Noise features reduce model clarity; leaked features corrupt evaluation | Feature importance analysis; domain review |

### Table 2: Missing Value Strategies

| Strategy | Method | Best When | Risk |
|---|---|---|---|
| Deletion | Remove records with missing values | Missing values are rare (under 5%); missingness is random | Loses data; may introduce bias if missingness is not random |
| Mean/median imputation | Replace with column mean or median | Numeric features; missingness is random | Distorts feature distribution; reduces variance |
| Mode imputation | Replace with most frequent value | Categorical features | May over-represent one category |
| Forward-fill | Carry the last known value forward | Time series data with sequential records | Inappropriate for non-time-ordered data |
| Indicator encoding | Add binary flag for "was missing"; fill original with placeholder | When missingness itself may be predictive | Adds a feature; doubles the representation of that column |

### Table 3: Feature Encoding Methods

| Method | Use Case | Example | Caution |
|---|---|---|---|
| One-hot encoding | Nominal categorical features (no order) | Color: Red, Blue, Green → IsRed, IsBlue, IsGreen | Creates many columns if cardinality is high |
| Label encoding | Ordinal categorical features (natural order) | Size: Small=1, Medium=2, Large=3 | Implies numeric relationships — inappropriate for nominal |
| Ordinal encoding | Ranked ordinal features | Survey rating: Low=1, Medium=2, High=3 | Same as label encoding for ordered categories |
| Binary encoding | High-cardinality nominal categories | ZIP codes, product IDs | Reduces columns vs one-hot but loses interpretability |

### Table 4: Scaling Methods

| Method | Formula | When to Use | Not Required For |
|---|---|---|---|
| Min-max normalization | (x - min) / (max - min) → range 0 to 1 | Neural networks; k-NN; SVM | Tree-based models (random forest, gradient boosting) |
| Z-score standardization | (x - mean) / std dev → mean 0, std 1 | Linear models; logistic regression; PCA | Tree-based models |
| No scaling | Use raw values | Tree-based models | When features are already comparable scale |

### Table 5: Train-Test Split Strategies

| Strategy | Description | Best For |
|---|---|---|
| Random split | Randomly assign records to train, validation, test | Non-time-ordered data with large sample size |
| Stratified split | Maintain class distribution proportions in each split | Imbalanced datasets where one class is rare |
| Time-based split | Train on earlier dates; test on later dates | Time series and forecasting models |
| K-fold cross-validation | Rotate through k folds; average k evaluation scores | Small datasets where every record is valuable |

### Table 6: Data Leakage Examples

| Leakage Type | Example | Why It Is Leakage |
|---|---|---|
| Target leakage | Including "loan_default_date" in a loan default prediction model | This field is only populated after the outcome occurs |
| Future data leakage | Training churn model with data that includes activity from after the churn event date | Model would not have access to that future activity at prediction time |
| Duplicate leakage | Same customer appears in both train and test splits | Model has already "seen" the test customer |
| Preprocessing leakage | Normalizing all data before splitting; using test set statistics for scaling | Test set statistics contaminate training-time calculations |

---

## Section 3: Feature Engineering Patterns

### Deriving Features from Dates and Timestamps

Raw date columns rarely express the signal a model needs directly. The following derived features are commonly useful:

- Day of week (0–6)
- Hour of day (0–23)
- Month of year (1–12)
- Is weekday / is weekend (binary)
- Is holiday (binary, requires calendar lookup)
- Days since last event (numeric)
- Days until deadline (numeric)

### Deriving Features from Text

When raw text is not the primary input but a text field exists alongside structured data:

- Text length in characters or words
- Presence of specific keywords (binary flags)
- Sentiment score (from Azure AI Language)
- Named entity count

### Interaction Features

Interaction features capture the combined effect of two features that are more predictive together than separately:

- Example: "hour_of_day" and "day_of_week" independently predict purchase likelihood weakly. "hour_of_day x day_of_week" as a combined feature captures "Friday evening" and "Monday morning" patterns more directly.

---

## Section 4: AI-900 Exam Tips

1. Data preparation consumes the majority of ML project time. This is not a sign of a failing project — it is normal. AI-900 may ask about the relative time investment across pipeline phases.

2. Missing value strategies have trade-offs. Deletion is simple but loses data. Imputation preserves records but introduces assumptions. When a scenario describes choosing between these, match the strategy to the scenario conditions (volume of missingness, whether missingness is random).

3. One-hot encoding is for nominal categories (no order); label encoding is for ordinal categories (ranked order). Applying label encoding to nominal categories implies false numerical relationships between categories.

4. Normalization and scaling are not required for tree-based models (random forest, gradient boosting, decision tree). They are required for models that use distance calculations or gradient descent (logistic regression, neural networks, k-NN, SVM). AI-900 scenarios may ask which preprocessing step is unnecessary for a given model type.

5. Data leakage produces a model that appears highly accurate during training and evaluation but performs poorly in production. If a scenario describes this gap between development performance and production performance, the answer likely involves data leakage.

6. Train-test split is mandatory for valid model evaluation. Evaluating a model on its own training data measures memorization, not generalization. AI-900 knows the purpose of the test set: to estimate real-world performance on unseen data.

7. Azure ML data assets provide versioning for datasets. Versioned assets ensure that model training is reproducible — you can re-run a training job months later using the exact same data version.

8. Preprocessing must be part of the deployed pipeline. If you normalize training data with statistics computed from training, the same normalization (using the training statistics, not fresh test statistics) must be applied to scoring data at inference time. This is a common source of preprocessing leakage if done incorrectly.

---

## Section 5: Required Reading

**Microsoft Learn — Explore and analyze data with Python:**
learn.microsoft.com/en-us/training/paths/explore-data-science-tools-in-azure/

**Microsoft Learn — Prepare data for machine learning:**
learn.microsoft.com/en-us/training/modules/introduction-to-data-for-machine-learning/

---

## Section 6: Study Checklist

- [ ] Name the four data quality dimensions and explain how each affects model performance.
- [ ] Describe three strategies for handling missing values and when to use each.
- [ ] Explain the difference between one-hot encoding and label encoding with examples.
- [ ] Explain when normalization is required and when it is not.
- [ ] Describe data leakage using a concrete example and explain how it causes production failure.
- [ ] Explain the purpose of the train-test split and why evaluation on training data is invalid.
- [ ] Describe two derived features you could engineer from a raw date column.
- [ ] Explain what a versioned data asset is in Azure ML and why it supports reproducibility.
- [ ] Complete the Module 13 quiz.
- [ ] Complete the Module 13 lab.
- [ ] Post initial discussion by Wednesday 11:59 PM and respond to two peers by Sunday 11:59 PM.

---

## Section 7: Supplemental Resources

**1. scikit-learn User Guide — Preprocessing data**
<https://scikit-learn.org/stable/modules/preprocessing.html>
The official scikit-learn documentation for StandardScaler, MinMaxScaler, OneHotEncoder, and imputation strategies. Provides runnable Python examples for every technique covered in Module 13 and is directly applicable to the lab's feature engineering exercises.

**2. Towards Data Science — A Comprehensive Guide to Data Preprocessing**
<https://towardsdatascience.com/a-comprehensive-guide-to-data-preprocessing-3bfbb4b0c6c7>
A practical walkthrough of handling missing values, encoding categorical variables, scaling, and detecting leakage with pandas and scikit-learn. Bridges the conceptual framework in the reading guide to working code patterns.

**3. Kaggle Learn — Feature Engineering**
<https://www.kaggle.com/learn/feature-engineering>
Kaggle's free micro-course on feature engineering, covering mutual information, creating interaction features, target encoding, and PCA for feature construction. Includes interactive notebooks executable in the browser — no local setup required.

---

End of Reading Guide — Module 13

---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 13 — Data Preparation and Feature Engineering** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 13 — Data Preparation and Feature Engineering**, we decompose the execution lifecycle into sequential, verifiable stages:

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
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 13 — Data Preparation and Feature Engineering**:

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
> **Question:** In the context of **Module 13 — Data Preparation and Feature Engineering**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**

---

## Deep Theoretical Foundations & Conceptual Architecture

### 1. Epistemological Framework & First Principles
To truly master **Data Preparation and Feature Engineering**, students must look beyond simple procedural commands or surface-level tooling. In computational science and enterprise information systems, every applied technology represents an abstraction built upon formal mathematical, physical, or organizational theorems.

```
+---------------------------------------------------------------------------------+
|                    HIERARCHICAL KNOWLEDGE ABSTRACTION MODEL                     |
|                                                                                 |
|  [Tier 4: Enterprise Application] -> Applied Labs, Scripts, CI/CD, Case Studies  |
|         ^                                                                       |
|  [Tier 3: System Architecture]    -> Architectural Invariants, APIs, Protocols  |
|         ^                                                                       |
|  [Tier 2: Algorithmic Logic]      -> Mathematical Models, State Machines, Big-O |
|         ^                                                                       |
|  [Tier 1: Foundational Physics]   -> Silicon Gates, Shannon Entropy, Signals    |
+---------------------------------------------------------------------------------+
```

In this module, our technical focus directly engages **Foundational Artificial Intelligence & Heuristic Search**:
* **Foundational Underpinnings:** State-space graph search algorithms (A*, minimax, alpha-beta pruning), knowledge representation, expert systems, and probabilistic reasoning models.
* **Domain Invariants:** Regardless of software updates, operating system iterations, or cloud vendor tooling, the fundamental mathematical and architectural constraints governing this module remain immutable.

---

### 2. Formal Mechanistic Model & Execution Invariants
Every operational system within this domain executes according to a strict deterministic lifecycle. Understanding this execution pipeline allows engineers and technical leaders to diagnose catastrophic failure modes before they reach production environments.

```
[Phase 1: Input Ingestion & Boundary Verification]
       │
       ▼
[Phase 2: State Transformation & Algorithmic Arbitration]
       │
       ▼
[Phase 3: Formal Verification, Persistence & Telemetry Emission]
```

1. **Boundary Ingestion & Deterministic Validation:**
   - All state transitions entering the system must satisfy preconditions and type safety invariants.
   - Bypassing input validation leads directly to memory corruption, state desynchronization, or security breach vectors.

2. **State Transformation & Mathematical Invariants:**
   - Intermediate transitions must preserve transactional isolation and state consistency.
   - Concurrency, resource contention, and network latency are arbitrated using proven algorithms rather than opportunistic heuristic assumptions.

3. **Atomic Persistence & Telemetry Verification:**
   - Successful execution commits changes atomically to non-volatile persistence layers.
   - Comprehensive telemetry and audit logs provide empirical verification that invariants held throughout the lifecycle.

---

### 3. Quantitative Trade-Offs & Amdahl's Law in Practice
Engineering decisions are never made in a vacuum; they represent conscious optimizations within a multi-dimensional constraint space:

```
Optimization Metric = f(Latency, Throughput, Cost, Resilience, Security)
```

* **Amdahl's Law:** Acceleration through parallelization is strictly bounded by the sequential fraction of the computational task. Adding resources without optimizing critical-path bottlenecks produces diminishing returns.
* **The CAP & PACELC Theorems:** In distributed networks, systems must explicitly choose their consistency, availability, and partition tolerance tradeoffs during transient network failures.
* **Defense-in-Depth vs. Operational Friction:** Security controls must balance protective efficacy against cognitive overhead and processing latency.

---

### 4. Critical Conceptual Misconceptions
Review these high-frequency theoretical traps frequently tested on certification examinations and probed during doctoral defenses:

| Common Misconception | Scientific & Architectural Reality | Consequence of Misunderstanding |
|---|---|---|
| *"Tools and frameworks replace foundational theory."* | Frameworks come and go; underlying data structures and protocols remain constant. | Rapid obsolescence of technical knowledge when tools update. |
| *"More computing power solves architectural latency."* | Inefficient Big-O complexity and unindexed queries scale exponentially with data. | Massive cloud cost overruns and cascading service degradation. |
| *"Default configurations are secure and production-ready."* | Defaults optimize for developer onboarding velocity, not hardened isolation. | Critical vulnerability exposures and compliance audit failures. |
| *"Empirical results alone prove correctness."* | Testing shows the presence of bugs, never their absence without formal verification. | Undetected catastrophic edge-case failures in production. |

---

### 5. Socratic Synthesis & Mastery Defense Prompts
Before proceeding to this module's laboratory exercises, synthesize concise, rigorous responses to the following defense prompts:
1. **First-Principles Invariant Defense:** How does the theoretical model in this module ensure state correctness under adverse operating conditions? What mathematical proof or telemetry metric validates this behavior?
2. **Architectural Trade-Off Analysis:** If forced to reduce execution latency by 50%, what specific compromises in consistency, redundancy, or capital expenditure would your architecture be forced to accept?
3. **Failure Mode Pathology:** Explain the exact mechanistic chain of events that occurs when this module's primary subsystem experiences an unhandled resource starvation condition.
