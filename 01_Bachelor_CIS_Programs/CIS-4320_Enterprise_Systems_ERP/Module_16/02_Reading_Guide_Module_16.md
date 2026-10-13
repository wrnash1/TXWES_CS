# Reading Guide: Module 16 - Final Exam Prep & Salesforce/SAP Certification

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4320 &BULL; ENTERPRISE SYSTEMS & ERP ARCHITECTURE</text>
    
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


## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Introduction

Welcome to **Module 16 - Final Exam Prep & Salesforce/SAP Certification**! This is your synthesis week. You will integrate everything covered across Modules 01–15 into a coherent understanding of enterprise systems, prepare for the course final exam, and lay the foundation for your Salesforce Certified Associate and/or SAP Certified Associate certification attempts.

This module does not introduce new topics — it reinforces and connects the high-yield concepts from every prior module, provides test-taking strategies for both certification exams, and directs you to the official study resources and practice exams that will maximize your readiness.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. These are the cross-cutting concepts that span the full course:

* **Core ERP operations**: The complete set of integrated business functions that an ERP system automates — financial accounting (FI), controlling (CO), materials management (MM), sales and distribution (SD), human capital management (HCM), and production planning (PP) — all sharing one database and delivering real-time cross-functional visibility.
* **Best practices in enterprise systems**: The vendor-recommended and industry-proven approaches for configuring, implementing, securing, and maintaining ERP/CRM platforms. Examples include: using standard SAP processes before customizing, applying the Salesforce "configuration before code" principle, enforcing Separation of Duties in financial workflows, and testing in sandbox before deploying to production.
* **System configuration vs. customization**: Configuration means adjusting standard system settings (e.g., defining a company code in SAP, creating a custom field in Salesforce) within the vendor-provided framework. Customization means writing code (ABAP, Apex) or modifying standard behavior to achieve requirements not met by configuration. Best practice is always to exhaust configuration options before customizing.

---

### 2. Certification Exam Tips

* **Salesforce Certified Associate exam overview:** 40 multiple-choice questions, 70 minutes, passing score 62% (approximately 25 correct). Focus areas: Salesforce ecosystem and navigation (32%), Functionality and use cases (28%), Trailhead and resources (20%), and Data model and ethics (20%). Register at [Webassessor / Salesforce Certification portal](https://www.salesforce.com/training/certification/).
* **SAP Certified Associate exam overview:** 80 questions, 180 minutes, passing score approximately 65%. The specific exam depends on your focus (SAP S/4HANA Finance, SD, MM, HCM). Register at [SAP Training and Certification Shop](https://training.sap.com/certification).
* **Salesforce final prep strategy:** Complete the [Salesforce Certified Associate Study Guide](https://trailhead.salesforce.com/credentials/associate) exam guide on Trailhead. Run through the Trailmix [Associate Certification Prep](https://trailhead.salesforce.com/users/strailhead/trailmixes/associate-cert-prep) and earn all badges. Practice with the Trailhead Superbadge challenges to apply knowledge under scenario conditions.
* **SAP final prep strategy:** Use the [openSAP platform](https://open.sap.com) for free SAP certification preparation courses. Review the SAP Learning Journey for your target exam on the SAP Training portal. Focus on scenario-based questions that require you to select the correct SAP module or transaction for a described business need.
* **Both exams — time management:** Both exams are scenario-heavy. If a question requires more than 90 seconds to answer, mark it and return at the end. Never leave questions unanswered — there is no penalty for guessing on either exam.
* **Study Resource:** Complete the Salesforce Trailhead [Trailblazer Community](https://trailhead.salesforce.com/trailblazer-community) — the official community forum where certification candidates share study tips, flag tricky exam topics, and post after-exam experience reports (within NDA).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Review the official [Salesforce Certified Associate Exam Guide](https://trailhead.salesforce.com/credentials/associate) — a free document that lists every tested topic with percentage weighting, helping you prioritize your review.
* **Required Video:** Review the complete [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1) playlist, focusing on any modules where your practice quiz scores were weakest.

---

### Lab & Command Integration

In this week's final review activities, you will complete the following:

* **Full concept map**: Create a visual diagram connecting all 15 prior module topics, showing how ERP modules (FI, MM, SD, HCM) feed data to each other, how CRM (Salesforce) connects to ERP through integration middleware, and where security and data migration fit in the overall architecture.
* **Certification readiness checklist**: Work through the Salesforce Associate exam guide topic list and rate your confidence (High / Medium / Low) for each topic area. For each Low-confidence area, identify the specific Trailhead module that covers it and schedule 30 minutes of targeted review.
* **Practice scenario analysis**: Work through five practice exam scenarios (provided in the course quiz bank) and for each incorrect answer, write a one-sentence explanation of why the correct answer is correct and why you initially chose the wrong one.

---

### 3. Study Checklist

* [ ] Review the glossary definitions from all 16 modules using your notes from prior weeks.
* [ ] Complete the [Salesforce Certified Associate Exam Guide](https://trailhead.salesforce.com/credentials/associate) topic review and identify gaps.
* [ ] Complete the Trailhead Trailmix [Associate Cert Prep](https://trailhead.salesforce.com/users/strailhead/trailmixes/associate-cert-prep) to earn all remaining certification-prep badges.
* [ ] Complete the full concept map, certification readiness checklist, and practice scenario analysis lab activities.
* [ ] Schedule your Salesforce Certified Associate exam through the Salesforce certification portal.

---

## 9. Supplemental Resources

1. **Salesforce Trailhead — Salesforce Certified Associate Exam Prep Trailmix**
   <https://trailhead.salesforce.com/users/strailhead/trailmixes/associate-cert-prep>
   The official Salesforce-curated Trailmix for the Certified Associate exam. Complete every badge to cover all weighted topic areas (Ecosystem and Navigation, Functionality and Use Cases, Data Model). Completion generates a Trailhead certificate you can share with Professor Nash as study documentation.

2. **SAP Learning — SAP S/4HANA Essentials Learning Journey**
   <https://learning.sap.com/learning-journeys/explore-sap-s-4hana>
   SAP's official free learning journey for the S/4HANA Essentials certification. Organized by process domain (FI, MM, SD, PP, HCM) with module-by-module video walkthroughs, guided exercises, and knowledge checks. Use the journey map to identify which modules align to quiz questions you missed in Modules 01–15 and target those sections for final review.

3. **openSAP — SAP S/4HANA Enterprise Management — Certification Preparation**
   <https://open.sap.com/courses/s4h16>
   A free MOOC-style course on the openSAP platform that covers the SAP S/4HANA business processes tested on associate-level certification exams. Includes video lectures, weekly assignments, and a final exam simulation. Particularly useful for students who need structured review of the Procure-to-Pay, Order-to-Cash, and Record-to-Report process chains that appear as scenario questions on the SAP exam.
