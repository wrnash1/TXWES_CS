# Reading Guide: Module 10 - SSH and Remote Access Security

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
      <strong style="margin-left: 10px; font-size: 14px;">CompTIA / LearnLinuxTV &bull; CIS-3325 Module 10</strong>
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




## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Exam Domain:** Domain 2.0 - Security

---

### Glossary

**SSH (Secure Shell)** - An encrypted network protocol for remote terminal access, file transfer, and port forwarding. Replaced insecure protocols like Telnet and rsh.

**Host Key** - A server's permanent key pair used to identify it to SSH clients. The public half is sent to clients during connection; clients store it in ~/.ssh/known_hosts.

**Key Pair** - A matched set of a private key and a public key. The private key proves identity; the public key is distributed to servers. Mathematically linked: only the holder of the private key can prove ownership.

**authorized_keys** - A file in ~/.ssh/ on the server that lists public keys whose owners are allowed to log in as that user without a password.

**known_hosts** - A file in ~/.ssh/ on the client that stores the host keys of previously connected servers. Used to detect man-in-the-middle attacks.

**sshd_config** - The SSH server daemon configuration file at /etc/ssh/sshd_config. Controls what the server accepts.

**ssh_config** - The SSH client configuration file at /etc/ssh/ssh_config. Can be overridden by ~/.ssh/config for per-user settings.

**Port Forwarding** - Using SSH to tunnel other protocols through an encrypted SSH connection. Local forwarding: remote service accessible locally. Remote forwarding: local service accessible through remote server.

**scp (Secure Copy)** - A command-line tool for copying files over SSH. Non-interactive.

**rsync** - A file synchronization tool that transfers only changed blocks. Can use SSH as transport. More efficient than scp for large directory synchronization.

---

### SSH Key Algorithms

| Algorithm | Key Option | Security | Notes |
|-----------|-----------|---------|-------|
| Ed25519 | -t ed25519 | Highest | Recommended for all new keys |
| RSA | -t rsa -b 4096 | High | Use 4096-bit minimum; widely compatible |
| ECDSA | -t ecdsa | Good | Elliptic curve; smaller than RSA |
| DSA | -t dsa | Weak | Deprecated; do not use |

---

### SSH File Locations and Required Permissions

| File | Location | Permissions | Purpose |
|------|----------|------------|---------|
| ~/.ssh/ | Client and server | 700 | SSH configuration directory |
| ~/.ssh/id_ed25519 | Client only | 600 | Private key (never copy to server) |
| ~/.ssh/id_ed25519.pub | Client | 644 | Public key (safe to distribute) |
| ~/.ssh/authorized_keys | Server | 600 | List of trusted public keys |
| ~/.ssh/known_hosts | Client | 600 | Server host key fingerprints |
| ~/.ssh/config | Client | 600 | Per-user client configuration |
| /etc/ssh/sshd_config | Server | 600 | SSH server configuration |
| /etc/ssh/ssh_config | Client | 644 | System-wide client configuration |

SSH enforces these permissions strictly. If ~/.ssh/ is 755 or authorized_keys is 644,
key-based authentication will fail.

---

### Key-Based Authentication Workflow

1. Generate key pair on the client: ssh-keygen -t ed25519
2. Copy public key to server: ssh-copy-id user@server
3. Verify: ssh user@server (should connect without password)
4. Confirm permissions: chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys
5. (Optional) Disable password auth after confirming keys work: PasswordAuthentication no in sshd_config

---

### sshd_config Hardening Reference

| Directive | Hardened Value | Effect |
|-----------|---------------|--------|
| PermitRootLogin | no | Completely block root SSH login |
| PasswordAuthentication | no | Require key-based auth; blocks brute-force |
| PubkeyAuthentication | yes | Enable key-based authentication |
| AllowUsers | user1 user2 | Whitelist; all others denied |
| AllowGroups | sshusers | Alternative to AllowUsers |
| Port | 2222 (or other) | Non-standard port reduces scan noise |
| ListenAddress | management_IP | Only listen on specific interface |
| MaxAuthTries | 3 | Reduce before lockout |
| LoginGraceTime | 30 | Seconds to complete auth (default 120) |
| X11Forwarding | no | Disable GUI forwarding if not needed |
| Banner | /etc/ssh/banner | Display legal notice before login |

After every sshd_config change:
1. Test syntax: sudo sshd -t
2. Restart service: sudo systemctl restart sshd

---

### scp Command Reference

| Command | Purpose |
|---------|---------|
| scp file user@host:/path/ | Copy local file to remote |
| scp user@host:/path/file /local/ | Copy remote file to local |
| scp -r /dir/ user@host:/path/ | Copy directory recursively |
| scp -P PORT file user@host:/path/ | Use non-standard port (capital P) |
| scp user1@host1:/path user2@host2:/path | Copy between two remote hosts |

---

### rsync Command Reference

| Flag | Meaning |
|------|---------|
| -a | Archive: preserves permissions, timestamps, owner, group, symlinks |
| -v | Verbose: show files being transferred |
| -z | Compress data in transit |
| -n | Dry run: show what would happen without making changes |
| --delete | Remove destination files not in source (makes destination a mirror) |
| -e "ssh -p PORT" | Use SSH with a specific port |
| --progress | Show transfer progress per file |
| -P | Same as --partial --progress |

---

### SSH Port Forwarding

Local port forwarding (-L):

```bash
ssh -L LOCAL_PORT:REMOTE_HOST:REMOTE_PORT user@jump_server
```

Traffic to localhost:LOCAL_PORT is forwarded through jump_server to REMOTE_HOST:REMOTE_PORT.

Remote port forwarding (-R):

```bash
ssh -R REMOTE_PORT:LOCAL_HOST:LOCAL_PORT user@remote_server
```

Traffic to REMOTE_PORT on remote_server is forwarded back to LOCAL_PORT on your local machine.

Useful flags:
- -N: No remote command (tunnel only)
- -f: Run in background

---

### ~/.ssh/config Syntax

```
Host ALIAS
    HostName IP_OR_HOSTNAME
    User USERNAME
    Port PORT_NUMBER
    IdentityFile PATH_TO_PRIVATE_KEY
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

- Host ALIAS: the name you use with the ssh command
- Host *: applies to all connections
- ServerAliveInterval: seconds between keepalive probes
- Permissions must be 600

---

### Exam Tips

1. Private key stays on the client. Public key goes to the server's authorized_keys. This is the most fundamental SSH concept and is directly tested.

2. ~/.ssh must be 700. Private keys and authorized_keys must be 600. If these permissions are wrong, SSH silently falls back to password auth or refuses to connect.

3. sshd_config is on the server; it controls what the server accepts. ssh_config is on the client; it controls how the client behaves. They are not the same file.

4. Always run sshd -t after editing sshd_config. A syntax error in sshd_config can make sshd refuse to restart, locking you out of remote access.

5. PasswordAuthentication no should only be set after verifying that key-based authentication works. Disabling passwords before setting up keys will lock everyone out.

6. scp uses -P (capital P) for port. ssh uses -p (lowercase). This difference appears on the exam.

7. rsync -n is a dry run that shows what would be transferred without making changes. Always use -n before --delete to preview what will be removed.

8. SSH REMOTE HOST IDENTIFICATION HAS CHANGED is a security warning indicating the server's host key has changed. Investigate before proceeding — this can indicate a MITM attack or a server rebuild.

---

#
---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 10 - SSH and Remote Access Security** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 10 - SSH and Remote Access Security**, we decompose the execution lifecycle into sequential, verifiable stages:

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
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 10 - SSH and Remote Access Security**:

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
> **Question:** In the context of **Module 10 - SSH and Remote Access Security**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**


## Study Checklist

Before the quiz and lab, confirm you can do all of the following without looking them up:

- Generate an Ed25519 key pair with ssh-keygen
- Copy a public key to a server with ssh-copy-id
- Set correct permissions on ~/.ssh/ and authorized_keys
- Explain the difference between id_ed25519 and id_ed25519.pub
- Describe what happens when you SSH to a server for the first time
- Explain what known_hosts does and when its warning appears
- List five sshd_config directives and their hardening values
- Test sshd_config syntax without restarting the service
- Use scp to copy a file to and from a remote server
- Use rsync for directory synchronization with and without --delete
- Explain local port forwarding with a specific use case
- Create a ~/.ssh/config entry for a frequently accessed server
- Explain the SSH agent and its purpose

---

## 9. Supplemental Resources

**1. OpenSSH Manual Pages — ssh(1), sshd(8), sshd_config(5), ssh_config(5)**
URL: https://man.openbsd.org/ssh
Coverage: The OpenBSD project maintains the authoritative OpenSSH manual pages. The ssh(1)
page covers all client flags including -L (local forward), -R (remote forward), -D (dynamic),
-A (agent forward), -N, and -f. The sshd_config(5) page documents every server directive
including PermitRootLogin, PasswordAuthentication, AllowUsers, MaxAuthTries, and
AuthorizedKeysFile. Essential reference for all SSH configuration topics in this module.

**2. SSH Key Management and Best Practices — Red Hat Enterprise Linux 9**
URL: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/securing_networks/using-secure-communications-between-two-systems-with-openssh_securing-networks
Coverage: Red Hat's OpenSSH security guide covering key generation with ssh-keygen, deploying
public keys, configuring sshd_config for hardening, certificate-based authentication, and
SSH agent usage. Includes step-by-step procedures for common administrative tasks and a
security hardening checklist aligned with RHEL recommendations.

**3. ssh-keygen(1) and ssh-copy-id(1) Man Pages — man7.org**
URL: https://man7.org/linux/man-pages/man1/ssh-keygen.1.html
Coverage: The ssh-keygen man page documents all key generation options including key types
(-t ed25519, rsa, ecdsa), bit sizes (-b), comments (-C), and passphrase management. The
ssh-copy-id man page explains the -i flag and how it writes keys to authorized_keys. Also
covers key fingerprint display and known_hosts management with -R for host key removal.

**4. rsync(1) Man Page and Tutorial — man7.org**
URL: https://man7.org/linux/man-pages/man1/rsync.1.html
Coverage: The rsync man page is comprehensive but dense. Key sections: -a (archive mode),
-v (verbose), -z (compress), --delete (mirror deletions), --dry-run (simulate), --exclude,
and --bwlimit. The FILTER RULES section covers include/exclude patterns for selective sync.
Understanding the trailing slash behavior (source/ vs source) is critical for correct usage.

**5. Arch Wiki — SSH Keys and OpenSSH**
URL: https://wiki.archlinux.org/title/SSH_keys
Coverage: Practical guide covering key pair generation, adding keys to ssh-agent with
ssh-add, configuring SSH config file entries, multiplexing with ControlMaster, and
troubleshooting authentication failures. The companion OpenSSH article covers server
configuration, security hardening, and jump host configuration with ProxyJump. Both are
regularly updated and include current best-practice recommendations.
