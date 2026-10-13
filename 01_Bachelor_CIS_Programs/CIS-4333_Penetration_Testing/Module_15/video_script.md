# Video Script: Module 15 — Specialized Testing Environments

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Production Notes

- **Runtime Target:** 30–35 minutes
- **Segments:** 7
- **Visual Aids:** Cloud architecture diagram, ICS/SCADA network diagram, mobile testing setup, API testing tool screenshots
- **Lab Environment:** Web application and API testing in an authorized lab environment

---

## Segment 1: Introduction to Specialized Environments (Lines 1–30)

[SLIDE: Module 15 Title Card]

Welcome to Module 15. We are covering specialized testing environments — the dimensions of penetration testing that extend beyond traditional network and application assessments into cloud infrastructure, operational technology, IoT, mobile applications, thick clients, and APIs.

Each of these environments has unique architecture, unique attack surfaces, and critically, unique safety considerations that affect how testing must be approached.

[SLIDE: Why Specialization Matters]

The PenTest+ PT0-002 exam covers specialized environments across Domain 3. But more importantly, these environments represent where the modern attack surface actually lives. More than 90 percent of enterprise organizations have significant cloud infrastructure. Industrial systems are increasingly networked. IoT is everywhere. APIs are the backbone of modern application architecture.

A penetration tester who only knows traditional network testing is equipped to assess a shrinking portion of the actual threat landscape.

[SLIDE: Authorization Emphasis]

Throughout this module: every specialized environment has specific authorization requirements, specific safety considerations, and in some cases, regulatory constraints that affect testing methodology. We will flag these as we go.

[PAUSE for transition]

---

## Segment 2: Cloud Penetration Testing (Lines 31–70)

[SLIDE: Cloud Architecture and Attack Surface]

Cloud environments introduce an attack surface that differs fundamentally from traditional on-premises networks.

Infrastructure as a Service (IaaS — AWS, Azure, GCP): The cloud provider manages physical infrastructure and hypervisors. The customer manages the operating system, applications, and data. The security boundary shifts: network perimeter controls are replaced by identity and access management, security groups, and cloud-native services.

Platform as a Service (PaaS): The provider manages the platform layer. The customer manages applications and data only. Serverless functions, managed databases, and container orchestration are PaaS examples.

Software as a Service (SaaS): The provider manages everything. The customer manages data and configuration only.

[SLIDE: Cloud-Specific Attack Vectors]

The most impactful cloud attack vectors differ from traditional network attacks:

Identity and Access Management (IAM) misconfigurations: Overprivileged roles, cross-account trust misconfigurations, wildcard permissions (`*` in IAM policies). A single misconfigured IAM role can give an attacker access to the entire AWS account.

Instance Metadata Service (IMDS) exploitation: AWS EC2 instances have a metadata service at 169.254.169.254 that can return temporary IAM credentials. SSRF vulnerabilities in EC2-hosted applications can reach this service and steal credentials.

Storage bucket misconfigurations: S3 buckets, Azure Blob Storage, and GCS buckets configured for public access expose data without authentication. Automated tools routinely scan for public buckets containing sensitive data.

Lambda and serverless function abuse: Environment variables in serverless functions often contain database credentials and API keys.

[SLIDE: Cloud Testing Tools]

Key tools for authorized cloud penetration testing:

Prowler: AWS security assessment tool that checks for misconfigurations across hundreds of security controls.

ScoutSuite: Multi-cloud security auditing tool (AWS, Azure, GCP, Oracle, Alibaba). Produces a visual HTML report of security findings.

Pacu: AWS exploitation framework. Modules for IAM enumeration, privilege escalation, data discovery, and persistence.

CloudMapper: Visualizes AWS networks and identifies exposed resources.

CloudFox: Multi-cloud tool for finding attackable surfaces including secrets, permissions, and network paths.

[SLIDE: Cloud Testing Authorization Requirements]

Cloud providers have specific testing policies:

AWS: Permits testing of EC2, RDS, CloudFront, API Gateway, Lambda, Lightsail, Elastic Beanstalk, and Fargate instances. Explicitly prohibits simulated DDoS, DNS zone walking, and port flooding that could affect AWS infrastructure. Testing must be of the customer's own resources.

Azure: Permits customer penetration testing of Azure-hosted resources. Requires adherence to Microsoft Cloud Unified Penetration Testing Rules of Engagement.

GCP: Permits testing of Google Cloud resources by customers. Pre-approval not required but testing must not affect Google's infrastructure.

In all cases: the customer's written authorization to test their cloud environment is still required. The cloud provider's policy permits testing; the customer's SOW defines authorization.

[PAUSE for transition]

---

## Segment 3: OT/ICS/SCADA Testing (Lines 71–110)

[SLIDE: The OT/ICS/SCADA Landscape]

Operational Technology (OT) includes any hardware and software that monitors or controls physical equipment, processes, and events. Industrial Control Systems (ICS) and Supervisory Control and Data Acquisition (SCADA) systems are OT categories.

These systems run:

- Power plants and utilities
- Water treatment facilities
- Manufacturing lines
- Oil and gas pipelines
- Building automation (HVAC, elevators, fire suppression)
- Transportation infrastructure

[SLIDE: Why OT Testing Is Different]

OT systems were not designed with security in mind. They were designed for reliability, safety, and real-time deterministic operation. Key differences from IT:

**Availability is paramount.** A web server being unavailable for an hour is an annoyance. A water treatment control system being unavailable can be a public safety emergency. Aggressive scanning, exploitation attempts, and denial-of-service tests that are routine in IT can physically damage equipment or cause safety-critical failures in OT.

**Long system lifecycles.** OT systems commonly run for 20–30 years. Patches may not be available, and patch cycles are measured in years.

**Real-time constraints.** Many OT protocols require deterministic timing. Network scanning that generates unexpected traffic can disrupt timing-sensitive operations.

[SLIDE: OT Network Architecture]

The Purdue Model (Industrial Automation and Control Systems reference architecture) defines five levels:

Level 0 — Physical processes (sensors, actuators)
Level 1 — Basic control (PLCs, RTUs)
Level 2 — Area supervisory (HMI, SCADA)
Level 3 — Site operations (historian, reporting)
Level 4–5 — Enterprise IT (ERP, corporate network)

Security "air gaps" between levels are often theoretical — real environments have IT/OT connections for remote monitoring, vendor maintenance, and data integration. These connections are primary attack paths.

[SLIDE: OT Testing Safety Approach]

Authorized OT security assessments require:

Passive assessment first: Network traffic analysis using tools like Dragos, Claroty, or Nozomi to build an asset inventory without generating any probe traffic. Capture and analyze existing traffic only.

Asset identification: Enumerate OT assets from documentation, network diagrams, and passive capture. Never rely on active scanning in live OT environments.

Architecture review: Assess network segmentation, boundary controls, and IT/OT integration points through documentation and configuration review.

Vulnerability assessment: Match identified assets to known vulnerabilities without active exploitation.

Active testing only in maintenance windows: If active testing is required, conduct only in isolated test environments or approved maintenance windows with full plant coordination.

[SLIDE: Common OT/ICS Vulnerabilities]

Default credentials on HMIs and PLCs.

Unencrypted OT protocols (Modbus, DNP3, BACnet, Profibus) — designed before security was a consideration.

IT/OT flat networks: Corporate IT and OT on the same physical network with no segmentation.

Remote access: VPN, RDP, or vendor remote support connections with weak authentication.

Outdated software: Windows XP, Windows 7 on HMI workstations.

[PAUSE for transition]

---

## Segment 4: IoT Security Testing (Lines 111–140)

[SLIDE: IoT Attack Surface]

The Internet of Things encompasses billions of devices: smart cameras, building management systems, medical devices, industrial sensors, consumer electronics, and connected vehicles. Each device is a potential attack vector.

IoT devices commonly have:

- Weak or hardcoded credentials
- Outdated firmware with unpatched vulnerabilities
- Minimal security features (no TLS, no authentication)
- Insecure update mechanisms
- Unnecessary exposed services

[SLIDE: IoT Testing Methodology]

Authorized IoT security testing follows OWASP IoT Attack Surface Areas:

**Device firmware analysis:** Extract firmware from the device (JTAG, UART, flash chip) and analyze statically. Tools: Binwalk (firmware extraction), Firmwalker (sensitive data identification), Ghidra (reverse engineering).

**Network traffic analysis:** Capture traffic between the device and cloud services. Identify unencrypted protocols, hard-coded IP addresses, and insecure API calls.

**API testing:** IoT devices communicate with cloud backends via APIs. Standard web API testing applies.

**Authentication testing:** Default credentials, weak credential requirements, credential brute-forcing.

**Physical interface testing:** UART debug ports, JTAG programming interfaces, SPI/I2C bus sniffing.

[SLIDE: IoT Testing Safety Considerations]

Safety note: Medical IoT devices (pacemakers, insulin pumps, infusion systems) and safety-critical industrial IoT require specialized safety assessment protocols. Testing these devices can potentially affect patient safety. Always involve domain experts and use isolated test devices.

[PAUSE for transition]

---

## Segment 5: Mobile Application Testing (Lines 141–170)

[SLIDE: Mobile Application Attack Surface]

Mobile applications (iOS and Android) present a unique attack surface combining client-side code, API communication, and device-level features.

OWASP Mobile Top 10 defines the primary risk categories:

1. Improper Platform Usage — misuse of platform features (iOS data protection, Android permissions)
2. Insecure Data Storage — sensitive data in cleartext local storage
3. Insecure Communication — missing TLS, certificate pinning bypass
4. Insecure Authentication — weak login, insecure token storage
5. Insufficient Cryptography — weak algorithms, hardcoded keys
6. Insecure Authorization — horizontal and vertical privilege escalation in APIs
7. Client Code Quality — buffer overflows, SQL injection in local databases
8. Code Tampering — tampering protections not implemented
9. Reverse Engineering — no obfuscation, extractable secrets
10. Extraneous Functionality — debug code, test credentials left in production builds

[SLIDE: Mobile Testing Tools]

**Android testing:**

MobSF (Mobile Security Framework): Automated static and dynamic analysis for Android APKs and iOS IPAs.

Drozer: Android-specific security testing framework that runs on-device.

Frida: Dynamic instrumentation toolkit — hook into running applications to bypass security controls, extract keys, and modify behavior.

Jadx: Decompile Android APKs to readable Java source code.

**iOS testing:**

iMazing: Extract iOS app bundles from physical devices.

Objection: Runtime mobile exploration, built on Frida. Bypass biometric authentication, dump keychain contents.

**Traffic analysis:**

Burp Suite with mobile proxy configuration: Route mobile app traffic through Burp for interception and modification.

SSL Kill Switch / Frida certificate pinning bypass: Override certificate pinning to enable Burp proxy interception.

[SLIDE: Mobile Testing Lab Setup]

For Android: A rooted device or Android emulator (Genymotion, Android Studio AVD). Root access enables Frida injection and full filesystem access for data storage analysis.

For iOS: A jailbroken device for full testing capability. Most dynamic analysis requires a jailbroken device. Static analysis of the IPA file can be performed without jailbreak.

[PAUSE for transition]

---

## Segment 6: Thick Client and API Testing (Lines 171–210)

[SLIDE: Thick Client Applications]

Thick clients are traditional desktop applications that contain business logic on the client side and communicate with a server. Unlike web applications, the attack surface includes the local application binary.

**Thick client testing methodology:**

Network traffic analysis: Capture and analyze client-server communication. Many thick clients use custom binary protocols or weakly implemented encryption. Burp Suite with network-level proxying and Wireshark.

Binary analysis: Decompile the application to analyze client-side validation logic, hardcoded credentials, and local encryption keys. Tools: dnSpy (for .NET), Ghidra, IDA Pro.

Local data storage: Examine files, registry entries, SQLite databases, and memory for sensitive data stored by the application.

Authentication testing: Analyze the authentication flow between client and server. Test for authentication bypass, session management weaknesses.

Business logic testing: Identify logic enforced only on the client side that can be bypassed by modifying the client application.

[SLIDE: API Security Testing]

APIs (REST, SOAP, GraphQL) are the primary communication layer in modern applications. API security testing is a critical discipline.

**OWASP API Security Top 10 (2023):**

API1 — Broken Object Level Authorization (BOLA/IDOR): Accessing another user's resources by manipulating object identifiers.

API2 — Broken Authentication: Weak token validation, JWT flaws, missing authentication.

API3 — Broken Object Property Level Authorization: Accessing or modifying object properties the user should not be able to access.

API4 — Unrestricted Resource Consumption: Rate limiting absent or ineffective.

API5 — Broken Function Level Authorization: Accessing admin endpoints as a regular user.

API6 — Unrestricted Access to Sensitive Business Flows: Exploiting business logic through repeated automated requests.

API7 — Server-Side Request Forgery (SSRF): Manipulating the server to make requests to internal resources.

API8 — Security Misconfiguration: Default configurations, exposed debug endpoints, unnecessary HTTP methods.

API9 — Improper Inventory Management: Undocumented or deprecated APIs still accessible.

API10 — Unsafe Consumption of APIs: Trusting and using data from third-party APIs without validation.

[SLIDE: API Testing Tools]

Postman: Industry standard for API development and testing. Supports collections, variables, authentication configurations, and automated test scripts.

Burp Suite: Web proxy with full API interception, modification, and repeater functionality.

OWASP ZAP: Open-source web application and API scanner.

GraphQL-specific tools: InQL (Burp extension), graphw00f (GraphQL fingerprinting), GraphQLmap (exploitation).

JWT testing: jwt.io for decoding and modification; jwt_tool for automated JWT vulnerability testing.

---

## Segment 7: PT0-002 Alignment and Summary (Lines 211–240)

[SLIDE: Exam Domain Alignment]

Specialized environments map across PT0-002 Domain 3:

Domain 3.7 — Perform application-based attacks: Web application attacks, API testing, thick client testing.

Domain 3.8 — Perform cloud-specific attacks: AWS/Azure/GCP attack vectors, misconfiguration exploitation, serverless attacks.

The exam covers concepts and tool identification. Know:

- What SSRF is and how it relates to IMDS attacks on cloud platforms
- The OWASP API Security Top 10 categories
- The difference between IaaS, PaaS, and SaaS security models
- Why OT testing requires passive-first approaches
- The tools associated with each environment: Pacu (AWS), ScoutSuite (cloud), Frida (mobile), Binwalk (IoT firmware)

[SLIDE: PT0-002 Tool Identification]

For the exam, match tools to environments:

| Environment | Key Tools |
|-------------|-----------|
| Cloud (AWS) | Pacu, ScoutSuite, Prowler, CloudFox |
| OT/ICS | Nozomi, Claroty, Shodan, passive Wireshark |
| IoT | Binwalk, Firmwalker, Frida, Ghidra |
| Mobile | MobSF, Drozer, Frida, Objection, Jadx |
| API | Burp Suite, Postman, jwt_tool, OWASP ZAP |
| Thick Client | dnSpy, Ghidra, Wireshark, Burp Suite |

[SLIDE: Module Summary]

Module 15 surveyed six specialized testing environments: cloud infrastructure (IAM misconfigurations, IMDS exploitation, Pacu and ScoutSuite), OT/ICS/SCADA (passive-first methodology, Purdue Model, safety considerations), IoT (firmware analysis, Binwalk, Frida), mobile applications (OWASP Mobile Top 10, Frida, Objection, MobSF), thick client applications, and API security (OWASP API Top 10, Burp Suite, Postman, JWT testing).

Each environment demands specialized knowledge. Critically, each has unique safety and authorization considerations that must be understood before testing begins.

Your lab focuses on web API and mobile API testing using Burp Suite against an authorized DVWA/WebGoat environment.

[END RECORDING]
