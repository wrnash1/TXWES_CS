# Quiz: Module 04 - Network Attacks - DDoS, Spoofing, MITM
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

**Question 1**
During an active malware outbreak, the incident response team decides to physically disconnect the infected web server from the corporate network switch, but leaves the server powered on to preserve memory artifacts. Which phase of the Incident Response Lifecycle does this action represent?
A) Identification
B) Containment
C) Eradication
D) Recovery
*   **Correct Answer:** B) Containment
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Identification is the phase where analysts confirm an incident is actually occurring — the decision to disconnect the cable is taken after identification is complete.
    *   *Why C is incorrect:* Eradication involves removing malware from the system (wiping drives, patching vulnerabilities). Disconnecting the network cable stops spread but leaves the malware in place.
    *   *Why D is incorrect:* Recovery restores the system to normal production operations, which cannot begin until eradication is confirmed and verified.

---

---

**Question 2**
A network administrator notices that all traffic on a LAN segment is being redirected through an unauthorized host before reaching the default gateway. A packet capture confirms the unauthorized host is sending unsolicited ARP replies. Which attack is taking place?
A) DNS Cache Poisoning
B) IP Spoofing
C) ARP Poisoning
D) Smurf Attack
*   **Correct Answer:** C) ARP Poisoning
*   **Distractor Analysis:**
    *   *Why A is incorrect:* DNS cache poisoning injects fraudulent DNS records into a resolver — it operates at Layer 7 and does not involve ARP replies or Layer 2 MAC address manipulation.
    *   *Why B is incorrect:* IP spoofing forges the source IP address field in packets but does not send unsolicited ARP replies or redirect Layer 2 traffic through an unauthorized host.
    *   *Why D is incorrect:* A Smurf attack sends ICMP echo requests with a spoofed source IP to broadcast addresses to flood the victim — it does not use ARP replies to redirect traffic.

---

---

**Question 3**
An organization's web servers become unreachable to legitimate customers. Analysis shows millions of HTTP GET requests per second arriving from thousands of geographically distributed IP addresses, all requesting a single resource-intensive database query page. Which type of attack is this?
A) SYN Flood
B) Smurf Attack
C) Application-Layer DDoS (Layer 7)
D) ARP Poisoning
*   **Correct Answer:** C) Application-Layer DDoS (Layer 7)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A SYN flood is a protocol-layer (Layer 4) attack that sends a high volume of TCP SYN packets without completing the handshake, exhausting connection state tables — it does not target specific application resources with HTTP GET requests.
    *   *Why B is incorrect:* A Smurf attack uses ICMP echo requests broadcast across a network to flood a victim — it operates at Layer 3 and does not involve HTTP application requests.
    *   *Why D is incorrect:* ARP poisoning is a local-segment Layer 2 attack that redirects traffic through an attacker — it does not involve external distributed traffic flooding a web server.

---

**Question 4**
A security analyst captures network traffic and observes that a host is sending ICMP echo requests with the victim organization's IP address as the source to multiple network broadcast addresses. Which attack does this traffic pattern indicate?
A) Man-in-the-Middle via ARP Poisoning
B) DNS Amplification Attack
C) Smurf Attack
D) Rogue DHCP Server Attack
*   **Correct Answer:** C) Smurf Attack
*   **Distractor Analysis:**
    *   *Why A is incorrect:* ARP poisoning sends fraudulent ARP replies on a local segment to redirect Layer 2 traffic — it does not involve ICMP echo requests sent to broadcast addresses.
    *   *Why B is incorrect:* DNS amplification sends small spoofed DNS queries to public resolvers that return large responses to the victim — it uses UDP port 53, not ICMP, and targets DNS servers rather than broadcast addresses.
    *   *Why D is incorrect:* A rogue DHCP server responds to DHCP discovery requests with false configuration (e.g., a malicious gateway IP) — it does not involve ICMP or broadcast amplification.

---

**Question 5**
A company wants to prevent attackers from intercepting and modifying traffic between its remote employees and internal systems. Which combination of controls BEST mitigates Man-in-the-Middle attacks?
A) Deploy an IDS sensor on the core switch and enable port mirroring to capture all traffic.
B) Enforce mutual TLS authentication and implement certificate pinning for all critical applications.
C) Require employees to change passwords every 60 days and use a minimum of 12 characters.
D) Enable full disk encryption on all laptops and require VPN split tunneling for remote access.
*   **Correct Answer:** B) Enforce mutual TLS authentication and implement certificate pinning for all critical applications.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* An IDS with port mirroring detects anomalies after the fact but does not prevent an active MITM interception — the attacker can still read and modify traffic while the IDS is alerting.
    *   *Why C is incorrect:* Password complexity and rotation policies strengthen authentication but do not protect against traffic interception in transit — an attacker in the middle intercepts encrypted sessions, not passwords.
    *   *Why D is incorrect:* Full disk encryption protects data at rest on the device. Split tunneling actually increases MITM risk by routing non-corporate traffic outside the VPN tunnel. Neither control prevents in-transit interception.
