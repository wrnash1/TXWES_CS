# Video Script: Module 10 — Wireless and Network Penetration Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Production Notes

- **Runtime Target:** 28–32 minutes
- **Segments:** 6
- **Visual Aids:** Wireshark captures, Aircrack-ng terminal output, network diagrams
- **Lab Environment:** Isolated wireless lab with authorized access points only

---

## Segment 1: Introduction and Legal Foundations (Lines 1–35)

[SLIDE: Module 10 Title Card]

Welcome back, everyone. Module 10 covers one of the most technically rich areas of penetration testing — wireless and network security assessment.

Before we touch a single tool, I want to reinforce a principle that governs everything in this module: you must have explicit written authorization to test any wireless network. Wireless signals cross physical boundaries. They leak into parking lots, neighboring offices, and public spaces. That makes unauthorized wireless testing not just unethical but criminally prosecutable under the Computer Fraud and Abuse Act, the Electronic Communications Privacy Act, and equivalent state and international laws.

[SLIDE: Legal Warning Box]

Your rules of engagement document must specifically authorize wireless testing and define the geographic scope. "Test all systems on the 192.168.1.0/24 network" does not implicitly authorize attacking the Wi-Fi network broadcasting that range. Get it in writing. Get it specific.

With that established, let us talk about why wireless testing matters.

[SLIDE: Wireless Attack Surface]

Modern enterprise environments rely on 802.11 wireless for everything from employee laptops to building automation systems. A compromised wireless network is a direct path into the corporate LAN. Wireless pen testing validates whether encryption is configured correctly, whether rogue access points exist, and whether the physical RF environment has been properly secured.

The CompTIA PenTest+ PT0-002 exam covers wireless attacks across Domain 3 (Attacks and Exploits) and Domain 4 (Reporting and Communication). We will map every technique today to exam objectives.

[PAUSE for transition]

---

## Segment 2: 802.11 Protocol Fundamentals (Lines 36–70)

[SLIDE: 802.11 Frame Types]

To attack wireless networks, you must understand how they work at the frame level. The 802.11 standard defines three frame categories: management frames, control frames, and data frames.

Management frames handle network operations — beacons, probes, authentication, and association. Control frames manage channel access — RTS, CTS, acknowledgment. Data frames carry the actual payload.

[SLIDE: The Authentication and Association Handshake]

When a client connects to an access point, the following sequence occurs:

First, the client discovers the network through passive beacon listening or active probe requests.

Second, the client sends an authentication request. In Open System Authentication, the AP always accepts. In pre-shared key environments, this step is ceremonial.

Third, the client sends an association request, and the AP responds with an association response.

Fourth, if WPA2 is in use, the four-way handshake occurs, establishing the pairwise transient key, or PTK, that protects the session.

[SLIDE: WPA2-Personal vs. WPA2-Enterprise]

WPA2-Personal uses a pre-shared key. Every device on the network uses the same passphrase. This creates a critical vulnerability: anyone who captures the four-way handshake and knows the passphrase can decrypt all traffic.

WPA2-Enterprise uses 802.1X and a RADIUS server. Each user authenticates with individual credentials. This is significantly more secure because compromise of one credential does not expose other users' traffic.

WPA3 addresses several WPA2 weaknesses through Simultaneous Authentication of Equals, which eliminates offline dictionary attacks against the handshake. However, WPA2 remains dominant in enterprise environments, making it our primary focus.

[SLIDE: Monitor Mode]

To capture wireless traffic, your wireless adapter must support monitor mode — the ability to capture all frames on a channel regardless of destination MAC address. Not all adapters support this. For lab work, adapters based on Atheros AR9271, Ralink RT3070, or Alfa AWUS036ACH chipsets are commonly recommended.

[PAUSE for transition]

---

## Segment 3: The Aircrack-ng Suite (Lines 71–110)

[SLIDE: Aircrack-ng Tool Family]

Aircrack-ng is the standard toolkit for wireless security assessment. It consists of multiple specialized tools.

Airmon-ng manages wireless interface modes. Running `airmon-ng start wlan0` places the interface into monitor mode, typically creating a new interface named wlan0mon.

Airodump-ng captures 802.11 frames. Running `airodump-ng wlan0mon` displays all visible access points with their BSSID, channel, encryption type, and connected clients. You can narrow capture to a specific network using `--bssid` and `--channel` flags.

[SLIDE: Capturing the Four-Way Handshake]

To capture a WPA2 handshake, you need to observe a client authenticating. You can wait for a natural authentication event, or — with authorization — you can use Aireplay-ng to send deauthentication frames that force clients to reconnect.

[DEMO TRANSCRIPT]

In your authorized lab environment, the capture command looks like this:

```
airodump-ng --bssid AA:BB:CC:DD:EE:FF --channel 6 --write capture wlan0mon
```

This writes captured frames to files named capture-01.cap and associated files.

[SLIDE: Deauthentication Attack]

The deauthentication attack exploits a fundamental weakness in 802.11: management frames are not authenticated. An attacker can forge a deauthentication frame from the access point's MAC address. The client, believing it came from the legitimate AP, disconnects and immediately reconnects — generating a fresh four-way handshake.

The command in an authorized environment:

```
aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF -c CC:DD:EE:FF:00:11 wlan0mon
```

The `--deauth 5` sends five deauthentication frames. The `-a` flag specifies the AP BSSID. The `-c` flag targets a specific client.

This is a denial-of-service technique. Use it only on explicitly authorized networks with client owners aware of the test.

[SLIDE: Cracking WPA2 with Aircrack-ng]

Once you have a handshake capture, offline cracking can begin. This does not require the network to remain online.

```
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b AA:BB:CC:DD:EE:FF capture-01.cap
```

Aircrack-ng hashes each candidate password using PBKDF2-HMAC-SHA1 with the SSID as the salt and compares the result against the captured handshake material.

Dictionary attacks work well against weak or common passphrases. Rule-based attacks using Hashcat's rule engine significantly extend coverage — applying transformations like capitalization, number appending, and character substitution to base words.

[SLIDE: Hashcat for WPA2]

For GPU-accelerated cracking, convert the capture to Hashcat format:

```
hcxpcapngtool -o hash.hc22000 capture-01.cap
hashcat -m 22000 hash.hc22000 /usr/share/wordlists/rockyou.txt
```

Hashcat mode 22000 handles WPA2 PMKID and EAPOL hashes simultaneously.

[PAUSE for transition]

---

## Segment 4: Evil Twin and Rogue AP Attacks (Lines 111–145)

[SLIDE: Evil Twin Attack Concept]

An evil twin is a rogue access point configured to mimic a legitimate network. The attacker creates an AP with the same SSID as the target and, ideally, a stronger signal. Clients that auto-connect to known SSIDs may connect to the evil twin instead of the legitimate AP.

This is particularly effective against:

- Open networks (coffee shops, hotels, corporate guest Wi-Fi)
- Networks where clients auto-connect by SSID without verifying BSSID

[SLIDE: Evil Twin with Hostapd and DHCP]

Setting up an evil twin in an authorized lab requires several components:

First, hostapd to create the access point. Second, a DHCP server (dnsmasq) to assign addresses. Third, optionally, a captive portal to harvest credentials.

A basic hostapd configuration:

```
interface=wlan0
driver=nl80211
ssid=TargetNetworkName
channel=6
hw_mode=g
```

[SLIDE: Captive Portal Credential Harvesting]

Many corporate environments use captive portals for guest access. An evil twin can present a cloned portal page. When users enter credentials, those credentials are captured by the attacker's server before being passed along (or not) to the real network.

In authorized testing, this technique validates whether employees can distinguish legitimate from malicious captive portals and whether they would enter corporate credentials into an unknown portal.

[SLIDE: Enterprise Evil Twin — EAP Downgrade]

Against WPA2-Enterprise networks, the evil twin attack extends further. Tools like hostapd-wpe (Wireless Pwnage Edition) configure a rogue enterprise AP that accepts EAP authentication attempts and captures the challenge-response exchange.

The captured NETNTLM hash can then be cracked offline or used in relay attacks.

This demonstrates why WPA2-Enterprise alone is insufficient — certificate validation must be enforced on the client side.

[PAUSE for transition]

---

## Segment 5: Network Pivoting and Firewall/IDS Evasion (Lines 146–195)

[SLIDE: Network Pivoting Concepts]

Once you have established a foothold on an internal network — whether through wireless compromise, phishing, or exploitation — pivoting allows you to reach systems that are not directly accessible from your initial position.

The core concept: your compromised machine becomes a proxy or tunnel endpoint into segments you could not otherwise reach.

[SLIDE: SSH Dynamic Port Forwarding]

SSH provides built-in tunneling capability. If you have SSH access to a compromised internal host, dynamic port forwarding creates a SOCKS proxy:

```
ssh -D 1080 -N user@compromised-host
```

You can then configure tools to route through this SOCKS proxy using proxychains:

```
proxychains nmap -sT -p 80,443,8080 10.10.20.0/24
```

[SLIDE: Metasploit Route and Socks Proxy]

Within Metasploit, the route command adds network routes through a Meterpreter session:

```
route add 10.10.20.0/24 [session_id]
use auxiliary/server/socks_proxy
set SRVPORT 1080
run
```

This enables the entire Metasploit framework and external tools via proxychains to reach the internal subnet.

[SLIDE: Firewall Evasion Techniques]

Firewalls filter traffic based on ports, protocols, and IP addresses. Common evasion strategies include:

Port redirection: Running services on unusual ports. Web shells on port 443 blend into HTTPS traffic. Command and control on port 53 exploits DNS.

Protocol tunneling: Encapsulating traffic within allowed protocols. DNS tunneling uses DNS queries to exfiltrate data and receive commands. ICMP tunneling hides data in ping packets.

Fragmentation: Splitting packets into small fragments that bypass stateless filter rules. Tools like fragroute automate this.

Source address spoofing: Decoy scanning in Nmap (`-D RND:10`) generates traffic from randomized source addresses alongside real probes, making the true scanner harder to identify.

[SLIDE: IDS Evasion Techniques]

Intrusion detection systems analyze traffic patterns and signatures. Evasion techniques exploit weaknesses in how IDS systems reassemble and interpret traffic.

Insertion attacks: Sending packets with TTL values too low to reach the target but high enough to be seen by the IDS. The IDS includes these packets in its reassembly while the target ignores them.

Evasion attacks: Sending packets that the target accepts but the IDS rejects, causing the IDS stream to desynchronize.

Timing attacks: Spreading reconnaissance over long periods to avoid rate-based detection thresholds.

Protocol violations: Using malformed packets that target systems handle but IDS signatures do not expect.

[SLIDE: Nmap Evasion Options]

Nmap provides built-in evasion capabilities for authorized testing:

```
nmap -f                   # Fragment packets
nmap --mtu 16             # Custom MTU fragmentation
nmap -D RND:10            # Decoy sources
nmap --source-port 53     # Spoof source port
nmap -T0                  # Slowest timing (paranoid)
nmap --data-length 25     # Append random data
```

These options are used in authorized assessments to test whether the target's IDS/IPS can detect scanning under realistic adversarial conditions.

[SLIDE: Pivot Diagrams]

[VISUAL: Network diagram showing attacker → DMZ host (compromised) → internal subnet → database segment]

This architecture is common. The penetration tester compromises a DMZ web server, pivots through it to reach the internal application server, then pivots again to the database segment. Each hop requires establishing a channel and routing traffic through the previous hop.

[PAUSE for transition]

---

## Segment 6: Assessment Methodology and Reporting (Lines 196–240)

[SLIDE: Wireless Assessment Workflow]

A structured wireless penetration test follows defined phases aligned with the PenTest+ framework.

Phase 1 — Planning: Confirm scope includes wireless. Identify target SSIDs, geographic boundaries, and authorized client MAC addresses. Obtain specific authorization for any deauthentication testing.

Phase 2 — Reconnaissance: Passive survey using airodump-ng. Document all SSIDs, BSSIDs, channels, encryption types, and client associations. Note rogue or unexpected access points.

Phase 3 — Exploitation: Attempt handshake capture (with authorization for deauth if needed). Attempt WPA2 cracking against authorized networks. Test for evil twin susceptibility.

Phase 4 — Post-Exploitation: If wireless access is obtained, enumerate the network segment. Identify pivot opportunities. Test network segmentation.

Phase 5 — Reporting: Document all findings with evidence. Note unencrypted networks, weak passphrases, lack of 802.1X, rogue APs, and missing wireless IDS.

[SLIDE: Common Wireless Findings]

In production wireless assessments, the most frequently documented findings include:

WPA2-Personal with weak passphrase — Critical. Offline dictionary attack succeeds. Remediation: Implement WPA2/WPA3-Enterprise with 802.1X.

Rogue access point — High. Unauthorized AP broadcasting inside the network perimeter. Remediation: Deploy wireless intrusion prevention system.

Missing management frame protection — Medium. 802.11w not enabled, allowing forged deauthentication. Remediation: Enable Management Frame Protection.

Open guest network without client isolation — Medium. Guest clients can reach each other. Remediation: Enable AP client isolation.

Misconfigured EAP — High. Server certificate not validated by client. Remediation: Enforce certificate validation in supplicant profiles.

[SLIDE: Exam Domain Alignment]

For the PT0-002 exam, wireless topics appear primarily in:

Domain 3.3 — Perform network attacks. Specifically wireless attacks including de-authentication, evil twin, and WPS attacks.

Domain 4.2 — Analyze and report findings. Wireless findings require CVSS scoring and specific remediation guidance.

Know the following tools for the exam: Aircrack-ng, Airodump-ng, Aireplay-ng, Kismet, Wireshark for wireless, Hashcat for WPA cracking.

[SLIDE: Module Summary]

This module covered the complete wireless pen testing workflow: 802.11 protocol mechanics, the Aircrack-ng tool suite, WPA2 handshake capture and cracking, evil twin attacks, network pivoting through compromised wireless access, and firewall and IDS evasion.

Every technique requires explicit written authorization. Wireless testing without authorization is a federal crime.

Your lab for this module will walk through each of these techniques in an isolated environment using a dedicated authorized access point.

See you in the lab.

[END RECORDING]
