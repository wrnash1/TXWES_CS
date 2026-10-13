# Reading Guide: Module 04 – Enterprise Security & Infrastructure Hardening

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CSC-6361 &BULL; ADVANCED COMPUTER NETWORKS (GRADUATE LEVEL)</text>
    
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

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Cisco Systems / David Bombal / Stanford &bull; CSC-6361 Module 04</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=k9Znd_f6rO0" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/k9Znd_f6rO0" title="Advanced Computer Networks, BGP, OSPF & SDN Architectures" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Advanced Computer Networks, BGP, OSPF & SDN Architectures</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

## CSC-6361 Advanced Computer Networks | Graduate Level
## Week 4: November 9–15, 2026

---

## Learning Objectives
By completing this reading guide, you will be able to:
1. Configure AAA using TACACS+ and RADIUS with proper fallback to local authentication.
2. Design and implement named extended ACLs for traffic filtering, including `established` keyword and reflexive ACLs.
3. Apply Control Plane Policing (CoPP) to protect router CPU from denial-of-service.
4. Configure Layer 2 security features: DHCP Snooping, Dynamic ARP Inspection, IP Source Guard, Port Security, and 802.1X.
5. Harden BGP sessions with prefix filtering, max-prefix limits, and MD5 authentication.
6. Build a comprehensive management plane hardening baseline for Cisco IOS devices.

---

## Required Free Readings

### 1. NIST SP 800-41 Rev 1 — Guidelines on Firewalls and Firewall Policy (Free)
**URL:** https://csrc.nist.gov/publications/detail/sp/800-41/rev-1/final
**Focus:** Section 3 (Firewall technologies), Section 4 (Firewall policy design). Provides the policy framework that ACL design must support.

### 2. IETF RFC 8446 — Transport Layer Security (TLS) 1.3 (Free)
**URL:** https://datatracker.ietf.org/doc/html/rfc8446
**Focus:** Section 1 (Introduction), Section 2 (Protocol Overview). Understanding TLS 1.3 is essential for evaluating encrypted management traffic (HTTPS, SSH).

### 3. Cisco AAA Configuration Guide — IOS XE (Free)
**URL:** https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_usr_aaa/configuration/xe-16/sec-usr-aaa-xe-16-book.html
**Focus:** TACACS+ vs. RADIUS configuration, aaa authentication/authorization/accounting commands, local fallback.

### 4. Cisco Layer 2 Security Guide — DHCP Snooping, DAI, IP Source Guard (Free)
**URL:** https://www.cisco.com/c/en/us/support/docs/lan-switching/ip-source-guard/116082-config-ip-source-guard-00.html
**Focus:** DHCP Snooping configuration, DAI validation, IP Source Guard — configuration and verification.

### 5. Cisco CIS Benchmark for IOS (Free Community Version)
**URL:** https://www.cisecurity.org/cis-benchmarks
Download the CIS Cisco IOS Benchmark (requires free registration). This is the industry-standard hardening checklist for Cisco IOS devices.
**Focus:** Review Level 1 (basic hardening) recommendations: management plane controls, SSH, service disabling.

### 6. Cisco BGP Security Best Practices (Free)
**URL:** https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/26634-bgp-best-practices.html
**Focus:** Prefix filtering, max-prefix, MD5 authentication, GTSM (TTL security).

---

## Key Security Hardening Baseline

### Device Hardening Checklist (Copy to Every IOS Device)
```
! Disable unnecessary services
no service tcp-small-servers
no service udp-small-servers
no ip finger
no ip http server
ip http secure-server
no ip bootp server
no cdp run                    ! Disable CDP on external-facing interfaces only

! SSH hardening
ip ssh version 2
ip ssh time-out 60
ip ssh authentication-retries 3
crypto key generate rsa modulus 2048

! Banner (legal warning — required for prosecution in many jurisdictions)
banner login ^
AUTHORIZED USERS ONLY. Unauthorized access is a federal crime under the
Computer Fraud and Abuse Act (18 U.S.C. 1030). All activity is logged.
^

! Disable EXEC sessions on console after inactivity
line console 0
 exec-timeout 5 0
 login authentication default

line vty 0 15
 transport input ssh
 exec-timeout 10 0
 login authentication default
 access-class MGMT-ACCESS in

! Logging
logging buffered 65536 informational
logging trap informational
service timestamps log datetime msec localtime show-timezone
service timestamps debug datetime msec localtime

! Password security
service password-encryption
security passwords min-length 12
enable secret 0 [use strong password]
```

### AAA Quick Reference
```
aaa new-model
tacacs server PRIMARY
 address ipv4 10.99.99.10
 key TacacsKey123
aaa group server tacacs+ ADMIN-GROUP
 server name PRIMARY
aaa authentication login default group ADMIN-GROUP local
aaa authorization exec default group ADMIN-GROUP local
aaa authorization commands 15 default group ADMIN-GROUP local
aaa accounting exec default start-stop group ADMIN-GROUP
aaa accounting commands 15 default start-stop group ADMIN-GROUP
```

### Layer 2 Security Quick Reference
```
! DHCP Snooping
ip dhcp snooping
ip dhcp snooping vlan 10,20,30
ip dhcp snooping database flash:dhcp-snooping.db
interface [uplink to DHCP server]
 ip dhcp snooping trust
interface range [access ports]
 ip dhcp snooping limit rate 15

! DAI (requires DHCP Snooping enabled first)
ip arp inspection vlan 10,20,30
interface [uplink]
 ip arp inspection trust

! IP Source Guard
interface [access port]
 ip verify source

! Port Security
interface [access port]
 switchport mode access
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation restrict
```

---

## Verification Commands Quick Reference
```
! AAA
show aaa sessions
show tacacs
debug aaa authentication

! ACLs
show ip access-lists                        ! View ACL hit counters
show ip access-lists ALLOW-WEB-ONLY        ! Specific ACL

! Layer 2 Security
show ip dhcp snooping binding               ! View binding table (MAC/IP/VLAN/Port)
show ip dhcp snooping statistics            ! Dropped packet counters
show ip arp inspection vlan 10              ! DAI statistics and forwarded/dropped counts
show port-security interface FastEth0/3    ! Port security status and MAC count
show dot1x interface FastEthernet0/5       ! 802.1X status

! BGP Security
show ip bgp neighbor 203.0.113.1           ! BGP session status, prefix counts
show ip bgp regexp _                        ! All BGP routes (debugging)
show ip prefix-list                         ! View configured prefix lists
```

---

## Graduate Discussion Prompt (Due Sunday, November 15, 2026, 11:59 PM CST)

**Scenario:** A small regional bank has experienced a security incident. A contractor connected an unauthorized laptop to a conference room Ethernet jack. The laptop was running a rogue DHCP server and an ARP spoofing tool. Within minutes, workstations throughout the building began sending traffic through the attacker's laptop instead of the legitimate default gateway — a classic man-in-the-middle attack that captured plaintext credentials for internal web applications.

**Write a graduate-level post (400+ words) addressing:**
1. **Attack Mechanics:** Explain precisely how the DHCP-based attack worked (rogue DHCP server) and how the ARP spoofing attack worked. What layer of the OSI model is each attack operating at, and why do traditional IP-based security tools (firewalls, IDS) fail to catch these attacks?
2. **Layer 2 Controls:** Which specific switch security features would have prevented each attack? For each control, explain exactly why it would have blocked the attack — not just that it would have.
3. **802.1X as a Systemic Solution:** The bank is considering deploying 802.1X with Cisco ISE to all wired access ports. What would have been different in this specific incident if 802.1X had been in place? What are the deployment challenges for 802.1X in a mixed environment (some devices cannot authenticate — printers, VoIP phones, IoT)?
4. **Defense-in-Depth Argument:** A bank executive argues that deploying 802.1X is expensive and complex, and that requiring VPN for all internal traffic would solve the same problem. Evaluate this argument — is it correct, and what are the trade-offs?

**Citation:** Cite NIST SP 800-41 (firewall/ACL policy), CIS Benchmarks for Cisco IOS, or a peer-reviewed paper on Layer 2 security attacks (available via IEEE Xplore through TXWES West Library).

---

## 9. Supplemental Resources

**1. Cisco Security Configuration Guide — AAA**
https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_usr_aaa/configuration/xe-16/sec-usr-aaa-xe-16-book.html
Authoritative Cisco IOS-XE configuration reference for AAA, TACACS+, and RADIUS implementation.

**2. NIST SP 800-53 — Security and Privacy Controls**
https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
Federal standard for security controls applicable to enterprise network infrastructure hardening.

**3. IETF RFC 2865 — Remote Authentication Dial In User Service (RADIUS)**
https://datatracker.ietf.org/doc/html/rfc2865
The original RADIUS protocol specification — essential reading for understanding the authentication exchange.

**4. Cisco White Paper — Control Plane Policing**
https://www.cisco.com/c/en/us/support/docs/quality-of-service-qos/qos-policing/116664-technote-qos-00.html
Technical explanation of CoPP design principles, rate-limit categories, and configuration examples.

---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 04 – Enterprise Security & Infrastructure Hardening** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 04 – Enterprise Security & Infrastructure Hardening**, we decompose the execution lifecycle into sequential, verifiable stages:

```
[Phase 1: Ingestion & Validation] ──> [Phase 2: State Transformation] ──> [Phase 3: Verification & Persistence]
       │                                       │                                       │
       ▼                                       ▼                                       ▼
Input Sanitization, Schema              Algorithmic Execution,                  Cryptographic Hashing,
Validation & Boundary Checks             Concurrency Arbitration                 Write-Ahead Logging & Audit
```

1. **Ingestion & Boundary Verification:** Inputs entering the boundary of this architecture must undergo strict structural validation. In software systems, this prevents buffer overflows, injection vectors, and malformed state propagation. In enterprise and governance systems, this ensures data integrity before ledger entry.
2. **State Transformation & Concurrency Arbitration:** During execution, intermediate states must maintain transactional isolation. Whether managing distributed lock managers (DLM), thread synchronization, or multi-area routing convergence, race conditions must be mathematically eliminated using provable synchronization primitives.
3. **Commit, Persistence, and Telemetry:** Once state transitions execute successfully, atomic commits guarantee persistence across non-volatile memory or distributed journals. Comprehensive telemetry events are simultaneously emitted to structured observability pipelines.

---

## 4. Real-World Engineering Scenarios & Failure Mode Analysis

### Case Study: High-Impact Enterprise Failure Mode
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 04 – Enterprise Security & Infrastructure Hardening**:

* **Incident Context:** During peak quarterly processing, an enterprise infrastructure stack running critical financial or operational workflows experienced cascading timeouts and data corruption.
* **Root Cause Diagnostics:** Technicians misconfigured operational parameters, ignoring queue saturation thresholds and bypassing circuit-breaker protections. When transient latency occurred on upstream dependencies, worker threads blocked indefinitely, leading to resource starvation, memory exhaustion, and silent data drops.
* **Remediation Architecture:**
  * Implemented an exponential backoff retry policy coupled with full jitter to eliminate thundering herd phenomena.
  * Deployed strict isolation boundaries (bulkheads) to restrict cascading failures to isolated tenant pools.
  * Enforced continuous automated telemetry alarms monitoring p99 latency, queue depth, and error budget exhaustion.

```python
# Production Architectural Invariant: Resilient Execution with Circuit Breaking
import time
import random

class ResilientExecutionGovernor:
    def __init__(self, failure_threshold=5, recovery_timeout=30):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF-OPEN

    def execute_with_guard(self, operation, *args, **kwargs):
        current_time = time.time()
        
        # Check Circuit State
        if self.state == "OPEN":
            if current_time - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF-OPEN"
            else:
                raise RuntimeError("CircuitBreakerOpen: Request rejected to preserve system invariants.")

        try:
            result = operation(*args, **kwargs)
            if self.state == "HALF-OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = current_time
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
            raise e
```

---

## 5. Critical Misconceptions & Certification Exam Traps

In both certification examinations (such as CompTIA, Cisco, AWS, Scrum.org) and doctoral defense committees, specific high-yield traps consistently cause students to fail. Review these critical distinctions:

| Common Student Misconception | Architectural Reality & Truth | Consequence of Misunderstanding |
|---|---|---|
| *"More resources or threads linearly scale performance."* | Amdahl's Law proves speedup is strictly capped by the sequential fraction of the task; thread contention adds lock overhead. | Costly infrastructure overprovisioning with degraded throughput. |
| *"Redundancy alone guarantees high availability."* | Unmonitored redundancy creates hidden common-mode failure points and split-brain states without quorum arbitration. | Catastrophic double-outages and corrupted ledger state. |
| *"Default vendor configurations are production-ready."* | Vendor defaults prioritize ease of setup over least privilege, hardened encryption, and tuned memory limits. | Severe security vulnerability exposure and predictable resource exhaustion. |
| *"Fast recovery is a substitute for data integrity."* | Recovering quickly with inconsistent or unverified state compounds operational damage beyond the initial downtime. | Long-term ledger corruption and regulatory audit failure. |

---

## 6. Formative Knowledge Synthesis & Applied Defense Prompts

To confirm mastery before proceeding to this module's laboratory exercises and synthesis quizzes, synthesize responses to the following peer-review prompts:

### Mastery Check 1: Invariant Analysis
> **Question:** In the context of **Module 04 – Enterprise Security & Infrastructure Hardening**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**
