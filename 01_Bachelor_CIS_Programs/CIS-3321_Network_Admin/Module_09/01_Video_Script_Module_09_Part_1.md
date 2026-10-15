# Video Script: Module 09 — Network Services: DNS, DHCP, and NTP

## CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Part 1 of 2 | Estimated Duration: 13–15 minutes

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

### Section 1: Introduction

Welcome to Module 09. I am Professor Nash. Every time you open a browser and type a website name, three invisible infrastructure services work together to make that connection happen — DNS resolves the hostname to an IP address, DHCP assigned your device an address in the first place, and NTP ensures every device on the network agrees on the current time. These services run silently in the background, and when they fail, users cannot reach anything. Module 09 covers all three in depth. Part 1 focuses on DNS — the naming system that makes the internet navigable — and DHCP, which automates address assignment. Part 2 covers NTP and NAT, two additional services critical for enterprise network operation.

---

### Section 2: DNS — The Naming System
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

[Alt-text: A DNS hierarchy diagram with five levels. The top node is the root (dot). The second level shows .com and .org top-level domains. The third level under .com shows example.com and google.com. The fourth level under example.com shows www.example.com. Six labeled arrows trace the DNS resolution path: (1) Client to Resolver, (2) Resolver to Root, (3) Root to Resolver with referral to TLD, (4) Resolver to TLD Server, (5) TLD to Resolver with referral to authoritative server, (6) Resolver to Authoritative Server returning the IP address.]

DNS — the Domain Name System — is a distributed, hierarchical database that translates human-readable hostnames into IP addresses. Without DNS, users would need to memorize the IP address of every website they visit.

The DNS resolution process works in six steps:

Step 1 — The client sends a recursive query to its configured DNS resolver. The resolver is typically the client's default gateway or a service like 8.8.8.8 (Google) or 1.1.1.1 (Cloudflare).

Step 2 — The resolver checks its cache. If the answer is cached and the TTL has not expired, it returns the answer immediately. If not, it begins iterative queries.

Step 3 — The resolver queries a root name server, asking where to find the .com TLD servers.

Step 4 — The root server responds with the address of the .com TLD name servers.

Step 5 — The resolver queries the .com TLD server, asking for the authoritative name server for example.com.

Step 6 — The resolver queries the authoritative name server for example.com, which returns the IP address. The resolver caches the result (respecting the TTL) and returns it to the client.

DNS uses UDP port 53 for standard queries and TCP port 53 for zone transfers and responses exceeding 512 bytes.

> Network+ Exam Tip: The client sends a recursive query to its resolver. The resolver uses iterative queries to the root, TLD, and authoritative servers. A "Non-authoritative answer" in nslookup output means the answer came from the resolver's cache, not directly from the authoritative name server.

---

### Section 3: DNS Record Types

[Alt-text: A DNS record type reference table with four columns: Record Type abbreviation, Full Name, Purpose, Example. The eight rows cover A, AAAA, CNAME, MX, NS, PTR, TXT, and SOA records with descriptions and examples for each.]

You need to know these DNS record types for the Network+ exam:

A record — Maps a hostname to an IPv4 address. The most common record type.

AAAA record — Maps a hostname to an IPv6 address.

CNAME record — A canonical name record creates an alias pointing one hostname to another. The resolver follows the CNAME chain until it reaches an A or AAAA record.

MX record — Mail Exchanger record. Identifies the mail server responsible for accepting email for a domain. Includes a priority value — lower number means higher priority.

NS record — Name Server record. Identifies the authoritative name servers for a domain.

PTR record — Pointer record. Maps an IP address back to a hostname (reverse DNS lookup). Stored in the in-addr.arpa zone. Used by email servers and network administrators.

TXT record — Text record. Stores arbitrary text. Widely used for SPF records (Sender Policy Framework — prevents email spoofing), DKIM records (email signing), and domain verification.

SOA record — Start of Authority. Contains administrative metadata about the DNS zone: the primary name server, admin contact email, serial number, and refresh timers.

> Network+ Exam Tip: MX records are always the answer when the question involves email delivery. PTR records are always the answer for reverse DNS lookup. TXT records are the answer for SPF and DKIM email authentication.

---

### Section 4: DHCP — Dynamic Host Configuration Protocol

[Alt-text: A DHCP sequence diagram with a client PC on the left and a DHCP Server on the right. Four horizontal arrows trace the DORA process. Arrow 1 labeled DISCOVER points right (client broadcasts to find any DHCP server). Arrow 2 labeled OFFER points left (server proposes an IP and configuration). Arrow 3 labeled REQUEST points right (client broadcasts acceptance of the offer). Arrow 4 labeled ACK points left (server confirms the lease). A box below lists the parameters in the ACK: IP Address, Subnet Mask, Default Gateway, DNS Server IP, Lease Duration.]

DHCP automates the assignment of IP addresses and network configuration parameters to clients.

The DHCP process follows the DORA sequence:

DISCOVER — The client broadcasts a DHCP Discover message (destination IP 255.255.255.255). The client has no IP address and is looking for any DHCP server.

OFFER — One or more DHCP servers respond with a DHCP Offer, proposing an available IP address with subnet mask, default gateway, DNS server, and lease duration.

REQUEST — The client broadcasts a DHCP Request, indicating which server's offer it accepts. Broadcasting (rather than unicasting) allows other servers that sent Offers to know their offer was not accepted and reclaim the address.

ACK — The chosen server sends a DHCP Acknowledgment confirming the lease. The client configures its interface with the delivered parameters.

At 50% of the lease duration, the client attempts a unicast renewal with the issuing server. At 87.5% of the lease (T2), the client broadcasts a renewal to any available DHCP server.

DHCP uses UDP port 67 (server) and UDP port 68 (client).

DHCP Relay Agent — When the DHCP server is on a different subnet, the local router acts as a relay agent (ip helper-address in Cisco IOS). The relay agent intercepts the broadcast DHCP Discover and forwards it as a unicast to the DHCP server. Without a relay agent, broadcast DHCP messages cannot cross subnet boundaries.

> Network+ Exam Tip: DHCP uses UDP ports 67 and 68. DORA is the acronym. When a Windows client cannot reach a DHCP server, it self-assigns an APIPA address in the 169.254.0.0/16 range. Seeing 169.254.x.x means DHCP failed.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

End of Part 1
