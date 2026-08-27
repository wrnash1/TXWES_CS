# Reading Guide: Module 02 - Subnetting and VLSM Configurations

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 1: Network Fundamentals - 20%)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

Subnetting is the single most heavily tested mathematical skill on the CCNA 200-301 exam. Variable Length Subnet Masking (VLSM) extends subnetting to real enterprise network design. This reading guide provides all reference tables, formulas, worked examples, and Cisco CLI commands you need to master both skills before the lab and quiz.

---

## 1. High-Yield Glossary

- **Subnet:** A logically subdivided segment of a larger IP network. Subnetting creates multiple smaller broadcast domains from a single network block.

- **Subnet mask:** A 32-bit value that identifies which portion of an IP address is the network portion and which is the host portion. Written in dotted-decimal (255.255.255.0) or prefix notation (/24).

- **CIDR (Classless Inter-Domain Routing):** An addressing and routing scheme that replaces the old Class A/B/C system. CIDR allows prefix lengths of any value from /1 to /32, enabling efficient address allocation.

- **Prefix length:** The number of consecutive 1-bits in a subnet mask, written with a forward slash before the number (e.g., /26). Equivalent to the count of network bits.

- **Host bits:** The bits in an IP address not covered by the subnet mask. These bits identify individual hosts within a subnet.

- **Block size:** The number of addresses in a subnet, calculated as 2 raised to the number of host bits. Also called the subnet increment.

- **Network address:** The first address in a subnet, where all host bits are 0. This address identifies the subnet itself and cannot be assigned to a host.

- **Broadcast address:** The last address in a subnet, where all host bits are 1. Used to send data to all hosts in the subnet. Cannot be assigned to a host.

- **Usable host range:** All addresses in a subnet between the network address and the broadcast address. Usable host count = 2^(host bits) - 2.

- **VLSM (Variable Length Subnet Masking):** The practice of using different subnet prefix lengths within the same major network address space. Allows large subnets for large LANs and small subnets (such as /30) for WAN point-to-point links, minimizing address waste.

- **Route summarization:** Combining multiple contiguous subnets into a single, shorter prefix advertisement. Also called supernetting or aggregation. Reduces routing table size.

- **Longest prefix match:** The rule routers use when forwarding packets. When multiple routing table entries match a destination, the router chooses the entry with the longest (most specific) prefix.

- **Classful addressing:** The legacy IPv4 system that assigned addresses as fixed Class A (/8), Class B (/16), or Class C (/24) networks based on the first octet value. CIDR replaced classful addressing.

- **Point-to-point link:** A WAN connection between exactly two devices. A /30 subnet (2 usable hosts) is standard for point-to-point router-to-router links.

---

## 2. Subnet Mask Quick-Reference Table

Memorize the entries for /24 through /30 before the quiz.

| Prefix | Dotted Decimal | Host Bits | Total Addresses | Usable Hosts | Block Size |
|---|---|---|---|---|---|
| /24 | 255.255.255.0 | 8 | 256 | 254 | 256 |
| /25 | 255.255.255.128 | 7 | 128 | 126 | 128 |
| /26 | 255.255.255.192 | 6 | 64 | 62 | 64 |
| /27 | 255.255.255.224 | 5 | 32 | 30 | 32 |
| /28 | 255.255.255.240 | 4 | 16 | 14 | 16 |
| /29 | 255.255.255.248 | 3 | 8 | 6 | 8 |
| /30 | 255.255.255.252 | 2 | 4 | 2 | 4 |
| /31 | 255.255.255.254 | 1 | 2 | 2* | 2 |
| /32 | 255.255.255.255 | 0 | 1 | 1* | 1 |

*Note: /31 and /32 are special cases. /31 allows 2 usable addresses on point-to-point links per RFC 3021. /32 identifies a single host (loopback or route injection).

---

## 3. Subnetting Formula Reference

Use these formulas for all subnetting calculations:

- Number of subnets created by borrowing b bits: 2^b
- Total addresses per subnet: 2^h where h = remaining host bits
- Usable hosts per subnet: 2^h - 2
- Block size (subnet increment): 256 minus the last non-zero octet of the subnet mask

The block-size shortcut: for 255.255.255.192 (/26), the last non-zero octet is 192. Block size = 256 - 192 = 64. Subnets begin at 0, 64, 128, 192.

---

## 4. Subnetting Worked Example

Given: 172.16.0.0/16 divided into subnets for 5 departments, each requiring up to 500 hosts.

Step 1 - Determine minimum host bits needed: 500 hosts requires at least 9 host bits (2^9 = 512, 2^8 = 256 is too small).

Step 2 - Calculate prefix length: 32 - 9 = /23.

Step 3 - Calculate block size: /23 in the third octet. 256 - 254 = 2. Block size is 2 in the third octet.

Step 4 - List subnets:

| Subnet | Network Address | First Host | Last Host | Broadcast |
|---|---|---|---|---|
| 1 | 172.16.0.0/23 | 172.16.0.1 | 172.16.1.254 | 172.16.1.255 |
| 2 | 172.16.2.0/23 | 172.16.2.1 | 172.16.3.254 | 172.16.3.255 |
| 3 | 172.16.4.0/23 | 172.16.4.1 | 172.16.5.254 | 172.16.5.255 |
| 4 | 172.16.6.0/23 | 172.16.6.1 | 172.16.7.254 | 172.16.7.255 |
| 5 | 172.16.8.0/23 | 172.16.8.1 | 172.16.9.254 | 172.16.9.255 |

---

## 5. VLSM Design Reference

VLSM assigns different prefix lengths to different network segments within the same address space. The allocation rule is: assign the largest subnet first, then allocate smaller subnets from the remaining space sequentially.

VLSM allocation order for a /24 address space (192.168.10.0/24):

| Segment | Hosts Required | Prefix Used | Network Address | Usable Range | Broadcast | Remaining |
|---|---|---|---|---|---|---|
| LAN A | 100 | /25 | 192.168.10.0 | .1 - .126 | .127 | .128 - .255 |
| LAN B | 50 | /26 | 192.168.10.128 | .129 - .190 | .191 | .192 - .255 |
| LAN C | 20 | /27 | 192.168.10.192 | .193 - .222 | .223 | .224 - .255 |
| WAN link | 2 | /30 | 192.168.10.224 | .225 - .226 | .227 | .228 - .255 |

Remaining space (.228 - .255) is available for future subnets. Without VLSM, assigning four /25 subnets would waste three full /25 blocks on segments needing far fewer hosts.

---

## 6. Cisco IOS IP Address Configuration Reference

| Task | Command | Notes |
|---|---|---|
| Assign IP address to interface | `ip address [addr] [mask]` | Entered in interface config mode |
| Enable the interface | `no shutdown` | Required — interfaces are shut down by default on routers |
| Verify all interfaces at once | `show ip interface brief` | Shows IP, method, and status for all interfaces |
| Verify single interface detail | `show interfaces Gi0/0` | Shows full counters, encapsulation, and line/protocol status |
| View routing table | `show ip route` | Confirms directly connected and static/dynamic routes |
| Test Layer 3 connectivity | `ping [ip-address]` | Tests path to destination; ICMP echoes |
| Extended ping (set source) | `ping [addr] source [interface]` | Forces ping to exit a specific interface for asymmetric testing |

---

## 7. Route Summarization Reference

Route summarization combines multiple subnets into a single advertisement. To find the summary route:

1. List the network addresses of all subnets to summarize in binary
2. Count the number of matching bits from the left
3. The summary network address is the common bits followed by zeros, with a prefix equal to the matching bit count

Example: Summarize 192.168.8.0/24, 192.168.9.0/24, 192.168.10.0/24, 192.168.11.0/24.

In binary (third octet only): 00001000, 00001001, 00001010, 00001011. The first 6 bits (000010) match. Summary: 192.168.8.0/22.

---

## 8. CCNA Exam Tips

1. The exam frequently offers "total addresses" and "usable hosts" as separate answer choices for the same subnet. Total = 2^h; usable = 2^h - 2. For /28: total = 16, usable = 14.

2. The block-size shortcut is faster than binary conversion: subtract the last non-zero octet value from 256 to get the block size. Use that block size as your increment between subnets.

3. VLSM exam questions typically show a network diagram with labeled host counts. Assign the largest subnet to the segment with the most hosts. Work from largest to smallest.

4. A /30 subnet (255.255.255.252) is the standard choice for point-to-point WAN links because it provides exactly 2 usable host addresses.

5. Route summarization exam questions require you to find the single aggregate prefix that covers all listed subnets without including non-listed addresses. Always check that the summary covers exactly the intended range.

6. Longest-prefix match determines which route a router uses. A more specific /28 route always wins over a less specific /24 route for a destination that matches both.

7. The exam may present an IP address and ask whether it is a valid host address, the network address, or the broadcast address for a given subnet. Calculate the host range and compare.

8. Classful subnet masks in dotted-decimal always end in 0, 128, 192, 224, 240, 248, 252, 254, or 255 in the host octet. Any other value in that octet is not a valid subnet mask.

---

## 9. Study Checklist

Work through each item before taking the quiz.

- [ ] Memorize the prefix, dotted-decimal, host bit count, and usable host count for /24 through /30
- [ ] Practice calculating the block size using the shortcut method for five different subnet masks
- [ ] Work through the subnetting example in Section 4 on paper without referring to the table
- [ ] Design a VLSM allocation for a new scenario: 10.0.0.0/24 with segments needing 80, 40, 12, and 2 hosts
- [ ] Configure IP addresses on four router interfaces in Packet Tracer using the VLSM subnets you calculated
- [ ] Verify your configuration using `show ip interface brief` and `ping`
- [ ] Review the Cisco IOS command reference table and understand each command's purpose
- [ ] Complete the Module 02 Packet Tracer lab activity
- [ ] Post your Module 02 discussion response by Wednesday at 11:59 PM

---

## Required Study Resources

- Cisco CCNA certification training information: cisco.com/c/en/us/training-events/training-certifications
- Free CCNA study notes and video summaries: professormesser.com

---

## 10. Supplemental Resources

The following open educational resources extend subnetting and VLSM concepts to CCNA exam depth. All resources are freely available.

1. **Cisco Networking Academy — CCNA: Introduction to Networks** (skillsforall.com): Module 11 of this free course covers IP addressing and subnetting with interactive exercises and auto-graded subnet calculation problems that simulate CCNA exam format.

2. **Jeremy's IT Lab — Subnetting (Days 7–9)** (youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ): These three video lessons teach the block-size shortcut method, VLSM design, and route summarization. Jeremy's approach to rapid subnet calculation is widely used by CCNA candidates.

3. **Subnetting Practice — subnettingpractice.com**: A free drill tool that generates random subnetting problems at varying difficulty levels. Practice is the only way to reach the speed required on the CCNA exam, where subnetting questions must be solved in under 90 seconds.

4. **Cisco Learning Network — IP Addressing Study Group** (learningnetwork.cisco.com): The Cisco Learning Network community forums include thousands of subnetting practice problems and worked solutions posted by CCNA candidates and certified engineers.

5. **GNS3 Academy — Free Subnetting Course** (academy.gns3.com): The GNS3 Academy offers a free subnetting course with video lessons and downloadable topology files for practicing IP addressing configurations on virtual routers, complementing the Packet Tracer approach used in this course.
