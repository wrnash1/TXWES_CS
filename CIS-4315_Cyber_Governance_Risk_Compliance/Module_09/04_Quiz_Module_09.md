# Quiz: Module 09 — Security Monitoring, Metrics, and Reporting

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 3 — Information Security Program

---

## Instructions

This quiz contains 10 multiple-choice questions. Each question has exactly four answer options. Select the single best answer for each question. Each question is worth 10 points for a total of 100 points.

These questions are written in the CISM exam style. Read each question carefully and identify what is specifically being asked before reviewing the options.

---

## Question 1

A security manager is designing a metrics program for a large healthcare organization. Which of the following BEST describes the primary purpose of a Key Risk Indicator (KRI)?

A. To measure how efficiently the security team patches vulnerabilities each month.

B. To provide a forward-looking signal that risk exposure is trending in a dangerous direction.

C. To document the number of security incidents that occurred during the reporting period.

D. To report the total number of security controls tested during the most recent audit.

### Answer and Analysis — Question 1

**Correct Answer: B**

**Why B is correct**: KRIs are leading indicators designed to provide early warning that risk exposure is increasing before an incident occurs. The forward-looking, predictive nature of KRIs is their defining characteristic and the key distinction from KPIs.

**Why A is wrong**: Measuring patch efficiency is a backward-looking performance metric — a KPI, not a KRI. KPIs assess how well a process performed, not where risk is headed.

**Why C is wrong**: Counting incidents that already occurred is a lagging indicator and a KPI. It tells you what happened, not what might happen. KRIs signal emerging risk.

**Why D is wrong**: Reporting audit results is a compliance or program management activity, not a risk trend indicator. This describes a program performance metric, not a risk indicator.

---

## Question 2

According to NIST SP 800-55, which of the following is a criterion for an effective security metric?

A. The metric should be reported to the board of directors at least annually.

B. The metric must be collected using automated tools rather than manual processes.

C. A change in the metric value should trigger a defined organizational response.

D. The metric must originate from a system that is within scope for a regulatory audit.

### Answer and Analysis — Question 2

**Correct Answer: C**

**Why C is correct**: NIST SP 800-55 defines "actionable" as a key criterion — an effective metric must be one that, when its value changes, causes a defined organizational response. Without actionability, a metric serves no practical purpose.

**Why A is wrong**: NIST SP 800-55 does not specify board reporting frequency as a criterion for metric validity. Reporting frequency is an organizational governance decision, not a metric quality criterion.

**Why B is wrong**: NIST SP 800-55 does not require automation. Manual metrics can be valid if they meet the five criteria. The requirement is consistency of collection, not method of collection.

**Why D is wrong**: Regulatory scope is not a NIST SP 800-55 criterion. Metrics should be relevant to business objectives and named risks, which may or may not align with regulatory scope.

---

## Question 3

A security operations center receives an average of 3,400 alerts per day from its SIEM. Analysts are closing alerts without investigation to keep pace with volume. Which of the following is MOST likely the root cause of this situation?

A. The organization has insufficient log retention policies.

B. The SIEM correlation rules are generating excessive false positive alerts.

C. The organization has not deployed an endpoint detection and response platform.

D. The security team does not have access to the SIEM dashboard.

### Answer and Analysis — Question 3

**Correct Answer: B**

**Why B is correct**: The described behavior — analysts dismissing alerts without investigation due to volume — is the classic presentation of alert fatigue, which is caused by poorly tuned SIEM correlation rules generating excessive false positives. This is a well-documented SIEM operations problem.

**Why A is wrong**: Log retention policies govern how long logs are stored, not how many alerts are generated. Inadequate retention would cause gaps in historical data, not overwhelming alert volume.

**Why C is wrong**: Lack of an EDR platform would reduce visibility into endpoint events but would not explain why the organization is receiving 3,400 alerts per day — if anything, it would mean fewer alerts.

**Why D is wrong**: Dashboard access is a user interface issue. Analysts closing alerts without investigation indicates they have access to the system but are overwhelmed by volume.

---

## Question 4

A CISO is preparing the quarterly security report for the board of directors. Which of the following content approaches is MOST appropriate for this audience?

A. Detailed technical analysis of all vulnerabilities discovered during the quarter.

B. A complete list of SIEM correlation rules and their detection rates.

C. Security posture summary, top risk items, compliance status, and explicit decisions required from the board.

D. Raw log statistics showing total event volume processed by the SIEM.

### Answer and Analysis — Question 4

**Correct Answer: C**

**Why C is correct**: Board-level reporting must present information in business terms that enable governance decisions. Security posture summary, risk items, compliance status, and explicit asks align precisely with what a board needs to fulfill its oversight responsibilities.

**Why A is wrong**: Detailed vulnerability technical analysis is operational detail appropriate for security teams and audit committees, not for the full board. Presenting this level of detail in a board report indicates poor communication judgment.

**Why B is wrong**: SIEM correlation rule details are deeply technical operational information. Board members have no decision-making role over specific SIEM rules.

**Why D is wrong**: Raw log statistics are a vanity metric. Total event volume processed tells the board nothing about security outcomes, risk posture, or program effectiveness.

---

## Question 5

An information security manager wants to ensure that logs from the organization's cardholder data environment are available for forensic investigation of any incident occurring up to nine months ago. Which regulatory standard's log retention requirement is MOST directly applicable?

A. HIPAA Security Rule

B. SOX Section 404

C. PCI-DSS

D. GDPR Article 5

### Answer and Analysis — Question 5

**Correct Answer: C**

**Why C is correct**: PCI-DSS v4.0 requires a minimum of 12 months of log retention with at least 3 months immediately available for analysis. The scenario involves a cardholder data environment, making PCI-DSS the directly applicable standard. Nine months of availability satisfies both the 3-month minimum online requirement and falls within the 12-month total retention window.

**Why A is wrong**: HIPAA applies to protected health information, not cardholder data. HIPAA requires 6 years of audit log retention, which is a longer period, but HIPAA is not the standard governing cardholder data environments.

**Why B is wrong**: SOX Section 404 applies to financial reporting controls and requires 7-year record retention, but it is not the standard governing cardholder data security monitoring logs.

**Why D is wrong**: GDPR Article 5 establishes data minimization and storage limitation principles. While GDPR affects European personal data, it does not specify log retention minimums and is not the primary standard for cardholder data environment monitoring.

---

## Question 6

An organization's security dashboard shows a critical vulnerability patching rate of 91%, which appears healthy. However, the number of critical vulnerabilities outstanding for more than 30 days has increased from 4 to 22 over the past quarter. Which of the following BEST explains this apparent contradiction?

A. The organization's vulnerability scanning tool is producing false positive results.

B. The patching rate KPI masks a growing backlog of unresolved critical vulnerabilities identified by the KRI.

C. The dashboard is displaying data from the wrong reporting period.

D. The organization has too many security tools deployed, causing data conflicts.

### Answer and Analysis — Question 6

**Correct Answer: B**

**Why B is correct**: This scenario illustrates exactly why both KPIs and KRIs are needed. The KPI (patching rate 91%) looks acceptable but does not capture accumulation. The KRI (vulnerabilities over 30 days: 22 and rising) reveals that the organization is consistently failing to address a growing subset of critical vulnerabilities. The KPI measures throughput; the KRI measures backlog and risk exposure.

**Why A is wrong**: Nothing in the scenario suggests false positives. The scenario describes a logical pattern consistent with process performance, not a scanning tool failure.

**Why C is wrong**: The data contradiction is internally consistent and described as a trend over one quarter. A reporting period error would likely produce obviously incorrect values, not a coherent story of a growing backlog.

**Why D is wrong**: The number of tools deployed is unrelated to the relationship between a patching rate KPI and a backlog KRI. Tool proliferation does not cause this type of metric contradiction.

---

## Question 7

Which of the following is the MOST accurate description of the normalization function in a SIEM platform?

A. Converting log retention periods to comply with applicable regulatory requirements.

B. Parsing log data from various sources into a common schema to enable cross-source correlation.

C. Removing duplicate log entries to reduce storage consumption.

D. Encrypting log data in transit between source systems and the SIEM.

### Answer and Analysis — Question 7

**Correct Answer: B**

**Why B is correct**: SIEM normalization is the process of parsing raw log data from diverse sources — each with its own format, field names, and timestamp conventions — and mapping it to a standardized schema. Without normalization, correlation rules cannot operate consistently across multiple data sources.

**Why A is wrong**: Adjusting retention periods to meet regulatory requirements is a log management policy function, not a SIEM normalization function. Normalization addresses format consistency, not retention duration.

**Why C is wrong**: Deduplication is a separate optimization function. Normalization specifically addresses format and schema inconsistencies, not duplicate record reduction.

**Why D is wrong**: Encrypting logs in transit is a log protection and transmission security control governed by network security policy. It is separate from the normalization process, which addresses data format and schema.

---

## Question 8

A security manager wants to protect audit logs from tampering by insiders who have administrative access to the systems being logged. Which of the following controls BEST addresses this threat?

A. Encrypting the logs at rest using AES-256.

B. Storing logs on a separate, dedicated log management infrastructure with access controlled independently from operational systems.

C. Requiring dual-factor authentication to access the SIEM console.

D. Configuring the SIEM to generate alerts when log volume drops below threshold.

### Answer and Analysis — Question 8

**Correct Answer: B**

**Why B is correct**: The threat is insider tampering by administrators who control the logged systems. Storing logs on a separate, independently-controlled infrastructure ensures that even a full compromise of an operational system does not give the attacker the ability to modify or delete the logs of that compromise. Separation of control is the key control.

**Why A is wrong**: Encrypting logs at rest protects confidentiality, not integrity against authorized users. An administrator with access to the encryption keys can still tamper with logs if they have access to the storage.

**Why C is wrong**: MFA on the SIEM console addresses unauthorized access but does not protect against insiders who already have legitimate SIEM credentials or who tamper with logs before they reach the SIEM.

**Why D is wrong**: Volume threshold alerting is a useful detective control that may detect log deletion attempts, but it is not the primary protective control. Prevention (separation of infrastructure) is stronger than detection alone.

---

## Question 9

An executive dashboard shows a "security posture score" of 72 out of 100 for the current quarter. Without any additional context, this number is LEAST useful for which of the following reasons?

A. The score does not include all security domains.

B. There is no target score, historical trend, or baseline against which to interpret 72.

C. The score should be reported in percentage format rather than a numeric score.

D. The dashboard should only display metrics that are Red or Amber status.

### Answer and Analysis — Question 9

**Correct Answer: B**

**Why B is correct**: A metric value without a target, threshold, or historical baseline is inherently uninterpretable. Is 72 excellent, acceptable, or alarming? Without knowing the target score, the prior quarter's score, or the industry benchmark, the number conveys no actionable information. This is a fundamental dashboard design principle.

**Why A is wrong**: The completeness of domain coverage is a separate concern. Even a score covering all domains would be uninterpretable without a reference point. The question asks for the LEAST useful reason in the absence of additional context.

**Why C is wrong**: Numeric scores and percentage scores are mathematically equivalent representations. The format is not the source of interpretive difficulty. The problem is absence of comparative context.

**Why D is wrong**: Restricting a dashboard to only Red and Amber items would eliminate Green status visibility and prevent monitoring of improvement. This does not address the interpretability problem.

---

## Question 10

A security manager is designing a SIEM correlation rule to detect potential account compromise. The rule fires when there are five or more failed authentication attempts from a single account followed by a successful login within a 10-minute window. Which of the following changes would BEST reduce false positive alerts from this rule?

A. Increase the failed attempt threshold from 5 to 50 before triggering an alert.

B. Add a condition requiring the successful login to originate from a different IP address or geographic location than the failed attempts.

C. Remove the successful login condition and alert on failed attempts only.

D. Reduce the time window from 10 minutes to 1 minute.

### Answer and Analysis — Question 10

**Correct Answer: B**

**Why B is correct**: Adding a geographic or IP location change condition dramatically improves rule precision. A user who mistypes their password five times and then logs in successfully from the same device is likely not compromised. The same pattern from a different country is a strong compromise indicator. This condition increases specificity without eliminating true positive detection.

**Why A is wrong**: Raising the threshold to 50 failed attempts would drastically reduce sensitivity, allowing most brute-force attempts to go undetected. An attacker using slow-and-low techniques might never reach 50 attempts. This sacrifices too much detection capability to reduce false positives.

**Why C is wrong**: Removing the successful login condition makes the rule fire on any five failed attempts, which would dramatically increase false positive volume. Legitimate users routinely make authentication errors.

**Why D is wrong**: Reducing the time window to 1 minute would cause the rule to miss slower, deliberate brute-force attacks that spread attempts over several minutes to evade detection. This change reduces coverage rather than improving precision.

---

## End of Quiz

**Total: 10 questions | 100 points**

Review your answers using the distractor analysis provided. For any question you answered incorrectly, revisit the corresponding section in the Module 9 Reading Guide before proceeding to the lab.
