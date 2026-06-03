# Quiz: Module 07 — Network Security Architecture

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Questions mirror the style and difficulty of CompTIA Security+ SY0-701 exam items.

---

### Question 1

A security engineer needs to deploy a solution that can automatically block malicious traffic in real time as it passes through the network perimeter. Which control BEST meets this requirement?

A. Network IDS with a SPAN port connection

B. Host-based IDS on each endpoint

C. Network IPS deployed inline

D. SIEM with automated alerting

**Correct Answer:** C

**Explanation:** An IPS deployed inline sits directly in the traffic path and can inspect and block malicious traffic in real time. An IDS (whether network or host-based) is a passive detection tool — it generates alerts but cannot block traffic. A SIEM aggregates and correlates log data for analysis; it does not inspect or block live traffic.

---

### Question 2

An organization's web application is being targeted by SQL injection attacks. The perimeter NGFW has not detected the attacks because they arrive over HTTPS on port 443. Which additional control would MOST effectively mitigate this specific threat?

A. Deploy a second NGFW in tandem with the existing one

B. Implement a Web Application Firewall (WAF) in front of the web application

C. Enable the IPS signatures for port 443 on the NGFW

D. Switch the web application from HTTPS to HTTP so the NGFW can inspect it

**Correct Answer:** B

**Explanation:** A WAF is specifically designed to inspect HTTP/HTTPS application traffic and protect against OWASP Top 10 attacks including SQL injection and XSS. It understands the HTTP protocol semantics needed to detect injection patterns. A second NGFW does not add application-layer web inspection. An IPS on port 443 cannot inspect the content of TLS-encrypted payloads without decryption. Switching to HTTP removes encryption and is not an acceptable security tradeoff.

---

### Question 3

A company runs a customer-facing web server that must be accessible from the internet, and an internal database server containing customer financial records. Which placement BEST represents a secure architecture?

A. Both servers on the internal network, accessible via port forwarding

B. Web server in the DMZ; database server on the internal network

C. Both servers in the DMZ for simplified firewall management

D. Web server on the internet with a direct connection to the database

**Correct Answer:** B

**Explanation:** The DMZ is designed specifically for servers that must accept connections from untrusted external networks. Placing the web server in the DMZ and the database server on the internal network ensures that if the web server is compromised, the attacker cannot directly reach the database — they must cross the inner firewall, which permits only the specific query traffic needed. Placing the database in the DMZ or using direct port forwarding exposes it to unnecessary risk.

---

### Question 4

An IPS deployed inline at a healthcare facility fails during a software update. Patient monitoring systems lose network connectivity. Which fail behavior was configured, and which would have been MORE appropriate for this environment?

A. Fail-open was configured; fail-closed would be more appropriate

B. Fail-closed was configured; fail-open would be more appropriate

C. Fail-closed was configured; fail-closed remains appropriate for healthcare

D. Fail-open was configured; fail-open remains appropriate for healthcare

**Correct Answer:** B

**Explanation:** Fail-closed blocks all traffic when the device fails — this is what caused the loss of connectivity to patient monitoring systems. In a healthcare environment where patient care depends on network availability, fail-open is more appropriate: when the device fails, traffic passes through uninspected rather than being blocked. The security risk of uninspected traffic during a brief failure is more acceptable than blocking clinical communications.

---

### Question 5

An organization wants to replace their remote access VPN with a solution where authenticated users can only access the specific application they are authorized for, rather than gaining access to the entire corporate subnet. Which solution BEST meets this requirement?

A. Site-to-site IPsec VPN with split tunneling

B. Zero Trust Network Access (ZTNA)

C. Full-tunnel SSL VPN

D. Network Access Control (NAC)

**Correct Answer:** B

**Explanation:** ZTNA provides application-specific access based on verified identity and device posture. Unlike traditional VPN, which grants network-level access to a broad subnet, ZTNA grants access only to the specific application the user is authorized for. Site-to-site VPN connects entire networks. Full-tunnel SSL VPN provides broad network access, not application-specific access. NAC verifies device posture before network access but does not limit access to specific applications.

---

### Question 6

A firewall policy contains the following rules in order: (1) PERMIT TCP from 10.0.0.0/8 to ANY on port 443; (2) DENY TCP from 10.0.1.50 to ANY on port 443; (3) DENY ALL. A workstation at 10.0.1.50 attempts to connect to an external HTTPS server. What is the result?

A. The connection is permitted by Rule 1

B. The connection is denied by Rule 2

C. The connection is denied by Rule 3

D. The connection is permitted because HTTPS is allowed by default

**Correct Answer:** A

**Explanation:** Firewall rules are evaluated top to bottom, and the first matching rule wins. Rule 1 matches the traffic from 10.0.1.50 (which is within 10.0.0.0/8) on port 443 and permits it. Rule 2, which would deny that specific host on port 443, is never reached because Rule 1 already matched. To achieve the intended behavior of denying 10.0.1.50, Rule 2 would need to be placed above Rule 1.

---

### Question 7

A security analyst notices that workstations on the internal network are making frequent DNS queries for domain names that follow a random-looking pattern: `xkqprzalbf3927.example.com`, `mzqtbnaldf7421.example.com`. What attack technique do these patterns suggest?

A. DNS cache poisoning

B. Domain Generation Algorithm (DGA) beaconing

C. DNS zone transfer

D. Pharming

**Correct Answer:** B

**Explanation:** Domain Generation Algorithms (DGAs) are used by malware to generate a large number of pseudo-random domain names that the malware's command-and-control infrastructure rotates through. This makes it difficult to block C2 communication by blacklisting domains. The random-looking patterns are the characteristic indicator. DNS cache poisoning modifies DNS responses. DNS zone transfer requests a copy of all DNS records. Pharming redirects legitimate URLs.

---

### Question 8

Which network segmentation technology enforces access policies between individual workloads running in the same subnet, preventing east-west lateral movement between workloads that share a VLAN?

A. VLAN tagging

B. Stateful perimeter firewall

C. Microsegmentation

D. DMZ

**Correct Answer:** C

**Explanation:** Microsegmentation applies access policies at the workload level — individual virtual machines, containers, or processes — regardless of whether they share a network segment. Traditional VLAN segmentation only separates traffic at the subnet level; workloads within the same VLAN can communicate freely. A perimeter firewall controls traffic entering or leaving the network, not east-west traffic within the network. A DMZ isolates publicly accessible servers but does not enforce workload-level policies.

---

### Question 9

A company configures their remote access VPN with split tunneling enabled. What is the PRIMARY security concern with this configuration?

A. Split tunneling increases VPN gateway load beyond capacity

B. Users' internet traffic bypasses corporate security controls, reducing visibility and protection

C. Split tunneling prevents access to internal resources

D. Encrypted tunnels cannot be established when split tunneling is active

**Correct Answer:** B

**Explanation:** With split tunneling, only traffic destined for corporate resources is routed through the VPN. Internet-bound traffic goes directly from the user's device to the internet, bypassing corporate proxy servers, web filtering, IPS, and DLP controls. This creates a gap where malware on the user's device can communicate with external C2 servers or exfiltrate data without inspection. Full tunneling routes all traffic through the corporate gateway, maintaining visibility and control.

---

### Question 10

An organization implements Network Access Control (NAC). A device connecting to the network fails the posture assessment because its antivirus definitions are 45 days old. What should NAC do with this device?

A. Permit full network access since the device is owned by the organization

B. Deny all network access and require the user to contact IT support

C. Place the device in a quarantine VLAN where it can only access remediation resources

D. Alert the SIEM and permit the connection pending manual review

**Correct Answer:** C

**Explanation:** A quarantine VLAN provides a restricted network environment where the non-compliant device can access only the resources it needs to remediate the compliance failure — in this case, an AV definition update server. This approach is more appropriate than a full deny (which creates a bad user experience and may require IT intervention for a self-correctable issue) while ensuring the non-compliant device does not gain access to the trusted network.

---

Module 07 Quiz — End
