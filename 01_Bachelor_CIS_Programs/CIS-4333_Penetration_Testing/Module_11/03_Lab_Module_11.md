# Lab Activity: Module 11 — Wireless Network Assessment

## Course: CIS-4333 Penetration Testing

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Lab Overview

In this lab you will work through a wireless penetration testing workflow using simulated environments. Because most students do not have dedicated wireless penetration testing hardware (external USB adapters capable of monitor mode and packet injection), this lab uses two parallel tracks:

- **Track A (Hardware available):** Students with a compatible USB wireless adapter (Alfa AWUS036ACH or similar) perform live exercises against a personal lab access point they own and control.
- **Track B (No hardware):** Students complete the TryHackMe "Wifi Hacking 101" room, which provides a browser-based environment with pre-captured handshake files and a guided aircrack-ng workflow.

Both tracks complete the same conceptual tasks and submit the same deliverable types. Read your chosen track's instructions carefully.

Estimated time: 90–120 minutes.

---

## Learning Objectives

By the end of this lab, you will be able to:

- Place a wireless adapter into monitor mode and verify the interface is active
- Use airodump-ng to enumerate nearby wireless networks and identify key parameters
- Capture or obtain a WPA2 four-way handshake
- Perform an offline dictionary attack against the captured handshake
- Document a wireless security finding with severity, impact, and remediation

---

## Legal and Safety Notice

All wireless activities in this lab must be performed only against networks and access points you own or have explicit written permission to test. Testing any wireless network without authorization violates the Computer Fraud and Abuse Act and Texas Penal Code. If using Track A, test only against your personal router with a dedicated test SSID. Never direct attacks at your neighbors, your apartment complex Wi-Fi, your university network, or any other network you do not personally own.

---

## Track A — Live Wireless Hardware (Steps A1–A5)

### Step A1 — Enable Monitor Mode

1. Connect your compatible USB wireless adapter to your Kali Linux VM (ensure it is passed through to the VM, not the host).
2. Verify the adapter is recognized:

```bash
iwconfig
```

3. Kill processes that may interfere with monitor mode:

```bash
airmon-ng check kill
```

4. Enable monitor mode:

```bash
airmon-ng start wlan1
```

(Use the correct interface name shown by `iwconfig`. Your monitor mode interface will typically be named `wlan1mon`.)

5. Verify monitor mode is active:

```bash
iwconfig wlan1mon
```

Confirm the Mode field shows "Monitor."

**Deliverable A1:** Screenshot showing `iwconfig wlan1mon` output with Mode: Monitor confirmed.

### Step A2 — Enumerate Wireless Networks

1. Start airodump-ng on the monitor interface:

```bash
airodump-ng wlan1mon
```

2. Allow it to run for 30–60 seconds to populate nearby networks.
3. Record the following for your personal test AP: BSSID, SSID, Channel, Encryption type, Power level.
4. Note any clients associated with your test AP (shown in the lower section of the output).

**Deliverable A2:** Screenshot of airodump-ng output showing your test AP with BSSID, SSID, Channel, and at least one associated client (use a smartphone or second device connected to your test AP).

### Step A3 — Capture a WPA2 Handshake

1. Open a second terminal. Start a focused capture on your test AP:

```bash
airodump-ng --bssid <YOUR_AP_BSSID> -c <CHANNEL> -w lab11_capture wlan1mon
```

2. In the first terminal, send deauthentication frames to force a client reconnection:

```bash
aireplay-ng --deauth 5 -a <YOUR_AP_BSSID> -c <CLIENT_MAC> wlan1mon
```

3. Watch the airodump-ng window for the "WPA handshake: <BSSID>" message in the top right corner.
4. Once captured, stop airodump-ng with Ctrl+C.

**Deliverable A3:** Screenshot of airodump-ng output showing the "WPA handshake: <BSSID>" confirmation message.

### Step A4 — Perform Offline Dictionary Attack

1. Ensure your test AP's PSK is included in a custom wordlist for this exercise. Create a short wordlist file that includes the PSK:

```bash
echo -e "wrongpassword1\nwrongpassword2\nYOUR_TEST_PSK\nwrongpassword3" > test_wordlist.txt
```

2. Run aircrack-ng against the captured handshake:

```bash
aircrack-ng -w test_wordlist.txt lab11_capture-01.cap
```

3. Confirm the PSK is recovered in the output.

**Deliverable A4:** Screenshot of aircrack-ng output showing "KEY FOUND! [ YOUR_PSK ]."

### Step A5 — WPS Assessment

1. Check whether WPS is enabled on your test AP using `wash`:

```bash
wash -i wlan1mon
```

2. Record whether WPS is Locked or Unlocked for your AP.
3. Document: If WPS is enabled and unlocked, what tool and command would you use to attempt a PIN attack? (You do not need to run a live Reaver attack — documenting the command and the vulnerability is sufficient for this step.)

**Deliverable A5:** Screenshot of `wash` output and a written explanation of the WPS vulnerability and the Reaver command syntax you would use.

---

## Track B — TryHackMe Browser Lab (Steps B1–B5)

### Step B1 — Access the Lab Environment

1. Navigate to tryhackme.com and log in (free account required).
2. Search for "Wifi Hacking 101" room or navigate to the Pentesting learning path and locate the wireless module.
3. Start the room and deploy the machine.

**Deliverable B1:** Screenshot of the TryHackMe room interface showing the machine is deployed and connected.

### Step B2 — Review the Aircrack-ng Suite

1. In the TryHackMe terminal, run:

```bash
airmon-ng
```

2. Review the help output for `airodump-ng` and `aireplay-ng`.
3. Answer the following questions in your own words (to be included in your lab report):
   - What is the purpose of `airmon-ng check kill` before enabling monitor mode?
   - What is the difference between the BSSID column and the STATION column in airodump-ng output?

**Deliverable B2:** Written answers to the two questions above.

### Step B3 — Analyze a Pre-Captured Handshake

1. In the TryHackMe room, a pre-captured `.cap` file containing a WPA2 handshake is provided. Locate it in the task instructions.
2. Verify the handshake is present in the file:

```bash
aircrack-ng <capture_file.cap>
```

3. Note the SSID and BSSID shown in the output.

**Deliverable B3:** Screenshot of aircrack-ng output showing the SSID, BSSID, and number of handshakes detected in the capture file.

### Step B4 — Perform Dictionary Attack

1. Using the wordlist provided by the TryHackMe room (typically `rockyou.txt` or a smaller subset):

```bash
aircrack-ng -w /path/to/wordlist <capture_file.cap>
```

2. Wait for the attack to complete and the key to be found.

**Deliverable B4:** Screenshot of aircrack-ng output showing "KEY FOUND! [ password ]."

### Step B5 — Answer the Room Questions

1. Complete all questions in the TryHackMe room tasks. These typically include the BSSID of the target AP, the SSID, the recovered password, and conceptual questions about the attack.

**Deliverable B5:** Screenshot of the TryHackMe room showing completed tasks with checkmarks.

---

## Part 3 — Wireless Security Finding Report (All Students)

Regardless of which track you completed, write a wireless security finding report entry using the following template:

### Finding: WPA2-Personal Weak Passphrase (or WPS Enabled if applicable)

- **Severity:** High
- **Affected Asset:** (SSID and BSSID of the tested access point)
- **Description:** Provide a two- to three-sentence description of the vulnerability. Explain that WPA2-Personal PSKs are recoverable offline once the four-way handshake is captured.
- **Proof of Concept:** Document the exact commands used to capture the handshake and crack the PSK. Include the recovered passphrase.
- **Business Impact:** Explain what an attacker with the recovered PSK can do: connect to the network, intercept traffic, pivot to internal resources.
- **Remediation Recommendations:** Provide at least two recommendations. Consider: migrate to WPA3, implement WPA2-Enterprise with 802.1X, enforce a minimum 20-character passphrase, disable WPS on all access points.

---

## Submission Checklist

Before submitting, confirm you have included:

- [ ] Track A: Deliverables A1 through A5 (or Track B: Deliverables B1 through B5)
- [ ] Wireless security finding report with all required fields
- [ ] Written answers to the two conceptual questions (all students)

Submit all screenshots and the finding report as a single PDF or ZIP file to the Canvas assignment portal.

---

---

## Part 9 — Challenge Exercise

### Challenge 1: Wireless Assessment Documentation Report

Using findings from your Module 11 lab activity (either Track A or Track B), produce a complete wireless security assessment report section as it would appear in a professional penetration test deliverable. Your report section must include: an executive summary paragraph (3–4 sentences) describing the overall wireless security posture without technical jargon, a findings table listing each identified issue with severity rating and OWASP/CVSS classification, a detailed finding entry for the WPA2 handshake/PSK recovery finding including proof of concept commands, recovered passphrase, evidence screenshot, business impact, and specific remediation steps, and a findings entry for any secondary wireless issue identified (WPS status, open network presence, rogue AP indicators, or encryption downgrade risk). Format the report section to be understandable to a CTO who has no wireless security background.

### Challenge 2: Attack Surface Comparison — WPA2-Personal vs WPA2-Enterprise

Research the technical differences between WPA2-Personal and WPA2-Enterprise authentication and write a structured comparison analysis covering: the authentication mechanism used by each (PSK vs. 802.1X/EAP), what data is capturable from the air for each type, whether offline cracking is possible for each and why, the infrastructure cost difference between the two, and what attack techniques remain viable against WPA2-Enterprise (evil twin, credential phishing via RADIUS impersonation, client certificate attacks). Conclude with a specific recommendation for which standard an organization with 200 employees and sensitive internal network access should implement, with justification based on the attack surface comparison.

### Reflection Questions

1. You capture a WPA2-Personal handshake during a wireless engagement. You run hashcat overnight and crack the PSK. However, you notice the passphrase is the company's name followed by the founding year: `AcmeCorp2008`. Write the "Finding" section of your penetration test report for this vulnerability — include severity rating, description, evidence, business impact, and remediation — and explain why this passphrase pattern is common in organizations and what specific remediation addresses both the technical weakness and the organizational behavior that created it.

2. During a wireless reconnaissance sweep, your airodump-ng output shows an access point with the same SSID as the client's corporate network but a different BSSID and signal that is stronger near the parking lot. You did not deploy this AP. What does this indicate, what is the immediate action you should take per professional engagement protocol, and what documentation must you create? How does this finding change the scope and urgency of the current engagement?

*End of Module 11 Lab Activity*
