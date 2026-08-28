# Reading Guide: Module 06 — Information Security Program Development

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4315 &BULL; CYBERSECURITY GOVERNANCE, RISK & COMPLIANCE (GRC)</text>
    
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


## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 3: Information Security Program

---

## Introduction

Welcome to Module 06. This reading guide provides comprehensive reference material to support the video lecture, lab, and quiz for this module. The focus is building an information security program from its founding charter through the policy hierarchy, strategy alignment, and resource planning.

CISM Domain 3 — Information Security Program — is heavily tested on the certification exam. Candidates who understand program development as a lifecycle, rather than a collection of isolated documents, perform significantly better. Use this guide to build that holistic perspective.

---

## 1. The Security Program Charter

### 1.1 Purpose and Definition

The security program charter is the authorizing document that establishes the formal existence, authority, scope, and accountability of the information security function. It is typically issued by senior executive leadership — the CEO, board, or steering committee — and signed by the CISO or designated security program owner.

The charter is not a policy, not a procedure, and not a standards document. It is a governance instrument. Its purpose is to grant authority, define scope, and establish accountability. Without it, the security function operates without formal organizational standing.

### 1.2 Charter Components Reference Table

| Component | Description | Why It Matters |
|---|---|---|
| Purpose and Scope | Defines what the program protects and what is out of scope | Prevents scope creep; sets program boundaries |
| Authority Grant | Names who authorizes security enforcement | Enables policy enforcement and escalation |
| Roles and Responsibilities | RACI for security activities across departments | Prevents gaps and overlaps in accountability |
| Business Alignment Statement | Connects security mission to business objectives | Justifies program existence to executives |
| Reporting Structure | Where CISO sits in org chart | Determines independence and access to leadership |
| Review Cycle | How often charter is revisited | Keeps charter current with organizational change |

### 1.3 Charter vs. Policy — Critical Distinction

A common exam trap is confusing the charter with a security policy. The distinction is fundamental.

The **charter** answers: "What is the security program empowered to do, and who authorized it?"

A **policy** answers: "What are employees required to do?"

The charter enables policies. Policies derive their enforceability from the authority granted in the charter. An organization can have excellent policies but no enforcement mechanism if the charter is absent or weak.

---

## 2. The Policy Hierarchy

### 2.1 Overview of the Four-Tier Model

The four-tier policy hierarchy is the industry-standard structure for organizing security documentation. Each tier serves a distinct purpose and has different characteristics regarding mandatory nature, update frequency, and audience.

| Tier | Document Type | Mandatory? | Update Frequency | Primary Audience |
|---|---|---|---|---|
| 1 | Policy | Yes | Every 1–2 years | All employees |
| 2 | Standard | Yes | Every 6–12 months | IT and security teams |
| 3 | Procedure | Yes | As needed (operational) | System administrators |
| 4 | Guideline | No (recommended) | As needed | Developers, end users |

### 2.2 Tier 1: Policies

Policies are high-level mandatory statements of intent. They establish WHAT the organization requires without specifying HOW to achieve it. This technology-neutral design allows policies to remain stable as technology evolves.

Key characteristics:

- Approved and signed by executive leadership or the board
- Reference regulatory requirements where applicable (HIPAA, GDPR, PCI DSS)
- State consequences for non-compliance
- Technology-neutral language
- Scope defined explicitly (who and what systems are covered)

Common policy examples: Acceptable Use Policy, Access Control Policy, Information Classification Policy, Incident Response Policy, Data Retention Policy.

### 2.3 Tier 2: Standards

Standards translate policy requirements into specific, mandatory technical or operational specifications. They answer the "how specifically" question that policies leave open. Standards are mandatory but can be updated more frequently than policies as technology changes.

Key characteristics:

- Reference the parent policy they implement
- Specify approved technologies, configurations, or methods
- May include exception process for deviations
- Reviewed and approved by the security architecture function

Example: An Access Control Policy requires MFA. The corresponding standard specifies that MFA must use TOTP or FIDO2 hardware keys; SMS OTP is explicitly excluded.

### 2.4 Tier 3: Procedures

Procedures are step-by-step operational instructions for implementing standards. They are the most granular tier and change most frequently because they reflect current system configurations, software versions, and vendor interfaces.

Key characteristics:

- Often owned by IT operations, not the security team
- Written for specific roles (e.g., Windows admin, network engineer)
- Include verification steps to confirm successful implementation
- Should be tested and validated against actual systems

### 2.5 Tier 4: Guidelines

Guidelines are advisory documents that provide recommended practices and contextual guidance. They are the only non-mandatory tier. Guidelines support culture and adoption without creating compliance obligations.

Key characteristics:

- Non-mandatory — violations do not trigger disciplinary action
- Useful for developer guidance, user tips, and best-practice documentation
- Support the spirit of policies and standards
- May be published as FAQs, wikis, or tip sheets

### 2.6 Policy Lifecycle

Every policy document follows a lifecycle: draft, review, approve, publish, communicate, enforce, and review/retire. The CISM exam tests understanding of this lifecycle, particularly the communication and enforcement phases. A policy that exists but is unknown to employees or unenforceable is not a functioning security control.

---

## 3. Security Strategy Alignment

### 3.1 The Business-Security Connection

Security strategy must derive from and support business strategy. This is not merely a best practice — it is the foundational principle of CISM Domain 3. Security programs that are built in isolation from business objectives become irrelevant, underfunded, and organizationally bypassed.

The security strategy answers three questions:

1. What business assets and capabilities does the security program protect?
2. What threats to those assets exist, and what is their business impact?
3. What security initiatives, in what sequence, best address those threats within available resources?

### 3.2 Security Strategy Document Structure

| Section | Content | Purpose |
|---|---|---|
| Executive Summary | One-page overview of strategy and key objectives | Board and executive consumption |
| Current State Assessment | Maturity scores across security domains | Establishes baseline |
| Threat Landscape | Key threats mapped to business impact | Contextualizes need |
| Target State | Desired maturity levels and capabilities | Defines the destination |
| Gap Analysis | Delta between current and target state | Identifies what must be built |
| Strategic Roadmap | Initiatives with timelines and owners | Execution plan |
| Resource Requirements | Budget, headcount, tools needed | Justifies investment |
| KPIs and Metrics | How success will be measured | Enables governance review |

### 3.3 Maturity Model Integration

Maturity models provide a common language for communicating security program progress to non-technical leadership. The CMMI-based five-level model is widely used:

| Level | Name | Description |
|---|---|---|
| 1 | Initial | Ad hoc, reactive, undocumented |
| 2 | Managed | Repeatable processes exist for some functions |
| 3 | Defined | Standardized, documented organization-wide |
| 4 | Quantitatively Managed | Metrics-driven, measurable outcomes |
| 5 | Optimizing | Continuous improvement, proactive threat adaptation |

Most organizations entering a security program build cycle are at Level 1 or 2. The strategy roadmap should define a realistic path to Level 3 over 24–36 months, with a long-term aspiration to Level 4.

### 3.4 Aligning Security Objectives to Business Objectives

| Business Objective | Derived Security Objective |
|---|---|
| Expand into EU markets | Achieve and maintain GDPR compliance |
| Acquire competitor company | Complete security integration within 18 months |
| Launch mobile application | Conduct mobile application security testing pre-launch |
| Achieve SOC 2 Type II certification | Implement and evidence required controls |
| Reduce operational costs | Consolidate security tools and automate monitoring |

---

## 4. Resource Planning

### 4.1 People Resources

Security staffing is a persistent challenge. Key planning considerations include:

- **Build vs. Buy**: Internal staff vs. MSSPs for detection, response, or compliance functions
- **Skill gap analysis**: Map current team competencies against required program capabilities
- **Coverage requirements**: 24/7 monitoring coverage requires shift planning or MSSP support
- **Career development**: Certification paths (CISM, CISSP, CEH) support retention

### 4.2 Budget Planning Framework

A risk-informed budget connects every expenditure to a risk or compliance requirement.

| Budget Category | Description | Typical % of Security Budget |
|---|---|---|
| Personnel | Salaries, benefits, training | 40–50% |
| Technology | Tools, licenses, infrastructure | 25–35% |
| Services | MSSPs, consulting, assessments | 10–20% |
| Compliance | Audits, certifications, legal | 5–10% |
| Contingency | Incident response reserve | 5–10% |

### 4.3 Annualized Loss Expectancy (ALE) for Budget Justification

ALE is the foundational quantitative tool for security investment justification.

**Formula:** ALE = SLE × ARO

Where:

- **SLE** (Single Loss Expectancy) = Asset Value × Exposure Factor
- **ARO** (Annual Rate of Occurrence) = Estimated probability of occurrence per year

**Investment justification formula:**

Control ROI = (ALE Before Control − ALE After Control) − Annual Control Cost

If the result is positive, the control investment is financially justified.

### 4.4 The Business Case Structure

| Section | Content |
|---|---|
| Problem Statement | Risk or gap being addressed, with quantified impact |
| Solution Options | 2–3 alternatives with pros, cons, and costs |
| Recommended Option | Preferred solution with rationale |
| Cost-Benefit Analysis | ALE reduction vs. control cost |
| Implementation Timeline | Phases, milestones, dependencies |
| Success Metrics | How outcomes will be measured |

---

## 5. CISM Exam Tips — Module 06

The following concepts are high-frequency exam topics from Domain 3.

**Charter and authority:**

- The charter is the governance document that enables program authority — it is distinct from policies
- CISO reporting structure (to CEO vs. CTO vs. CFO) affects program independence — the exam may present scenarios testing this
- Without executive sponsorship documented in a charter, security programs lack enforcement capability

**Policy hierarchy:**

- Know all four tiers by name and be able to identify which tier a given document belongs to
- Policies are mandatory; guidelines are not — this distinction is tested frequently
- Technology-neutral language belongs in policies; specific technical requirements belong in standards

**Strategy alignment:**

- Security strategy must be derived from and support business strategy — this is the CISM foundational principle
- The exam will present scenarios where security appears to conflict with business objectives; the correct answer almost always finds a way to enable the business while managing risk
- Maturity models are tools for communication and roadmap building, not compliance checkboxes

**Resource planning:**

- ALE calculation and interpretation is a reliable exam topic
- The decision to accept residual risk belongs to senior management, not the security team
- Budget justification requires business language — risk quantification in financial terms

---

## 6. Key Terms Glossary

| Term | Definition |
|---|---|
| Security Program Charter | Authorizing document establishing the security program's mandate, authority, scope, and accountability |
| Policy | Mandatory high-level statement of what must be done; technology-neutral |
| Standard | Mandatory technical specification implementing a policy requirement |
| Procedure | Step-by-step operational instruction implementing a standard |
| Guideline | Non-mandatory recommended practice supporting policy intent |
| Security Strategy | Multi-year plan connecting security objectives to business objectives |
| Maturity Model | Framework for assessing and communicating security program development stages |
| ALE | Annualized Loss Expectancy — expected financial loss from a risk over one year |
| SLE | Single Loss Expectancy — financial loss from one occurrence of a risk event |
| ARO | Annual Rate of Occurrence — estimated probability of a risk event per year |
| Business Case | Structured justification for security investment including cost-benefit analysis |
| Gap Analysis | Comparison of current security state to target state to identify missing capabilities |

---

## 7. Required and Recommended Readings

**Required (Zero-Textbook-Cost resources):**

- NIST SP 800-100: Information Security Handbook — Chapter 3 (Program Management) — [csrc.nist.gov](https://csrc.nist.gov/publications/detail/sp/800-100/final)
- NIST SP 800-53 Rev 5: Security and Privacy Controls — PM Control Family (Program Management) — [csrc.nist.gov](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- ISACA: Information Security Program Overview — available in CISM Review Manual excerpts on isaca.org

**Recommended:**

- ISO/IEC 27001:2022 — Section 5 (Leadership) and Section 6 (Planning) for policy and strategy alignment context
- SANS Security Policy Templates — open resource at sans.org/information-security-policy

---

## 8. Study Checklist

- [ ] Identify the six components of a security program charter
- [ ] Distinguish the charter from policies and explain why both are needed
- [ ] Name all four tiers of the policy hierarchy and give an example document for each
- [ ] Explain why policies should be technology-neutral
- [ ] Describe the four steps for aligning security strategy to business objectives
- [ ] Calculate ALE given SLE and ARO values
- [ ] Build a basic business case structure for a security investment
- [ ] Complete the Module 06 lab (charter drafting exercise)
- [ ] Take the Module 06 quiz
- [ ] Post to the Module 06 discussion forum by Wednesday 11:59 PM

---

## 9. Supplemental Resources

**NIST SP 800-100 — Information Security Handbook: A Guide for Managers**
URL: https://csrc.nist.gov/publications/detail/sp/800-100/final
Description: Free NIST publication providing comprehensive management-level guidance on developing and operating an information security program, including program management, security planning, risk management integration, and resource planning. Chapter 4 covers security program management directly, covering the charter, policy hierarchy, and resource allocation topics central to Module 06.

**ISACA CISM Review Manual — Domain 3: Information Security Program**
URL: https://www.isaca.org/credentialing/cism/cism-exam-resources
Description: ISACA's official CISM exam preparation resources for Domain 3, covering information security program development, management, and governance. The review manual chapters on program charter, policy hierarchy, and strategic alignment provide exam-focused summaries of the concepts covered in this module and include practice questions aligned with the CISM item format.

**CIS Controls v8 — Implementation Groups and Safeguards**
URL: https://www.cisecurity.org/controls/v8
Description: The Center for Internet Security's free Controls v8 publication organizes 153 safeguards across 18 control families into three Implementation Groups based on organizational maturity and resources. This is directly applicable to Module 06's discussion of phased security program development — Implementation Group 1 represents foundational controls, Groups 2 and 3 represent progressively mature capabilities. Free download available at the CIS website.
