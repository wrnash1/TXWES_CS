# Module 09 Applied Laboratory Implementation: Peer-to-Peer Systems & Distributed Hash Tables (DHT)
## CSC-6362 | Texas Wesleyan University

---

### Practical Deliverable Specifications
Construct an evidence-based implementation or executive blueprint addressing the core competencies of **Peer-to-Peer Systems & Distributed Hash Tables (DHT)**.

#### Deliverable Structure
1. **Executive Summary (1 Page):** Strategic problem framing, organizational context, and proposed technical intervention.
2. **Technical Architecture & Implementation Blueprint (3–4 Pages):**
   * Detailed architectural diagrams (C4 model or UML component diagrams).
   * Algorithmic specifications, data flows, and protocol interactions.
   * Reproducible configuration manifests, code artifacts (Python / Go / Terraform), or quantitative experimental models.
3. **Empirical Evaluation & Stress Testing (1–2 Pages):**
   * Benchmarking metrics (throughput, latency, MTTR, fault recovery duration).
   * Security threat model and failure mode mitigation analysis.
4. **Institutional Governance & Compliance Matrix:**
   * Direct cross-walk mapping to applicable national standards and accreditation rubrics.

#### Submission Format
Submit your formal technical report as a compiled PDF or Markdown document with annotated system telemetry, configuration code, and verified logs.

---

### Hands-On Technical Execution Blueprint & Laboratory Tasks

To ensure rigorous experiential mastery of these principles, complete the following four applied technical tasks using your virtual laboratory or cloud environment:

#### Task 1: Environment Initialization & Topology Verification
1. Launch your Linux / Cloud workbench and verify connectivity across the management subnet:
   ```bash
   ip addr show
   ping -c 3 127.0.0.1
   uname -a
   ```
2. Verify that network virtualization modules and necessary utilities are active:
   ```bash
   lsmod | grep -E "vxlan|openvswitch|br_netfilter" || echo "Loading virtualization modules..."
   sudo modprobe vxlan br_netfilter
   ```
3. Record the initialization telemetry and capture baseline network interface metrics.

#### Task 2: Automated Configuration & Infrastructure as Code (IaC)
1. Construct an automated configuration script or declaration manifest establishing the core architecture.
2. Ensure strict encapsulation parameters:
   - Define VNI (Virtual Network Identifier) tags or equivalent segmentation markers.
   - Configure MTU sizing (1550+ bytes or appropriate MSS clamping) to prevent fragmentation overhead across tunnel endpoints.
3. Apply the configuration and inspect active state:
   ```bash
   ip link show type vxlan || ip link show
   ss -tulpn
   ```

#### Task 3: Fault Injection, Stress Testing & Telemetry Collection
1. Simulate high-traffic saturation and edge-case network partitions using automated benchmarking:
   ```bash
   # Benchmark latency, jitter, and throughput
   iperf3 -s &
   iperf3 -c 127.0.0.1 -t 10 -P 4
   ```
2. Monitor kernel buffer drops, queue exhaustion, and packet loss under load:
   ```bash
   netstat -s | grep -i "buffer\|drop\|retransmit"
   ```
3. Document exact failure thresholds where throughput degrades or latency exceeds enterprise SLAs.

#### Task 4: Compliance Cross-Walk & Threat Mitigation Matrix
Map your implementation against national regulatory standards:
- **NIST SP 800-53 Rev. 5:** Identify applicable AC (Access Control), SC (System and Communications Protection), and SI (System and Information Integrity) controls.
- **Audit Logging:** Verify that all control-plane state changes are routed to `/var/log/syslog` or an external SIEM agent.

---

### Formal Deliverable Checklist & Submission Requirements
Before submitting your laboratory report to Canvas, verify that you have included:
- [ ] Annotated C4 Architecture / Topology Diagram showing physical underlay and virtual overlay mappings.
- [ ] Complete configuration manifests, bash scripts, or IaC code artifacts.
- [ ] Benchmarking telemetry output showing throughput, p99 latency, and loss metrics under stress.
- [ ] 2-page executive analysis detailing failure mode mitigations and governance compliance.
