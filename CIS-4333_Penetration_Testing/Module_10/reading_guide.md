# Reading Guide: Module 10 — Wireless and Network Penetration Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Overview

This reading guide accompanies Module 10 and provides the conceptual foundation for wireless and network penetration testing. All techniques described assume explicit written authorization from the system/network owner. Unauthorized wireless testing violates federal law under 18 U.S.C. § 2511 (Electronic Communications Privacy Act) and 18 U.S.C. § 1030 (Computer Fraud and Abuse Act).

---

## Learning Objectives

After completing this module, students will be able to:

1. Explain the 802.11 authentication and association process at the frame level.
2. Identify the cryptographic weaknesses in WPA2-Personal that enable offline cracking.
3. Execute a supervised wireless assessment using the Aircrack-ng suite.
4. Describe the evil twin attack and its application in enterprise testing.
5. Explain network pivoting concepts and implement SSH and Metasploit-based tunnels.
6. Apply firewall and IDS evasion techniques in authorized assessment scenarios.
7. Map wireless findings to CVSS scores and remediation recommendations.

---

## Section 1: 802.11 Protocol Architecture

### 1.1 Frame Structure

The 802.11 MAC frame consists of a fixed header, variable-length body, and frame check sequence. The two-byte Frame Control field encodes the frame type and subtype. Key subtypes for security testing include:

- Beacon (Management, Subtype 8): Broadcast by APs every 102.4 ms by default.
- Probe Request (Management, Subtype 4): Sent by clients searching for known SSIDs.
- Authentication (Management, Subtype 11): Initiates the authentication sequence.
- Deauthentication (Management, Subtype 12): Terminates an association.
- EAPOL (Data): Carries the four-way WPA2 handshake frames.

### 1.2 The WPA2 Four-Way Handshake

The four-way handshake establishes session keys between a client (supplicant) and access point (authenticator). The process requires both parties to prove knowledge of the PMK (Pairwise Master Key, derived from the PSK) without transmitting it:

**Message 1:** AP sends ANonce (AP nonce) to client.

**Message 2:** Client derives PTK using ANonce, SNonce (client nonce), AP MAC, and client MAC. Client sends SNonce and MIC (Message Integrity Code) to AP.

**Message 3:** AP verifies the MIC, derives the same PTK, and sends the GTK (Group Temporal Key) encrypted with the PTK.

**Message 4:** Client sends acknowledgment.

The critical vulnerability: Messages 2 and 3 contain sufficient information for an offline attacker to verify passphrase guesses. If an attacker captures the full handshake (or even a PMKID from Message 1), they can run dictionary or brute-force attacks without interacting with the network again.

### 1.3 WPA3 and SAE

WPA3 replaces PSK with SAE (Simultaneous Authentication of Equals), based on the Dragonfly handshake. SAE provides forward secrecy — past session keys cannot be derived even if the current password is later compromised. SAE also eliminates offline dictionary attacks because each authentication attempt requires a live exchange.

Transition mode (WPA2/WPA3 mixed) downgrades susceptible clients to WPA2, preserving the attack surface. Testing should note whether transition mode is enabled.

---

## Section 2: Aircrack-ng Suite Deep Dive

### 2.1 Tool Architecture

The Aircrack-ng suite is a collection of focused tools, each handling one aspect of wireless assessment:

| Tool | Function |
|------|----------|
| airmon-ng | Interface mode management |
| airodump-ng | Packet capture and visualization |
| aireplay-ng | Frame injection (deauth, fake auth, fragmentation) |
| aircrack-ng | WEP/WPA2 key recovery |
| airdecap-ng | Decrypt captured WEP/WPA2 traffic |
| packetforge-ng | Craft arbitrary 802.11 frames |

### 2.2 Interface Configuration

Before capturing, confirm the adapter supports monitor mode and injection. The `iw list` command shows interface capabilities. `airmon-ng check kill` terminates processes (NetworkManager, wpa_supplicant) that interfere with monitor mode.

Monitor mode places the adapter in promiscuous capture mode for all 802.11 traffic on the tuned channel. The adapter does not associate with any network. Standard 2.4 GHz channels are 1–14 (region-dependent). The 5 GHz band uses channels 36–165.

Channel hopping with `--channel` fixed prevents missing traffic on specific networks. Airodump-ng's `--band a` flag extends capture to 5 GHz.

### 2.3 PMKID Capture (Clientless Attack)

The PMKID attack, published by Jens Steube in 2018, enables WPA2 cracking without capturing a four-way handshake. The PMKID is derived as:

```
PMKID = HMAC-SHA1-128(PMK, "PMK Name" || AP_MAC || Client_MAC)
```

The PMKID is transmitted in the EAPOL-Key frame that begins the four-way handshake — specifically in the RSN Information Element of Message 1. An attacker can request this single frame from the AP without waiting for a client to connect.

Tool `hcxdumptool` captures PMKIDs efficiently:

```
hcxdumptool -i wlan0mon --enable_status=1 -o pmkid_capture.pcapng
hcxpcapngtool -o hash.hc22000 pmkid_capture.pcapng
hashcat -m 22000 hash.hc22000 wordlist.txt
```

---

## Section 3: Evil Twin and Rogue AP Attacks

### 3.1 Open Network Evil Twin

The simplest evil twin targets open networks. The attacker creates an AP with the same SSID and no encryption. Clients configured for auto-connect will associate with whichever AP has the stronger signal.

Once connected, all client traffic flows through the attacker's device. ARP spoofing or the inherent routing position provides man-in-the-middle access. SSL stripping attacks (sslstrip) can downgrade HTTPS connections if HSTS is not enforced.

### 3.2 WPA2-Personal Evil Twin

Against password-protected networks, the evil twin operates slightly differently. The attacker creates an AP with the same SSID but no password (or a known password). Clients that auto-connect based on SSID matching (rather than BSSID matching) may associate.

This attack is most effective when combined with a deauthentication flood against the legitimate AP, degrading its availability and compelling clients to connect elsewhere.

### 3.3 WPA2-Enterprise Evil Twin (EAP Credential Harvesting)

Enterprise networks use 802.1X, but client-side misconfiguration is common. If the supplicant (client software) does not verify the RADIUS server's TLS certificate, an attacker's rogue AP can accept EAP authentication attempts.

`hostapd-wpe` captures PEAP/EAP-TTLS challenge-response exchanges. For EAP-TTLS/PAP, credentials may be captured in cleartext within the tunnel. For PEAP-MSCHAPv2, the captured NETNTLM hash can be cracked with Hashcat mode 5500.

Remediation: Enforce RADIUS certificate validation in 802.1X supplicant profiles. Deploy certificate pinning or deploy client certificates (EAP-TLS) to eliminate password-based EAP entirely.

---

## Section 4: Network Pivoting

### 4.1 Pivot Concepts and Architecture

Network pivoting leverages a compromised host as a relay point to reach otherwise inaccessible network segments. Enterprise networks commonly use multiple security zones:

- DMZ: Internet-facing servers, limited inbound access from internet
- Internal LAN: Corporate workstations, servers
- Restricted zones: Database servers, OT/ICS, sensitive data repositories
- Management network: Out-of-band management for network devices

A firewall may permit HTTP/S from the internet to the DMZ but block direct internet access to the internal LAN. A pivot through the compromised DMZ host bypasses these restrictions.

### 4.2 SSH Tunneling

SSH supports three tunneling modes:

**Local port forwarding:** `ssh -L 8080:internal-server:80 user@pivot-host` — connections to localhost:8080 are forwarded through pivot-host to internal-server:80.

**Remote port forwarding:** `ssh -R 4444:localhost:4444 user@pivot-host` — connections to pivot-host:4444 are forwarded back to the attacker's machine on port 4444. Useful for reverse shells through restrictive egress filters.

**Dynamic port forwarding (SOCKS):** `ssh -D 1080 -N user@pivot-host` — creates a SOCKS4/5 proxy on localhost:1080 that routes all connections through the pivot host.

### 4.3 Metasploit Pivoting

Metasploit's route command adds network routes through active Meterpreter sessions. After routing, Metasploit modules (scanners, exploits) can reach previously inaccessible subnets.

The `auxiliary/server/socks_proxy` module exposes these routes as a SOCKS proxy for external tools. `proxychains` transparently routes arbitrary tools through the proxy.

**Portfwd** within Meterpreter provides individual port forwarding without requiring a full SOCKS proxy:

```
meterpreter> portfwd add -l 3389 -p 3389 -r 10.10.20.5
```

This forwards the attacker's local port 3389 to the target host's RDP port through the Meterpreter session.

---

## Section 5: Firewall and IDS Evasion

### 5.1 Firewall Architectures

Understanding the firewall type determines the appropriate evasion strategy:

**Stateless/packet filtering:** Examines individual packets against rules. Fragmentation and source port spoofing are effective.

**Stateful inspection:** Tracks connection state. Requires more sophisticated evasion including protocol manipulation.

**Next-generation firewalls (NGFW):** Perform deep packet inspection, application identification, and user-based policy. Tunnel traffic within legitimate application protocols (HTTPS, DNS) to evade.

**Web application firewalls (WAF):** Specific to HTTP/S. Encode payloads, vary parameter names, use chunked encoding to evade signature-based rules.

### 5.2 Protocol Tunneling

DNS tunneling encapsulates arbitrary data within DNS queries and responses. The attacker controls a domain and runs a DNS server that decodes the tunneled data. Tools include `iodine` (IP-over-DNS), `dnscat2` (command and control over DNS).

ICMP tunneling hides data in the variable-length data field of ICMP Echo packets. Tools include `ptunnel-ng`.

HTTPS tunneling uses legitimate TLS connections to carry C2 traffic. SSL inspection at the perimeter firewall can detect this — testing should note whether SSL inspection is deployed.

### 5.3 IDS Evasion Fundamentals

IDS evasion exploits the ambiguity between how the IDS and the target interpret the same traffic.

**Fragmentation:** The IDS may not reassemble fragmented packets correctly, missing signatures that span fragment boundaries.

**TTL manipulation:** Inserting packets with TTLs that expire before reaching the target but not before being logged by the IDS. The IDS sees an incomplete stream; the target sees a different stream.

**Polymorphic shellcode:** Using encoding (XOR, shikata_ga_nai) to change the binary signature of shellcode on each use, defeating static signature matching.

**Timing evasion:** Slowing scan rates below detection thresholds. Nmap's `-T0` paranoid timing inserts 5-minute delays between probes.

---

## Section 6: PenTest+ Exam Alignment

### 6.1 Domain Mapping

| Topic | PT0-002 Domain | Objective |
|-------|---------------|-----------|
| Wireless attacks | 3.3 | Network attacks |
| Evil twin | 3.3 | Wireless attacks |
| Pivoting | 3.4 | Post-exploitation |
| Firewall evasion | 3.3 | Evasion techniques |
| IDS evasion | 3.3 | Evasion techniques |

### 6.2 High-Frequency Exam Topics

Know the following for the PT0-002 exam:

- The WPA2 four-way handshake and what is needed for offline cracking (ANonce, SNonce, MIC, SSID)
- Difference between WPA2-Personal (PSK) and WPA2-Enterprise (802.1X/RADIUS)
- The PMKID attack and why it does not require a client association
- How deauthentication attacks exploit unauthenticated management frames
- The purpose and configuration of evil twin attacks
- SSH port forwarding syntax for local, remote, and dynamic modes
- Nmap evasion flags: `-f`, `--mtu`, `-D`, `--source-port`, `-T0`
- IDS evasion concepts: insertion, evasion, TTL manipulation

---

## Key Terms

**BSSID:** Basic Service Set Identifier — the MAC address of the access point radio.

**SSID:** Service Set Identifier — the human-readable network name.

**PTK:** Pairwise Transient Key — the per-session encryption key derived from the PMK.

**GTK:** Group Temporal Key — the key used to encrypt broadcast and multicast traffic.

**PMKID:** Pairwise Master Key Identifier — a hash value in EAPOL-Key frames enabling clientless WPA2 attacks.

**802.1X:** The IEEE standard for port-based network access control used in WPA2-Enterprise.

**SOCKS proxy:** A protocol-agnostic proxy that tunnels arbitrary TCP/UDP connections.

**Evil twin:** A rogue access point configured to mimic a legitimate network to intercept client connections.

**NETNTLM:** A challenge-response hash format used in Windows authentication, capturable via rogue EAP servers.

---

## Review Questions

1. What four pieces of information are required to perform an offline WPA2 dictionary attack after capturing a four-way handshake?

2. How does the PMKID attack differ from a traditional handshake capture, and what makes it more accessible?

3. Explain why WPA2-Enterprise is more secure than WPA2-Personal and what client-side misconfiguration can undermine this security.

4. Describe the difference between SSH local port forwarding and dynamic port forwarding. When would you use each?

5. What is an insertion attack in the context of IDS evasion, and how does TTL manipulation enable it?

---

## References

- CompTIA PenTest+ PT0-002 Exam Objectives, Domain 3.3, 3.4
- Aircrack-ng Documentation: https://aircrack-ng.org/doku.php
- Vanhoef, M., & Piessens, F. (2017). "Key Reinstallation Attacks: Forcing Nonce Reuse in WPA2." ACM CCS 2017.
- Steube, J. (2018). "PMKID Attack on WPA/WPA2." Hashcat Blog.
- RFC 1928 — SOCKS Protocol Version 5.
- Nmap Reference Guide: https://nmap.org/book/man.html
