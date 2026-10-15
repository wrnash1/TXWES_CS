# Video Script: Module 03 – IP Addressing: IPv4, Subnetting, CIDR
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Part 2 of 2 | Estimated Duration: 12–14 minutes
## Recorded by: Professor Nash | Texas Wesleyan University

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Professor Messer &bull; CompTIA Network+ (N10-008) Complete Training Course &bull; Module 03</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLG49S3nxzAnmpm1HP80g85VIyFCxs34ee" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLG49S3nxzAnmpm1HP80g85VIyFCxs34ee" title="Professor Messer &bull; CompTIA Network+ (N10-008) Complete Training Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Professor Messer &bull; CompTIA Network+ (N10-008) Complete Training Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

---

### Pre-Roll Slide

---

### Section 1: Part 2 Introduction

Welcome back to Module 03. In Part 1 we covered IPv4 address structure, classful addressing, RFC 1918 private ranges, and binary conversion. Now in Part 2 we tackle CIDR notation and the core subnetting calculations you will need for both the exam and your career. I am going to walk you through a step-by-step process, then we will do several practice problems together. Have your pencil ready.

---

### Section 2: CIDR Notation and the Subnet Table
<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-3321 NETWORK ADMINISTRATION</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">IPv4 Addressing Structure, Subnet Masking &amp; RFC 1918 Private Scopes</text>

  <!-- Octet Decomposition -->
  <g transform="translate(40, 95)">
    <rect width="770" height="110" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
    <text x="385" y="24" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">32-Bit Dotted-Decimal Architecture Example: 192.168.1.50 /24</text>

    <!-- Octet 1 -->
    <rect x="25" y="40" width="165" height="55" fill="#0f172a" rx="4"/>
    <text x="107" y="60" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">Octet 1: 192</text>
    <text x="107" y="80" fill="#38bdf8" font-size="11" font-family="monospace" text-anchor="middle">11000000</text>

    <!-- Octet 2 -->
    <rect x="215" y="40" width="165" height="55" fill="#0f172a" rx="4"/>
    <text x="297" y="60" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">Octet 2: 168</text>
    <text x="297" y="80" fill="#38bdf8" font-size="11" font-family="monospace" text-anchor="middle">10101000</text>

    <!-- Octet 3 -->
    <rect x="405" y="40" width="165" height="55" fill="#0f172a" rx="4"/>
    <text x="487" y="60" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">Octet 3: 1</text>
    <text x="487" y="80" fill="#38bdf8" font-size="11" font-family="monospace" text-anchor="middle">00000001</text>

    <!-- Octet 4 -->
    <rect x="595" y="40" width="150" height="55" fill="#0f172a" rx="4"/>
    <text x="670" y="60" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">Octet 4: 50</text>
    <text x="670" y="80" fill="#10b981" font-size="11" font-family="monospace" text-anchor="middle">00110010 (Host)</text>
  </g>

  <!-- RFC 1918 Private Address Ranges -->
  <g transform="translate(40, 220)">
    <rect width="770" height="200" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="385" y="24" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">RFC 1918 Private IP Address Spaces (Non-Routable over Public Internet)</text>

    <!-- Class A Private -->
    <rect x="25" y="40" width="225" height="140" fill="#0f172a" stroke="#38bdf8" rx="4"/>
    <text x="137" y="62" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Class A Private</text>
    <text x="137" y="82" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">10.0.0.0 /8</text>
    <text x="35" y="105" fill="#94a3b8" font-size="10">Range:</text>
    <text x="35" y="120" fill="#cbd5e1" font-size="10">10.0.0.0 – 10.255.255.255</text>
    <text x="35" y="145" fill="#94a3b8" font-size="10">Usable Hosts:</text>
    <text x="35" y="160" fill="#38bdf8" font-size="10" font-weight="bold">16,777,214 Hosts</text>

    <!-- Class B Private -->
    <rect x="270" y="40" width="230" height="140" fill="#0f172a" stroke="#f59e0b" rx="4"/>
    <text x="385" y="62" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">Class B Private</text>
    <text x="385" y="82" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">172.16.0.0 /12</text>
    <text x="280" y="105" fill="#94a3b8" font-size="10">Range:</text>
    <text x="280" y="120" fill="#cbd5e1" font-size="10">172.16.0.0 – 172.31.255.255</text>
    <text x="280" y="145" fill="#94a3b8" font-size="10">Usable Hosts:</text>
    <text x="280" y="160" fill="#f59e0b" font-size="10" font-weight="bold">1,048,574 Hosts (16 Subnets)</text>

    <!-- Class C Private -->
    <rect x="520" y="40" width="225" height="140" fill="#0f172a" stroke="#10b981" rx="4"/>
    <text x="632" y="62" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Class C Private</text>
    <text x="632" y="82" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">192.168.0.0 /16</text>
    <text x="530" y="105" fill="#94a3b8" font-size="10">Range:</text>
    <text x="530" y="120" fill="#cbd5e1" font-size="10">192.168.0.0 – 192.168.255.255</text>
    <text x="530" y="145" fill="#94a3b8" font-size="10">Usable Hosts:</text>
    <text x="530" y="160" fill="#10b981" font-size="10" font-weight="bold">65,534 Hosts (256 Subnets)</text>
  </g>

  <!-- Footer Banner -->
  <rect x="40" y="430" width="770" height="35" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="452" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ Exam Rule: APIPA (Automatic Private IP Addressing) is 169.254.0.0/16 — assigned automatically when DHCP fails.</text>
</svg>
</div>

[Alt-text: A seven-row reference table. Column headers are CIDR Prefix, Subnet Mask, Block Size, and Usable Hosts. Rows from top to bottom: /24 with mask 255.255.255.0, block size 256, 254 usable hosts. /25 with mask 255.255.255.128, block size 128, 126 hosts. /26 with mask 255.255.255.192, block size 64, 62 hosts. /27 with mask 255.255.255.224, block size 32, 30 hosts. /28 with mask 255.255.255.240, block size 16, 14 hosts. /29 with mask 255.255.255.248, block size 8, 6 hosts. /30 with mask 255.255.255.252, block size 4, 2 hosts.]

CIDR (Classless Inter-Domain Routing) notation expresses the subnet mask as a prefix length — the number of consecutive 1 bits in the mask. A /24 means 24 bits are 1 (the network portion), and 8 bits are 0 (the host portion).

The key formula you need is: Usable hosts = 2 to the power of (host bits) minus 2. We subtract 2 to exclude the network address (all host bits zero) and the broadcast address (all host bits one).

For a /26: 32 minus 26 equals 6 host bits. 2 to the power of 6 equals 64. Minus 2 equals 62 usable hosts.

The "block size" shortcut: subtract the last octet of the subnet mask from 256. For /26, mask is 192 in the last octet. 256 minus 192 equals 64. The subnets within a /24 that use a /26 mask start at 0, 64, 128, and 192.

This block size approach is the fastest way to identify which subnet an address belongs to. Memorize the table I just showed you — /24 through /30. These cover the vast majority of exam questions.

---

### Section 3: Four-Step Subnet Calculation Process

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
