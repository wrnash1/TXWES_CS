# Reading Guide: Module 15 - IoT Standards and Regulatory Compliance
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Introduction
Welcome to **Module 15 – IoT Standards and Regulatory Compliance**! This module examines the regulatory landscape and technical standards that govern how IoT devices are designed, manufactured, and deployed — from consumer smart home devices to industrial sensors in critical infrastructure. The absence of a single universal IoT security standard has historically allowed vendors to ship devices with weak defaults, no patch mechanisms, and no disclosure timelines. Regulators and standards bodies in multiple jurisdictions are now closing these gaps through legislation, certification programs, and technical standards.

You will learn the key IoT security standards (ETSI EN 303 645, NIST IR 8259A, ISO/IEC 27400), regulatory requirements (California SB-327, the EU Cyber Resilience Act, FCC IoT labeling), and how these requirements map to specific technical controls — default password prohibitions, mandatory disclosure policies, minimum cryptographic requirements, and software bill of materials (SBOM) obligations. Understanding how to apply these frameworks to real device designs is essential for both the certification exam and professional practice.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **ETSI EN 303 645**: A European Telecommunications Standards Institute standard that defines baseline cybersecurity requirements for consumer IoT devices. Its 13 provisions include: no universal default passwords (each device must have a unique default or require the user to set one at first use), a published vulnerability disclosure policy, software must be kept updated (devices must support secure update), credentials and security-sensitive data must be stored securely, and communication security using TLS with certificates validated by the device. EN 303 645 is the technical basis for the EU's Cyber Resilience Act product requirements and the UK's Product Security and Telecommunications Infrastructure (PSTI) Act.
*   **NIST IR 8259A (IoT Device Cybersecurity Capability Core Baseline)**: A NIST publication defining six core cybersecurity capabilities that IoT devices should support: (1) device identification (unique identity), (2) device configuration (ability to change configuration), (3) data protection (cryptographic protection of stored and transmitted data), (4) logical access to interfaces (authentication before access), (5) software update (ability to receive authenticated firmware updates), and (6) cybersecurity state awareness (ability to report security state and log events). NIST IR 8259A is the baseline used by U.S. federal procurement requirements and informs voluntary IoT labeling programs.
*   **Software Bill of Materials (SBOM)**: A formal, machine-readable inventory of all software components (open-source libraries, third-party packages, operating system components) included in a device's firmware or software, along with their versions and known vulnerabilities. The U.S. Executive Order 14028 (May 2021) mandated SBOMs for software sold to the federal government; NTIA defined minimum SBOM elements (supplier name, component name, version, unique ID, dependency relationship, author, timestamp). For IoT devices, an SBOM enables operators to quickly determine whether a device is affected by a newly published CVE — critical for patching decisions across large fleets.
*   **EU Cyber Resilience Act (CRA)**: A European Union regulation (effective 2024, enforcement phased to 2027) requiring manufacturers of products with digital elements — including IoT devices — to meet mandatory cybersecurity requirements before CE marking and EU market placement. CRA requirements include: no known exploitable vulnerabilities at time of shipment, unique default credentials, encrypted communications, security patch support for the expected product lifetime, vulnerability disclosure within 24 hours of discovery, and an SBOM. Products that fail CRA requirements can be banned from EU sale and face fines up to €15 million or 2.5% of global annual turnover.
*   **IoT Security Labeling**: Voluntary or mandatory certification programs that allow consumers to identify IoT devices meeting a defined security baseline. The U.S. FCC Cyber Trust Mark (proposed 2023) applies NIST IR 8259A criteria; devices that qualify display a QR code linking to a registry of security commitments. Singapore's Cybersecurity Labelling Scheme (CLS) operates four tiers, with Tier 4 requiring independent third-party penetration testing. Labeling programs create market incentives for manufacturers to implement security baselines without mandating specific technical implementations.

---

### 2. Certification Exam Tips
*   **Standard-to-requirement mapping:** Memorize which standard covers which requirement. ETSI EN 303 645 = consumer IoT baseline (EU/UK), no universal default passwords is Provision 1. NIST IR 8259A = U.S. federal baseline, six capabilities. CRA = EU mandatory regulation with market enforcement. Exam scenarios describe a device characteristic (e.g., "all units ship with the same admin/admin password") and ask which standard is violated.
*   **California SB-327 vs ETSI EN 303 645:** California SB-327 (effective January 2020) was the first U.S. law prohibiting universal default passwords for connected devices — it requires either a unique preprogrammed password per device or forced password change on first use. ETSI EN 303 645 Provision 1 requires the same for EU. Both prohibit identical default credentials across a product line. Exam questions may contrast these or ask which is law vs which is a standard.
*   **SBOM scope and use:** An SBOM lists components but does not by itself fix vulnerabilities — it enables operators to run CVE scans against known component versions. The exam may present a scenario where a newly discovered CVE affects a library used in 10,000 deployed devices and ask what artifact enables rapid impact assessment: the SBOM. The minimum SBOM elements from NTIA are testable.
*   **Vulnerability disclosure timelines:** ETSI EN 303 645 requires manufacturers to have a publicly known vulnerability disclosure policy. EU CRA requires disclosure within 24 hours of learning of an actively exploited vulnerability and a patch within 90 days. The exam may ask which framework specifies a disclosure timeline or what constitutes compliant vulnerability handling.
*   **Study Resource:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — all 10 OWASP IoT Top 10 categories map directly to requirements in ETSI EN 303 645, NIST IR 8259A, and the CRA. Reviewing the OWASP categories through the lens of which regulatory requirement addresses each is an efficient exam preparation strategy.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — review all 10 OWASP IoT Top 10 categories alongside the standards covered in this module. Each OWASP category corresponds to one or more requirements in ETSI EN 303 645, NIST IR 8259A, and the EU Cyber Resilience Act, enabling you to trace regulatory requirements to technical controls.
*   **Required Video:** The [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0) includes coverage of IoT security standards and compliance requirements, discussing how ETSI, NIST, and regulatory frameworks translate into device design and manufacturing requirements.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Perform a compliance gap analysis**: Given a specification for a fictional consumer smart thermostat (shared default password "admin", no TLS for cloud communication, no firmware update mechanism, no vulnerability disclosure policy), evaluate it against each of the 13 ETSI EN 303 645 provisions and produce a gap analysis table showing which provisions are met, which are violated, and the specific technical remediation required for each gap.
*   **Generate and analyze an SBOM**: Using the `syft` tool (or a provided pre-generated SBOM JSON file) for a sample embedded Linux image, identify all included packages and their versions, cross-reference two component entries against the NVD (National Vulnerability Database) CVE feed, and document whether the device would be affected by a specific named CVE and what the remediation would be.
*   **Map regulatory requirements to technical controls**: Create a traceability matrix mapping the six NIST IR 8259A capabilities to specific implementation examples from prior course modules — for example, mapping "logical access to interfaces" to X.509 certificate authentication from Module 06, and "software update" to the OTA pipeline and A/B partition scheme from Module 10.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize which standard covers which requirement category.
- [ ] Read the OWASP IoT Top 10 categories at [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) and map each to an ETSI EN 303 645 provision or NIST IR 8259A capability.
- [ ] Watch the IoT standards and compliance sections of [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0).
- [ ] Review SBOM minimum elements and vulnerability disclosure timelines before the lab.
- [ ] Proceed to the weekly hands-on lab activity.
