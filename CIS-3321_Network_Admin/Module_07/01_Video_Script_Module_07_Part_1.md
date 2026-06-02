# Video Script: Module 07 – WAN and Cloud Connectivity

## CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Part 1 of 2 | Estimated Duration: 13–15 minutes

## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: Course banner — "CIS-3321 Network Administration | Module 07: WAN and Cloud Connectivity | Texas Wesleyan University"]

---

### Section 1: Introduction

[00:00 – 01:00]

[SHOW SLIDE: Professor Nash on camera with module title card]

Welcome to Module 07. I'm Professor Nash. Up to this point in the course we have focused on local area networks — the devices, cables, protocols, and wireless standards that connect machines inside a single building or campus. This module expands the scope. Wide Area Networks connect sites across cities, countries, and continents. Cloud connectivity extends the enterprise network into provider-managed infrastructure. And VPN technologies allow remote users and branch offices to use public internet infrastructure securely as if they were inside the corporate network.

Part 1 covers WAN technology types — the physical and logical services carriers provide — and cloud service and deployment models. Part 2 covers VPN technologies, IPsec modes, and remote access solutions.

---

### Section 2: WAN Technology Overview

[01:00 – 04:30]

[SHOW DIAGRAM: A map-style illustration showing two corporate buildings connected through a cloud labeled "Carrier WAN Network." Inside the carrier cloud, multiple labeled WAN technology types are shown: MPLS, DSL, Cable/DOCSIS, Metro Ethernet, and SD-WAN. Each is connected to the edge routers of the two buildings via labeled WAN links.]

[Alt-text: A network topology diagram showing two corporate office buildings connected through a carrier WAN cloud. Inside the cloud are labeled technology boxes: MPLS, DSL, Cable/DOCSIS, Metro Ethernet, and SD-WAN. Each technology is shown as a possible WAN link connecting the two building edge routers through the carrier infrastructure.]

A Wide Area Network is any network that spans a geographic area too large for LAN technologies — connecting offices in different cities, states, or countries using carrier-provided services.

The key WAN technologies you need to know for the exam:

**MPLS (Multiprotocol Label Switching)** — A carrier service where packets are forwarded based on short path labels rather than IP addresses. MPLS enables traffic engineering and guaranteed Quality of Service (QoS) with defined traffic classes. It is the enterprise standard for branch office connectivity when guaranteed latency and uptime are required — critical for VoIP, video conferencing, and ERP traffic. MPLS runs on dedicated carrier infrastructure, not the public internet.

**DSL (Digital Subscriber Line)** — Broadband over traditional copper telephone lines. ADSL (Asymmetric DSL) provides faster download speeds than upload. Distance-limited — performance degrades beyond approximately 18,000 feet from the carrier's central office. Best-effort service with no QoS guarantees. Used for small offices and home-office users. Maximum practical speed is typically 20–40 Mbps downstream.

**Cable / DOCSIS** — Broadband over cable television coaxial infrastructure. DOCSIS (Data Over Cable Service Interface Specification) modems connect to the cable provider's headend. Bandwidth is shared with neighbors on the same cable segment, meaning peak-hour congestion is possible. Speeds can reach several hundred Mbps downstream. Also a best-effort service.

**Metro Ethernet** — A carrier service that delivers Ethernet connectivity between sites in the same metropolitan area over the carrier's fiber infrastructure. The customer sees a simple Ethernet interface — the carrier handles the underlying transport. Metro Ethernet provides high bandwidth (typically 100 Mbps to 10 Gbps) with defined SLAs. Common for connecting buildings in the same city.

**SD-WAN (Software-Defined WAN)** — A modern approach that uses software control to intelligently route traffic across multiple WAN connections (MPLS, internet, LTE) based on real-time conditions and application policy. SD-WAN can prioritize VoIP traffic over a dedicated link and route bulk data over cheaper internet links simultaneously. Increasingly common in enterprise deployments as a replacement for or complement to MPLS.

> Network+ Exam Tip: MPLS provides guaranteed QoS. DSL and cable are best-effort. When a scenario requires guaranteed latency for VoIP or video, MPLS is the answer. When a scenario describes a remote employee using a home connection, DSL or cable is the implied WAN type.

---

### Section 3: WAN Connection Types and Circuit Terms

[04:30 – 07:30]

[SHOW DIAGRAM: A comparison table showing three WAN circuit categories: Dedicated (T1/T3, leased line), Circuit-Switched (legacy PSTN/ISDN, dial-on-demand), and Packet-Switched (MPLS, Frame Relay, ATM). Each row shows typical speed, billing model, connection type, and a use case.]

[Alt-text: A three-row comparison table. Row 1: Dedicated/Leased Line — T1 at 1.544 Mbps or T3 at 45 Mbps, always-on fixed bandwidth, billed monthly, used for private point-to-point site connectivity. Row 2: Circuit-Switched — PSTN/ISDN, on-demand connection established per call, billed per usage, legacy backup links. Row 3: Packet-Switched — MPLS, Frame Relay, ATM, shared carrier infrastructure, variable bandwidth, labeled or virtual-circuit forwarding, used for multi-site enterprise WANs.]

Let me define the key circuit types you need to recognize:

**Leased Line (T1/T3)** — A dedicated point-to-point circuit with fixed bandwidth between two sites. T1 provides 1.544 Mbps across 24 DS0 channels. T3 provides 44.736 Mbps. Leased lines guarantee dedicated bandwidth — no sharing with other customers. More expensive than shared services; used for critical, guaranteed-bandwidth connections.

**Circuit-Switched** — A dedicated path is established on demand for the duration of a session, then released. The original telephone network (PSTN) is circuit-switched. ISDN (Integrated Services Digital Network) is a legacy digital circuit-switched technology. Modern use case: dial-on-demand backup links.

**Packet-Switched** — Data is divided into packets that share network infrastructure with other customers. MPLS, Frame Relay (legacy), and ATM (legacy) are packet-switched. This is the dominant WAN model today.

**Frame Relay** — A legacy packet-switched WAN technology using virtual circuits. Defined by Committed Information Rate (CIR). Largely replaced by MPLS and Metro Ethernet. Still appears on the Network+ exam for recognition purposes.

**ATM (Asynchronous Transfer Mode)** — A legacy cell-switched technology using fixed 53-byte cells. Used in older backbone networks and some DSL infrastructure. Largely historical but exam-relevant.

---

### Section 4: Cloud Service Models — IaaS, PaaS, SaaS

[07:30 – 11:00]

[SHOW DIAGRAM: A stacked layer pyramid showing three cloud service models. At the base: IaaS (Infrastructure as a Service) — the customer manages OS and above. In the middle: PaaS (Platform as a Service) — the customer manages applications only. At the top: SaaS (Software as a Service) — the customer configures only. Each layer shows what the provider manages vs. what the customer manages.]

[Alt-text: A three-tier pyramid diagram showing cloud service model responsibility. Bottom tier labeled IaaS: the provider manages physical hardware, hypervisor, and networking; the customer manages OS, middleware, runtime, application, and data. Middle tier labeled PaaS: the provider adds management of OS, middleware, and runtime; the customer manages only application and data. Top tier labeled SaaS: the provider manages everything including the application; the customer only configures settings and uses the software.]

Cloud computing has transformed how organizations acquire and consume IT infrastructure. The three service models define who is responsible for what:

**IaaS (Infrastructure as a Service)** — The cloud provider delivers virtualized compute (VMs), storage, and networking. The customer installs and manages the operating system, patches it, installs middleware, and runs applications. Examples: AWS EC2, Azure Virtual Machines, Google Compute Engine. Best for: organizations that need flexible compute resources but want control over the OS and software stack.

**PaaS (Platform as a Service)** — The provider manages the infrastructure, OS, middleware, and runtime environment. The customer deploys and manages only the application code and data. Examples: AWS Elastic Beanstalk, Azure App Service, Google App Engine. Best for: development teams that want to focus on writing code without managing servers or OS patching. This is the model where a developer pushes code and the platform handles the rest.

**SaaS (Software as a Service)** — The provider manages and delivers a complete application. The customer only configures settings and uses the software through a browser or client. Examples: Microsoft 365, Salesforce, Google Workspace. Best for: business applications where the organization does not need to customize the underlying code.

> Network+ Exam Tip: The key distinction is the boundary of customer responsibility. IaaS — you manage OS and up. PaaS — you manage application and data only. SaaS — you configure and use. When a scenario says "the team wants to deploy code without managing virtual machines," the answer is PaaS.

---

### Section 5: Cloud Deployment Models

[11:00 – 13:30]

[SHOW DIAGRAM: Four deployment model icons side by side. Public Cloud: single cloud with a padlock showing shared multi-tenant infrastructure. Private Cloud: cloud icon with a building showing exclusive organizational ownership. Hybrid Cloud: two arrows connecting public and private cloud. Community Cloud: shared cloud showing multiple organization logos with common interests.]

[Alt-text: Four labeled icons arranged horizontally. First icon labeled Public Cloud shows a shared cloud with multiple user icons representing multi-tenant infrastructure owned by the provider. Second icon labeled Private Cloud shows a cloud within a building perimeter representing dedicated organizational infrastructure. Third icon labeled Hybrid Cloud shows bidirectional arrows connecting a public cloud icon to a private cloud/building icon. Fourth icon labeled Community Cloud shows a cloud shared by multiple organization logos representing organizations with common compliance or mission requirements.]

The deployment model describes who owns and operates the cloud infrastructure — separate from the service model (IaaS/PaaS/SaaS):

**Public Cloud** — Infrastructure owned and operated by a third-party provider, shared among multiple customers (tenants). Resources are allocated and billed on demand. Advantages: no capital expense, rapid elasticity, pay-per-use. Providers: AWS, Microsoft Azure, Google Cloud Platform. Security consideration: shared infrastructure requires trust in provider isolation mechanisms.

**Private Cloud** — Infrastructure dedicated to a single organization. Can be on-premises (in the organization's own data center) or hosted by a provider exclusively for that organization. Provides greater control and security for regulated industries (healthcare, finance, government). Higher cost than public cloud.

**Hybrid Cloud** — A combination of public and private cloud environments connected by secure links. Organizations keep sensitive workloads in the private cloud while bursting to the public cloud for variable demand. Common pattern: private cloud for regulated data, public cloud for customer-facing web applications.

**Community Cloud** — Shared infrastructure among organizations with common requirements — for example, federal agencies sharing a government-authorized cloud, or healthcare organizations sharing a HIPAA-compliant platform.

In Part 2, we move to VPN technologies — IPsec, SSL/TLS VPN, tunneling protocols, and remote access architectures.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

*End of Part 1*
