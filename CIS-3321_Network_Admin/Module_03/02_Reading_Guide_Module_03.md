# Reading Guide: Module 03 – IP Addressing: IPv4, Subnetting, CIDR
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

### Introduction

Module 03 covers the most calculation-intensive topic on the CompTIA Network+ exam: IPv4 addressing and subnetting. You must be able to determine the network address, broadcast address, valid host range, and number of usable hosts for any given IP address and subnet mask — and do it reliably under exam time pressure. This guide provides reference tables, the four-step calculation process, practice problems, and the exam tips you need to succeed.

---

### 1. Core Vocabulary

**IPv4 Address** — A 32-bit logical address written in dotted-decimal notation (e.g., 192.168.1.10). Divided into a network portion and a host portion by the subnet mask.

**Subnet Mask** — A 32-bit value that identifies which bits belong to the network and which belong to the host. Bits set to 1 indicate network bits; bits set to 0 indicate host bits. Written in dotted-decimal or CIDR slash notation.

**CIDR (Classless Inter-Domain Routing)** — A method of expressing subnet masks as a prefix length (number of consecutive 1 bits) after a slash. Example: /24 means 24 network bits.

**Network Address** — The first address in a subnet (all host bits set to 0). Not assignable to a host. Identifies the subnet itself.

**Broadcast Address** — The last address in a subnet (all host bits set to 1). Not assignable to a host. Packets sent to the broadcast address reach all hosts on the subnet.

**Usable Host Range** — All addresses between the network address and the broadcast address. Formula: 2^(host bits) - 2.

**Block Size** — The total number of addresses in a subnet, calculated as 256 minus the interesting octet of the subnet mask. Equals 2^(host bits).

**Classful Addressing** — The original fixed-class IP address scheme. Class A (/8), Class B (/16), Class C (/24). Largely replaced by CIDR.

**RFC 1918** — The standard defining private IPv4 address ranges not routed on the public internet.

**APIPA (Automatic Private IP Addressing)** — The 169.254.0.0/16 range self-assigned by Windows hosts when DHCP fails.

**Loopback Address** — 127.0.0.1. Used to test the local TCP/IP stack. Pinging this address verifies the NIC driver and IP stack are functional.

**VLSM (Variable Length Subnet Masking)** — Using different prefix lengths on different subnets within the same major network to allocate addresses more efficiently.

**Default Gateway** — The IP address of the router interface on the local subnet. Hosts send all traffic destined for remote networks to the default gateway.

**NAT (Network Address Translation)** — Router function translating private internal IP addresses to public addresses for internet access.

**PAT (Port Address Translation)** — Also called NAT overload. Maps many private IPs to a single public IP using unique port numbers to track sessions.

---

### 2. IP Address Class Reference Table

| Class | First Octet Range | Default Mask | CIDR | Approx. Hosts/Network | Notes                          |
|-------|-------------------|--------------|------|-----------------------|--------------------------------|
| A     | 1 – 126           | 255.0.0.0    | /8   | ~16,777,214           | 127.x.x.x reserved (loopback) |
| B     | 128 – 191         | 255.255.0.0  | /16  | ~65,534               |                                |
| C     | 192 – 223         | 255.255.255.0| /24  | 254                   |                                |
| D     | 224 – 239         | N/A          | N/A  | N/A                   | Multicast                      |
| E     | 240 – 255         | N/A          | N/A  | N/A                   | Experimental/Reserved          |

---

### 3. RFC 1918 Private Address Ranges

Memorize these three ranges exactly, including the boundaries.

| Class | Network           | CIDR | Range Start  | Range End         |
|-------|-------------------|------|--------------|-------------------|
| A     | 10.0.0.0          | /8   | 10.0.0.0     | 10.255.255.255    |
| B     | 172.16.0.0        | /12  | 172.16.0.0   | 172.31.255.255    |
| C     | 192.168.0.0       | /16  | 192.168.0.0  | 192.168.255.255   |

**Special addresses to memorize:**

- 127.0.0.1 — Loopback (tests local TCP/IP stack)
- 169.254.0.0/16 — APIPA (DHCP failure self-assignment)
- 0.0.0.0 — Unspecified address (before DHCP assignment)
- 255.255.255.255 — Limited broadcast (all hosts on local segment)

---

### 4. Subnet Reference Table — /24 through /30

This is the most important table in this module. Memorize every row.

| CIDR | Subnet Mask       | Block Size | Total Addresses | Usable Hosts |
|------|-------------------|------------|-----------------|--------------|
| /24  | 255.255.255.0     | 256        | 256             | 254          |
| /25  | 255.255.255.128   | 128        | 128             | 126          |
| /26  | 255.255.255.192   | 64         | 64              | 62           |
| /27  | 255.255.255.224   | 32         | 32              | 30           |
| /28  | 255.255.255.240   | 16         | 16              | 14           |
| /29  | 255.255.255.248   | 8          | 8               | 6            |
| /30  | 255.255.255.252   | 4          | 4               | 2            |
| /32  | 255.255.255.255   | 1          | 1               | 0 (host route) |

Block size formula: 256 minus the interesting octet of the subnet mask.

Usable hosts formula: 2^(host bits) - 2, where host bits = 32 - prefix length.

---

### 5. Binary Conversion Reference Table

| Decimal | Binary    | Power | Value |
|---------|-----------|-------|-------|
| 128     | 10000000  | 2^7   | 128   |
| 192     | 11000000  | 2^7+2^6 | 128+64 |
| 224     | 11100000  | 2^7+2^6+2^5 | 128+64+32 |
| 240     | 11110000  | 2^7 through 2^4 | 128+64+32+16 |
| 248     | 11111000  | 2^7 through 2^3 | sum=248 |
| 252     | 11111100  | 2^7 through 2^2 | sum=252 |
| 255     | 11111111  | all 8 bits | sum=255 |

---

### 6. Four-Step Subnet Calculation Process

Use this process for every subnetting question on the exam.

**Step 1:** Identify the CIDR prefix and calculate the block size.

- Block size = 256 minus the interesting octet of the subnet mask.
- The "interesting octet" is the last non-255, non-0 octet.

**Step 2:** Find the network address.

- Look at the same octet in the IP address.
- Find the largest multiple of the block size that does not exceed that octet value.
- That multiple, with all lower octets set to 0, is the network address.

**Step 3:** Find the broadcast address.

- Broadcast = Network address in interesting octet + Block size - 1.
- All remaining octets become 255.

**Step 4:** Determine the usable host range.

- First usable host = Network address + 1.
- Last usable host = Broadcast address - 1.

---

### 7. Worked Practice Problems

**Problem 1:** Given 192.168.1.75 / 255.255.255.224 (/27)

- Block size: 256 - 224 = 32
- Interesting octet: 75
- Multiples of 32: 0, 32, 64, 96 — largest ≤ 75 is 64
- Network address: 192.168.1.64
- Broadcast: 64 + 32 - 1 = 95 → 192.168.1.95
- Usable range: 192.168.1.65 through 192.168.1.94
- Usable hosts: 30

**Problem 2:** Given 10.10.10.130 / 255.255.255.192 (/26)

- Block size: 256 - 192 = 64
- Interesting octet: 130
- Multiples of 64: 0, 64, 128 — largest ≤ 130 is 128
- Network address: 10.10.10.128
- Broadcast: 128 + 64 - 1 = 191 → 10.10.10.191
- Usable range: 10.10.10.129 through 10.10.10.190
- Usable hosts: 62

**Problem 3:** Point-to-point link needs exactly 2 usable hosts.

- Use /30: block size 4, 2 usable hosts
- Example: 172.16.0.0/30 → Network 172.16.0.0, Broadcast 172.16.0.3, hosts .1 and .2

**Problem 4:** How many subnets does 192.168.5.0/27 create from the original /24?

- Borrowed bits: 27 - 24 = 3 bits
- Number of subnets: 2^3 = 8 subnets
- Subnets start at: .0, .32, .64, .96, .128, .160, .192, .224

---

### 8. Subnetting from a /24 — Number of Subnets vs. Hosts

| Prefix | Borrowed Bits | Subnets | Hosts per Subnet |
|--------|---------------|---------|------------------|
| /24    | 0             | 1       | 254              |
| /25    | 1             | 2       | 126              |
| /26    | 2             | 4       | 62               |
| /27    | 3             | 8       | 30               |
| /28    | 4             | 16      | 14               |
| /29    | 5             | 32      | 6                |
| /30    | 6             | 64      | 2                |

---

### 9. Certification Exam Tips

**Tip 1:** Subnetting is tested in scenario form. You will be given an IP address and mask and asked to identify the network address, broadcast address, valid host range, or whether a specific host is in the correct subnet. Practice the four-step process until it is automatic.

**Tip 2:** The block size shortcut (256 minus the mask octet) is faster than binary conversion. Use it. Block size 64 → subnets at 0, 64, 128, 192.

**Tip 3:** The /30 subnet for point-to-point links is a guaranteed exam topic. It provides exactly 2 usable hosts with 4 total addresses. Know it cold.

**Tip 4:** RFC 1918 boundary trap: 172.32.x.x is NOT private (the private B range ends at 172.31.x.x). 192.169.x.x is NOT private (the private C range ends at 192.168.x.x). The exam deliberately tests these near-boundary addresses.

**Tip 5:** APIPA (169.254.x.x) is not RFC 1918. It is a separate self-assignment range. If a device has a 169.254.x.x address, DHCP failed.

**Tip 6:** When an exam question asks for the number of subnets created by borrowing bits, the formula is 2^(borrowed bits). When it asks for the number of usable hosts, the formula is 2^(host bits) - 2.

**Tip 7:** The loopback address is 127.0.0.1. The entire 127.x.x.x range is reserved for loopback. Pinging 127.0.0.1 tests the local IP stack and NIC driver, not the network.

**Tip 8:** VLSM allows different subnet sizes within the same major network. It requires classless routing protocols (OSPF, EIGRP, RIPv2) that carry the subnet mask with routing updates.

---

### 10. Required Reading and Viewing

**Required Reading:** Computer Networking: Principles, Protocols and Practice — read the sections on IPv4 addressing and subnetting. Work through every calculation example by hand.

**Required Viewing:** Professor Messer's Network+ N10-008 video series — watch the IPv4 addressing and subnetting segments. Available free at professormesser.com.

**Supplemental Reference:** CompTIA official N10-008 exam objectives at comptia.org — review Domain 1.0 Networking Concepts for the subnetting and addressing objectives.

---

### 11. Study Checklist

- [ ] Memorize all three RFC 1918 private address ranges, including exact boundaries
- [ ] Memorize the /24 through /30 subnet table (mask, block size, usable hosts)
- [ ] Practice the four-step subnet calculation process on at least 10 different addresses
- [ ] Memorize the binary conversion values for common subnet mask octets (128, 192, 224, 240, 248, 252, 255)
- [ ] Identify the APIPA range and explain what it indicates
- [ ] Explain the loopback address and what pinging it tests
- [ ] Calculate the number of subnets created when borrowing 1, 2, 3, and 4 bits from a /24
- [ ] Watch Professor Messer's subnetting videos at professormesser.com
- [ ] Read the IPv4 addressing chapter in the OER textbook
- [ ] Complete the Lab 03 subnet calculation and Packet Tracer activity
- [ ] Post your Module 03 Discussion initial response by Wednesday at 11:59 PM
- [ ] Complete the Module 03 Quiz

---

## 9. Supplemental Resources

The following free resources extend Module 03 content on IPv4 addressing, subnetting, and CIDR. No purchase is required.

**1. Professor Messer — IPv4 Addressing and Subnetting Free Videos**
URL: https://www.professormesser.com/network-plus/n10-008/n10-008-video/
Relevance: Professor Messer provides dedicated videos on IPv4 addressing, subnetting, and CIDR notation. His subnetting video walks through the block-size method step by step, which directly matches the four-step process in this reading guide.

**2. Subnet Practice Tool — SubnettingPractice.com**
URL: https://www.subnettingpractice.com/
Relevance: A free interactive subnetting drill tool that generates random subnetting problems and provides immediate feedback. Repetitive practice using this tool is the fastest way to master the speed subnetting required for the Network+ exam.

**3. RFC 1918 — Address Allocation for Private Internets**
URL: https://datatracker.ietf.org/doc/html/rfc1918
Relevance: The original IETF standard defining the three private IPv4 address ranges. Reading the actual RFC is brief (3 pages) and definitively clarifies the exact boundaries of 10.x.x.x, 172.16–31.x.x, and 192.168.x.x.

**4. Cisco — Understanding IP Addressing and Subnetting Basics**
URL: https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html
Relevance: Cisco's official free documentation on IPv4 addressing and subnetting principles. Covers binary-to-decimal conversion, subnet calculation, and CIDR with worked examples from an industry-authoritative source.

**5. IP Subnet Calculator — NetworkCalc.com**
URL: https://networkcalc.com/subnet-calculator
Relevance: A free online subnet calculator for verifying subnetting calculation results. Use it to check your work after completing manual calculations — not as a replacement for learning the manual method.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
