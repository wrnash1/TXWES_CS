# Quiz: Module 14 - Industrial IoT (IIoT) and SCADA Systems
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
Which database type is optimized specifically for storing and querying continuous streams of sensor data tagged with timestamps?
*   A) Relational Database (SQL)
*   B) Time-Series Database (TSDB)
*   C) Graph Database
*   D) Key-Value Store
*   **Correct Answer:** B) TSDBs (e.g., InfluxDB) are optimized for sequential write speeds, time-range queries, and computing moving averages over time windows.
*   **Distractor Analysis:**
    *   *Why correct:* TSDBs exploit time-ordering to achieve higher write throughput and efficient time-windowed aggregations that would require complex, slow queries in a general-purpose relational database. They also support native data retention policies for automatic lifecycle management.
    *   Graph databases track node relationships and traversal queries. Key-value stores provide O(1) lookup of current state but lack temporal range query and aggregation capability. Relational databases support flexible queries but are not optimized for high-frequency time-ordered inserts.

---

**Question 2**
Which of the following is the most accurate definition of the **Purdue Reference Model** and its role in ICS/SCADA network security?
*   A) A cloud platform architecture model that defines how IoT devices authenticate to AWS IoT Core, Azure IoT Hub, and GCP IoT Core using tiered credential types — API keys at Level 1, SAS tokens at Level 2, and X.509 certificates at Level 3.
*   B) A hierarchical network segmentation model that divides ICS environments into five levels — from physical sensors and actuators at Level 0 up to enterprise IT at Level 4/5 — with firewall-enforced conduits between levels to prevent IT-to-OT lateral movement.
*   C) A manufacturing quality framework that defines five maturity levels for industrial IoT deployments, from basic sensor connectivity at Level 1 up to fully autonomous AI-driven process control at Level 5.
*   D) A cryptographic protocol stack for industrial networks specifying which cipher suites are permitted at each OSI layer, from link-layer encryption at Layer 2 up to application-layer TLS at Layer 7.
*   **Correct Answer:** B) A hierarchical network segmentation model dividing ICS environments into five levels, with firewall-enforced conduits between levels to prevent IT-to-OT lateral movement.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes cloud IoT platform authentication tiers — a topic covered in Module 06. The Purdue Model predates cloud platforms and addresses OT network segmentation, not cloud credential hierarchies.
    *   *Why B is correct:* The Purdue Reference Model (ISA-95) is the foundational segmentation model for ICS/SCADA security. It defines Level 0 (sensors/actuators), Level 1 (PLCs/RTUs), Level 2 (HMI/SCADA servers), Level 3 (historian/MES), and Level 4/5 (enterprise IT). A DMZ between Level 3 and Level 4 prevents direct enterprise-to-OT connectivity — a critical control since enterprise networks are far more exposed to external threats.
    *   *Why C is incorrect:* This describes a fictional IoT maturity model. The Purdue Model is a segmentation architecture, not a maturity or capability framework.
    *   *Why D is incorrect:* The Purdue Model concerns network zone separation, not cryptographic protocol selection. Cipher suite requirements are defined by standards like TLS 1.3 and IEC 62443, not the Purdue Model.

---

**Question 3**
A security assessment of a water utility's SCADA network finds that the Modbus TCP port (502) on a PLC controlling chemical dosing pumps is directly reachable from the corporate office network — no firewall separates the two segments. An engineer on the corporate network confirms they can send Modbus write commands to the PLC without any authentication challenge. What is the primary security risk, and which control most directly addresses it?
*   A) The primary risk is that Modbus TCP operates over UDP rather than TCP, making packet capture easy; the fix is to switch the PLC to a TCP-based industrial protocol that includes a connection-state handshake.
*   B) The primary risk is that an attacker who compromises any corporate workstation can send unauthenticated Modbus write commands directly to the dosing pump PLC, potentially altering chemical concentrations to unsafe levels; the fix is to deploy a firewall conduit between the corporate and OT networks that blocks all direct access to PLC port 502, routing only authorized historian reads through a DMZ application proxy.
*   C) The primary risk is that Modbus TCP does not support TLS 1.3, so all telemetry data transmitted from the PLC to the SCADA server is unencrypted; the fix is to install TLS certificates on the PLC and upgrade the SCADA server to require encrypted connections.
*   D) The primary risk is that the PLC is running an outdated firmware version with a known CVE; the fix is to apply the vendor's latest firmware patch, after which Modbus will require certificate-based mutual authentication before accepting write commands.
*   **Correct Answer:** B) An attacker with corporate network access can send unauthenticated write commands to the PLC; the fix is a firewall conduit blocking direct OT access with historian reads routed through a DMZ proxy.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Modbus TCP operates over TCP (port 502), not UDP. Switching protocols does not address the root issue: Modbus has no authentication in any variant. The protocol itself cannot be made to require authentication without replacing it entirely with an authenticated industrial protocol.
    *   *Why B is correct:* Modbus has no built-in authentication — any device that can reach port 502 can issue write commands. With no firewall between corporate and OT, a compromised corporate workstation becomes a direct path to safety-critical process control. The Purdue Model remedy is a firewall conduit enforcing IT-to-OT boundaries, with only specific historian polling traffic permitted through a DMZ — not direct PLC access.
    *   *Why C is incorrect:* Confidentiality of telemetry (TLS) is a secondary concern. The immediate, safety-critical risk is unauthenticated write commands — an attacker does not need to eavesdrop; they can directly manipulate the process. Modbus also has no TLS extension; replacing it with OPC-UA in SignAndEncrypt mode would be required, which is a much larger remediation than described.
    *   *Why D is incorrect:* A firmware patch does not add authentication to Modbus — the protocol itself has no authentication fields. Patching addresses known CVEs in the PLC firmware, but the unauthenticated network access path remains until network segmentation is implemented.

---

**Question 4**
The 2010 Stuxnet malware specifically targeted Siemens S7-315 and S7-417 PLCs operating centrifuges at the Natanz uranium enrichment facility. Stuxnet spread via infected USB drives, installed itself on Windows engineering workstations, and then modified PLC ladder logic to intermittently over-speed centrifuges while reporting normal operation to the SCADA HMI. Which combination of ICS security control failures did Stuxnet exploit?
*   A) Stuxnet exploited weak WPA2 Wi-Fi passwords on the facility's industrial wireless network, gaining initial access by cracking the pre-shared key and then pivoting to the PLC via the wireless segment's flat network topology.
*   B) Stuxnet exploited the absence of removable media controls (USB drives used as the initial infection vector), the absence of application whitelisting on engineering workstations (enabling malware execution), and the absence of PLC program integrity verification (no signing or hashing of ladder logic uploads), allowing the malware to modify PLC logic undetected.
*   C) Stuxnet exploited an unauthenticated OPC-UA endpoint on the Siemens SCADA server, using the None security mode to read and overwrite PLC program blocks remotely without requiring a valid username or certificate.
*   D) Stuxnet exploited a public-facing web application in the facility's DMZ, using a SQL injection vulnerability to extract the PLC programming software's credentials from a backend database and then used those credentials to authenticate to the PLC over the internet.
*   **Correct Answer:** B) Stuxnet exploited absent removable media controls, absent engineering workstation application whitelisting, and absent PLC program integrity verification.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The Natanz facility operated as an air-gapped network — it had no wireless connectivity. Stuxnet's propagation mechanism was USB removable media, specifically targeting the air gap. Wi-Fi cracking was not part of the attack.
    *   *Why B is correct:* Stuxnet's attack chain exploited three distinct control failures: (1) USB drives were used routinely to transfer PLC programs, bypassing network controls — removable media policies could have blocked this initial vector; (2) engineering workstations ran Windows with no application whitelisting, allowing the Stuxnet executable to install and run; (3) Siemens Step 7 software accepted unsigned PLC program uploads without verification, so modified ladder logic was installed without alerting operators. The HMI spoofing (reporting normal speeds) exploited the absence of independent process monitoring.
    *   *Why C is incorrect:* OPC-UA was not the attack vector in Stuxnet. Stuxnet targeted the Siemens Step 7 software on the engineering workstation directly, using proprietary Siemens S7 communication protocols — not OPC-UA.
    *   *Why D is incorrect:* The facility was air-gapped with no internet-connected DMZ accessible to the PLCs. SQL injection against a web application played no role in Stuxnet — the attack was entirely internal, spread by USB drives carried by personnel.

---

**Question 5**
An ICS security engineer is evaluating a chemical plant's compliance with IEC 62443. The current architecture has all PLCs, HMI workstations, historians, and corporate ERP systems on a single flat /16 network with no firewall rules between them. The engineer proposes implementing IEC 62443 zones and conduits. Which of the following descriptions correctly identifies a zone and a conduit in IEC 62443 terminology, and which network change would create one compliant conduit?
*   A) A zone is a firewall rule permitting traffic between two network segments; a conduit is a group of devices sharing the same IP subnet. Creating a compliant conduit requires assigning the PLCs and HMI to the same /24 subnet and blocking all traffic from the ERP system's subnet using a network ACL.
*   B) A zone is a logical grouping of assets with similar security requirements and a defined security level (SL 1–4); a conduit is the communication channel between two zones, protected by a security gateway (firewall or DMZ) that enforces allowed protocols and directions. A compliant conduit between the supervisory zone (HMI/SCADA) and the operations zone (historian/MES) would allow only read-only historian polling on the defined protocol and port, with all other traffic blocked.
*   C) A zone is a VLAN tag applied to switch ports to segregate traffic at Layer 2; a conduit is a VPN tunnel encrypting traffic between two VLANs. Creating a compliant conduit requires establishing a site-to-site IPsec VPN between the PLC VLAN and the corporate VLAN so that all Modbus traffic is encrypted in transit.
*   D) A zone is a physical security perimeter (locked server room or cabinet) enclosing a set of industrial devices; a conduit is a fiber optic cable providing air-gap-equivalent isolation between zones. Creating a compliant conduit requires replacing all copper Ethernet cables between OT and IT zones with fiber to prevent electromagnetic eavesdropping.
*   **Correct Answer:** B) A zone is a logical grouping of assets with a defined security level; a conduit is the protected communication channel between zones, enforced by a security gateway.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* IEC 62443 does not define zones as firewall rules or conduits as IP subnets. Subnet assignment is a network design decision, not a security zone definition. A network ACL without a stateful firewall or security gateway does not constitute a compliant conduit.
    *   *Why B is correct:* IEC 62443-3-2 defines a zone as a logical grouping of ICS assets with a common security level (SL 1 = protection against unintentional or accidental violations; SL 4 = protection against state-sponsored sophisticated attacks). A conduit is the data path between zones, secured by a firewall or application-layer proxy that enforces the allowed protocol, direction, and authentication requirements. A properly configured conduit between the supervisory zone and operations zone would permit only outbound historian reads on a specific port, blocking all inbound and protocol-violating traffic.
    *   *Why C is incorrect:* VLANs are a Layer 2 segmentation mechanism that can support zone implementation but are not themselves the IEC 62443 zone definition. A VPN tunnel encrypts traffic but does not restrict which protocols or commands are permitted — encrypted Modbus commands with no authentication are still unauthenticated commands. Encryption alone does not satisfy conduit security requirements.
    *   *Why D is incorrect:* IEC 62443 zones are logical, not physical enclosures. Physical security is addressed in the standard but is separate from zone and conduit definitions. Fiber optic cable prevents electromagnetic eavesdropping but does not enforce protocol restrictions or authentication — it is not a conduit in IEC 62443 terms.
