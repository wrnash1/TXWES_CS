# Reading Guide: Module 14 - Industrial IoT (IIoT) and SCADA Systems
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Introduction
Welcome to **Module 14 – Industrial IoT (IIoT) and SCADA Systems**! This module examines the convergence of operational technology (OT) with information technology (IT) in industrial environments — manufacturing plants, power grids, water treatment facilities, and oil and gas pipelines. Industrial control systems such as SCADA (Supervisory Control and Data Acquisition), PLCs (Programmable Logic Controllers), and DCS (Distributed Control Systems) were originally designed as isolated, air-gapped networks. Connecting them to IP networks and the internet introduces cybersecurity risks that did not exist in the original design, with consequences ranging from production downtime to physical equipment damage and public safety incidents.

You will learn the architecture of SCADA and ICS networks, how the Purdue Reference Model defines network segmentation zones, and why IT/OT convergence creates security challenges unique to industrial environments. Real-world ICS attacks — including Stuxnet, the Ukraine power grid attacks, and the Oldsmar water treatment facility incident — illustrate the stakes. Security frameworks including IEC 62443 and NIST SP 800-82 provide guidance for securing these environments.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **SCADA (Supervisory Control and Data Acquisition)**: An industrial control system architecture that uses remote terminal units (RTUs) or PLCs to collect sensor data from distributed field devices (valves, pumps, breakers), transmit it over a communications network to a central supervisory server, and allow human operators to monitor and control physical processes through an HMI (Human-Machine Interface). SCADA systems are used in power distribution, water treatment, oil and gas pipelines, and transportation infrastructure. Legacy SCADA systems communicate over proprietary protocols (Modbus, DNP3) that lack authentication, making them vulnerable when exposed to IP networks.
*   **Purdue Reference Model (ISA-95)**: A hierarchical network segmentation model that divides ICS/SCADA networks into five levels: Level 0 (physical process — sensors and actuators), Level 1 (intelligent field devices — PLCs, RTUs), Level 2 (supervisory control — HMI, SCADA servers), Level 3 (site operations — historian, manufacturing execution systems), and Level 4/5 (enterprise IT — ERP, corporate network, internet). Security best practice requires firewall-enforced conduits between levels and a DMZ between Level 3 and Level 4 to prevent direct IT-to-OT connectivity. The model defines where IT security controls apply and where OT-specific controls are needed.
*   **IT/OT Convergence**: The integration of operational technology (OT) — hardware and software that monitors and controls physical industrial processes — with information technology (IT) systems for data analytics, remote management, and enterprise connectivity. IT/OT convergence enables capabilities like predictive maintenance and remote monitoring but creates security risks: OT systems designed for 20–30 year operational lifespans often run unpatched legacy firmware that cannot be updated without process interruption, and enterprise network compromises can now pivot to OT environments that control physical processes.
*   **IEC 62443**: An international standards series for industrial automation and control system (IACS) cybersecurity, developed by ISA (International Society of Automation). IEC 62443 defines security levels (SL 1–4) based on threat capability, a zone-and-conduit network segmentation model, and security requirements for asset owners, system integrators, and component manufacturers. IEC 62443-3-3 defines system security requirements; IEC 62443-4-2 defines component security requirements. It is the primary compliance framework for industrial control system security globally.
*   **OT-Specific Attack Surface**: Industrial control systems present attack vectors distinct from enterprise IT, including: unpatched legacy PLCs and RTUs running proprietary OS without patch management; unauthenticated industrial protocols (Modbus, DNP3, OPC-UA without authentication enabled) that accept commands from any source; engineering workstations with remote access software connected to both corporate and OT networks simultaneously; removable media (USB drives used to update PLC programs) that bypass network controls; and vendor remote access channels maintained for support that remain open 24/7 without monitoring.

---

### 2. Certification Exam Tips
*   **Purdue Model zone mapping:** Memorize the five levels and which devices belong at each level. Exam scenarios describe a device type (PLC, HMI, historian, ERP) and ask which Purdue level it occupies, or describe an attack path and ask which boundary was violated.
*   **Protocol authentication gaps:** Modbus and DNP3 have no built-in authentication — any device on the network can send commands. OPC-UA has optional security modes (None, Sign, SignAndEncrypt). Exam questions may ask which protocol is most vulnerable to unauthenticated command injection or which OPC-UA security mode provides integrity protection.
*   **IT vs OT CIA triad priority reversal:** In IT security, the CIA triad prioritizes Confidentiality first. In OT/ICS security, the priority is reversed: Availability first (a plant shutdown or safety system failure is catastrophic), Integrity second (false sensor data causes wrong control actions), Confidentiality last. Exam scenarios describing an OT security decision should apply this priority ordering.
*   **Real-world ICS attacks for context:** Stuxnet (2010) targeted Siemens PLCs via USB propagation, manipulating centrifuge speeds while reporting normal to operators. The 2015/2016 Ukraine power grid attacks used spear-phishing to pivot from enterprise to OT, triggering relay trips to cut power. The 2021 Oldsmar water treatment attack used TeamViewer remote access to alter sodium hydroxide concentration. Each illustrates a specific attack vector testable on exams.
*   **Study Resource:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) covers insecure network services and lack of physical hardening — both highly relevant to legacy ICS devices with unauthenticated protocols and physically accessible control panels.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — focus on the insecure network services and lack of physical hardening sections, which apply directly to legacy ICS/SCADA devices with unauthenticated protocols and control panels that are physically accessible in industrial facilities.
*   **Required Video:** The [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0) includes coverage of industrial IoT architecture and ICS/SCADA integration patterns, discussing network segmentation strategies and the security implications of connecting legacy control systems to IP networks.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Map a simulated Purdue Model network**: Using a network diagram tool or draw.io, create a five-level Purdue Model diagram for a simulated water treatment facility. Place specific device types (sensor RTU, PLC, HMI server, historian, ERP system, internet DMZ) at their correct levels and draw firewall conduits between levels, labeling the allowed protocol and direction for each conduit.
*   **Analyze Modbus protocol structure**: Using Wireshark with a pre-captured Modbus TCP packet trace, identify function codes for read holding registers (FC 03) and write single coil (FC 05), observe the absence of authentication fields in the Modbus frame structure, and document how an attacker could craft a write command to change a coil state without any credential.
*   **Apply IEC 62443 zone segmentation to a scenario**: Given a description of a manufacturing plant's current flat network (all OT devices on the same VLAN as corporate PCs), identify the IEC 62443 zone violations, propose a zone-and-conduit segmentation design, and specify which industrial protocols require a security proxy or encrypted tunnel at each conduit boundary.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize the five Purdue Model levels and example devices at each level.
- [ ] Read the insecure network services section at [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/).
- [ ] Watch the IIoT/SCADA sections of [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0).
- [ ] Review IT vs OT CIA triad priority reversal and protocol authentication gaps before the lab.
- [ ] Proceed to the weekly hands-on lab activity.
