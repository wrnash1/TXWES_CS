# Video Script: Module 09 — Network Services: DNS, DHCP, and NTP

## CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Part 2 of 2 | Estimated Duration: 11–13 minutes

## Recorded by: Professor Nash | Texas Wesleyan University

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Professor Messer &bull; CompTIA Network+ (N10-008) Complete Training Course &bull; Module 09</strong>
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

Welcome back to Module 09. In Part 1 we covered DNS record types, the resolution hierarchy, and the DHCP DORA process. Now in Part 2 we add NTP for time synchronization and NAT for address translation. NTP and NAT both appear frequently on the Network+ exam, and NAT in particular has three subtypes you need to distinguish.

---

### Section 2: NTP — Network Time Protocol
<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-3321 NETWORK ADMINISTRATION</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">Core Network Services: DNS Resolution Hierarchy &amp; DHCP DORA Handshake</text>

  <!-- Left: DNS Resolution Hierarchy -->
  <g transform="translate(40, 95)">
    <rect width="380" height="325" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
    <text x="190" y="24" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">DNS Hierarchical Namespace (Port 53)</text>

    <!-- Root -->
    <rect x="130" y="40" width="120" height="35" fill="#0f172a" stroke="#d9a74a" rx="4"/>
    <text x="190" y="62" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">Root Domain (.)</text>

    <line x1="160" y1="75" x2="80" y2="105" stroke="#64748b" stroke-width="2"/>
    <line x1="220" y1="75" x2="300" y2="105" stroke="#64748b" stroke-width="2"/>

    <!-- TLDs -->
    <rect x="25" y="105" width="110" height="32" fill="#0f172a" stroke="#38bdf8" rx="3"/>
    <text x="80" y="126" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">.edu / .com</text>

    <rect x="245" y="105" width="110" height="32" fill="#0f172a" stroke="#38bdf8" rx="3"/>
    <text x="300" y="126" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">.org / .net</text>

    <line x1="80" y1="137" x2="80" y2="165" stroke="#64748b" stroke-width="2"/>

    <!-- Second Level -->
    <rect x="20" y="165" width="130" height="32" fill="#0f172a" stroke="#10b981" rx="3"/>
    <text x="85" y="186" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">txwes.edu</text>

    <line x1="85" y1="197" x2="85" y2="225" stroke="#64748b" stroke-width="2"/>

    <!-- Host / Subdomain -->
    <rect x="15" y="225" width="140" height="32" fill="#0f172a" stroke="#a855f7" rx="3"/>
    <text x="85" y="246" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle">canvas.txwes.edu</text>

    <!-- Key Record Types Table -->
    <rect x="170" y="155" width="195" height="150" fill="#0f172a" rx="4"/>
    <text x="267" y="174" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">Essential Record Types</text>
    <text x="180" y="196" fill="#38bdf8" font-size="10"><b>A:</b> IPv4 Address</text>
    <text x="180" y="214" fill="#10b981" font-size="10"><b>AAAA:</b> IPv6 Address</text>
    <text x="180" y="232" fill="#d9a74a" font-size="10"><b>CNAME:</b> Canonical Alias</text>
    <text x="180" y="250" fill="#f59e0b" font-size="10"><b>MX:</b> Mail Exchange Server</text>
    <text x="180" y="268" fill="#c084fc" font-size="10"><b>PTR:</b> Reverse DNS (IP→Name)</text>
    <text x="180" y="286" fill="#ef4444" font-size="10"><b>SOA / NS:</b> Authority / Nameserver</text>
  </g>

  <!-- Right: DHCP DORA Process -->
  <g transform="translate(440, 95)">
    <rect width="370" height="325" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="185" y="24" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">DHCP 4-Step Handshake (D-O-R-A)</text>

    <rect x="25" y="45" width="80" height="30" fill="#0f172a" stroke="#cbd5e1" rx="4"/><text x="65" y="65" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">CLIENT</text>
    <rect x="265" y="45" width="80" height="30" fill="#0f172a" stroke="#cbd5e1" rx="4"/><text x="305" y="65" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">DHCP SRV</text>

    <line x1="65" y1="80" x2="65" y2="280" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4"/>
    <line x1="305" y1="80" x2="305" y2="280" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4"/>

    <!-- 1. DISCOVER -->
    <line x1="65" y1="105" x2="300" y2="125" stroke="#ef4444" stroke-width="2"/>
    <polygon points="305,125 293,120 295,130" fill="#ef4444"/>
    <text x="185" y="112" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">1. DISCOVER (Broadcast)</text>

    <!-- 2. OFFER -->
    <line x1="305" y1="145" x2="70" y2="165" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="65,165 77,160 75,170" fill="#38bdf8"/>
    <text x="185" y="152" fill="#93c5fd" font-size="10" font-weight="bold" text-anchor="middle">2. OFFER (Unicast IP Lease)</text>

    <!-- 3. REQUEST -->
    <line x1="65" y1="185" x2="300" y2="205" stroke="#d9a74a" stroke-width="2"/>
    <polygon points="305,205 293,200 295,210" fill="#d9a74a"/>
    <text x="185" y="192" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">3. REQUEST (Broadcast Accept)</text>

    <!-- 4. ACKNOWLEDGE -->
    <line x1="305" y1="225" x2="70" y2="245" stroke="#10b981" stroke-width="2"/>
    <polygon points="65,245 77,240 75,250" fill="#10b981"/>
    <text x="185" y="232" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle">4. ACK (Lease Confirmed)</text>

    <!-- Lease Details -->
    <rect x="25" y="260" width="320" height="50" fill="#0f172a" rx="4"/>
    <text x="35" y="278" fill="#f8fafc" font-size="9"><b>Client Receives:</b> IP Address, Subnet Mask, Default Gateway,</text>
    <text x="35" y="295" fill="#38bdf8" font-size="9">DNS Servers, Lease Time. Ports: UDP 67 (Server) / 68 (Client).</text>
  </g>

  <!-- Footer Banner -->
  <rect x="40" y="430" width="770" height="35" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="452" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ Security Warning: DHCP Snooping prevents rogue DHCP servers by designating switch ports as trusted or untrusted.</text>
</svg>
</div>

[Alt-text: A four-level NTP stratum diagram. Stratum 0 shows a GPS satellite and atomic clock icon labeled Reference Clock. Stratum 1 shows two server icons labeled Primary NTP Servers synchronized directly to Stratum 0. Stratum 2 shows four server icons labeled Secondary NTP Servers synchronized to Stratum 1. Stratum 3 shows eight device icons including workstations and network switches. Downward arrows between each stratum represent time synchronization flowing down the hierarchy.]

NTP — Network Time Protocol — synchronizes clocks across all devices in a network. Accurate time is not just a convenience — it is a security requirement.

Why time synchronization matters:

Authentication and certificates — TLS certificates have valid-from and valid-to dates. A device with a clock off by more than a few minutes may reject valid certificates or accept expired ones. Kerberos authentication, used in Active Directory, fails if the time difference between client and server exceeds five minutes.

Log correlation — When investigating a security incident across multiple devices, accurate timestamps allow reconstruction of the event sequence. If each device has a different time, log correlation becomes impossible.

Replay attack prevention — IPsec and Kerberos use timestamps to reject replayed authentication packets. Without accurate time, replay protection fails.

NTP uses a hierarchical stratum model. Stratum 0 is the reference clock (GPS receiver or atomic clock). Stratum 0 devices are not on the network — they feed time to Stratum 1 servers directly. Stratum 1 servers synchronize to Stratum 0. Stratum 2 servers synchronize to Stratum 1. Most enterprise network devices synchronize to Stratum 2 or Stratum 3 servers.

NTP uses UDP port 123. Stratum 16 indicates unsynchronized.

> Network+ Exam Tip: NTP uses UDP port 123. Stratum 1 is most accurate on the network. Kerberos fails if clock skew exceeds 5 minutes.

---

### Section 3: NAT — Network Address Translation

[Alt-text: Two NAT diagrams. Left diagram labeled Static NAT shows one private IP 192.168.1.10 mapping through a NAT router to one public IP 203.0.113.10, labeled One-to-one permanent mapping. Right diagram labeled PAT / NAT Overload shows three private IP addresses (192.168.1.10, 192.168.1.11, 192.168.1.12) all translating through a NAT router to the single public IP 203.0.113.1 with unique translated source port numbers. Labeled Many-to-one mapping using unique port numbers.]

NAT — Network Address Translation — modifies IP address information in packet headers as traffic passes through a router, allowing private-addressed devices to use public IP addresses for internet access.

The three types you must know:

Static NAT — A one-to-one permanent mapping between a single private IP and a single public IP. Used when an internal server must be reachable from the internet at a specific public IP. Example: web server at 192.168.1.10 permanently mapped to 203.0.113.10.

Dynamic NAT — Maps private IPs to a pool of public IPs on demand. The mapping is created when a client initiates a connection and released when it ends. Requires as many public IPs as concurrent outside connections.

PAT (Port Address Translation) / NAT Overload — Maps many private IPs to a single public IP using unique source port numbers to track each session. This is how home routers and most enterprise edge routers work. When an internal host at 192.168.1.10 port 1500 sends traffic outbound, the NAT router rewrites the source IP to the public IP and assigns a unique translated source port. Return traffic is forwarded back using the translation table.

Inside local — The private IP of an internal host as seen from the inside network.

Inside global — The public IP of an internal host as seen from outside after translation.

> Network+ Exam Tip: PAT (NAT Overload) allows thousands of internal hosts to share a single public IP. Static NAT is always the answer when an internal server must be reachable at a fixed public address.

---

### Section 4: IPAM and DNS/DHCP Integration

[Alt-text: A three-box horizontal flow diagram. Left box labeled DHCP Server. Center box labeled IPAM with text: Centralized tracking of IP assignments and scope utilization. Right box labeled DNS Server. Bidirectional arrows between DHCP and IPAM and between IPAM and DNS are labeled Dynamic DNS Updates.]

IPAM — IP Address Management — is a framework for tracking IP address allocation, DNS records, and DHCP scope utilization across an enterprise network.

Dynamic DNS (DDNS) — When DHCP assigns a new address to a client, it can automatically notify the DNS server to create or update the A and PTR records. This keeps DNS synchronized with DHCP assignments without manual updates.

DHCP starvation — An attack where a malicious device sends large numbers of DHCP Discover messages with spoofed MAC addresses, exhausting all available addresses in the DHCP scope. DHCP Snooping (covered in Module 08) mitigates this attack.

Module 09 key takeaways: DNS resolves hostnames using a hierarchical query process. DHCP automates address assignment using the DORA sequence. NTP uses UDP 123 and the stratum hierarchy. PAT (NAT Overload) allows many private IPs to share one public IP. Dynamic DNS keeps A and PTR records current as DHCP assignments change.

Module 10 covers routing protocols — static routes, OSPF, and BGP.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

End of Part 2
