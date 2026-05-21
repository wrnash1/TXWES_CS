# Reading Guide: Module 15 - ERP Post-Implementation

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Introduction

Welcome to **Module 15 - ERP Post-Implementation**! Going live on an ERP system is not the end of the project — it is the beginning of a long-term operational and improvement cycle. Post-implementation activities determine whether the investment delivers its promised business value, whether users adopt the system effectively, and whether the platform stays healthy as the business evolves.

This module covers the hypercare stabilization period immediately after go-live, user adoption measurement, ongoing performance reviews, defect management, and the module upgrade lifecycle that keeps the ERP current over years of operation.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **User adoption tracking**: The measurement of how thoroughly and correctly employees are using the new ERP system after go-live. Metrics include login frequency, transaction completion rates, manual workaround detection, and user satisfaction survey scores. Low adoption is the most common indicator that change management was insufficient.
* **System performance reviews**: Regularly scheduled technical assessments that examine database growth trends, query response times, background job runtimes, and hardware utilization to ensure the system continues to meet performance SLAs as transaction volume grows over time.
* **Bug databases**: Defect tracking systems (e.g., Jira, ServiceNow) used to log, prioritize, assign, and track to closure the issues discovered after go-live — ranging from minor UI inconsistencies to critical calculation errors. A well-managed bug database provides transparency to stakeholders on the post-go-live health of the system.
* **Upgrading modules**: The process of applying vendor-delivered enhancements, patches, and new feature releases to the production ERP system. In on-premise SAP, module upgrades require a full project cycle (testing, change management, cutover); in SaaS Salesforce, major releases are applied automatically three times per year.

---

### 2. Certification Exam Tips

* **Hypercare period:** The 30–90 day period immediately after go-live when the full implementation team remains available to resolve critical issues quickly. Hypercare ends when the system is stable and the support model transitions to the normal run organization (BASIS team, functional support team, or managed service provider).
* **KPIs for ERP success:** Common post-implementation KPIs include: reduction in month-end close time, decrease in inventory stockout frequency, improvement in on-time delivery rate, and reduction in payroll processing errors. Exam questions may ask what metrics indicate whether an ERP implementation delivered value.
* **Salesforce release management:** For Salesforce admins, post-implementation best practices include: reviewing Salesforce's Release Notes before each seasonal update, testing in a sandbox before the production release, enabling/disabling new features through critical updates, and monitoring the Health Check score for security configuration quality.
* **Support tiers:** Post-go-live ERP support is typically organized in three tiers: Tier 1 (help desk — password resets, navigation help), Tier 2 (functional support — configuration questions, minor fixes), Tier 3 (technical escalation — ABAP bugs, infrastructure issues, major defects requiring development).
* **Study Resource:** Complete the Salesforce Trailhead module [Salesforce Optimizer](https://trailhead.salesforce.com/content/learn/modules/salesforce-optimizer) — a free module covering the tools Salesforce provides for ongoing org health monitoring and performance optimization.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Complete the Salesforce Trailhead module [Salesforce Optimizer](https://trailhead.salesforce.com/content/learn/modules/salesforce-optimizer) — a free module covering the Optimizer tool and Health Check features that administrators use for post-implementation monitoring and improvement.
* **Required Video:** Watch the video lecture on **ERP Post-Implementation** in the official course playlist: [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Draft user satisfaction survey templates**: Create a 10-question post-go-live survey covering system ease of use, training adequacy, help desk responsiveness, and whether the system meets the user's daily work needs. Include Likert scale questions and one open-ended feedback question.
* **Analyze system performance query logs**: Given a sample set of SAP or Salesforce performance metrics (login counts, page load times, slow report runtimes), identify two areas of concern and recommend one action for each based on the data.
* **Write bug ticket triage outlines**: Define a severity classification scheme (Critical, High, Medium, Low) for post-go-live defects, providing criteria for each level and a target resolution time. Then classify five sample bug descriptions into the appropriate severity level.

---

### 3. Study Checklist

* [ ] Read all glossary definitions and be able to explain what happens in the hypercare period and when it ends.
* [ ] Complete [Salesforce Optimizer](https://trailhead.salesforce.com/content/learn/modules/salesforce-optimizer) on Trailhead (earn the badge).
* [ ] Watch the video lecture on **ERP Post-Implementation** in [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).
* [ ] Complete the lab survey design, performance log analysis, and bug severity classification exercises.
* [ ] Proceed to the weekly quiz.
