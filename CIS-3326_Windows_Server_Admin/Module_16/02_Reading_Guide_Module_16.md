# Reading Guide: Module 16 - Final Exam Prep and Windows Server Administration Certification

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction

Welcome to **Module 16 – Final Exam Prep and Windows Server Administration Certification**! This final module consolidates the key concepts from all 15 preceding modules and maps them directly to the AZ-800 (Administering Windows Server Hybrid Core Infrastructure) and AZ-801 (Configuring Windows Server Hybrid Advanced Services) exam objectives. Use this guide as your comprehensive review checklist before the final exam.

As a student, you will review all major topic domains, practice scenario-based reasoning, and confirm your readiness across installation, AD DS, GPO, networking, security, virtualization, and identity services. Make sure to complete the checklist and review all glossary terms from previous modules before sitting for the final.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. These terms span all 15 modules and represent the highest-frequency topics on the certification exam:

* **AZ-800 Exam Domain Summary**: The AZ-800 exam covers five domains: (1) Deploy and manage Windows Server infrastructure, (2) Manage on-premises and hybrid AD DS, (3) Manage Windows Server and workloads in a hybrid environment, (4) Manage virtual machines and containers, and (5) Implement and manage an on-premises and hybrid networking infrastructure.
* **Hybrid Identity (Azure AD Connect + AD FS)**: The combination of on-premises AD DS synchronized to Microsoft Entra ID via Azure AD Connect, optionally federated through AD FS. Enables SSO across on-premises and cloud resources. Key decision: Password Hash Sync vs. Pass-Through Authentication vs. Federation.
* **LSDOU + Enforced + Block Inheritance**: The complete GPO processing model. Local → Site → Domain → OU, last writer wins, unless Enforced (higher-level GPO always wins) or Block Inheritance (OU refuses higher-level GPOs, except Enforced ones). The most commonly tested GPO concept on AZ-800.
* **Authoritative Restore vs. AD Recycle Bin**: Two recovery paths for deleted AD objects. AD Recycle Bin (`Restore-ADObject`) is faster and preserves all attributes — use it first if enabled. Authoritative restore from backup using `ntdsutil` is the fallback when Recycle Bin is unavailable or the retention window has passed.
* **BitLocker Network Unlock vs. TPM-only**: For headless servers that cannot accept a PIN at boot, BitLocker Network Unlock automatically decrypts the drive when the server boots on the trusted internal network. TPM-only is convenient but provides no protection against booting the server on an untrusted network.
* **Always On VPN vs. DirectAccess**: Always On VPN is the modern replacement — it works with all Windows 10/11 editions, non-domain devices, and IPv4 networks. DirectAccess requires Enterprise edition, domain membership, and IPv6. For any new deployment scenario on AZ-800, Always On VPN is the correct answer.

---

### 2. Certification Exam Tips

* **Read every scenario question twice**: AZ-800 scenario questions hide the key constraint in the last sentence. Common constraints include "without additional cost," "without reinstalling the OS," "must work when the WAN link is down," and "must not require user interaction." Identify the constraint before evaluating answers.
* **Use elimination on distractors**: Each answer choice on the AZ-800 is plausible in some context. Eliminate answers that are technically correct but wrong for the specific constraint in the scenario. The most common distractor is a solution that works but requires more steps or higher cost than necessary.
* **PowerShell syntax on the exam**: You will see PowerShell cmdlets in answer choices. Know the difference between `Get-ADUser`, `Set-ADUser`, `New-ADUser`, and `Remove-ADUser`, and understand when to use `-Filter`, `-Identity`, and `-SearchBase` parameters.
* **Microsoft Learn Reference**: Use [Microsoft Learn – AZ-800 Study Guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-800) as your final review reference. It maps every exam objective to the corresponding documentation, providing the authoritative checklist for certification readiness.

---

### Required Readings & Videos

To prepare for the final exam, you must complete the following readings and reviews:

* **Required Reading:** Review the official AZ-800 exam study guide at [Microsoft Learn: AZ-800 Study Guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-800). Cross-reference each objective with the reading guides from Modules 01–15 to identify any gaps.
* **Required Video:** Re-watch any video lectures from the course playlist where you feel less confident: [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).

---

### Lab & Command Integration

In this final module's lab, you will complete a comprehensive review exercise covering AD DS administration, GPO creation and troubleshooting, BitLocker configuration, PowerShell remoting, and performance monitoring — consolidating all hands-on skills from the semester into a single capstone scenario.

---

### 3. Study Checklist

* [ ] Review the glossary terms from all 16 modules.
* [ ] Review the official AZ-800 study guide at [Microsoft Learn: AZ-800 Study Guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-800).
* [ ] Re-watch any video lectures you need to reinforce in [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).
* [ ] Complete the capstone lab exercise.
* [ ] Proceed to the final exam.
