# Video Script: Module 09 — Security Monitoring, Metrics, and Reporting

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## CISM Domain Alignment: Domain 3 — Information Security Program

---

## Production Notes

[INSTRUCTOR: Deliver at a measured pace. Pause at each [PAUSE] marker for 2–3 seconds. Advance slides at each [SHOW SLIDE] marker. Display diagrams at each [SHOW DIAGRAM] marker.]

---

## Opening — Welcome and Context (Minutes 0–2)

Welcome back to CIS-4315, Cyber Governance, Risk, and Compliance. I am Professor Nash, and today we are covering Module 9: Security Monitoring, Metrics, and Reporting.

[SHOW SLIDE: Module 9 Title Card]

Think about this for a moment. A Chief Information Security Officer walks into a board meeting. The CFO asks: "Are we more secure this quarter than last quarter?" If the CISO cannot answer that question with data, there is a fundamental problem — not just with communication, but with the security program itself.

[PAUSE]

That question — "How do we know if we are secure?" — is the engine behind everything we cover today. Security monitoring answers that question in real time. Metrics give it a quantitative language. Reporting translates that language for the audiences who need to act on it.

[SHOW SLIDE: Learning Objectives]

By the end of this module, you will be able to:

- Distinguish between Key Performance Indicators and Key Risk Indicators and explain their roles in a security program.

- Describe how SIEM systems collect, correlate, and alert on security event data.

- Design a metrics dashboard appropriate for both technical and executive audiences.

- Explain the principles of log management and the requirements for forensically sound log retention.

- Structure an executive security report that aligns to business objectives.

[PAUSE]

Let us get started.

---

## Part 1 — Security Metrics: KPIs and KRIs (Minutes 2–8)

[SHOW SLIDE: What Gets Measured Gets Managed]

The first principle of security metrics is a management classic: what gets measured gets managed. But in security, we add a corollary — what gets measured incorrectly gets mismanaged.

[PAUSE]

Security metrics fall into two broad families. The first is the **Key Performance Indicator**, or KPI. KPIs tell you how well your security controls and processes are performing. The second is the **Key Risk Indicator**, or KRI. KRIs tell you whether your risk exposure is trending in a dangerous direction.

[SHOW SLIDE: KPI vs. KRI Comparison Table]

Let me give you concrete examples of each.

A KPI might be: "Percentage of vulnerabilities remediated within the SLA." If your SLA says critical vulnerabilities must be patched within 72 hours, and you patched 94 percent of them on time this month, that is a KPI reading 94 percent.

A KRI might be: "Number of unpatched critical vulnerabilities older than 30 days." If that number is climbing month over month, it is a leading indicator that your risk exposure is increasing even if your patching rate looks acceptable.

[PAUSE]

Notice the distinction. KPIs look backward — they tell you what happened. KRIs look forward — they signal what might happen. Both are essential. A mature security program needs both lenses.

[SHOW SLIDE: Qualities of a Good Security Metric]

ISACA's CISM framework and NIST SP 800-55 both provide guidance on what makes a metric useful. A good security metric must be:

- **Measurable** — You can collect the data consistently.

- **Actionable** — A change in the metric triggers a response.

- **Relevant** — The metric connects to a business objective or a named risk.

- **Comparable** — You can benchmark it against your own history or industry peers.

- **Cost-effective** — The effort to collect and report the metric is proportional to its value.

[PAUSE]

A metric that fails any of these tests is called a **vanity metric** — it looks impressive but drives no decision. A classic vanity metric is "total number of firewall blocks per day." Firewalls block millions of packets. The raw count tells you nothing about whether those blocks represent a real threat or routine noise.

[SHOW DIAGRAM: Metrics Hierarchy — Strategic, Tactical, Operational]

Good metrics programs are layered. At the operational level, technical teams track metrics like patch latency, alert volume, and mean time to detect. At the tactical level, security managers track program metrics like training completion rates and audit findings closure. At the strategic level, executives see metrics like cost per incident, risk reduction trend, and regulatory compliance posture.

[PAUSE]

Each layer feeds the one above it. The CISM-aligned security manager must be fluent in all three layers and able to translate between them.

---

## Part 2 — Security Dashboards (Minutes 8–12)

[SHOW SLIDE: The Purpose of a Security Dashboard]

A security dashboard is a visual tool that presents the current state of your metrics in a format designed for a specific audience. The critical word there is "specific audience." A dashboard built for a SOC analyst looks nothing like a dashboard built for a board of directors, and neither should it.

[PAUSE]

Let us walk through the architecture of an effective security dashboard.

[SHOW DIAGRAM: Three-Layer Dashboard Model]

The first layer is the **status layer**. This gives you RAG status — Red, Amber, Green — across your major control domains: network security, endpoint protection, identity and access management, data protection, and so on. A glance at this layer tells leadership whether anything is critically out of bounds.

The second layer is the **trend layer**. Metrics without trend context are nearly meaningless. A patching rate of 87 percent sounds mediocre, but if it was 61 percent three months ago, it tells a story of improvement. Every metric in a mature dashboard should display trend direction.

[PAUSE]

The third layer is the **drill-down layer**. For each status indicator, there should be a pathway to supporting detail. If network security shows Red, the analyst needs to quickly access the underlying data — which controls failed, which assets are affected, what the timeline is.

[SHOW SLIDE: Dashboard Design Principles]

Dashboard design for security follows several key principles drawn from data visualization research and security operations best practice.

First, limit primary metrics. Cognitive science tells us that humans can track approximately seven items simultaneously before information overload occurs. Your primary dashboard view should show no more than seven to ten key metrics.

Second, use progressive disclosure. Summary cards link to detail views. A board-level dashboard should never show raw log data. A SOC dashboard should never bury the critical alert count five clicks deep.

[PAUSE]

Third, align metrics to the audience's decision rights. A board member cannot order a patch. A board member can approve emergency budget for a breach response. Build your executive dashboard around decisions they can actually make.

Fourth, include context. A metric shown without a target, a threshold, or a historical baseline is an incomplete communication. Always anchor numbers to something meaningful.

[SHOW SLIDE: Executive Dashboard vs. Operational Dashboard]

Let me contrast these two dashboard types explicitly.

An **executive security dashboard** typically shows four to six metrics: overall security posture score, regulatory compliance status, open high and critical risk items, incident trend, security investment ROI, and threat landscape summary.

An **operational security dashboard** typically shows real-time alert volume, open incidents by severity, SIEM event rate, endpoint compliance percentage, failed authentication attempts, and vulnerability scan coverage.

[PAUSE]

A common mistake is presenting the operational dashboard to executives. Data overload causes executives to disengage or to ask irrelevant tactical questions in a governance forum. Always build audience-appropriate views.

---

## Part 3 — SIEM Systems and Log Management (Minutes 12–18)

[SHOW SLIDE: What Is a SIEM?]

SIEM stands for Security Information and Event Management. It is one of the most important tools in a modern security monitoring program. Let us break down what it does and why it matters.

[PAUSE]

A SIEM performs two core functions, which correspond to its two-word name. **Security Information Management** is the collection, normalization, storage, and analysis of log and event data from across the enterprise. **Security Event Management** is the real-time correlation of events to detect patterns that indicate a security incident.

[SHOW DIAGRAM: SIEM Data Flow — Sources to Alerts]

Think about all the sources of security-relevant data in a typical organization: firewalls, intrusion detection systems, endpoint detection and response agents, Active Directory, DNS servers, web proxies, cloud access security brokers, application logs, and physical access control systems.

Without a SIEM, a human analyst would need to manually correlate events across dozens of separate consoles. A SIEM ingests all of those sources, normalizes them into a common format, and applies correlation rules to surface meaningful alerts.

[PAUSE]

Here is a classic example of why correlation matters. A single failed login attempt on a Monday morning is noise. One hundred failed login attempts across fifty different accounts over a five-minute window on a Sunday night is a brute-force attack in progress. A human analyst watching only one log source might miss this entirely. A SIEM with a properly tuned correlation rule fires an alert within seconds.

[SHOW SLIDE: Key SIEM Capabilities]

Let us walk through the key capabilities that a security manager should understand when evaluating or operating a SIEM.

**Log Aggregation** — The SIEM collects logs from all sources, often using agents installed on endpoints and servers, or via syslog forwarding from network devices.

**Normalization** — Raw logs arrive in dozens of different formats. The SIEM parses and maps them into a common schema so that correlation rules can operate consistently.

[PAUSE]

**Correlation Rules** — These are the engine of threat detection. Rules define patterns that, when matched, generate an alert. Examples include: multiple authentication failures followed by a successful login, outbound traffic to a known malicious IP, or privilege escalation within five minutes of a new user account creation.

**Alerting and Ticketing** — When a correlation rule fires, the SIEM creates an alert. Most enterprise SIEMs integrate with IT service management platforms to automatically create incident tickets.

**Dashboards and Reporting** — SIEMs provide their own visualization layer for SOC teams and produce scheduled reports for management.

[SHOW SLIDE: Log Management Principles]

Log management is the foundation on which SIEM sits. Without comprehensive, reliable log data, SIEM correlation is blind.

[PAUSE]

The core principles of log management come from NIST SP 800-92, Guide to Computer Security Log Management. Let us walk through them.

**Log Generation** — Every security-relevant system must generate logs. This seems obvious, but many organizations discover during a forensic investigation that a critical system had logging disabled or was generating logs that were never collected.

**Log Collection and Transmission** — Logs must be transmitted from source to the SIEM or log repository in a timely and secure manner. Delayed or corrupted log transmission breaks the real-time detection capability.

[PAUSE]

**Log Storage and Retention** — How long you keep logs matters enormously. Regulatory requirements vary. PCI-DSS requires one year of log retention with three months immediately available. HIPAA requires a six-year retention period for audit logs. GDPR adds a wrinkle by requiring that you minimize data retention — but security logs are generally carved out as a legitimate interest.

**Log Protection** — Logs are a target for attackers. A sophisticated adversary will attempt to clear or modify logs to cover their tracks. Logs must be stored in a write-once or tamper-evident manner, ideally on infrastructure separate from the systems being logged.

[SHOW SLIDE: Log Management Challenges]

Real-world log management faces several persistent challenges that a CISM-aligned manager needs to anticipate.

First, **log volume**. A medium-sized enterprise can generate hundreds of gigabytes of log data per day. Storage and processing costs are significant. This creates pressure to reduce what you log, which reduces visibility.

Second, **alert fatigue**. Poorly tuned SIEM correlation rules generate enormous volumes of false positive alerts. Security analysts who spend their days chasing false positives become desensitized and begin missing real incidents. Tuning SIEM rules is an ongoing, critical operational task.

[PAUSE]

Third, **cloud and hybrid environments**. Cloud platforms generate logs in proprietary formats through their own native logging services. Integrating AWS CloudTrail, Azure Monitor, and GCP Cloud Logging into a centralized SIEM requires deliberate architecture work.

Fourth, **encrypted traffic**. As more enterprise traffic moves to TLS encryption, the traditional network log visibility decreases. Organizations must deploy SSL inspection or rely more heavily on endpoint-based telemetry.

---

## Part 4 — Executive Reporting (Minutes 18–22)

[SHOW SLIDE: The Art of the Security Report]

Security reporting to executive leadership is a discipline unto itself. Technical accuracy is necessary but not sufficient. The security manager must translate complex technical findings into business-relevant narratives that drive decision-making.

[PAUSE]

The most important principle of executive security reporting is this: lead with business impact, not technical detail. An executive does not need to know that 14 CVEs were identified in the quarterly vulnerability scan. The executive needs to know that three of those CVEs exist on systems that process payment card data, that exploitation could result in a regulatory fine of up to 4 percent of global revenue, and that remediation will require 40 hours of engineering time.

[SHOW SLIDE: Structure of an Executive Security Report]

A well-structured executive security report typically contains four sections.

Section one is the **Executive Summary**. Two to three paragraphs maximum. Current security posture, most significant developments since the last report, and a clear bottom-line assessment: are we improving, steady, or declining?

Section two is the **Metrics Scorecard**. A visual table showing five to eight core metrics, each with current value, target, trend direction, and RAG status. This section should be scannable in under sixty seconds.

[PAUSE]

Section three is the **Risk Register Summary**. The top five to ten open risks, each with a brief description, current risk rating, and remediation status. Focus on risks where management action is needed.

Section four is the **Program Highlights and Actions Required**. Achievements since the last report, upcoming initiatives, and explicit asks from leadership — budget approvals, policy decisions, staffing authorizations.

[SHOW SLIDE: Common Executive Reporting Mistakes]

Let me flag the most common mistakes security managers make in executive reporting.

Using undefined acronyms. If your executive audience does not live in the security world, terms like CVE, EDR, or C2 are meaningless without definition.

[PAUSE]

Presenting activity as progress. "We reviewed 4,200 logs this month" is not a security achievement. What were the outcomes?

Burying the lead. The most important information must appear first. Do not save your critical risk finding for page seven.

Failing to quantify risk in financial terms. Boards think in dollars and regulatory exposure. Frame risk accordingly.

[SHOW SLIDE: CISM Exam Connection]

Before we close, let me draw the CISM exam connections for this module.

CISM Domain 3 covers Information Security Program Management. Metrics and reporting are explicitly tested. Expect questions on:

- The difference between KPIs and KRIs.

- The role of SIEM in an information security program.

- Characteristics of effective security metrics.

- Appropriate reporting frequency and format for different audiences.

- Log retention requirements in regulatory contexts.

[PAUSE]

---

## Summary (Minutes 22–24)

[SHOW SLIDE: Module 9 Summary]

Let us bring it together.

Security monitoring is the ongoing process of collecting and analyzing security data to detect threats and assess program effectiveness. Effective monitoring requires comprehensive, reliable log data and a SIEM system capable of correlating that data into actionable intelligence.

[PAUSE]

Metrics are the language of security governance. KPIs measure performance. KRIs measure risk trajectory. Both are needed. Good metrics are measurable, actionable, relevant, comparable, and cost-effective. Vanity metrics that satisfy none of these criteria should be ruthlessly eliminated.

Dashboards present metrics visually and must be audience-appropriate. Executive dashboards surface business-level indicators. Operational dashboards enable SOC team decision-making. Both use trend context and progressive disclosure.

[PAUSE]

Executive reporting translates technical security data into business language. Lead with business impact. Quantify risk in financial terms. Structure reports for a sixty-second scan.

[SHOW SLIDE: Looking Ahead — Module 10]

In Module 10, we shift from ongoing monitoring to crisis response. We will build an Incident Response Plan from the ground up, drawing on NIST SP 800-61 and CISM Domain 4 — Incident Management. The skills from today's module — knowing your metrics, understanding your SIEM, and communicating clearly to leadership — all feed directly into effective incident response.

See you in Module 10.

[END OF SCRIPT]

---

## Appendix: Slide and Diagram List

1. Module 9 Title Card
2. Learning Objectives
3. KPI vs. KRI Comparison Table
4. Qualities of a Good Security Metric
5. Metrics Hierarchy — Strategic, Tactical, Operational (Diagram)
6. The Purpose of a Security Dashboard
7. Three-Layer Dashboard Model (Diagram)
8. Dashboard Design Principles
9. Executive Dashboard vs. Operational Dashboard
10. What Is a SIEM?
11. SIEM Data Flow — Sources to Alerts (Diagram)
12. Key SIEM Capabilities
13. Log Management Principles
14. Log Management Challenges
15. The Art of the Security Report
16. Structure of an Executive Security Report
17. Common Executive Reporting Mistakes
18. CISM Exam Connection
19. Module 9 Summary
20. Looking Ahead — Module 10
