# Video Script: Module 03 – IP Addressing: IPv4, Subnetting, CIDR
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Part 1 of 2 | Estimated Duration: 13–15 minutes
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

[SHOW SLIDE: Course banner — "CIS-3321 Network Administration | Module 03: IP Addressing — IPv4, Subnetting, and CIDR | Texas Wesleyan University"]

---

### Section 1: Introduction

[00:00 – 01:15]

[SHOW SLIDE: Professor Nash on camera with module title card]

Welcome to Module 03. I'm Professor Nash, and this module covers the topic that students both fear and find most rewarding when they master it: IPv4 addressing and subnetting. I want to tell you upfront — subnetting is math, but it is not complicated math. It requires binary arithmetic, a clear process, and practice. By the end of this module, you will be able to look at any IP address with any subnet mask and immediately determine the network address, broadcast address, usable host range, and number of hosts.

Part 1 covers IPv4 address structure, classful addressing, private address ranges, and the fundamentals of binary conversion. Part 2 covers CIDR notation and the subnetting calculation process with exam-style practice problems.

---

### Section 2: IPv4 Address Structure

[01:15 – 04:00]

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

[SHOW DIAGRAM: The IPv4 address 192.168.1.50 displayed in large text. Below it, the binary representation: 11000000.10101000.00000001.00110010. Each of the four octets is labeled. A note shows "32 total bits, 4 octets of 8 bits each."]

[Alt-text: The IPv4 address 192.168.1.50 displayed in large text. Directly below it is the binary representation: 11000000 dot 10101000 dot 00000001 dot 00110010. The four binary groups are separated by dots, and each group is labeled "octet." Text beneath reads "32 total bits divided into 4 octets of 8 bits each."]

An IPv4 address is a 32-bit number. To make it readable, we write it in dotted-decimal notation — four decimal numbers separated by dots, each representing 8 binary bits. Each group of 8 bits is called an octet.

Because 8 bits can represent 256 unique values (2 to the power of 8 equals 256), each octet can range from 0 to 255. That is why you will never see an IP address with a number greater than 255 in any octet.

Every IPv4 address has two parts: the network portion and the host portion. The subnet mask determines where the boundary between network and host falls.

When the subnet mask bits are 1, those bits belong to the network. When the subnet mask bits are 0, those bits belong to the host. A mask of 255.255.255.0 means the first 24 bits are network bits and the last 8 bits are host bits.

---

### Section 3: Classful Addressing

[04:00 – 07:00]

[SHOW DIAGRAM: A table showing the five IP address classes. Class A: first octet 1–126, default mask /8, hosts per network approximately 16 million. Class B: first octet 128–191, default mask /16, hosts per network approximately 65,000. Class C: first octet 192–223, default mask /24, hosts per network 254. Class D: first octet 224–239, multicast. Class E: first octet 240–255, experimental/reserved.]

[Alt-text: A five-row table. Row 1: Class A, range 1.0.0.0 to 126.255.255.255, default subnet mask slash 8, maximum hosts approximately 16 million per network. Row 2: Class B, range 128.0.0.0 to 191.255.255.255, default mask slash 16, approximately 65,534 hosts per network. Row 3: Class C, range 192.0.0.0 to 223.255.255.255, default mask slash 24, 254 hosts per network. Row 4: Class D, range 224.0.0.0 to 239.255.255.255, multicast use only. Row 5: Class E, range 240.0.0.0 to 255.255.255.255, experimental/reserved.]

Before CIDR was developed in the early 1990s, IP addresses were assigned in fixed classes. The class system was simple but inefficient — it caused massive waste of address space, which is a primary reason we ran out of IPv4 addresses.

Class A addresses start with a first octet of 1 through 126. A Class A network has a default mask of /8, meaning only the first octet is the network portion. The remaining 24 bits are for hosts, allowing approximately 16 million hosts per network. Only 126 Class A networks exist, and they were originally assigned to large organizations and governments.

Class B addresses start with a first octet of 128 through 191. The default mask is /16. The first two octets identify the network. Approximately 65,534 hosts per network. Used for large organizations.

Class C addresses start with a first octet of 192 through 223. The default mask is /24. The first three octets identify the network, and the last octet is for hosts — giving 254 usable hosts per network.

Class D (224–239) is multicast. Class E (240–255) is experimental and reserved.

One critical address to remember: 127.x.x.x is the loopback range. The specific address 127.0.0.1 is the loopback address — pinging it tests your local TCP/IP stack without sending any traffic to the network.

> **Network+ Exam Tip:** The exam frequently asks you to identify address classes from a given IP address. The first octet determines the class: 1–126 is Class A, 128–191 is Class B, 192–223 is Class C. The number 127 is the loopback range — not Class A for host assignment purposes.

---

### Section 4: Private IP Address Ranges (RFC 1918)

[07:00 – 09:00]

[SHOW DIAGRAM: A table showing the three RFC 1918 private address ranges. Row 1: Class A private — 10.0.0.0/8, range 10.0.0.0 to 10.255.255.255. Row 2: Class B private — 172.16.0.0/12, range 172.16.0.0 to 172.31.255.255. Row 3: Class C private — 192.168.0.0/16, range 192.168.0.0 to 192.168.255.255.]

[Alt-text: A three-row table titled RFC 1918 Private Address Ranges. Row 1: Class A private range, 10.0.0.0 slash 8, spanning 10.0.0.0 through 10.255.255.255. Row 2: Class B private range, 172.16.0.0 slash 12, spanning 172.16.0.0 through 172.31.255.255. Row 3: Class C private range, 192.168.0.0 slash 16, spanning 192.168.0.0 through 192.168.255.255.]

RFC 1918 defines three address ranges that are reserved for private use and are not routed on the public internet. Every internal network — your home network, your office LAN, a campus network — uses addresses from these ranges. NAT (Network Address Translation) is used to translate private addresses to public addresses when traffic needs to reach the internet.

Class A private: 10.0.0.0/8. This is a single massive network with over 16 million host addresses. Large enterprises use the 10.x.x.x range for their internal networks.

Class B private: 172.16.0.0/12. The valid range is 172.16.0.0 through 172.31.255.255. This is a commonly tested boundary — 172.32.x.x is NOT private; it is a public address range.

Class C private: 192.168.0.0/16. The valid range is 192.168.0.0 through 192.168.255.255. Your home router almost certainly uses a 192.168.x.x address. 192.169.x.x is NOT private.

Also memorize: APIPA range is 169.254.0.0/16. This is the self-assigned address range Windows uses when DHCP fails.

> **Network+ Exam Tip:** The exam presents boundary addresses like 172.32.x.x or 192.169.x.x and asks if they are private. They are not — they fall just outside the RFC 1918 ranges. Also note: 169.254.x.x is NOT an RFC 1918 private range; it is the APIPA range.

---

### Section 5: Binary-to-Decimal Conversion

[09:00 – 11:30]

[SHOW DIAGRAM: A binary conversion chart. Eight columns labeled with powers of 2 from left to right: 128, 64, 32, 16, 8, 4, 2, 1. A row below shows the binary digit 1 in each column. A sum shows 128+64+32+16+8+4+2+1 = 255. A second example row shows 11000000 with 128+64 = 192.]

[Alt-text: A binary conversion table. The top row labels eight columns with values 128, 64, 32, 16, 8, 4, 2, and 1, representing decreasing powers of 2. A first data row shows all 1s in every column, with the sum 255 shown at the right. A second data row shows 1 in the 128 and 64 columns and 0 in all others, with the sum 192 shown at the right.]

To truly understand subnetting, you need to be comfortable with binary-to-decimal conversion. Don't worry — it is simpler than it looks.

Every bit position in an octet has a value: 128, 64, 32, 16, 8, 4, 2, 1. These are the powers of 2 from position 7 down to position 0.

To convert binary to decimal, add up the values of each position where the bit is 1.

Example: 11000000 in binary. Positions with 1s: 128 and 64. Sum: 192. So 11000000 binary equals 192 decimal. That is why a /26 subnet mask has 255.255.255.192 in the last octet.

Example: 11111111. All positions are 1. Sum: 128+64+32+16+8+4+2+1 = 255. That is where the 255 in subnet masks comes from.

Example: 11100000. Positions 128, 64, 32 are 1. Sum: 224. So a /27 subnet mask ends in 224.

Practice these conversions until you can do them in your head. For the Network+ exam, you will not have a calculator, so binary fluency is essential.

---

### Section 6: Part 1 Summary

[11:30 – 13:30]

[SHOW SLIDE: Summary bullet list]

In Part 1, we covered IPv4 address structure — 32 bits in four octets, network portion versus host portion. We reviewed the classful addressing system — A, B, C, D, E. We memorized the RFC 1918 private address ranges. And we practiced binary-to-decimal conversion, which is the foundation of all subnet calculations.

In Part 2, we apply these skills to CIDR notation and walk through complete subnet calculations with exam-style problems. Bring a pencil.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

*End of Part 1*
