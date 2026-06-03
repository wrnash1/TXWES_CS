# Reading Guide: Module 08 — Endpoint Security

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment

---

## Overview

This reading guide supports Module 08 of CIS-4328. It covers the full endpoint security stack tested on the Security+ exam: EDR versus antivirus, CIS hardening benchmarks, patch management, host-based firewalls, full disk encryption, application allowlisting, and mobile device management.

All readings use zero-cost, openly licensed resources.

---

## Learning Objectives

By the end of this module, you will be able to:

- Describe the evolution from traditional antivirus to NGAV to EDR and explain the key capability added at each stage.

- Explain what CIS Benchmarks are, how they are structured, and how they are used in enterprise hardening programs.

- Describe the patch management lifecycle and apply a risk-based prioritization approach.

- Explain how full disk encryption protects against physical theft, including the role of the TPM.

- Describe application allowlisting and contrast it with blacklisting, including the specific threat it addresses.

- Distinguish MDM from MAM and identify the appropriate choice for BYOD scenarios.

- Explain the security value of host-based firewalls as a defense-in-depth control.

---

## Primary Readings

### Reading 1 — CIS Benchmarks Overview

Source: [https://www.cisecurity.org/cis-benchmarks/](https://www.cisecurity.org/cis-benchmarks/)

Read: The overview page and download the CIS Benchmark for Windows 10 or Windows 11 (Level 1 sections only — the full document is very long; focus on the Introduction and any 10 hardening controls of your choosing).

Focus areas:

- The Level 1 vs. Level 2 distinction and the rationale for each.

- The format of a CIS recommendation: rationale, impact, and remediation.

- How the benchmark translates to Group Policy or registry settings.

### Reading 2 — CISA Known Exploited Vulnerabilities Catalog

Source: [https://www.cisa.gov/known-exploited-vulnerabilities-catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

Read: The introduction and methodology, then browse any 10 entries to understand the format.

Focus areas:

- How CISA classifies vulnerabilities as "known exploited."

- The remediation deadlines CISA sets for federal agencies and the rationale for those timelines.

- Why the KEV catalog changes patch prioritization for any organization beyond just federal agencies.

### Reading 3 — NIST SP 800-124 Rev. 2: Guidelines for Managing Mobile Device Security

Source: [https://csrc.nist.gov/publications/detail/sp/800-124/rev-2/final](https://csrc.nist.gov/publications/detail/sp/800-124/rev-2/final)

Read: Section 4 (Mobile Device Management Technologies) and Section 5 (Recommendations).

Focus areas:

- The distinction between device management (MDM) and application management (MAM/containerization).

- Security considerations for BYOD vs. corporate-owned device policies.

- The role of remote wipe and certificate-based authentication in mobile security.

---

## Supplemental Readings

### Reading 4 — Microsoft: BitLocker Overview

Source: [https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/)

Read: The overview and "How BitLocker Works" sections.

Focus areas:

- The role of the TPM in storing and protecting the BitLocker encryption key.

- The difference between TPM-only protection and TPM + PIN protection.

- Recovery key scenarios and why they must be stored securely and separately.

### Reading 5 — CISA Endpoint Security Guide

Source: [https://www.cisa.gov/sites/default/files/publications/Capacity_Enhancement_Guide-Securing_Endpoints.pdf](https://www.cisa.gov/sites/default/files/publications/Capacity_Enhancement_Guide-Securing_Endpoints.pdf)

Read: The full document (approximately 20 pages).

Focus areas:

- EDR capabilities and the distinction from traditional AV.

- Application allowlisting as a high-impact control.

- The relationship between endpoint controls and the MITRE ATT&CK framework.

---

## Concept Reference Tables

### Table 1 — Endpoint Protection Technology Comparison

| Technology | Detection Method | Capability | Exam Use Case |
|---|---|---|---|
| Traditional AV | Signature-based | Detect and quarantine known malware | Legacy environments |
| NGAV | Behavioral + ML | Detect polymorphic and behavioral threats | Modern signature-less malware |
| EDR | Continuous telemetry + behavioral | Detect, investigate, respond, hunt | Forensic timeline, incident response |
| XDR | Multi-domain telemetry correlation | Unified detection across endpoint/network/cloud | Enterprise SOC integration |

### Table 2 — Full Disk Encryption Options

| Product | Platform | Key Storage | Exam Notes |
|---|---|---|---|
| BitLocker | Windows | TPM + AD/Azure AD | TPM + PIN = strongest; recovery key required |
| FileVault | macOS | iCloud or institutional key | Enterprise uses MDM-managed recovery key |
| LUKS | Linux | Passphrase or key file | Common in enterprise Linux deployments |
| Self-Encrypting Drive (SED) | Hardware-level | Drive firmware | Effective only with proper user-defined key |

### Table 3 — Mobile Device Management Models

| Model | Scope | Best For | Privacy Impact |
|---|---|---|---|
| MDM | Full device | Corporate-owned devices | High — organization sees full device |
| MAM | Application and data only | BYOD | Low — personal data untouched |
| COPE | Full device, personal use permitted | Corporate-issued with personal use policy | Medium |
| COBO | Full device, business only | High-security or kiosk deployments | High |

### Table 4 — Application Control Comparison

| Approach | Default Stance | Effectiveness Against Zero-Day | Operational Complexity |
|---|---|---|---|
| Blacklisting (AV) | Allow all, block known bad | Low | Low |
| Allowlisting | Block all, permit approved | High | High |
| NGAV behavioral | Block suspicious behavior | Medium-High | Medium |
| EDR detection | Detect and respond | High (but post-execution) | Medium |

---

## Key Terms and Definitions

**Antivirus (AV)** — Endpoint protection using signature-based detection of known malware.

**NGAV** — Next-Generation Antivirus; adds behavioral analysis and machine learning to signature detection.

**EDR** — Endpoint Detection and Response; provides continuous telemetry recording, behavioral detection, threat hunting, and automated response.

**XDR** — Extended Detection and Response; correlates endpoint, network, cloud, and identity telemetry.

**CIS Benchmarks** — Industry-standard configuration hardening baselines for operating systems, applications, and cloud platforms, developed by the Center for Internet Security.

**System Hardening** — The process of reducing a system's attack surface by removing unnecessary components and applying secure configurations.

**Gold Image** — A standardized, pre-hardened OS image used for deploying new systems with a consistent security baseline.

**Patch Management** — The lifecycle of identifying, testing, and deploying software updates to address vulnerabilities.

**CISA KEV** — CISA Known Exploited Vulnerabilities catalog; authoritative list of vulnerabilities actively exploited in the wild.

**Compensating Control** — A substitute control applied when the primary control (patching) cannot be implemented immediately.

**FDE** — Full Disk Encryption; encrypts all data on a storage device.

**BitLocker** — Microsoft's full disk encryption solution for Windows.

**TPM** — Trusted Platform Module; a hardware chip that stores cryptographic keys and performs boot-time integrity measurements.

**Secure Boot** — UEFI feature that verifies bootloader signatures before execution, preventing bootkits.

**SED** — Self-Encrypting Drive; hardware-level disk encryption built into the drive firmware.

**Application Allowlisting** — Security control permitting only approved applications to execute; blocks all others by default.

**Application Blacklisting** — Security control blocking known malicious applications; permits all others by default.

**AppLocker** — Windows built-in application control policy tool.

**WDAC** — Windows Defender Application Control; kernel-level application execution policy tool.

**MDM** — Mobile Device Management; platform for managing and enforcing security policies on mobile devices.

**MAM** — Mobile Application Management; manages only corporate applications and their data, not the full device.

**BYOD** — Bring Your Own Device; policy allowing employees to use personal devices for work.

**Remote Wipe** — MDM capability to erase all data on a managed device remotely.

**Host-Based Firewall** — A firewall running on the individual endpoint, independent of network perimeter controls.

**Configuration Drift** — The gradual divergence of a system's configuration from the approved security baseline over time.

---

## Security+ Exam Alignment

The following SY0-701 exam objectives are covered in this module:

- 2.5 — Explain the purpose of mitigation techniques used to secure the enterprise.

- 4.1 — Given a scenario, apply common access control concepts.

- 4.6 — Given a scenario, implement and configure wireless security.

---

## Critical Thinking Questions

1. An organization relies entirely on signature-based antivirus across 5,000 endpoints. A new ransomware campaign uses a polymorphic packer that generates a unique binary for each target, ensuring no two samples share the same hash. Why does this defeat signature-based AV? What would EDR offer that AV cannot in this scenario?

2. A security team is trying to decide between deploying application allowlisting and deploying EDR as their primary endpoint control enhancement. Compare the two approaches: what threats does each control best address, what are the operational requirements of each, and under what circumstances would you choose one over the other?

3. A company deploys BitLocker with TPM-only protection (no PIN required). A laptop is stolen from an unlocked, powered-off state. Is the data protected? Now consider the same scenario where the attacker is a sophisticated nation-state actor who can manipulate the boot process. What does TPM-only protection not defend against?

4. An organization allows employees to use personal iPhones for corporate email and Slack. The CISO wants the ability to remote-wipe corporate data if an employee is terminated without affecting the employee's personal photos and messages. Which mobile device management model supports this requirement? What are the limitations?

5. A patch for a critical vulnerability is released. The vulnerability has a CVSS score of 9.8 and is listed on the CISA KEV catalog. The affected system is a legacy manufacturing control system that cannot be patched without a four-hour production shutdown. What is your recommended approach? Identify the compensating controls and the timeline.

---

## Review Checklist

Before taking the Module 08 quiz, verify you can do each of the following without notes:

- Explain what EDR provides that traditional AV cannot.

- State what CIS Level 1 and Level 2 benchmarks represent.

- Describe the patch management lifecycle in five steps.

- Explain what the CISA KEV catalog is and how it changes patch prioritization.

- Describe how BitLocker with TPM protects a stolen laptop.

- Explain why application allowlisting is more effective than blacklisting against zero-days.

- Distinguish MDM from MAM and identify when each is appropriate.

- Explain why a host-based firewall provides protection that a perimeter firewall cannot.

---

Module 08 Reading Guide — End
