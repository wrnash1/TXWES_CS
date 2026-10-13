# Reading Guide: Module 16 - Final Exam Prep & AZ-900 Certification

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4331 &BULL; MICROSOFT AZURE CLOUD ARCHITECTURE</text>
    
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


## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

### Introduction

Welcome to **Module 16 - Final Exam Prep & AZ-900 Certification**! This is the culminating module of the course. You have covered all major AZ-900 domain areas across Modules 01-15. This module consolidates your learning, reinforces high-frequency exam topics, and prepares you to take the **Microsoft Azure Fundamentals (AZ-900)** certification exam.

The AZ-900 exam covers three broad domains: Cloud Concepts (25-30%), Azure Architecture and Services (35-40%), and Azure Management and Governance (30-35%). Use this module to identify any knowledge gaps, practice applying concepts in scenario format, and review the Microsoft Learn AZ-900 practice assessments before scheduling your exam.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **AZ-900 Exam Domains**: The exam is structured into three weighted domains. Cloud Concepts (~25-30%): cloud service models (IaaS/PaaS/SaaS), deployment models, shared responsibility, benefits of cloud. Azure Architecture and Services (~35-40%): compute, networking, storage, databases, identity, security tools. Azure Management and Governance (~30-35%): cost management, RBAC, governance tools (Policy, Blueprints, locks), monitoring, and management tools (ARM, CLI, Cloud Shell).

* **AZ-900 Exam Format**: 40-60 multiple-choice, multiple-select, drag-and-drop, and scenario-based questions. The passing score is 700 out of 1000. The exam is 45 minutes. It can be taken online proctored or at a Pearson VUE testing center. No prior Azure experience is required, but hands-on practice significantly improves performance.

* **Microsoft Learn Practice Assessment**: Microsoft provides a free official practice assessment for AZ-900 at [Microsoft Learn AZ-900 Practice Assessment](https://learn.microsoft.com/en-us/certifications/exams/az-900/practice/assessment?assessment-type=practice&assessmentId=23). It contains 50 scenario-based questions with detailed explanations. Complete it at least twice before your exam date.

---

### 2. Certification Exam Tips

* **Highest-frequency topics**: Based on AZ-900 exam weighting, prioritize: IaaS/PaaS/SaaS classification, shared responsibility model, Availability Zones vs. Region Pairs, RBAC scope hierarchy, Azure Policy vs. Blueprints vs. locks, ExpressRoute vs. VPN Gateway, blob access tiers (especially Archive rehydration), and Pricing Calculator vs. TCO Calculator.
* **Scenario elimination strategy**: AZ-900 questions are often answerable by elimination. Identify answers that are clearly wrong (wrong service category, wrong direction of data flow, impossible behavior) and narrow down to two plausible answers before making a final choice.
* **SLA numbers to know**: Single VM = 99.9% SLA. Two VMs in Availability Set = 99.95%. Two VMs across Availability Zones = 99.99%. Azure SQL Database (General Purpose) = 99.99%. These numbers appear in scenario questions asking which configuration achieves a specific SLA.
* **Free services and free tiers**: Some Azure services are always free (Azure Active Directory Free tier, Azure Policy evaluation, inbound data transfer). AZ-900 may ask what is included at no cost — know that inbound data to Azure is free and that outbound data incurs egress charges.
* **Study Resource**: Complete the official Microsoft Learn AZ-900 learning path before your exam — it covers all exam objectives with interactive exercises and knowledge checks at [Microsoft Learn – AZ-900 Full Learning Path](https://learn.microsoft.com/en-us/certifications/azure-fundamentals/). Use the practice assessment at [AZ-900 Practice Assessment](https://learn.microsoft.com/en-us/certifications/exams/az-900/practice/assessment?assessment-type=practice&assessmentId=23) to gauge exam readiness.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Complete the full AZ-900 learning path on Microsoft Learn if you have not already done so. The learning path covers all three exam domains with knowledge checks at [Microsoft Learn – AZ-900 Full Learning Path](https://learn.microsoft.com/en-us/certifications/azure-fundamentals/).
* **Required Video:** Review the complete AZ-900 exam prep course by freeCodeCamp, focusing on any sections where you need reinforcement: [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).

---

### Lab & Command Integration

In this final module, your lab activities focus on exam preparation rather than new service configuration:

* **Complete the Microsoft Learn AZ-900 Practice Assessment**: Take the free official practice assessment at [AZ-900 Practice Assessment](https://learn.microsoft.com/en-us/certifications/exams/az-900/practice/assessment?assessment-type=practice&assessmentId=23). Review the detailed explanations for any questions you miss — the explanations link directly to the relevant Microsoft documentation.
* **Review all module labs**: Return to the hands-on labs from Modules 01-15 and confirm you can explain what each Azure service does and why you performed each step. Being able to narrate what you did in a lab reinforces the conceptual knowledge tested on AZ-900.
* **Schedule your AZ-900 exam**: Visit the [Microsoft Certification Exam AZ-900 page](https://learn.microsoft.com/en-us/certifications/exams/az-900/) to register through Pearson VUE for an in-person or online proctored exam. Exam vouchers are available through academic programs at a discounted rate.

---

### 3. Study Checklist

* [ ] Complete the full Microsoft Learn AZ-900 learning path at [Microsoft Learn – AZ-900 Full Learning Path](https://learn.microsoft.com/en-us/certifications/azure-fundamentals/).
* [ ] Take the official AZ-900 Practice Assessment at [AZ-900 Practice Assessment](https://learn.microsoft.com/en-us/certifications/exams/az-900/practice/assessment?assessment-type=practice&assessmentId=23) and review all explanations.
* [ ] Review the key glossary terms and certification exam tips from Modules 01-15.
* [ ] Complete the final exam lab activities and revisit any module labs where confidence is low.
* [ ] Schedule your AZ-900 certification exam at [Microsoft Certification – AZ-900](https://learn.microsoft.com/en-us/certifications/exams/az-900/).

---

## 9. Supplemental Resources

1. Official AZ-900 exam skills outline — the authoritative list of all topics tested on the exam, updated with each exam version: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900

2. John Savill's AZ-900 Study Cram (YouTube) — comprehensive video review of all AZ-900 exam domains in a structured study format: https://www.youtube.com/watch?v=tQp1YkB2Tgs

3. Microsoft Azure free account — create a free Azure account to get hands-on practice with all services covered in the AZ-900 exam: https://azure.microsoft.com/en-us/free/
