# Quiz: Module 07 - WAN and Cloud Connectivity
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

**Question 1**
A company has multiple branch offices that need to communicate over a carrier network with guaranteed quality of service and predictable latency for VoIP traffic. Which WAN technology is best suited for this requirement?
A) DSL (ADSL) — asymmetric broadband over copper phone lines with variable contention-based latency
B) DOCSIS cable — shared coaxial broadband where neighborhood traffic affects available bandwidth
C) MPLS (Multiprotocol Label Switching) — a carrier service that uses labels to forward packets with defined traffic classes and guaranteed QoS
D) GRE tunneling — encapsulates multiprotocol traffic in IP headers for transit across a public network
*   **Correct Answer:** C) MPLS (Multiprotocol Label Switching) — a carrier service that uses labels to forward packets with defined traffic classes and guaranteed QoS
*   **Distractor Analysis:**
    *   *Why A is incorrect:* ADSL is an asymmetric best-effort broadband service; it does not provide guaranteed latency or quality of service guarantees required for enterprise VoIP.
    *   *Why B is incorrect:* Cable/DOCSIS bandwidth is shared among local subscribers, creating variable latency that is unsuitable for latency-sensitive VoIP traffic.
    *   *Why D is incorrect:* GRE is a tunneling protocol that encapsulates packets — it provides no QoS guarantees and typically runs over an existing WAN link rather than replacing it.

---

**Question 2**
A network administrator is configuring a site-to-site VPN between two corporate offices. The VPN must encrypt the entire original IP packet — including the original source and destination headers — so that only the VPN gateway addresses are visible to the transit network. Which IPsec mode accomplishes this?
A) Transport mode — encrypts only the IP payload while leaving the original IP header intact and visible
B) Tunnel mode — wraps the entire original IP packet (header + payload) inside a new IP header with VPN gateway addresses
C) GRE over plaintext — encapsulates the original packet inside a new IP header without encryption
D) SSL/TLS Transport — uses TLS record-layer encryption on individual TCP segments between hosts
*   **Correct Answer:** B) Tunnel mode — wraps the entire original IP packet (header + payload) inside a new IP header with VPN gateway addresses
*   **Distractor Analysis:**
    *   *Why A is incorrect:* IPsec Transport mode encrypts only the payload, leaving the original IP header exposed — internal source/destination addresses would be visible to the transit network, violating the requirement.
    *   *Why C is incorrect:* GRE over plaintext provides encapsulation but no encryption; original headers would be visible and the traffic would not be secured in transit.
    *   *Why D is incorrect:* SSL/TLS Transport operates at the session layer and encrypts application data between hosts — it does not wrap entire IP packets the way IPsec Tunnel mode does, and it is not used for site-to-site infrastructure VPNs.

---

**Question 3**
A remote employee is working from a hotel where the firewall blocks all traffic except ports 80 and 443. They need to connect to the corporate VPN. Which VPN technology will traverse this restrictive firewall successfully?
A) IPsec using IKEv2 on UDP port 500 and NAT-T on UDP port 4500
B) L2TP/IPsec on UDP port 1701 with IPsec encapsulation on UDP 500
C) SSL/TLS VPN on TCP port 443, which appears as standard HTTPS traffic to the firewall
D) PPTP on TCP port 1723 with GRE protocol 47 for the data tunnel
*   **Correct Answer:** C) SSL/TLS VPN on TCP port 443, which appears as standard HTTPS traffic to the firewall
*   **Distractor Analysis:**
    *   *Why A is incorrect:* IPsec IKEv2 requires UDP 500 and UDP 4500 for NAT traversal — both of these ports are blocked in this scenario.
    *   *Why B is incorrect:* L2TP/IPsec requires UDP 1701 for L2TP and UDP 500/4500 for IPsec — all blocked. It would not function in this environment.
    *   *Why D is incorrect:* PPTP requires TCP 1723 and GRE protocol 47 — TCP 1723 is not in the allowed list, and GRE is a non-TCP/UDP protocol that most restrictive firewalls block entirely.

---

**Question 4**
A company wants to migrate its customer-facing web application to the cloud. The development team wants to focus solely on writing and deploying application code without managing virtual machines, operating systems, or patching. Which cloud service model meets this requirement?
A) IaaS (Infrastructure as a Service) — provides virtual machines, storage, and networking; the team manages OS, middleware, and applications
B) PaaS (Platform as a Service) — the provider manages infrastructure and OS; the team deploys and manages only the application code
C) SaaS (Software as a Service) — the provider delivers a fully managed application; the team only configures and uses it
D) Private Cloud — on-premises virtualized infrastructure owned and operated exclusively by the company
*   **Correct Answer:** B) PaaS (Platform as a Service) — the provider manages infrastructure and OS; the team deploys and manages only the application code
*   **Distractor Analysis:**
    *   *Why A is incorrect:* IaaS requires the team to manage the OS, middleware, security patches, and runtime — exactly what they want to avoid. The team would still be responsible for everything above the hypervisor.
    *   *Why C is incorrect:* SaaS delivers a pre-built application (like email or CRM) — the team cannot deploy custom application code to a SaaS platform; they can only use what the provider offers.
    *   *Why D is incorrect:* Private cloud is a deployment model (where infrastructure is hosted), not a service model that eliminates OS management responsibility. It describes who owns the hardware, not who manages the software stack.

---

**Question 5**
A security architect is designing a remote-access solution for employees who work from home. The solution must encrypt all traffic between the employee's device and the corporate network, authenticate users with individual credentials, and prevent split tunneling so all internet traffic routes through the corporate firewall. Which combination of controls best satisfies all three requirements?
A) Deploy a full-tunnel SSL/TLS VPN with certificate-based user authentication and a VPN policy enforcing that all traffic is routed through the corporate gateway.
B) Configure WPA3-SAE on the corporate wireless network and require employees to connect to the office Wi-Fi remotely.
C) Enable IPsec Transport mode between employee laptops and the nearest branch router using a shared group PSK for authentication.
D) Implement a site-to-site GRE tunnel between the home router and corporate edge router, with no additional encryption layer.
*   **Correct Answer:** A) Deploy a full-tunnel SSL/TLS VPN with certificate-based user authentication and a VPN policy enforcing that all traffic is routed through the corporate gateway.
*   **Distractor Analysis:**
    *   *Why A is correct:* SSL/TLS VPN provides encrypted tunneling, certificate-based per-user authentication satisfies the individual credential requirement, and a full-tunnel policy routes all traffic (including internet) through the corporate firewall — meeting all three requirements.
    *   *Why B is incorrect:* WPA3-SAE is a wireless LAN security protocol for local network access — it cannot be used remotely from a home location and has no remote-access VPN capability.
    *   *Why C is incorrect:* IPsec Transport mode encrypts only the payload between two hosts and leaves the original IP header exposed — it is not designed for remote-access VPN. A shared PSK also fails the individual credential requirement.
    *   *Why D is incorrect:* GRE provides encapsulation but no encryption — all traffic would be transmitted in plaintext, failing the encryption requirement entirely.
