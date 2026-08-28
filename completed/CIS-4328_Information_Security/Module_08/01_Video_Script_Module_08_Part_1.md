# Video Script: Module 08 — Endpoint Security (Part 1 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

### [INTRO — 0:00]

Welcome to Module 08, Part 1. I'm Professor Nash.

Every network ultimately terminates at an endpoint — a laptop, workstation, server, mobile device, or IoT sensor. Endpoints are where users work, where data lives, and where most attacks land. Perimeter security stops threats at the network edge; endpoint security stops them when they arrive on the device — or, increasingly, detects them after they have already arrived.

Module 08 covers the full endpoint security stack: the evolution from antivirus to EDR, system hardening using CIS benchmarks, patch management, host-based firewalls, full disk encryption, application allowlisting, and mobile device management.

Security+ Domain 2 and Domain 4 both draw from endpoint security concepts. This domain is also where you will see the most performance-based questions — configuring controls, identifying appropriate tools, and making risk-based decisions about protection layers.

Part 1 covers the foundational concepts and the technology landscape. Part 2 covers configurations, hardening, MDM, and exam traps.

---

### [SECTION 1 — Antivirus to EDR: The Evolution — 1:00]

Endpoint protection has gone through three distinct generations. Understanding the evolution explains why the exam tests both legacy and modern approaches.

#### Generation 1 — Traditional Antivirus (AV)

Traditional AV operates on **signature-based detection**: every known malware sample has a signature — typically a hash or a byte pattern — stored in a signature database. When AV scans a file, it compares the file to the signature database.

Strengths: effective against known malware, low false positives.

Weaknesses: useless against unknown malware (zero-days), ineffective against fileless malware (no file to scan), requires frequent signature updates. An attacker who modifies even a single byte of known malware produces a different hash — bypassing signature detection.

#### Generation 2 — Next-Generation Antivirus (NGAV)

NGAV added **behavioral analysis and machine learning** on top of signature detection. Rather than matching a known signature, NGAV observes what a process does and classifies it as malicious based on behavior.

Example: NGAV can flag a process that reads thousands of files and renames them with a `.locked` extension — behavior characteristic of ransomware — even if the ransomware's signature is unknown.

Strengths: detects novel and polymorphic malware; detects some fileless attacks.

Weaknesses: higher false positive rate than signature AV; still limited in forensic capability.

#### Generation 3 — EDR (Endpoint Detection and Response)

**EDR** is the current standard for enterprise endpoint protection. EDR does not just detect — it records, investigates, and responds.

Core EDR capabilities:

- **Continuous monitoring and telemetry recording**: every process execution, file write, registry change, network connection, and user action is logged.

- **Behavioral detection**: flags suspicious activity patterns using machine learning and threat intelligence.

- **Threat hunting**: security analysts can query the EDR telemetry to search for indicators of compromise across all endpoints.

- **Automated response**: EDR can isolate a compromised endpoint from the network, kill a malicious process, or roll back file changes — automatically or on analyst command.

- **Root cause analysis**: because every action is recorded, EDR provides a forensic timeline showing exactly how an attacker entered, what they did, and what they accessed.

**Exam distinction**: Traditional AV prevents. EDR detects, investigates, and responds. When an exam question asks "what tool provides a complete forensic timeline of endpoint activity?" — EDR is the answer.

#### XDR — Extended Detection and Response

**XDR** extends EDR beyond the endpoint by correlating telemetry from network, email, cloud, and identity systems into a unified detection platform. XDR is the evolution beyond EDR when multi-domain visibility is needed.

---

### [SECTION 2 — CIS Benchmarks and System Hardening — 5:30]

**System hardening** is the process of reducing a system's attack surface by removing unnecessary features, disabling unused services, and configuring security settings to meet a defined baseline.

#### CIS Benchmarks

The **CIS (Center for Internet Security) Benchmarks** are the industry-standard configuration baselines for operating systems, applications, databases, and cloud platforms. They are freely available, consensus-developed, and widely accepted by regulators including NIST, PCI DSS, and HIPAA frameworks.

CIS Benchmarks are organized into two levels:

- **Level 1** — practical security improvements with minimal operational impact. Suitable for most environments.

- **Level 2** — higher security settings for environments with elevated risk tolerance for operational disruption. May affect system functionality.

Key hardening actions from CIS Benchmarks:

- Disable guest accounts and default accounts.

- Remove or disable unneeded services and protocols (Telnet, FTP, LLMNR, NetBIOS).

- Configure minimum password length, complexity, and age requirements.

- Enable audit logging and configure log retention.

- Set screen lock timeouts.

- Disable autorun/autoplay for removable media.

- Configure the host-based firewall to deny inbound by default.

- Remove unnecessary software and browser plugins.

**Exam point**: The CIS Benchmarks are the reference standard for hardening. When the exam asks "what provides a standard configuration baseline for operating systems?" — the answer is CIS Benchmarks.

#### Images and Templates

In enterprise environments, hardened configurations are baked into a **gold image** — a standardized OS image that includes the security baseline. All new systems are deployed from the gold image, ensuring consistent hardening from day one.

Configuration drift — systems diverging from the baseline over time — is monitored using **configuration management tools** (Ansible, Puppet, Chef) or **SCAP-compliant scanners** that compare current configurations against the benchmark.

---

### [SECTION 3 — Patch Management — 9:00]

**Patch management** is the process of identifying, testing, and deploying software updates to address vulnerabilities.

#### The Patch Management Cycle

1. **Vulnerability identification** — a new CVE is published or a vulnerability scanner finds an unpatched system.

2. **Risk assessment** — evaluate the severity (CVSS score), exploitability, and the system's exposure.

3. **Testing** — patches are tested in a non-production environment to verify they do not break applications.

4. **Deployment** — patches are pushed to production systems, often in maintenance windows.

5. **Verification** — confirm the patch was applied successfully.

#### Patch Prioritization

Not all patches are equal. Patching everything immediately is operationally infeasible. Prioritization factors:

- CVSS severity score (Critical and High first).

- Active exploitation in the wild (CISA's Known Exploited Vulnerabilities catalog).

- Asset criticality (patch critical servers before general workstations).

- Exposure (internet-facing systems before internal).

**Exam point**: The CISA KEV (Known Exploited Vulnerabilities) catalog is the authoritative source for vulnerabilities under active exploitation. A high-CVSS vulnerability on the KEV catalog requires emergency patching regardless of normal patch cycles.

#### Compensating Controls When Patching Is Not Immediate

When a patch cannot be immediately applied (legacy system, testing required, vendor delay):

- Network isolation or firewall rules to limit exposure.

- IPS signatures to detect exploitation attempts.

- WAF rules for web application vulnerabilities.

- Enhanced monitoring and alerting.

These are **compensating controls** — temporary measures that reduce risk while the primary control (patching) is being prepared.

---

### [SECTION 4 — Host-Based Firewalls — 12:30]

A **host-based firewall** runs on the individual endpoint and controls inbound and outbound connections at the host level.

Why host-based firewalls matter even with perimeter controls:

- Once an attacker is inside the network (via phishing, supply chain, or VPN), the perimeter firewall no longer helps. The host-based firewall provides a final layer of protection.

- Enforces per-host rules even when the device is off the corporate network (traveling employee on a hotel WiFi network).

- Can block lateral movement between endpoints on the same subnet.

Windows Defender Firewall and Linux's `iptables`/`nftables` are examples. Enterprise management platforms (Microsoft Endpoint Manager, Group Policy) deploy and enforce host firewall rules centrally.

**Exam point**: Host-based firewall = endpoint control. Network firewall = perimeter control. Both are needed — defense in depth.

---

### [OUTRO — 14:30]

Part 1 has covered:

- The evolution from signature AV to behavioral NGAV to full EDR with continuous recording and response.

- CIS Benchmarks as the standard hardening reference with Level 1 and Level 2 profiles.

- Patch management lifecycle, prioritization using CVSS and the CISA KEV catalog, and compensating controls.

- Host-based firewalls as an endpoint-level defense that operates independently of network perimeter controls.

In Part 2 we cover full disk encryption, application allowlisting, mobile device management, and the Security+ exam traps specific to this domain.

See you in Part 2.

---

End of Part 1 — Module 08
