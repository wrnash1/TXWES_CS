# Lab Activity: Module 04 – IPv6 Addressing and Transition Technologies
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

### Lab Overview

**Lab Title:** IPv6 Address Observation, Abbreviation Practice, and EUI-64 Verification

**Format:** Part 1 — Command-Line IPv6 Observation on Local Machine; Part 2 — IPv6 Worksheet

**Estimated Time:** 60–75 minutes

**Points:** 100 points total

**Prerequisites:**

- Module 04 video lectures watched (both Part 1 and Part 2)
- Module 04 Reading Guide reviewed, especially the address type table and EUI-64 process
- A Windows, Linux, or macOS computer (no additional software required)
- Pencil and paper for Part 2 calculations

**Learning Objectives:**

By completing this lab, you will be able to:

- Identify automatically generated IPv6 link-local addresses on a local machine
- Verify the loopback address ::1 using ping
- Determine the IPv6 address type from its prefix
- Apply both IPv6 abbreviation rules to shorten and expand addresses
- Perform the EUI-64 calculation to derive an interface identifier from a MAC address
- Compare IPv6 address configuration between SLAAC and DHCPv6

---

### Background

IPv6 is already active on your computer right now — most modern operating systems generate link-local addresses on every network interface automatically, even without an IPv6 router on the network. This lab uses that existing behavior to observe IPv6 in action without requiring any additional configuration.

---

### Part 1: Observing IPv6 on Your Local Machine

**Objective:** Use command-line tools to find and analyze the IPv6 addresses already configured on your system.

#### Step 1: View All Network Interface Configuration

Open a command prompt or terminal.

Windows:

`ipconfig /all`

Linux/Mac:

`ip addr`

or (older systems):

`ifconfig -a`

Record your observations:

**For each active network interface, find and record:**

- Interface name: ____________________
- IPv4 address: ____________________
- IPv6 link-local address (starts with fe80::): ____________________
- Any global unicast IPv6 address (starts with 2 or 3): ____________________
- MAC address (Physical Address): ____________________

**Question 1:** What is the prefix of your link-local IPv6 address? Which address type does this prefix identify, and is this address routed on the internet?

**Question 2:** Compare your link-local IPv6 address with your MAC address. Can you see the connection? The interface identifier portion of the link-local address (after the fe80:: prefix) may be derived from your MAC address using EUI-64 (or may be a random value on newer systems that use privacy extensions). Describe any relationship you observe.

#### Step 2: Test the IPv6 Loopback Address

Windows:

`ping ::1`

Linux/Mac:

`ping6 ::1`

or:

`ping -6 ::1`

Record your results:

- Packets sent: ____________________
- Packets received: ____________________
- RTT (round trip time): ____________________

**Question 3:** What does successfully pinging ::1 confirm about your system's IPv6 stack? Which address type is ::1, and what is its IPv4 equivalent?

#### Step 3: Identify All IPv6 Addresses Present

Review all IPv6 addresses shown in Step 1.

**Question 4:** For each IPv6 address you found, identify its type (link-local, loopback, global unicast, unique local, or multicast) based on its prefix. Use the address type table from the reading guide.

#### Step 4: Check for IPv6 Multicast Memberships (Optional)

Windows:

`netsh interface ipv6 show joins`

Linux:

`ip maddr show`

**Question 5:** List two multicast group addresses you observe. What prefix do they use? What do they represent? (Hint: ff02::1 = all-nodes, ff02::1:ffxx:xxxx = solicited-node multicast)

---

### Part 2: IPv6 Abbreviation and EUI-64 Worksheet

**Instructions:** Complete all calculations by hand. Show your work for full credit.

#### Exercise 1: Full Address to Abbreviated Form

Apply both IPv6 abbreviation rules to shorten each address.

A. 2001:0db8:0000:0000:0000:0000:0000:0001

Abbreviated: ____________________

B. fe80:0000:0000:0000:021a:2bff:fe3c:4d5e

Abbreviated: ____________________

C. 2001:0db8:85a3:0000:0000:8a2e:0370:7334

Abbreviated: ____________________

D. ff02:0000:0000:0000:0000:0000:0000:0001

Abbreviated: ____________________

#### Exercise 2: Abbreviated Address to Full Form

Expand each abbreviated address to its full 128-bit form.

A. 2001:db8::1

Full form: ____________________

B. fe80::1

Full form: ____________________

C. ::1

Full form: ____________________

D. 2001:db8:0:1::5

Full form: ____________________

#### Exercise 3: Address Type Identification

For each IPv6 address below, identify the address type using the prefix.

| Address                        | Address Type                      |
|--------------------------------|-----------------------------------|
| fe80::1a2b:3c4d:5e6f           |                                   |
| 2001:db8:abc::1                |                                   |
| ::1                            |                                   |
| fd12:3456:789a::10             |                                   |
| ff02::1                        |                                   |
| 2601:600:8200:1234::50         |                                   |

#### Exercise 4: EUI-64 Calculation

Given the following MAC addresses, calculate the EUI-64 interface identifier.

**MAC Address A:** 00:50:56:AB:CD:EF

Step 1 — Split into halves: ____________________

Step 2 — Insert FF:FE: ____________________

Step 3 — Flip the seventh bit (convert first byte): ____________________

EUI-64 Interface ID (in IPv6 group format): ____________________

**Assembled global unicast address** using prefix 2001:db8:1::/64:

Full address: ____________________

Abbreviated address: ____________________

**MAC Address B:** AA:BB:CC:00:11:22

EUI-64 Interface ID: ____________________

Note on the seventh bit for AA: AA hex = 10101010 binary. The seventh bit (bit 1, index 1 from left) is 1. Flip to 0: 10101000 = A8. So AA becomes A8 in the first byte.

---

### Deliverables

Submit the following to the Canvas assignment dropbox:

**Deliverable 1 (25 points):** Screenshots of your ipconfig /all (or ip addr) output and ping ::1 output from Part 1, Steps 1 and 2. Include your typed answers to Questions 1 through 5.

**Deliverable 2 (50 points):** Completed Part 2 worksheet with all exercises filled in. Show your work for EUI-64 calculations. Submit as typed answers or a scanned/photographed handwritten worksheet.

**Deliverable 3 (25 points):** A typed comparison (100–150 words) explaining the difference between SLAAC and stateful DHCPv6, including when each would be the preferred choice in an enterprise network. Reference your observation of the link-local address from Part 1 as an example of automatic IPv6 configuration.

---

### Grading Rubric

| Deliverable | Points | Full Credit Criteria |
|-------------|--------|----------------------|
| Screenshots and questions answered | 25 | Both screenshots captured; Questions 1–5 answered with correct address type identification |
| Worksheet exercises | 50 | All abbreviation exercises correct; address types correctly identified; EUI-64 calculation steps shown and correct |
| Written comparison | 25 | 100–150 words; SLAAC vs. DHCPv6 accurately contrasted; link-local observation correctly referenced |
| **Total** | **100** | |

---

### Common Issues and Fixes

**Issue:** No IPv6 global unicast address visible.

**Fix:** This is normal. A global unicast address requires an IPv6-capable router on your network. Most home and campus networks use IPv4 with NAT. Link-local addresses are always present and sufficient for this lab.

**Issue:** ping ::1 fails on Linux.

**Fix:** Try ping6 ::1 or ping -6 ::1. Some distributions require the explicit ping6 command or -6 flag for IPv6.

**Issue:** Link-local address does not appear to relate to MAC address.

**Fix:** Modern operating systems use privacy extensions (RFC 4941) that generate random interface IDs instead of EUI-64 to protect privacy. Your system may be using a random ID. This is expected behavior — document it and use the EUI-64 worksheet exercises to practice the calculation regardless.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
