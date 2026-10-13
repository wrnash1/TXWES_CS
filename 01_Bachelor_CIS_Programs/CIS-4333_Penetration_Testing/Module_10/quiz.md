# Quiz: Module 10 — Wireless and Network Penetration Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Time limit: 20 minutes.

---

## Questions

**Question 1**

During a WPA2 four-way handshake capture, which element is transmitted by the access point in Message 1 that is critical to offline passphrase cracking?

A. The GTK (Group Temporal Key) encrypted with the PMK

B. The ANonce (Access Point Nonce)

C. The SNonce (Supplicant Nonce) encrypted with the PSK

D. The PTK (Pairwise Transient Key) in cleartext

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. The GTK is transmitted in Message 3, not Message 1, and it is encrypted with the PTK (which does not yet exist in Message 1).
- B is correct. The ANonce in Message 1 is used by the client to derive the PTK. Combined with the SNonce from Message 2 and the SSID, it enables offline dictionary attacks.
- C is incorrect. The SNonce is transmitted in Message 2 (from the client to the AP), not Message 1. It is not encrypted with the PSK.
- D is incorrect. The PTK is never transmitted in cleartext. It is independently derived by both parties.

---

**Question 2**

A penetration tester discovers that a WPA2-Enterprise network does not validate the RADIUS server's TLS certificate on client devices. Which tool would best exploit this misconfiguration?

A. Aircrack-ng with rockyou.txt

B. hcxdumptool targeting PMKID frames

C. hostapd-wpe configured as a rogue enterprise AP

D. aireplay-ng with --deauth to capture the handshake

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. Aircrack-ng cracks WPA2-Personal PSK handshakes. Enterprise networks use 802.1X, not PSK.
- B is incorrect. PMKID attacks target WPA2-Personal. Enterprise networks using 802.1X do not generate PMKID values in the same way.
- C is correct. hostapd-wpe creates a rogue enterprise AP that accepts EAP authentication. When clients do not verify the server certificate, they connect to the rogue AP and submit credentials, which hostapd-wpe captures.
- D is incorrect. Deauthentication causes reconnection but generates a new 802.1X exchange, not a PSK handshake. It does not directly yield credentials.

---

**Question 3**

An attacker sends forged deauthentication frames from the access point's MAC address to all clients. Which 802.11 frame type is being abused?

A. Control frame, subtype CTS

B. Data frame, subtype QoS Data

C. Management frame, subtype Deauthentication

D. Management frame, subtype Disassociation

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. CTS (Clear to Send) is a control frame used for channel reservation, not association management.
- B is incorrect. QoS Data frames carry payload data, not association management.
- C is correct. Deauthentication (Management subtype 12) terminates an association. These frames are unauthenticated in WPA2, enabling forgery.
- D is incorrect. Disassociation (Management subtype 10) is a related but distinct frame that removes a client from the basic service set. Deauthentication is the standard tool for forcing reconnection in this attack.

---

**Question 4**

A tester needs to reach a database server at 10.10.30.5:3306 that is only accessible from an internal web server at 10.10.20.10, which the tester can access via SSH. Which command creates the necessary tunnel?

A. `ssh -D 1080 -N user@10.10.20.10`

B. `ssh -L 3306:10.10.30.5:3306 user@10.10.20.10`

C. `ssh -R 3306:localhost:3306 user@10.10.20.10`

D. `ssh -L 10.10.30.5:3306:localhost:3306 user@10.10.20.10`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Dynamic port forwarding creates a SOCKS proxy for general routing. It would work with proxychains but is not the most direct solution for a single specific port.
- B is correct. `-L 3306:10.10.30.5:3306` creates a local port forward: connections to localhost:3306 on the attacker's machine are forwarded through 10.10.20.10 to 10.10.30.5:3306.
- C is incorrect. `-R` creates remote port forwarding — it forwards a port on the remote (SSH server) back to the attacker's machine. This is used for reverse shells, not for reaching internal hosts.
- D is incorrect. The syntax is malformed. The `-L` flag syntax is `localport:remotehost:remoteport` — the bind address on the left side should be a local port number, not a remote IP.

---

**Question 5**

Which Hashcat mode is used for cracking WPA2 EAPOL and PMKID hashes captured from 802.11 traffic?

A. Mode 1000 (NTLM)

B. Mode 5500 (NetNTLMv1)

C. Mode 22000 (WPA-PBKDF2-PMKID+EAPOL)

D. Mode 2500 (WPA/WPA2 — deprecated)

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. Mode 1000 is for NTLM hashes, used in Windows Active Directory attacks.
- B is incorrect. Mode 5500 is for NetNTLMv1, which appears in SMB/NTLM authentication challenges.
- C is correct. Mode 22000 is the current unified mode for WPA/WPA2 cracking, handling both PMKID and EAPOL-based captures from hcxpcapngtool output.
- D is incorrect. Mode 2500 was the legacy WPA/WPA2 mode. It has been deprecated and replaced by mode 22000, which is more robust and handles PMKID.

---

**Question 6**

During a network pivot, a tester wants to scan 10.10.30.0/24 through a Meterpreter session on a compromised host in the 10.10.20.0/24 subnet. After running `route add 10.10.30.0/24 [session_id]`, which module enables external tools to use this route?

A. `auxiliary/scanner/portscan/tcp`

B. `auxiliary/server/socks_proxy`

C. `post/multi/manage/autoroute`

D. `exploit/multi/handler`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. The TCP port scanner runs within Metasploit itself, which can use the route directly. But it does not expose the route to external tools.
- B is correct. `auxiliary/server/socks_proxy` creates a SOCKS proxy server that routes connections through Metasploit's routing table, allowing proxychains and other external tools to reach the internal subnet.
- C is incorrect. `post/multi/manage/autoroute` sets up routes automatically from within a session — it performs the routing setup but does not create the SOCKS proxy for external tool access.
- D is incorrect. `exploit/multi/handler` is for catching incoming shells. It does not provide pivot routing capability.

---

**Question 7**

A tester wants to evade a stateless packet-filtering firewall that blocks traffic on all ports except 80, 443, and 53. Which technique is MOST likely to succeed?

A. Nmap -T0 paranoid timing to slow scan rate below threshold

B. Nmap -D RND:10 to generate decoy source addresses

C. Tunneling C2 traffic over DNS on port 53

D. Nmap -f packet fragmentation to bypass signature detection

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. Timing evasion addresses detection thresholds in IDS systems. A stateless firewall's port-based rules are not affected by timing.
- B is incorrect. Decoy scanning disguises the true source but does not bypass port-based firewall rules. Traffic on blocked ports is still dropped regardless of source address.
- C is correct. DNS (port 53) is one of the permitted ports. Tunneling C2 traffic as DNS queries bypasses port-based filtering entirely. Tools like dnscat2 implement this.
- D is incorrect. Fragmentation can bypass stateless firewall rules that examine payload content, but the fragments still arrive on whatever port is being used. If the port is blocked, fragmented packets on that port are still dropped.

---

**Question 8**

The PMKID attack on WPA2-Personal is advantageous over traditional handshake capture because:

A. It is faster to crack because the PMKID uses MD5 instead of PBKDF2-HMAC-SHA1.

B. It can be performed without waiting for a client to authenticate to the access point.

C. It bypasses WPA2-Enterprise authentication entirely.

D. It works against WPA3-SAE networks without modification.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. The PMKID itself uses HMAC-SHA1, and cracking still requires PBKDF2-HMAC-SHA1 derivation for each candidate passphrase. Cracking speed is similar to traditional handshake attacks.
- B is correct. The PMKID is transmitted in the first EAPOL-Key frame from the AP to any connecting client — or can be solicited with a single probe. No complete client authentication is needed.
- C is incorrect. The PMKID attack targets WPA2-Personal (PSK). Enterprise networks use 802.1X and do not have a PSK to derive the PMKID.
- D is incorrect. WPA3-SAE does not use PMKID in the same manner. WPA3 is designed to prevent offline dictionary attacks.

---

**Question 9**

An IDS analyst notices that Nmap probe packets targeting their web server have TTL values of exactly 1 on arrival, while the actual TCP SYN packets appear normal. This is characteristic of which evasion technique?

A. Polymorphic shellcode encoding

B. Insertion attack using low-TTL decoy packets

C. Protocol tunneling over ICMP

D. Source port spoofing to bypass ACL rules

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Polymorphic shellcode addresses payload signature detection in IDS rules, not TTL manipulation.
- B is correct. In an insertion attack, packets with TTL values low enough to expire before reaching the target (but not before the IDS sees them) are inserted alongside legitimate probes. The IDS reconstructs a stream including these packets; the target sees only the normal packets.
- C is incorrect. ICMP tunneling hides data in the payload of ICMP packets. It does not involve TTL manipulation for evasion purposes.
- D is incorrect. Source port spoofing exploits ACL rules that permit traffic from specific "trusted" source ports (like port 53 or 20). It is unrelated to TTL values.

---

**Question 10**

A client requests a wireless penetration test of their corporate headquarters. The scope document specifies testing of "all wireless networks operated by the client." During the survey, the tester discovers a neighbor's SSID is broadcasting within the building. What is the correct action?

A. Test the neighbor's network since it is within the building's RF footprint and poses a risk to the client.

B. Document the neighbor's SSID as an out-of-scope finding and include it as an informational note in the report.

C. Attempt passive capture only since that does not interact with the neighbor's network.

D. Notify the client that their scope authorization includes all signals detected within the facility.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. "All wireless networks operated by the client" explicitly excludes third-party networks. Testing a neighbor's network without their authorization is a federal crime regardless of physical location.
- B is correct. The appropriate action is to document the neighbor's signal as an informational finding — noting the RF leakage as a potential risk (unwanted signals inside the facility) — without testing it.
- C is incorrect. While passive capture is less invasive, intentionally capturing frames from a network without authorization still raises ECPA concerns. More importantly, the correct action is documentation and notification, not any level of testing.
- D is incorrect. The scope document language "operated by the client" is the controlling constraint. Physical proximity does not imply authorization.

---

## Answer Key

| Question | Answer |
|----------|--------|
| 1 | B |
| 2 | C |
| 3 | C |
| 4 | B |
| 5 | C |
| 6 | B |
| 7 | C |
| 8 | B |
| 9 | B |
| 10 | B |
