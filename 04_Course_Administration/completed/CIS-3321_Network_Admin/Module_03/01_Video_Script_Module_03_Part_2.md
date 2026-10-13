# Video Script: Module 03 – IP Addressing: IPv4, Subnetting, CIDR
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Part 2 of 2 | Estimated Duration: 12–14 minutes
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: "Module 03 Part 2 — CIDR Notation, Subnet Calculations, and Exam Practice"]

---

### Section 1: Part 2 Introduction

[00:00 – 00:45]

[SHOW SLIDE: Professor Nash on camera]

Welcome back to Module 03. In Part 1 we covered IPv4 address structure, classful addressing, RFC 1918 private ranges, and binary conversion. Now in Part 2 we tackle CIDR notation and the core subnetting calculations you will need for both the exam and your career. I am going to walk you through a step-by-step process, then we will do several practice problems together. Have your pencil ready.

---

### Section 2: CIDR Notation and the Subnet Table

[00:45 – 03:30]

[SHOW DIAGRAM: A subnet reference table. Three columns: CIDR Prefix, Subnet Mask, Block Size, Usable Hosts. Rows: /24 = 255.255.255.0, block 256, 254 hosts. /25 = 255.255.255.128, block 128, 126 hosts. /26 = 255.255.255.192, block 64, 62 hosts. /27 = 255.255.255.224, block 32, 30 hosts. /28 = 255.255.255.240, block 16, 14 hosts. /29 = 255.255.255.248, block 8, 6 hosts. /30 = 255.255.255.252, block 4, 2 hosts.]

[Alt-text: A seven-row reference table. Column headers are CIDR Prefix, Subnet Mask, Block Size, and Usable Hosts. Rows from top to bottom: /24 with mask 255.255.255.0, block size 256, 254 usable hosts. /25 with mask 255.255.255.128, block size 128, 126 hosts. /26 with mask 255.255.255.192, block size 64, 62 hosts. /27 with mask 255.255.255.224, block size 32, 30 hosts. /28 with mask 255.255.255.240, block size 16, 14 hosts. /29 with mask 255.255.255.248, block size 8, 6 hosts. /30 with mask 255.255.255.252, block size 4, 2 hosts.]

CIDR (Classless Inter-Domain Routing) notation expresses the subnet mask as a prefix length — the number of consecutive 1 bits in the mask. A /24 means 24 bits are 1 (the network portion), and 8 bits are 0 (the host portion).

The key formula you need is: Usable hosts = 2 to the power of (host bits) minus 2. We subtract 2 to exclude the network address (all host bits zero) and the broadcast address (all host bits one).

For a /26: 32 minus 26 equals 6 host bits. 2 to the power of 6 equals 64. Minus 2 equals 62 usable hosts.

The "block size" shortcut: subtract the last octet of the subnet mask from 256. For /26, mask is 192 in the last octet. 256 minus 192 equals 64. The subnets within a /24 that use a /26 mask start at 0, 64, 128, and 192.

This block size approach is the fastest way to identify which subnet an address belongs to. Memorize the table I just showed you — /24 through /30. These cover the vast majority of exam questions.

---

### Section 3: Four-Step Subnet Calculation Process

[03:30 – 07:00]

[SHOW SLIDE: Four-step process listed vertically: Step 1 — Identify the CIDR prefix and calculate block size. Step 2 — Find the network address. Step 3 — Find the broadcast address. Step 4 — Identify the usable host range.]

Here is the four-step process I want you to use for every subnet calculation problem.

**Step 1:** Identify the CIDR prefix and calculate the block size. Block size equals 256 minus the interesting octet of the subnet mask. For /26, mask is 192, block size is 64.

**Step 2:** Find the network address. Look at the interesting octet of the IP address. Find the largest multiple of the block size that does not exceed that octet. That is your network address.

**Step 3:** Find the broadcast address. Take the network address in the interesting octet and add the block size minus 1. That gives you the broadcast.

**Step 4:** The usable host range is everything between the network address and the broadcast address.

Let me walk through a complete example.

Given: IP address 192.168.1.75 with mask 255.255.255.224 (/27).

Step 1: /27, mask is 224, block size = 256 - 224 = 32.

Step 2: The interesting octet is the last one (75). Multiples of 32: 0, 32, 64, 96. The largest multiple of 32 that does not exceed 75 is 64. Network address = 192.168.1.64.

Step 3: Broadcast = 64 + 32 - 1 = 95. Broadcast address = 192.168.1.95.

Step 4: Usable range = 192.168.1.65 through 192.168.1.94.

That is 30 usable hosts (2 to the power of 5 minus 2 = 30). The host at 192.168.1.75 is within this range, so it is valid.

---

### Section 4: Exam-Style Practice Problems

[07:00 – 10:30]

[SHOW SLIDE: Problem set with three IP addresses and masks]

Let's do three more practice problems at exam pace.

**Problem 1:** Host IP 10.50.20.130, mask 255.255.255.192 (/26).

Block size: 256 - 192 = 64. Interesting octet = 130. Multiples of 64: 0, 64, 128. Largest not exceeding 130 = 128. Network = 10.50.20.128. Broadcast = 128 + 64 - 1 = 191. So broadcast = 10.50.20.191. Usable range = 10.50.20.129 through 10.50.20.190. Host 130 is valid.

**Problem 2:** Host IP 172.16.5.100, mask 255.255.255.240 (/28).

Block size: 256 - 240 = 16. Interesting octet = 100. Multiples of 16: 0, 16, 32, 48, 64, 80, 96, 112. Largest not exceeding 100 = 96. Network = 172.16.5.96. Broadcast = 96 + 16 - 1 = 111. So broadcast = 172.16.5.111. Usable range = 172.16.5.97 through 172.16.5.110. 14 usable hosts.

**Problem 3:** Two routers connected by a point-to-point link. What mask provides exactly 2 usable host addresses with minimal waste?

Block size 4, /30, mask 255.255.255.252. 2 to the power of 2 minus 2 = 2 usable hosts. This is the standard mask for point-to-point router links. One address for each router interface, zero waste.

> **Network+ Exam Tip:** The /30 subnet for point-to-point links is one of the most frequently tested subnetting scenarios. If you see a scenario involving two routers connected directly, /30 is almost always the correct answer.

---

### Section 5: Number of Subnets vs. Hosts

[10:30 – 12:00]

[SHOW SLIDE: Table showing borrowed bits, number of subnets, hosts per subnet. Starting from /24: borrow 1 bit = 2 subnets, 126 hosts each. Borrow 2 = 4 subnets, 62 hosts. Borrow 3 = 8 subnets, 30 hosts. Borrow 4 = 16 subnets, 14 hosts.]

When you subnet a network, you borrow bits from the host portion of the address. Each bit you borrow doubles the number of subnets but halves the number of hosts per subnet.

Starting from a /24 (254 usable hosts, one subnet):

Borrow 1 bit → /25 → 2 subnets, 126 hosts each.

Borrow 2 bits → /26 → 4 subnets, 62 hosts each.

Borrow 3 bits → /27 → 8 subnets, 30 hosts each.

Borrow 4 bits → /28 → 16 subnets, 14 hosts each.

The formula for number of subnets is 2 to the power of borrowed bits. The formula for hosts per subnet is 2 to the power of remaining host bits minus 2.

Design principle: always choose the smallest subnet that accommodates your host count plus some growth room. Avoid over-provisioning to conserve address space.

---

### Section 6: Lab Preview and Module Closing

[12:00 – 13:30]

[SHOW SLIDE: Lab preview — subnet calculation worksheet]

In this week's lab, you will work through a set of subnet calculation exercises — given an IP address and mask, you will determine the network address, broadcast address, usable range, and number of hosts. You will also configure IP addresses on Packet Tracer virtual hosts to verify your calculations by testing connectivity.

Before the lab, memorize the /24 through /30 subnet table from the reading guide. Practice at least ten problems with different addresses and masks.

Key module takeaways: IPv4 is 32 bits in four octets. The subnet mask separates network bits from host bits. RFC 1918 defines three private ranges. The four-step calculation gives you network address, broadcast, and host range for any subnet. Block size equals 256 minus the interesting octet.

In Module 04 we transition to IPv6 — 128-bit addresses, hexadecimal notation, and the transition mechanisms that allow IPv4 and IPv6 to coexist.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

*End of Part 2*
