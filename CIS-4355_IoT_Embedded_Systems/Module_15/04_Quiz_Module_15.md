# Quiz: Module 15 - IoT Standards and Regulatory Compliance
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
Which design principle recommends securing an IoT system at the device level, the network level, and the cloud application level?
*   A) Single Point of Failure
*   B) Defense in Depth (End-to-End Security)
*   C) Simple Access Controls
*   D) Direct Interface Trust
*   **Correct Answer:** B) Defense in Depth ensures that if a control fails at one layer (e.g., Wi-Fi security), other layers (e.g., device authentication, TLS) continue to protect the system.
*   **Distractor Analysis:**
    *   *Why correct:* Defense in Depth applies overlapping, independent security controls so that no single control failure results in a complete compromise. For IoT systems this means: device-level controls (secure boot, unique credentials), network-level controls (TLS, VLAN segmentation), and cloud-level controls (IoT policies, least-privilege access). Each layer compensates for weaknesses in the others.
    *   Single Point of Failure describes an architectural weakness, not a security design principle. Simple Access Controls and Direct Interface Trust describe insecure approaches that the principle of defense in depth explicitly opposes.

---

**Question 2**
Which of the following is the most accurate definition of **ETSI EN 303 645** and its significance for IoT device security?
*   A) A European cloud security standard that defines minimum encryption requirements for data stored in EU-based data centers processing personal IoT sensor data, specifying AES-256 for data at rest and TLS 1.3 for data in transit as mandatory baselines.
*   B) A cybersecurity baseline standard for consumer IoT devices that defines 13 provisions — including prohibiting universal default passwords, requiring a published vulnerability disclosure policy, and mandating secure software update capability — which forms the technical basis for EU and UK IoT product security regulations.
*   C) An IETF protocol specification that standardizes how IoT devices report security events to a cloud SIEM platform using a structured JSON telemetry format, enabling centralized security monitoring across heterogeneous device fleets.
*   D) An ISO quality management standard that specifies the manufacturing process controls required to produce IoT devices with verifiable hardware security features, including requirements for tamper-evident packaging and supply chain traceability documentation.
*   **Correct Answer:** B) A cybersecurity baseline standard defining 13 provisions for consumer IoT devices, including no universal default passwords and mandatory vulnerability disclosure policy.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes data-at-rest and data-in-transit encryption requirements for cloud storage — a separate concern from device security baselines. ETSI EN 303 645 focuses on device-level security controls, not cloud data center requirements. The EU's GDPR and NIS2 Directive govern cloud data protection obligations.
    *   *Why B is correct:* ETSI EN 303 645 (published 2020) is the foundational consumer IoT security standard in Europe. Its 13 provisions cover the most common IoT vulnerabilities: Provision 1 prohibits universal default passwords (each device must have a unique credential or force the user to set one at first use), Provision 2 requires a published vulnerability disclosure policy, and Provision 3 requires that software is kept updated. It directly underpins both the UK PSTI Act and the EU Cyber Resilience Act's technical requirements.
    *   *Why C is incorrect:* No such IETF standard exists under the EN 303 645 designation. Security event reporting to SIEM platforms uses formats like CEF (Common Event Format) or the OCSF (Open Cybersecurity Schema Framework), neither of which is ETSI EN 303 645.
    *   *Why D is incorrect:* ISO quality management standards (ISO 9001) govern manufacturing processes, but ETSI EN 303 645 is a cybersecurity technical specification, not a manufacturing QMS. Tamper-evident packaging and supply chain traceability are addressed in separate standards (e.g., NIST SP 800-161).

---

**Question 3**
A manufacturer ships 2 million consumer smart doorbells. All units ship from the factory with the username "admin" and password "admin123" hardcoded — the same credentials on every device. Customers are not prompted to change the password during setup. Six months after launch, a researcher discovers that 400,000 devices have been compromised and enrolled in a botnet. Which regulatory requirement was violated, and which specific remediation would have prevented the mass compromise?
*   A) The manufacturer violated ETSI EN 303 645 Provision 1 (no universal default passwords) and California SB-327 — both require that each device ship with a unique default password per device or force the user to set a new password during initial configuration. Generating unique per-device passwords at manufacture (derived from the device serial number with a cryptographic function) or implementing a mandatory first-use password change screen would have prevented attackers from using a single credential to access the entire fleet.
*   B) The manufacturer violated NIST SP 800-53 Control AC-14 (Permitted Actions Without Identification or Authentication) — this control requires federal agencies to document all actions that can be performed without authentication. Remediation requires the manufacturer to submit a System Security Plan (SSP) to NIST describing the doorbell's authentication architecture.
*   C) The manufacturer violated the EU General Data Protection Regulation (GDPR) Article 32 by failing to implement appropriate technical measures to protect personal data — the identical credentials constitute insufficient pseudonymization. Remediation requires the manufacturer to appoint a Data Protection Officer (DPO) and file a breach notification within 72 hours with the supervisory authority.
*   D) The manufacturer violated ISO/IEC 27001 Annex A control A.9.2.1 (User Registration and De-registration) by failing to maintain a formal user registration process. Remediation requires the manufacturer to implement an ISO 27001 Information Security Management System (ISMS) and conduct annual certification audits.
*   **Correct Answer:** A) Violated ETSI EN 303 645 Provision 1 and California SB-327 — both prohibit universal default passwords; per-device unique credentials or forced first-use password change would have prevented the mass compromise.
*   **Distractor Analysis:**
    *   *Why A is correct:* Universal default credentials are explicitly prohibited by both ETSI EN 303 645 Provision 1 and California SB-327 (effective January 2020). The Mirai botnet (2016) demonstrated that mass compromise of IoT devices using identical default credentials is a realistic, large-scale threat. Per-device unique passwords (e.g., printed on the device label and derived from a hardware identifier using a keyed hash) ensure that compromising one device's password does not compromise the fleet.
    *   *Why B is incorrect:* NIST SP 800-53 is a control catalog for U.S. federal information systems — it does not apply to consumer electronics manufacturers. Consumer IoT device manufacturers are not required to submit SSPs to NIST.
    *   *Why C is incorrect:* GDPR governs the processing of personal data by data controllers and processors — it does not directly mandate IoT device password policies. While a data breach notification obligation may apply to the doorbell manufacturer, the specific requirement violated was the product security law (ETSI EN 303 645 / SB-327), not GDPR Article 32.
    *   *Why D is incorrect:* ISO 27001 is a voluntary management system standard for organizations protecting their own information assets — it is not a product security standard that mandates specific device credential designs. A manufacturer could hold ISO 27001 certification while still shipping devices with universal default passwords.

---

**Question 4**
A security operations team at an industrial company learns that a newly published CVE (CVSS 9.8 Critical) affects libssl version 1.0.2, a library used in the OpenSSL package. They need to determine within hours which of their 15,000 deployed IoT sensors are affected so they can prioritize emergency patching. Which artifact, if it had been required of the device manufacturer, would most directly enable this rapid impact assessment?
*   A) A penetration testing report produced by a third-party security firm at the time of device certification, which would include a list of all vulnerabilities found during the assessment and confirmation that libssl was tested for known CVEs at that point in time.
*   B) A Software Bill of Materials (SBOM) for each device model's firmware, listing all included software components and their versions in a machine-readable format — enabling the team to query which device models include libssl 1.0.2 within minutes and immediately scope the affected fleet.
*   C) A device twin record in the cloud IoT platform storing the device's current firmware version string, which could be queried to determine how many devices are running firmware versions that predate the security patch release date.
*   D) A signed firmware update package from the manufacturer, which would indicate that the manufacturer has already addressed the CVE and all devices that have received the latest OTA update are no longer affected.
*   **Correct Answer:** B) A Software Bill of Materials (SBOM) listing all firmware components and versions enables immediate query to scope which device models include the vulnerable libssl version.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A penetration test report captures the vulnerability state at a point in time — it cannot tell you whether a newly published CVE (discovered after the test) affects any specific component. Pen test reports also do not typically enumerate all library versions in a machine-readable format suitable for CVE cross-referencing.
    *   *Why B is correct:* An SBOM is a machine-readable inventory of software components (supplier, component name, version, unique identifier). When a new CVE is published, the security team runs an automated scan of their SBOM registry against the CVE's affected component and version range — a query that returns results in seconds for 15,000 devices. NTIA minimum SBOM elements, mandated by U.S. Executive Order 14028, were specifically designed to enable this use case.
    *   *Why C is incorrect:* A firmware version string (e.g., "v2.3.1") indicates the overall firmware build but does not enumerate the individual library components and their versions included in that build. The team would still need to know whether firmware v2.3.1 includes libssl 1.0.2 — which requires the SBOM.
    *   *Why D is incorrect:* A signed firmware update package confirms the manufacturer has released a patch, but it does not tell the security team which of their 15,000 deployed devices have already received the update and which have not. Device-level patch status tracking requires the fleet management system's device registry, not the firmware package itself.

---

**Question 5**
A manufacturer of industrial IoT gateways sells into both the EU and U.S. markets. Their devices ship with default credentials that are unique per device, support TLS 1.3 for cloud communication, and include a firmware update mechanism. However, the company has no published vulnerability disclosure policy, and when a researcher reports a critical RCE vulnerability, the company takes 14 months to release a patch and never notifies customers. Which compliance failures does this represent under current IoT security frameworks?
*   A) No compliance failures — the company met the primary technical requirements (unique credentials, TLS, update mechanism) and disclosure timelines are voluntary guidelines with no binding obligations on private manufacturers in either the EU or U.S.
*   B) The company violated ETSI EN 303 645 Provision 2 (no published vulnerability disclosure policy) and the EU Cyber Resilience Act requirement to disclose actively exploited vulnerabilities within 24 hours and release patches within 90 days — both of which apply to products sold in EU markets.
*   C) The company violated HIPAA Security Rule §164.308(a)(6) by failing to implement security incident response procedures, and the FTC Safeguards Rule by failing to notify affected customers of the security incident within 30 days of discovering the vulnerability.
*   D) The company violated PCI DSS Requirement 6.3 by failing to protect all system components from known vulnerabilities by installing applicable security patches within one month of release, which applies because the gateways process payment card data in retail deployments.
*   **Correct Answer:** B) Violated ETSI EN 303 645 Provision 2 (no vulnerability disclosure policy) and EU CRA requirements for timely disclosure and patching.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Vulnerability disclosure policies and patch timelines are not merely voluntary guidelines in the EU. ETSI EN 303 645 Provision 2 (a published vulnerability disclosure policy) is a mandatory requirement for products claiming conformity with EN 303 645 and is incorporated into the EU CRA. The CRA's 24-hour disclosure and 90-day patch obligations are legally binding for EU market access.
    *   *Why B is correct:* ETSI EN 303 645 Provision 2 explicitly requires manufacturers to "make it straightforward to report security issues" via a published vulnerability disclosure policy — this is a named, auditable requirement, not a best-practice recommendation. The EU Cyber Resilience Act (applicable to products placed on the EU market) requires that manufacturers notify ENISA of actively exploited vulnerabilities within 24 hours of becoming aware and provide a patch within 90 days. A 14-month patch timeline and no customer notification are direct violations of both obligations.
    *   *Why C is incorrect:* HIPAA governs protected health information held by covered entities and business associates — it does not apply to general-purpose industrial IoT gateways unless they specifically process health data in a HIPAA-covered context. The FTC Safeguards Rule applies to financial institutions, not industrial device manufacturers.
    *   *Why D is incorrect:* PCI DSS applies to entities that store, process, or transmit payment card data — it is not a product security regulation for device manufacturers. Even if some deployments process payment data, PCI DSS obligations fall on the merchant or payment processor, not the gateway manufacturer.
