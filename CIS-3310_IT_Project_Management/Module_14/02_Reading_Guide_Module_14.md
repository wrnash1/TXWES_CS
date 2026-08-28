# Reading Guide: Module 14 — Procurement and Contract Management

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3310 &BULL; IT PROJECT MANAGEMENT & AGILE METHODOLOGIES</text>
    
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


## Course: CIS-3310 IT Project Management

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Project+ (PK0-005)

---

## Introduction

Procurement and Contract Management is a consistently tested knowledge area on the CompTIA Project+ exam. Questions appear in two forms: process identification (which procurement process is this activity part of?) and contract type application (which contract type is appropriate given this scenario, and who bears the cost risk?). This reading guide provides the complete reference framework for both.

---

## Section 1 — High-Yield Glossary

### Procurement Management

The knowledge area governing the processes required to acquire goods and services from outside the project team or organization. Covers planning, conducting, controlling, and closing procurements.

### Make-or-Buy Analysis

A systematic evaluation of whether it is more cost-effective and strategically appropriate to produce a product or service internally (make) or acquire it from an external vendor (buy). Inputs include internal capability, cost comparison, capacity, time constraints, and strategic considerations.

### Statement of Work (SOW)

A document that describes the work to be performed under a contract. Includes deliverables, technical specifications, schedule expectations, acceptance criteria, and performance conditions. The SOW is part of the procurement documents and becomes an exhibit in the final contract.

### Procurement Management Plan

A subsidiary plan within the Project Management Plan that documents procurement strategy, contract types to be used, procurement authority, source selection criteria, how proposals will be evaluated, and risk allocation decisions.

### Request for Proposal (RFP)

A solicitation document used when the buyer wants vendors to propose both an approach and a price. Evaluation criteria include technical methodology, vendor qualifications, and cost. Used when the problem is defined but the solution approach is open.

### Request for Quotation (RFQ)

A solicitation document used when the requirement is well-defined and the buyer wants vendors to submit a price for a specified product or service. Evaluation is typically price-focused.

### Invitation for Bid (IFB)

A formal solicitation document used primarily in government procurement. Requirements are fully specified; award goes to the lowest compliant bidder. Price is the sole evaluation criterion.

### Source Selection Criteria

The weighted factors used to evaluate and compare vendor proposals. Common criteria include technical approach, past performance, staffing qualifications, management approach, and price.

### Fixed-Price Contract

A contract type where the seller agrees to complete the work for a defined price. The seller bears cost risk. Subtypes: Firm Fixed-Price (FFP), Fixed-Price Incentive Fee (FPIF), Fixed-Price with Economic Price Adjustment (FPEPA).

### Cost-Reimbursable Contract

A contract type where the buyer reimburses the seller's actual allowable costs plus a fee. The buyer bears cost risk. Subtypes: Cost Plus Fixed Fee (CPFF), Cost Plus Incentive Fee (CPIF), Cost Plus Award Fee (CPAF).

### Time and Materials Contract (T&M)

A hybrid contract type where the buyer pays a fixed rate per labor unit plus actual material costs. Risk is shared; buyer has open-ended cost exposure unless a Not-to-Exceed clause is included.

### Bidder Conference

A meeting held with all prospective vendors simultaneously to explain the requirements, answer questions, and ensure all bidders receive the same information. Supports a fair and auditable procurement process.

### Procurement Performance Review

A structured evaluation of vendor performance against contract requirements. May result in cure notices if the vendor is underperforming.

### Cure Notice

A formal written notification to a vendor that their performance is deficient and they must correct the identified issues within a specified time period or face contract termination.

### Termination for Convenience

The buyer's right to end a contract for any reason, even without cause. The seller is typically entitled to payment for work completed to date.

### Termination for Cause

Contract termination due to the seller's breach of contract obligations. The buyer may pursue remedies and may not owe payment for incomplete or deficient work.

---

## Section 2 — Procurement Process Reference

| Process | Process Group | Key Inputs | Key Outputs |
|---------|--------------|------------|-------------|
| Plan Procurement Management | Planning | Project charter, scope baseline, make-or-buy decisions, risk register | Procurement Management Plan, Statement of Work, source selection criteria |
| Conduct Procurements | Executing | Procurement Management Plan, SOW, source selection criteria, seller proposals | Signed agreements (contracts), selected sellers |
| Control Procurements | Monitoring and Controlling | Signed agreements, work performance data, approved change requests | Work performance information, change requests, contract updates |
| Close Procurements | Closing | Signed agreements, procurement documentation, accepted deliverables | Closed contracts, updated organizational process assets |

---

## Section 3 — Solicitation Document Comparison

| Document | Used When | Evaluation Basis | Award Criteria |
|----------|-----------|-----------------|----------------|
| RFP (Request for Proposal) | Scope defined; approach open | Technical + price | Highest scored (weighted criteria) |
| RFQ (Request for Quotation) | Scope and specs fully defined | Price only or price-dominant | Lowest price meeting requirements |
| IFB (Invitation for Bid) | Formal government procurement; full specification | Price only | Lowest compliant bidder |

---

## Section 4 — Contract Type Comparison

| Contract Type | Subtype | Buyer Risk | Seller Risk | Best Used When |
|---------------|---------|-----------|------------|----------------|
| Fixed-Price | FFP | Low | High | Scope is clear and stable |
| Fixed-Price | FPIF | Low | High (with incentive) | Clear scope; performance incentives desired |
| Fixed-Price | FPEPA | Low-Medium | High | Long-duration; inflation risk present |
| Cost-Reimbursable | CPFF | High | Low | Scope unclear; R&D or discovery work |
| Cost-Reimbursable | CPIF | High | Low-Medium | Scope unclear; cost-sharing incentives desired |
| Cost-Reimbursable | CPAF | High | Low | Scope unclear; subjective performance criteria |
| Time and Materials | T&M | Medium-High | Low | Scope unclear; immediate start required; staff augmentation |

### Risk Allocation Summary

| Contract Family | Who Bears Cost Risk | Key Phrase to Remember |
|-----------------|-------------------|------------------------|
| Fixed-Price | Seller | "Seller owns the overrun" |
| Cost-Reimbursable | Buyer | "Buyer writes the check for actuals" |
| Time and Materials | Buyer (open-ended) | "Hours and materials — no ceiling unless capped" |

---

## Section 5 — Make-or-Buy Decision Factors

### Reasons to Make (Internal)

- Work involves proprietary systems or confidential data
- Internal team has the required expertise
- Long-term strategic competency development
- Lower total cost when internal capacity exists
- Speed advantage from using known internal systems

### Reasons to Buy (External)

- Internal expertise is unavailable or insufficient
- Vendor can deliver faster due to specialization
- Work is not a core organizational competency
- Reduces need to hire and train permanent staff
- Risk transfer through contractual accountability

---

## Section 6 — Statement of Work Components

A complete SOW includes:

1. Description of work — what is to be performed or produced
2. Deliverables — specific outputs with acceptance criteria
3. Technical requirements — specifications, standards, interfaces
4. Schedule — milestones, delivery dates, performance windows
5. Acceptance criteria — the measurable conditions that constitute completion
6. Place of performance — location requirements, remote vs. on-site
7. Period of performance — start and end dates
8. Reporting requirements — status reporting format and frequency
9. Special requirements — security clearances, certifications, compliance

---

## Section 7 — Source Selection Process

| Step | Activity |
|------|----------|
| 1 | Issue solicitation document (RFP, RFQ, or IFB) |
| 2 | Hold bidder conference (if used) |
| 3 | Receive and log proposals by deadline |
| 4 | Evaluate proposals against source selection criteria |
| 5 | Conduct vendor presentations or clarifications (if needed) |
| 6 | Apply weighted scoring matrix to rank vendors |
| 7 | Recommend award to highest-scoring compliant vendor |
| 8 | Negotiate and execute contract |

---

## Section 8 — Project+ Exam Tips

> **Exam Tip 1 — Risk flows to the party who can control it best:**
> Fixed-Price shifts risk to the seller because the seller can control their own costs. Cost-Reimbursable retains risk with the buyer because scope uncertainty means the seller cannot accurately estimate costs. When asked who bears more risk, think about who has the best information to manage cost uncertainty.
>
> **Exam Tip 2 — RFP versus RFQ versus IFB:**
> RFP = approach + price (you want ideas); RFQ = price on a defined item (you know what you want); IFB = price only, lowest compliant wins (formal government). The exam will describe the situation — match the solicitation type to the description.
>
> **Exam Tip 3 — T&M always needs a Not-to-Exceed clause:**
> T&M contracts are described as "hybrid" because they blend fixed-rate labor with actual material costs. The buyer's cost risk in T&M is open-ended unless a ceiling is contractually specified. If an exam question mentions cost overrun risk in a T&M context, the mitigation is a Not-to-Exceed (NTE) clause.
>
> **Exam Tip 4 — Contract changes go through procurement change control:**
> Changes to a contract must follow the procurement change control system — they cannot simply be verbally agreed upon or handled as informal adjustments. The integrated change control process applies to contract modifications just as it does to scope or schedule changes.
>
> **Exam Tip 5 — SOW is not the contract:**
> The SOW describes what is being bought. The contract is the full legal agreement that includes the SOW plus pricing, payment terms, dispute resolution, warranties, termination provisions, and other legal terms and conditions.
>
> **Exam Tip 6 — Bidder conferences ensure equal information:**
> Bidder conferences (also called vendor conferences or pre-bid meetings) are held to ensure all prospective vendors hear the same information at the same time. This prevents information asymmetry and makes the procurement process auditable and defensible.
>
> **Exam Tip 7 — Termination for convenience vs. for cause:**
> Termination for convenience allows the buyer to end any contract at will — the seller receives payment for work completed. Termination for cause occurs when the seller has breached contract requirements — the buyer may pursue remedies. The exam will describe the situation; identify which applies.
>
> **Exam Tip 8 — Procurement closure precedes project closure:**
> In a project with external vendors, each procurement must be formally closed before the overall project can be closed. Procurement closure includes verifying all deliverables were accepted, all payments made, and all contract documentation archived as organizational process assets.

---

## Section 9 — Study Checklist

- [ ] Name the four procurement management processes and their process groups
- [ ] Describe how a make-or-buy decision is made and list three factors for each option
- [ ] Distinguish RFP, RFQ, and IFB — when each is used and how award is determined
- [ ] List all three Fixed-Price contract subtypes and when each applies
- [ ] List all three Cost-Reimbursable contract subtypes and when each applies
- [ ] Explain T&M contracts and why a Not-to-Exceed clause is important
- [ ] Explain who bears cost risk under Fixed-Price vs. Cost-Reimbursable vs. T&M
- [ ] List the components of a Statement of Work
- [ ] Describe the purpose of a bidder conference
- [ ] Distinguish termination for convenience from termination for cause
- [ ] Complete the Module 14 Lab vendor evaluation exercise
- [ ] Take the Module 14 Quiz (10 questions)
- [ ] Post Module 14 Discussion initial response by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

The following free, openly licensed resources extend the concepts in this module. All links are publicly accessible — no account or purchase required.

1. **Project Management Open Textbook — Chapter 12: Project Procurement Management**
   *BC Campus OpenEd* — [opentextbc.ca/projectmanagement — Chapter 12](https://opentextbc.ca/projectmanagement/chapter/chapter-12-project-procurement-management/)
   Covers make-or-buy analysis, contract types, SOW components, and vendor evaluation with worked examples applicable to IT procurement decisions.

2. **PMI — Procurement Management Overview (Free Article)**
   *Project Management Institute* — [pmi.org/learning/library/procurement-management-contract-types](https://www.pmi.org/learning/library/procurement-management-contract-types-6234)
   PMI's overview of contract type selection logic, risk allocation principles, and the role of the procurement management plan — directly tested on Project+ and PMP exams.

3. **NIGP — Understanding Contract Types: Fixed-Price vs. Cost-Reimbursable (Free)**
   *National Institute of Governmental Purchasing* — [nigp.org/learning/contract-types-overview](https://www.nigp.org/learning/contract-types-overview)
   Practical breakdown of when each contract type is appropriate, including T&M considerations and risk-shifting implications for buyer and seller.

4. **YouTube — \"Statement of Work Tutorial for Project Managers\" (Adriana Girdler)**
   [youtube.com/watch?v=0HiDzaFkPIQ](https://www.youtube.com/watch?v=0HiDzaFkPIQ)
   Step-by-step walkthrough of SOW structure — scope of work, deliverables, acceptance criteria, and compliance requirements. Directly supports the Module 14 lab SOW drafting exercise.

5. **Smartsheet — RFP vs. RFQ vs. IFB: A Plain-Language Guide (Free)**
   [smartsheet.com/content/rfp-vs-rfq](https://www.smartsheet.com/content/rfp-vs-rfq)
   Side-by-side comparison of the three primary solicitation document types with guidance on when each is appropriate — covers the award criteria differences tested on the Project+ exam.
