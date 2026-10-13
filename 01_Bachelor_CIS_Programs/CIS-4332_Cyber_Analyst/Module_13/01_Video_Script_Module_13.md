# Video Script: Module 13 — Compliance and Security Controls Validation

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Slide 1 — Introduction

Welcome to Module 13: Compliance and Security Controls Validation. I am Professor Nash.

In Modules 11 and 12 we focused on incident response and forensics — what happens when something goes wrong. This module focuses on prevention and verification — how analysts confirm that the controls designed to prevent incidents are actually working.

Security controls validation is the process of testing whether implemented controls are functioning as intended and providing the protection they were designed to deliver. Compliance is the process of demonstrating that your security program meets the requirements of relevant frameworks, regulations, and standards.

These are core analyst skills. The CySA+ exam expects you to understand control frameworks, testing methodologies, audit evidence, and gap analysis.

---

## Slide 2 — Why Controls Validation Matters

Security teams deploy firewalls, endpoint protection, MFA, and DLP systems. But deploying a control is not the same as the control working.

Firewalls have misconfigured rules that allow prohibited traffic. MFA deployments have exceptions for legacy systems. DLP policies miss sensitive data categories. Endpoint protection agents fall off systems and never get reinstalled.

Controls drift. They decay. They break. Validation is the discipline that catches the gap between what the organization believes is protected and what is actually protected.

For analysts, this is important because your detection capabilities are themselves controls. If your SIEM logging pipeline breaks, you lose visibility. Controls validation applies to your own tooling just as much as to firewalls and endpoint agents.

---

## Slide 3 — Control Frameworks Overview

A security control framework is a structured set of practices and safeguards designed to manage security risk. Three frameworks dominate the enterprise security landscape.

The NIST Cybersecurity Framework, or CSF, organizes security into five functions: Identify, Protect, Detect, Respond, and Recover. It is outcome-based and flexible, designed to apply across industries and organization sizes.

The CIS Controls, published by the Center for Internet Security, are 18 prioritized controls grouped by implementation group. They are highly prescriptive and provide specific, actionable safeguards.

NIST Special Publication 800-53 provides a comprehensive catalog of security controls used by federal agencies and organizations requiring rigorous control documentation.

---

## Slide 4 — NIST Cybersecurity Framework Deep Dive

The NIST CSF was first published in 2014 and updated in version 2.0 in 2024. It is the most widely adopted security framework in the United States.

The five functions represent concurrent, continuous activities rather than sequential steps.

Identify covers asset management, business environment understanding, governance, risk assessment, and supply chain risk.

Protect covers access control, awareness training, data security, information protection processes, maintenance, and protective technology.

Detect covers anomaly detection, continuous monitoring, and detection processes — this is where most analyst work lives.

Respond covers response planning, communications, analysis, mitigation, and improvements.

Recover covers recovery planning, improvements, and communications.

---

## Slide 5 — CIS Controls Overview

The CIS Controls are organized into three implementation groups representing increasing maturity:

Implementation Group 1 contains the basic hygiene controls that every organization should have, regardless of size or sector. These include inventory of hardware and software, secure configuration, email and web browser protections, malware defenses, and data recovery.

Implementation Group 2 adds controls appropriate for organizations with more resources and more sophisticated threats.

Implementation Group 3 contains advanced controls for organizations with mature security programs facing sophisticated adversaries.

The CIS Controls are particularly useful for gap analysis because they are specific and measurable. Either you have an accurate hardware inventory or you do not.

---

## Slide 6 — Control Testing Methodologies

There are three primary methods for testing security controls.

Examination involves reviewing documentation, configurations, and policies to verify that controls are designed correctly. You read the firewall ruleset and verify it aligns with policy.

Interview involves questioning personnel responsible for controls to verify that procedures are followed. You ask the system administrator whether they review privilege escalation alerts weekly as the policy requires.

Testing involves actively exercising controls to verify they function as intended. You send a simulated phishing email to verify email filtering blocks it. You attempt to access a restricted file share to verify access controls prevent unauthorized access.

The most rigorous validation combines all three methods.

---

## Slide 7 — Control Categories

Controls are categorized by function and type.

By function, controls are preventive (stop bad things from happening), detective (identify when bad things happen), corrective (fix things after they happen), or deterrent (discourage bad behavior).

By type, controls are technical (implemented in systems — firewalls, encryption), administrative (implemented in policies and procedures — access control policies, security awareness training), or physical (implemented in the physical environment — locks, badge readers, surveillance cameras).

For the CySA+ exam, know these categories and be able to classify a given control correctly. Analysts frequently need to identify what type of control is missing when analyzing a security gap.

---

## Slide 8 — Compliance Frameworks and Regulations

In addition to voluntary security frameworks, many organizations must comply with regulatory requirements that mandate specific security controls.

HIPAA (Health Insurance Portability and Accountability Act) applies to healthcare organizations and mandates protection of Protected Health Information (PHI).

PCI DSS (Payment Card Industry Data Security Standard) applies to organizations that process payment card data and requires specific controls around cardholder data protection.

SOX (Sarbanes-Oxley Act) applies to publicly traded companies and requires controls over financial reporting systems.

GDPR (General Data Protection Regulation) applies to organizations handling data of EU residents and requires data protection controls and breach notification.

Analysts working in regulated industries must understand how their security controls map to regulatory requirements.

---

## Slide 9 — Compliance Dashboards

A compliance dashboard provides a real-time or near-real-time view of an organization's compliance posture against a selected framework or regulation.

Compliance dashboards aggregate data from multiple sources: vulnerability scanners, configuration management databases, log management systems, and endpoint management platforms.

Typical dashboard metrics include:

- Percentage of assets with current vulnerability scans
- Percentage of systems meeting baseline configuration standards
- Number and age of unpatched critical vulnerabilities
- MFA adoption rate
- Percentage of systems with endpoint protection active
- Control exception counts and ages

Analysts use compliance dashboards to identify which controls need attention and to produce evidence for auditors.

---

## Slide 10 — Audit Evidence Collection

An audit is a formal review of whether an organization's security controls meet a defined standard. Auditors require evidence — documented proof that controls exist and are operating.

Types of audit evidence include:

- Policy documents showing controls are defined
- Configuration screenshots showing controls are implemented
- Log extracts showing controls are operating (for example, authentication logs showing MFA is being enforced)
- Vulnerability scan reports showing assessments are performed
- Change management records showing changes are reviewed and approved
- Training completion records showing personnel are trained

Analysts frequently support audit evidence collection by running reports, extracting log data, and producing screenshots of tool configurations.

---

## Slide 11 — Gap Analysis

A gap analysis compares the organization's current security posture against a target framework or standard. It identifies where controls are missing, insufficient, or failing.

The gap analysis process follows these steps.

First, select the target framework — the standard you are measuring against.

Second, inventory existing controls — document what you currently have.

Third, map existing controls to framework requirements — identify which requirements are met by which controls.

Fourth, identify gaps — requirements with no satisfying control, or where the control is present but insufficient.

Fifth, prioritize gaps — rank based on risk, exploitability, and business impact.

Sixth, develop a remediation plan — define actions, owners, and timelines for closing each gap.

---

## Slide 12 — Security Control Inheritance

In large organizations, some controls are implemented centrally and inherited by multiple systems or business units. This concept is called control inheritance.

For example, an organization may implement centralized identity management with MFA enforcement. All systems that rely on that identity provider inherit the MFA control without implementing it independently.

Understanding control inheritance is important for analysts performing control validation because it tells you where to look. If a control is inherited, validate it at the source — the central system — not at each inheriting system individually.

---

## Slide 13 — Continuous Controls Monitoring

One-time audits provide a point-in-time view of compliance. Continuous controls monitoring provides ongoing visibility.

Modern security programs implement automated, continuous monitoring of key controls using tools like Security Content Automation Protocol (SCAP) scanners, configuration management platforms, and SIEM-based compliance dashboards.

SCAP is a NIST standard that defines a common language for expressing security configurations and checking whether systems comply. SCAP-compatible tools can automatically scan systems against defined configuration benchmarks and report deviations.

Continuous monitoring shifts the compliance model from "we passed the audit last year" to "we know our current compliance status right now."

---

## Slide 14 — CySA+ Exam Connection

For the CySA+ CS0-003 exam, the compliance and controls domain appears across multiple objectives. Focus on:

- The NIST CSF five functions and what each covers
- The CIS Controls and their implementation group structure
- Control categories — preventive, detective, corrective, deterrent
- Control types — technical, administrative, physical
- Audit evidence types and their purpose
- Gap analysis methodology
- The difference between compliance and security

The exam will test whether you can map a described security activity to the correct framework function, identify what type of control is missing from a scenario, and explain what audit evidence is required to demonstrate control effectiveness.

---

## Slide 15 — Summary

Module 13 covered compliance and security controls validation. We examined the NIST CSF and CIS Controls as the primary frameworks analysts use to organize and assess security programs. We walked through control testing methodologies, compliance dashboards, audit evidence collection, and gap analysis.

The key insight from this module is that controls validation bridges the gap between what an organization thinks is protected and what is actually protected. Analysts who can validate controls and communicate gaps clearly are valuable at every level of a security organization.

---

## Slide 16 — Looking Ahead

In Module 14 we shift to Security Automation and Scripting. You will learn how to use Python to automate log analysis, write scripts that interact with security tool APIs, and understand how SOAR platforms work. These are among the highest-demand skills in the current security job market.

Complete all Module 13 activities before our next session.

---

End of Module 13 Video Script — 220 lines
