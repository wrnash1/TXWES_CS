# Reading Guide: Module 14 — SSH and Remote Administration

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3325 &BULL; OPERATING SYSTEM ADMINISTRATION</text>
    
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
      <strong style="margin-left: 10px; font-size: 14px;">CompTIA / LearnLinuxTV &bull; CIS-3325 Module 14</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78" title="CompTIA Linux+ (XK0-005) & LPI Linux Essentials Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>CompTIA Linux+ (XK0-005) & LPI Linux Essentials Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->




## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Overview

This guide accompanies the Module 14 video lectures on SSH, secure file transfer, port forwarding, and Ansible. Estimated reading and review time: 90 minutes.

---

### Learning Objectives

After completing this module, you will be able to:

- Explain asymmetric key cryptography as applied to SSH authentication
- Generate Ed25519 and RSA SSH key pairs with appropriate security parameters
- Distribute and install public keys correctly using `ssh-copy-id` and manual methods
- Harden `sshd_config` by disabling root login, password auth, and applying access controls
- Transfer files securely using `scp` and SFTP
- Configure SSH port forwarding for local, remote, and dynamic tunneling
- Write basic Ansible inventories and playbooks for multi-host administration

---

### Key Terms

**Asymmetric Cryptography**
A cryptographic system using mathematically linked key pairs (public and private). Data encrypted with one key can only be decrypted with the other.

**Ed25519**
An elliptic curve digital signature algorithm considered the current best practice for SSH keys. Fast, compact, and secure.

**Passphrase**
An optional password that encrypts the private key file on disk. Without a passphrase, anyone who copies your private key can use it.

**ssh-agent**
A background process that holds decrypted private keys in memory, allowing key-based authentication without re-entering the passphrase for each connection.

**authorized_keys**
A file in `~/.ssh/` on the server that contains the public keys permitted to authenticate as that user.

**known_hosts**
A file in `~/.ssh/` on the client that records the public key fingerprints of servers you have previously connected to. Used to detect host key changes (potential MITM attacks).

**Port Forwarding**
Redirecting network traffic from one port through an SSH connection to another port on a different host.

**SOCKS Proxy**
A protocol-agnostic proxy server. SSH dynamic forwarding creates a SOCKS5 proxy that can handle any TCP traffic.

**Ansible**
An agentless IT automation platform that uses SSH and Python to configure systems, deploy applications, and orchestrate workflows.

**Idempotent**
An operation that produces the same result regardless of how many times it is applied. Ansible modules are idempotent: running them multiple times does not cause repeated changes.

---

### Section 1: SSH Protocol Details

**OpenSSH Components**

The OpenSSH package provides:

- `ssh` — client
- `sshd` — server daemon
- `ssh-keygen` — key generation and management
- `ssh-copy-id` — public key distribution
- `ssh-agent` — key caching daemon
- `ssh-add` — add keys to ssh-agent
- `scp` — file copy
- `sftp` — interactive file transfer
- `ssh-keyscan` — gather host public keys

**Connection Sequence**

1. TCP connection established (port 22 by default)
2. Protocol version negotiation
3. Algorithm negotiation (ciphers, MACs, key exchange)
4. Key exchange — server's host key verified against `known_hosts`
5. Authentication — public key or password
6. Session — shell, command, or subsystem (SFTP)

**Host Key Verification**

On first connection to a new host, SSH shows a fingerprint:

```
The authenticity of host 'server.example.com' can't be established.
ED25519 key fingerprint is SHA256:abc123...
Are you sure you want to continue connecting (yes/no)?
```

Before accepting, verify the fingerprint out-of-band (by phone, ticketing system, or server console). Accepting an unverified fingerprint is a man-in-the-middle vulnerability.

To view a server's host key fingerprint:

```bash
ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
```

**Host Key Rotation**

When a server is reinstalled or its host key changes, SSH clients will refuse to connect with a TOFU (Trust On First Use) warning:

```
WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
```

Remove the old entry from `known_hosts`:

```bash
ssh-keygen -R hostname
ssh-keygen -R 192.168.1.10
```

---

### Section 2: SSH Key Management Best Practices

**Dedicated Keys per Role**

Use separate key pairs for different purposes:

- Personal workstation key (`~/.ssh/id_ed25519`)
- Deployment automation key (`~/.ssh/id_ed25519_deploy`)
- Backup automation key (`~/.ssh/id_ed25519_backup`)

This limits the blast radius if one key is compromised.

**Key Rotation**

Rotate SSH keys regularly (at minimum annually, or immediately after a potential compromise):

1. Generate new key pair
2. Add new public key to all `authorized_keys` files
3. Test new key works
4. Remove old public key from all `authorized_keys` files
5. Revoke/delete old private key

**ssh-agent Best Practices**

Start ssh-agent at login:

```bash
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_ed25519
```

Limit key lifetime in agent:

```bash
ssh-add -t 3600 ~/.ssh/id_ed25519   # Expire after 1 hour
```

List loaded keys:

```bash
ssh-add -l
```

Remove all keys from agent:

```bash
ssh-add -D
```

**Certificate-Based Authentication**

SSH supports CA-signed certificates as an alternative to per-host `authorized_keys` management. An SSH certificate authority signs user and host keys:

```bash
# Sign a user key (CA side)
ssh-keygen -s ca_key -I "username" -n "username" -V +52w user_key.pub
```

This scales better than managing `authorized_keys` across hundreds of servers. The Linux+ exam covers this conceptually.

---

### Section 3: sshd_config Reference

**Full Hardened sshd_config Options**

| Directive | Recommended Value | Effect |
|-----------|------------------|--------|
| `Port` | 22 or custom | SSH listening port |
| `PermitRootLogin` | `no` | Block root SSH access |
| `PasswordAuthentication` | `no` | Require key auth |
| `PermitEmptyPasswords` | `no` | Block empty passwords |
| `PubkeyAuthentication` | `yes` | Enable key auth |
| `MaxAuthTries` | `3` | Limit auth attempts per connection |
| `MaxSessions` | `10` | Max sessions per connection |
| `ClientAliveInterval` | `300` | Keepalive interval (seconds) |
| `ClientAliveCountMax` | `2` | Keepalive failure limit |
| `AllowUsers` | List | Whitelist specific users |
| `AllowGroups` | `sshusers` | Whitelist specific groups |
| `X11Forwarding` | `no` | Disable X11 forwarding |
| `AllowTcpForwarding` | `no` | Disable port forwarding (restrictive) |
| `Banner` | `/etc/ssh/banner` | Show pre-auth warning banner |
| `LogLevel` | `VERBOSE` | Enhanced logging |
| `LoginGraceTime` | `60` | Seconds to complete authentication |

**The Banner Directive**

A pre-authentication login banner is required by many compliance frameworks (PCI-DSS, HIPAA). Create the banner file:

```bash
sudo nano /etc/ssh/ssh_banner
```

Sample banner content:

```
*********************************************************************
AUTHORIZED ACCESS ONLY
This system is for authorized users only. All activity is monitored
and logged. Unauthorized access will be prosecuted.
*********************************************************************
```

Set in `sshd_config`:

```
Banner /etc/ssh/ssh_banner
```

**Match Blocks**

`sshd_config` supports conditional blocks with the `Match` directive:

```
Match Group sftp-only
    ForceCommand internal-sftp
    ChrootDirectory /srv/sftp/%u
    PasswordAuthentication yes
    X11Forwarding no
    AllowTcpForwarding no
```

Match blocks apply only to connections that match the specified criteria. Supported keywords: `User`, `Group`, `Host`, `LocalAddress`, `LocalPort`, `Address`.

---

### Section 4: File Transfer Tools Comparison

| Tool | Protocol | Interactive | Compression | Incremental | Best For |
|------|----------|-------------|-------------|-------------|---------|
| `scp` | SCP/SFTP | No | Yes | No | Quick one-off copies |
| `sftp` | SFTP | Yes | No | No | Manual file management |
| `rsync` | rsync over SSH | No | Yes | Yes | Synchronization, backups |
| `git` | SSH/HTTPS | No | Yes | Yes | Code deployment |

**rsync Advanced Options**

```bash
# Mirror with delete (remove files on dest that don't exist on source)
rsync -avz --delete /source/ user@host:/dest/

# Exclude patterns
rsync -avz --exclude='*.tmp' --exclude='.git' /source/ user@host:/dest/

# Dry run (show what would be transferred)
rsync -avz --dry-run /source/ user@host:/dest/

# Bandwidth limit (100 KB/s)
rsync -avz --bwlimit=100 /source/ user@host:/dest/
```

---

### Section 5: Ansible Architecture

**Ansible Components**

- **Control Node**: the machine running Ansible (your workstation or CI/CD server)
- **Managed Nodes**: the servers being configured (no agent required)
- **Inventory**: list of managed nodes and groups
- **Playbook**: YAML file describing desired states
- **Module**: reusable Ansible unit that performs a specific action
- **Role**: structured directory of tasks, handlers, templates, and files for a reusable configuration
- **Task**: a single call to an Ansible module
- **Handler**: a task triggered by `notify:` that runs once at the end of a play (typically service restarts)

**Ansible Inventory Formats**

INI format (simple):

```ini
[webservers]
web01 ansible_host=192.168.1.10 ansible_user=admin
web02 ansible_host=192.168.1.11

[dbservers]
db01 ansible_host=192.168.1.20 ansible_ssh_private_key_file=~/.ssh/db_key
```

YAML format (more features):

```yaml
all:
  children:
    webservers:
      hosts:
        web01:
          ansible_host: 192.168.1.10
        web02:
          ansible_host: 192.168.1.11
```

**Ansible Variables**

Variables can be defined at multiple levels:

- Inventory variables (per-host or per-group)
- Playbook `vars:` section
- Role defaults and variables
- Command line `-e "var=value"`
- Vault-encrypted files for secrets

Example with variables:

```yaml
---
- name: Deploy application
  hosts: webservers
  vars:
    app_port: 8080
    app_user: appuser

  tasks:
    - name: Create application user
      user:
        name: "{{ app_user }}"
        state: present
```

---

### Practice Review Questions

Answer these before taking the quiz:

1. What is the difference between `~/.ssh/id_ed25519` and `~/.ssh/id_ed25519.pub`?

2. What permissions must `~/.ssh/authorized_keys` have for SSH to accept it?

3. What is the effect of setting `PasswordAuthentication no` in `sshd_config` before distributing SSH keys to all administrators?

4. Write the `ssh` command to forward local port 3306 to `db.internal:3306` through a bastion at `bastion.example.com`.

5. What is the difference between `scp -r` and `rsync -avz`?

6. In Ansible, what is the purpose of a handler?

7. You want to test an Ansible playbook without making any changes. What flag do you add?

8. What does the `become: yes` directive in an Ansible playbook do?

---

#
---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 14 — SSH and Remote Administration** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 14 — SSH and Remote Administration**, we decompose the execution lifecycle into sequential, verifiable stages:

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
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 14 — SSH and Remote Administration**:

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
> **Question:** In the context of **Module 14 — SSH and Remote Administration**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**


## Additional Resources

- `man 5 sshd_config` — complete SSH server configuration reference
- `man 1 ssh-keygen` — key generation options
- `man 1 ssh` — SSH client options including port forwarding
- Ansible Documentation: [docs.ansible.com](https://docs.ansible.com)
- CompTIA Linux+ XK0-005 Objectives: 2.1 (Security), 4.3 (Automation)
- NIST SP 800-82: Guide to Industrial Control Systems Security (SSH guidance)

---

### Key Takeaways

- Always use Ed25519 for new key generation. RSA 4096 for compatibility with older systems.
- Private key permissions must be `600`; `~/.ssh/` must be `700`. SSH silently ignores improperly permissioned keys.
- Never disable password authentication in `sshd_config` before confirming key authentication works from another terminal.
- Port forwarding (`-L`, `-R`, `-D`) turns SSH into a versatile secure tunneling platform.
- Ansible's agentless model means SSH must be working correctly before Ansible can manage hosts — fixing SSH issues is always the first step in Ansible troubleshooting.

---

## 9. Supplemental Resources

**1. [OpenSSH Manual — ssh.com Academy](https://www.ssh.com/academy/ssh/command)**
The SSH Academy provides accessible, well-organized documentation for all OpenSSH tools: `ssh`, `scp`, `sftp`, `ssh-keygen`, `ssh-agent`, and `ssh-add`. Particularly useful sections cover key algorithm choices (Ed25519 vs RSA), port forwarding types with diagrams, and the `~/.ssh/config` file directives. A strong companion to the official man pages for Module 14 lab preparation.

**2. [Ansible Getting Started Documentation](https://docs.ansible.com/ansible/latest/getting_started/index.html)**
The official Ansible getting started guide. Covers installation, inventory file formats (INI and YAML), ad-hoc commands, basic playbook structure (tasks, modules, handlers), variables, and facts. This is the authoritative source for the Ansible concepts introduced in Module 14 and the starting point for the CompTIA Linux+ automation objectives (XK0-005 Domain 4.3).

**3. [SSH Hardening Guide — Mozilla InfoSec](https://infosec.mozilla.org/guidelines/openssh)**
Mozilla's published SSH hardening guidelines, maintained by their security engineering team. Provides specific `sshd_config` and `ssh_config` recommendations with rationale, organized into Modern, Intermediate, and Old compatibility tiers. Covers key exchange algorithms, ciphers, MACs, authentication methods, and operational security practices. Directly applicable to the Module 14 lab's sshd_config hardening tasks.
