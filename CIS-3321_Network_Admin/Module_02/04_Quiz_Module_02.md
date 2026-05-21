# Quiz: Module 02 - TCP/IP Model and Network Protocols
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

**Question 1**
An administrator wants to segment a switch's ports logically into separate broadcast domains. Which technology should they configure?
A) NAT (Network Address Translation)
B) DHCP (Dynamic Host Configuration Protocol)
C) VLAN (Virtual Local Area Network)
D) STP (Spanning Tree Protocol)
*   **Correct Answer:** C) VLAN (Virtual Local Area Network)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* NAT translates between public and private IP addresses at Layer 3; it does not segment local switch broadcast domains.
    *   *Why B is incorrect:* DHCP dynamically assigns IP configuration to clients; it does not create broadcast domain boundaries on a switch.
    *   *Why D is incorrect:* STP (Spanning Tree Protocol) prevents Layer 2 switching loops in redundant topologies; it does not divide a switch into isolated broadcast domains.

---

**Question 2**
A network technician is troubleshooting email delivery. Users can receive email but cannot send new messages to external recipients. Which protocol and port combination is most likely involved in the sending failure?
A) IMAP on port 143 — the client cannot retrieve messages from the mail server
B) SMTP on port 25 — the outbound mail server cannot relay messages to external domains
C) POP3 on port 110 — the client is downloading messages and deleting them from the server
D) HTTPS on port 443 — the webmail interface is unreachable due to a TLS certificate error
*   **Correct Answer:** B) SMTP on port 25 — the outbound mail server cannot relay messages to external domains
*   **Distractor Analysis:**
    *   *Why A is incorrect:* IMAP (port 143) is used to access and read email stored on a server; it is a receive-side protocol, not involved in sending messages to external recipients.
    *   *Why C is incorrect:* POP3 (port 110) downloads messages from a server to a client; it is a receive-side protocol and has no role in sending outbound email.
    *   *Why D is incorrect:* HTTPS (port 443) would affect the webmail interface login, but the question specifies outbound mail delivery failure, which is an SMTP function.

---

**Question 3**
A network engineer needs to verify basic IP connectivity and measure round-trip latency to a remote server. Which command is most appropriate?
A) ping
B) traceroute
C) netstat -ano
D) nslookup
*   **Correct Answer:** A) ping
*   **Distractor Analysis:**
    *   *Why B is incorrect:* `traceroute` maps each intermediate router hop along the path; it provides routing path information, not a simple latency/connectivity test.
    *   *Why C is incorrect:* `netstat -ano` displays active local TCP/UDP connections, listening ports, and process IDs on the local machine — it does not test remote connectivity.
    *   *Why D is incorrect:* `nslookup` queries DNS servers to resolve hostnames to IP addresses; it does not measure IP-layer connectivity or latency.

---

**Question 4**
A workstation receives an IP address of 169.254.x.x after booting. The user cannot access any network resources. What is the most likely cause?
A) The DNS server is offline and cannot resolve hostnames.
B) The workstation failed to receive a DHCP lease and self-assigned an APIPA address.
C) The default gateway is configured with an incorrect subnet mask.
D) The network switch port has Port Security enabled and is blocking the device's MAC address.
*   **Correct Answer:** B) The workstation failed to receive a DHCP lease and self-assigned an APIPA address.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A DNS failure would produce a valid DHCP-assigned IP address; the user could still ping IP addresses directly. An APIPA address (169.254.x.x) specifically indicates the DHCP discovery process failed entirely.
    *   *Why C is incorrect:* A gateway subnet mask error would still result in a valid IP address being assigned; it would not produce the 169.254.x.x APIPA range.
    *   *Why D is incorrect:* Port Security blocking a MAC address would prevent all frames from passing, resulting in no network link — not an APIPA address assignment.

---

**Question 5**
A security audit finds that administrators are managing network switches using a protocol that transmits all credentials and commands in cleartext over port 23. Which security control should be implemented to remediate this vulnerability?
A) Disable Telnet and configure SSH on port 22 for all switch management sessions.
B) Enable HTTPS on port 443 and disable HTTP on port 80 for the switch web interface.
C) Implement SNMP v3 with authentication and encryption to replace SNMP v1 community strings.
D) Deploy a RADIUS server to centralize authentication for all management access using 802.1X.
*   **Correct Answer:** A) Disable Telnet and configure SSH on port 22 for all switch management sessions.
*   **Distractor Analysis:**
    *   *Why A is correct:* Port 23 is Telnet, which is the cleartext protocol described in the scenario. SSH (port 22) provides encrypted terminal access and is the direct replacement.
    *   *Why B is incorrect:* Switching HTTP to HTTPS addresses web interface security, but the scenario specifically identifies port 23 (Telnet) as the problem, not HTTP/HTTPS.
    *   *Why C is incorrect:* Upgrading to SNMPv3 addresses insecure SNMP community strings (port 161), not the Telnet management vulnerability on port 23.
    *   *Why D is incorrect:* RADIUS/802.1X centralizes authentication but does not by itself replace the unencrypted Telnet protocol with an encrypted one.
