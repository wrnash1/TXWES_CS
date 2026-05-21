# Reading Guide: Module 14 - Threat Modeling in DevSecOps

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Introduction

Welcome to **Module 14 - Threat Modeling in DevSecOps**! This module covers threat modeling as the design-phase security activity that identifies potential attack vectors, threat actors, and mitigations before a single line of code is written. In a DevSecOps context, threat modeling is the shift-left security activity that precedes SAST, SCA, and DAST — informing which security controls and pipeline gates are most important for a given system. You will learn structured threat modeling methods (STRIDE), how to map threats to mitigations, and how threat model outputs drive pipeline security requirements. These concepts are tested on the CDP exam and are essential for senior DevSecOps roles.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The CDP certification exam expects you to recognize and apply these concepts in scenario-based questions:

* **Chaos engineering definition**: A discipline of proactively experimenting on a system in production or staging by injecting controlled failures — network latency, service crashes, resource exhaustion — to discover weaknesses before they cause unplanned outages. In a DevSecOps pipeline, chaos engineering validates that security controls (circuit breakers, fallback authentication, secrets rotation on failure) behave correctly under adverse conditions.

* **Failure injection (Chaos Monkey)**: The practice of deliberately terminating service instances (Netflix's Chaos Monkey) or injecting faults (Gremlin, LitmusChaos) into a running system to observe how it degrades. From a security perspective, failure injection tests whether systems fail safe — whether authentication falls back to secure defaults, whether secrets are rotated automatically on node failure, and whether fallback paths maintain security properties.

* **Resilience testing**: Systematic validation that a system recovers correctly from failure scenarios — including security-relevant failures such as a secrets manager becoming unavailable, a certificate expiring, or an API gateway failing. Resilience testing in DevSecOps ensures that security controls do not introduce single points of failure and that graceful degradation maintains an acceptable security posture.

* **Fallback paths**: Pre-defined alternative execution routes that a system follows when a primary path fails. In security-critical systems, fallback paths must be designed with the same security rigor as primary paths — an insecure fallback is as exploitable as an insecure primary path. Threat modeling identifies fallback paths as potential attack surfaces that require explicit security analysis.

---

### 2. Certification Exam Tips

* **STRIDE Threat Categories**: The CDP exam tests the STRIDE framework: Spoofing (false identity), Tampering (unauthorized modification), Repudiation (denying actions), Information Disclosure (data leakage), Denial of Service (availability attacks), Elevation of Privilege (unauthorized privilege gain). Know which mitigation category addresses each threat type.
* **Threat Modeling in the SDLC**: Threat modeling belongs at the design phase — before code is written. It produces a prioritized list of threats that informs which security controls are built into the system and which pipeline gates are required. The CDP exam tests that you can place threat modeling correctly in the SDLC relative to SAST, SCA, and DAST.
* **Attack Trees and Data Flow Diagrams**: Know that threat modeling uses DFDs (Data Flow Diagrams) to identify trust boundaries and data flows, and attack trees to decompose threats hierarchically. The exam may present a DFD and ask you to identify which elements represent trust boundary crossings that require security controls.
* **Study Resource**: The [Microsoft Threat Modeling Tool documentation](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool) and the [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) provide comprehensive references for STRIDE, attack trees, and threat modeling in agile/DevOps workflows — both are relevant to CDP exam scenarios.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading**: Read the [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) — a concise, practical guide to threat modeling in agile environments covering STRIDE, PASTA, data flow diagrams, trust boundaries, and how to integrate threat modeling into sprint ceremonies. This is a direct reference for CDP exam threat modeling questions.
* **Required Video**: Watch the threat modeling and chaos engineering segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg) — covers mapping server failure scenarios, documenting resilience paths, and how chaos engineering validates that security controls survive infrastructure failures.

---

### Lab & Command Integration

In this week's hands-on lab, you will apply threat modeling and resilience analysis by:

* **Map server crash scenarios**: For a sample three-tier web application (frontend, API, database), enumerate at least five STRIDE threat categories — identify the threat, the asset at risk, the attack vector, and the corresponding mitigation or pipeline security gate.
* **Outline system resilience paths handling cluster node drops**: Document what happens to authentication, secrets delivery, and authorization when the secrets manager pod (Vault) becomes unavailable — identifying whether the system fails open (insecure) or fails closed (secure).
* **Document fallback workflows**: For each identified failure scenario, write a one-paragraph security analysis explaining whether the fallback path maintains the required security properties and what remediation is needed if it does not.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand how chaos engineering and threat modeling complement each other in a DevSecOps program.
* [ ] Read the OWASP Threat Modeling Cheat Sheet at [https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html).
* [ ] Watch the threat modeling and chaos engineering segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg).
* [ ] Complete the STRIDE threat enumeration and resilience path analysis in the lab activity.
* [ ] Proceed to the weekly hands-on lab activity.
