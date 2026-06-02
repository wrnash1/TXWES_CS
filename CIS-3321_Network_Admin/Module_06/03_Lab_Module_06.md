# Lab Activity: Module 06 – Wireless Networking: 802.11 Standards and Security

## CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Texas Wesleyan University | Professor Nash

---

### Overview

This lab has two parts. Part 1 uses built-in command-line tools to scan and analyze nearby Wi-Fi networks on your physical machine. Part 2 uses Cisco Packet Tracer to configure a wireless access point with WPA2-AES and connect a wireless client. Together, the two parts connect the lecture content on 802.11 standards, frequency bands, channels, and security protocols to observable real-world behavior.

Estimated Time: 60–75 minutes

Required Tools:

- Windows 10 or 11 (for Part 1 Windows commands), OR a Linux system with `iw` or `nmcli` installed
- Cisco Packet Tracer 8.x (free download at netacad.com with a free account)

---

### Learning Objectives

By the end of this lab, you will be able to:

1. Use command-line tools to scan nearby wireless networks and extract 802.11 standard, frequency band, channel, and security information.
2. Identify which 802.11 standard and security protocol a network is using based on command output.
3. Configure a wireless access point in Packet Tracer with WPA2-Personal using AES encryption.
4. Connect a wireless client to a secured SSID and verify connectivity.
5. Explain the channel assignments observed in your environment using the non-overlapping channel rule.

---

### Part 1: Wireless Network Scanning with Command-Line Tools

#### Part 1A: Windows — netsh wlan show networks

On Windows, the `netsh wlan` command can display all Wi-Fi networks visible to your wireless adapter, including SSID, authentication type, encryption, and signal strength.

Step 1: Open a Command Prompt (not necessarily elevated).

Step 2: Run the basic scan command:

```bat
netsh wlan show networks
```

This displays a condensed list. Each network shows the SSID, network type (Infrastructure or Ad Hoc), authentication method, and encryption type.

Step 3: Run the detailed mode command:

```bat
netsh wlan show networks mode=bssid
```

This expands each entry to include the BSSID (AP MAC address), signal strength, radio type, channel, and basic rates.

Step 4: Record your results in the table below. You must capture at least five distinct networks (or as many as are visible in your location). If fewer than five are visible, record all visible networks and note the total count.

Observation Table — Part 1A:

| # | SSID | Authentication | Encryption | Radio Type | Channel | Signal |
|---|------|---------------|------------|------------|---------|--------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

Analysis Questions — Part 1A:

Question 1: Look at the "Radio Type" column in your output. What 802.11 standard designations appear (for example, 802.11n, 802.11ac, 802.11ax)? For each standard you observe, identify the frequency band it should be operating in based on what you learned in the lecture.

Question 2: How many of the networks you observed are using WPA2-Personal (PSK) vs. WPA3? How many (if any) are using WEP or open (no encryption)? If you found any open networks or WEP networks, explain why this is a security concern.

Question 3: Look at the channel numbers listed for the networks operating on 2.4 GHz. Are any neighboring APs on adjacent channels (for example, channels 2 through 5, or 7 through 10)? If so, explain what problem this creates and what channels should have been used instead.

---

#### Part 1B: Linux — iw and nmcli (Alternative if Windows is unavailable)

If you are using Linux (or a VM with a wireless adapter passed through), use the following commands.

Step 1: List available wireless interfaces:

```bash
iw dev
```

Note the interface name (commonly `wlan0` or `wlp2s0`).

Step 2: Scan for nearby networks. Replace `wlan0` with your interface name:

```bash
sudo iw dev wlan0 scan | grep -E "SSID:|freq:|signal:|capability:|RSN:|WPA:"
```

Step 3: Alternatively, use NetworkManager's `nmcli`:

```bash
nmcli dev wifi list
```

This displays SSID, BSSID, mode, channel, rate, signal, bars, and security type in a single readable table.

Step 4: Record the output in the same observation table format used in Part 1A above. If both Windows and Linux are available, compare the results for the same physical location.

Question 4: Compare the `nmcli` output format to the `netsh wlan show networks mode=bssid` output. Which provides more immediately readable information? Which requires post-processing to interpret? Explain.

---

#### Part 1C: Frequency Band and Security Analysis

Use your collected data to answer the following questions.

Question 5: Identify one network from your scan that is using 5 GHz. What 802.11 standard is it using? What are the advantages of 5 GHz over 2.4 GHz in a high-density environment like a classroom or office building?

Question 6: If you observed any network using WPA2-CCMP (AES), explain why AES-CCMP is considered secure while WEP (RC4 with a static key) is not. Reference the specific vulnerability that makes WEP crackable.

---

### Part 2: Wireless AP Configuration in Cisco Packet Tracer

In Part 2, you will build a small wireless network topology in Packet Tracer, configure an access point with WPA2-Personal using AES encryption, and verify that a wireless client can connect and communicate.

#### Step 1: Build the Topology

Open Packet Tracer and create the following topology:

- 1 Wireless Router (use the WRT300N or Linksys WRT300N from the Network Devices > Wireless Devices section)
- 2 Laptop PCs (from End Devices — use the Laptop device, which has a wireless NIC)
- 1 PC (wired, connected to the wireless router's LAN port via straight-through Cat5e cable)

Connect the wired PC to LAN port 1 on the wireless router using a copper straight-through cable.

The two laptops will connect wirelessly — no physical cable needed.

#### Step 2: Configure the Wireless Router

Click on the wireless router. Go to the GUI tab.

Under the Wireless section, configure:

- SSID: CIS3321-Lab06
- Network Mode: Mixed (to support multiple standards)
- Radio Band: 2.4 GHz
- Channel: 6

Under the Wireless Security section, configure:

- Security Mode: WPA2 Personal
- Encryption: AES
- Passphrase: NetPlus2024!

Save the configuration.

#### Step 3: Configure DHCP on the Wireless Router

On the same router GUI, go to the Setup tab. Under the Network Setup section:

- Set the router IP to 192.168.6.1 with subnet mask 255.255.255.0
- Enable the DHCP server
- Set the DHCP range to start at 192.168.6.100 and end at 192.168.6.150

Save the configuration.

#### Step 4: Connect the Laptops Wirelessly

Click on Laptop 1. Go to the Config tab, then select the Wireless0 interface. Enter:

- SSID: CIS3321-Lab06
- Authentication: WPA2-PSK
- PSK Pass Phrase: NetPlus2024!
- Encryption Type: AES

Set the IP configuration to DHCP.

Repeat for Laptop 2.

#### Step 5: Verify Connectivity

On Laptop 1, open the Desktop tab and launch the Command Prompt. Run:

```bat
ipconfig
```

Confirm that Laptop 1 received a DHCP address in the 192.168.6.100–150 range.

Then ping the wireless router:

```bat
ping 192.168.6.1
```

Then ping Laptop 2 using its assigned DHCP address:

```bat
ping 192.168.6.10x
```

Replace 10x with the actual address from Laptop 2's ipconfig output.

Then ping the wired PC, which should also have a DHCP address in the same range.

#### Step 6: Security Verification

On the wireless router GUI, change the Security Mode temporarily to WEP and set a 10-character hex key. Save.

Observe what happens to the laptop connections — they should disconnect because the client is still configured for WPA2-PSK.

Restore the configuration to WPA2-Personal/AES with passphrase NetPlus2024!. Save. Confirm the laptops reconnect.

Lab Questions — Part 2:

Question 7: After completing Step 5, record the DHCP-assigned IP addresses for both laptops and the wired PC. Are all three in the same subnet? What is the network address and broadcast address for the 192.168.6.0/24 network?

Question 8: In Step 6, why did the laptops disconnect when you changed the router to WEP? What would a real-world attacker need to do to capture and crack the WEP key? Name the specific WEP vulnerability that makes this possible.

Question 9: You configured the wireless router to use channel 6. If a neighboring business's AP is visible on your scan and it is using channel 6, what problem exists and what channels would you reassign to avoid it? What is the term for the interference that results from APs on the same or overlapping channels?

Question 10: Your wireless router is set to Mixed mode (supporting 802.11b/g/n). If you were to upgrade the router to 802.11ac only, what change to the radio band configuration would be required? Why can't 802.11ac operate on 2.4 GHz?

---

### Deliverables

Submit the following in a single PDF or Word document:

1. Part 1 Observation Table — Completed with at least five networks (or all visible networks if fewer than five are in range). Include the full `netsh wlan show networks mode=bssid` output or `nmcli dev wifi list` output as a screenshot or copy-pasted text block.

2. Part 1 Written Responses — Answers to Questions 1 through 6 in complete sentences.

3. Part 2 Topology Screenshot — A screenshot of your completed Packet Tracer topology showing the wireless router, two laptops, and one wired PC with all green link indicators visible.

4. Part 2 Connectivity Screenshot — A screenshot showing a successful ping from Laptop 1 to Laptop 2 and to the wireless router (192.168.6.1).

5. Part 2 Written Responses — Answers to Questions 7 through 10 in complete sentences.

---

### Grading Rubric (100 Points Total)

| Item | Points |
|------|--------|
| Part 1 Observation Table — at least 5 networks recorded with all columns filled | 15 |
| Part 1A/1B — Full command output included (screenshot or copy-paste) | 10 |
| Question 1 — 802.11 standard identified with correct frequency band mapping | 8 |
| Question 2 — Security type analysis with correct identification of WPA2 vs open/WEP risk | 8 |
| Question 3 — Channel overlap analysis with correct identification of 1/6/11 rule | 8 |
| Question 4 — Linux/Windows tool comparison | 6 |
| Question 5 — 5 GHz network identified with correct standard and band advantages | 7 |
| Question 6 — WEP vulnerability explained (IV reuse, RC4 static key) | 7 |
| Part 2 Topology Screenshot — correct devices and connections | 5 |
| Part 2 Connectivity Screenshot — successful ping output visible | 5 |
| Question 7 — DHCP addresses recorded, network/broadcast correct | 7 |
| Question 8 — WEP disconnection explained, IV reuse vulnerability named | 7 |
| Question 9 — Co-channel interference explained, 1/6/11 reassignment stated | 7 |
| Question 10 — 802.11ac 5 GHz requirement explained correctly | 4 |
| Total | 100 |

---

### Submission Instructions

Save your document as: Lab06_Firstname_Lastname.pdf

Submit to the Module 06 Lab assignment in the course LMS before the posted deadline. Late submissions are subject to the course late policy.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
