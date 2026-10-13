#!/usr/bin/env python3
"""
Texas Wesleyan University - Curriculum Visual Media Injection Engine (CIS-3321 Network Administration)
Replaces visual placeholder cues ([SHOW DIAGRAM: ...]) across CIS-3321
with responsive, publication-quality technical SVG illustrations in university branding.
"""

import os
import re

BASE_DIR = "/home/wrnash1/Developer/TXWES_CS/01_Bachelor_CIS_Programs/CIS-3321_Network_Admin"

# 1. Module 01: OSI 7-Layer Model & Data Encapsulation PDU Stack
M01_SVG = '''<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 490" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-3321 NETWORK ADMINISTRATION</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">OSI 7-Layer Reference Model &amp; Protocol Data Unit (PDU) Encapsulation</text>

  <!-- Left: OSI 7 Layers -->
  <g transform="translate(40, 95)">
    <rect width="400" height="340" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
    <text x="200" y="24" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">OSI 7-Layer Stack (Top to Bottom)</text>

    <!-- Layer 7 -->
    <rect x="20" y="38" width="360" height="36" fill="#0f172a" stroke="#a855f7" rx="3"/>
    <text x="35" y="60" fill="#c084fc" font-size="11" font-weight="bold">Layer 7: Application</text>
    <text x="365" y="60" fill="#94a3b8" font-size="10" text-anchor="end">HTTP, DNS, DHCP, SSH (Data)</text>

    <!-- Layer 6 -->
    <rect x="20" y="79" width="360" height="36" fill="#0f172a" stroke="#a855f7" rx="3"/>
    <text x="35" y="101" fill="#c084fc" font-size="11" font-weight="bold">Layer 6: Presentation</text>
    <text x="365" y="101" fill="#94a3b8" font-size="10" text-anchor="end">TLS/SSL, JPEG, ASCII, Encryption</text>

    <!-- Layer 5 -->
    <rect x="20" y="120" width="360" height="36" fill="#0f172a" stroke="#a855f7" rx="3"/>
    <text x="35" y="142" fill="#c084fc" font-size="11" font-weight="bold">Layer 5: Session</text>
    <text x="365" y="142" fill="#94a3b8" font-size="10" text-anchor="end">RPC, NetBIOS, Sockets (Dialog)</text>

    <!-- Layer 4 -->
    <rect x="20" y="161" width="360" height="36" fill="#0f172a" stroke="#3b82f6" rx="3"/>
    <text x="35" y="183" fill="#60a5fa" font-size="11" font-weight="bold">Layer 4: Transport</text>
    <text x="365" y="183" fill="#93c5fd" font-size="10" text-anchor="end">TCP / UDP Ports (Segment)</text>

    <!-- Layer 3 -->
    <rect x="20" y="202" width="360" height="36" fill="#0f172a" stroke="#ef4444" rx="3"/>
    <text x="35" y="224" fill="#f87171" font-size="11" font-weight="bold">Layer 3: Network</text>
    <text x="365" y="224" fill="#fca5a5" font-size="10" text-anchor="end">IP Addressing, Routers (Packet)</text>

    <!-- Layer 2 -->
    <rect x="20" y="243" width="360" height="36" fill="#0f172a" stroke="#10b981" rx="3"/>
    <text x="35" y="265" fill="#34d399" font-size="11" font-weight="bold">Layer 2: Data Link</text>
    <text x="365" y="265" fill="#86efac" font-size="10" text-anchor="end">MAC Addr, Switches (Frame)</text>

    <!-- Layer 1 -->
    <rect x="20" y="284" width="360" height="36" fill="#0f172a" stroke="#d9a74a" rx="3"/>
    <text x="35" y="306" fill="#fde047" font-size="11" font-weight="bold">Layer 1: Physical</text>
    <text x="365" y="306" fill="#fef08a" font-size="10" text-anchor="end">Cables, Radio, Bits (1s &amp; 0s)</text>
  </g>

  <!-- Right: Encapsulation Flow -->
  <g transform="translate(460, 95)">
    <rect width="350" height="340" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="175" y="24" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Data Encapsulation Flow (Downward)</text>

    <!-- Payload -->
    <rect x="25" y="45" width="300" height="35" fill="#0f172a" stroke="#a855f7" rx="3"/>
    <text x="175" y="67" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle">Application Data Payload</text>

    <!-- Transport Segment -->
    <rect x="25" y="100" width="300" height="40" fill="#0f172a" stroke="#3b82f6" rx="3"/>
    <rect x="30" y="105" width="90" height="30" fill="#1e3a8a" rx="2"/>
    <text x="75" y="124" fill="#93c5fd" font-size="10" font-weight="bold" text-anchor="middle">TCP/UDP Hdr</text>
    <text x="215" y="124" fill="#c084fc" font-size="10" text-anchor="middle">Data Segment</text>

    <!-- Network Packet -->
    <rect x="25" y="160" width="300" height="40" fill="#0f172a" stroke="#ef4444" rx="3"/>
    <rect x="30" y="165" width="65" height="30" fill="#7f1d1d" rx="2"/>
    <text x="62" y="184" fill="#fca5a5" font-size="9" font-weight="bold" text-anchor="middle">IP Header</text>
    <rect x="100" y="165" width="70" height="30" fill="#1e3a8a" rx="2"/>
    <text x="135" y="184" fill="#93c5fd" font-size="9" text-anchor="middle">TCP Hdr</text>
    <text x="240" y="184" fill="#c084fc" font-size="10" text-anchor="middle">IP Packet</text>

    <!-- Data Link Frame -->
    <rect x="25" y="220" width="300" height="40" fill="#0f172a" stroke="#10b981" rx="3"/>
    <rect x="30" y="225" width="60" height="30" fill="#064e3b" rx="2"/>
    <text x="60" y="244" fill="#86efac" font-size="9" font-weight="bold" text-anchor="middle">Frame Hdr</text>
    <rect x="95" y="225" width="55" height="30" fill="#7f1d1d" rx="2"/>
    <text x="122" y="244" fill="#fca5a5" font-size="8" text-anchor="middle">IP Hdr</text>
    <rect x="155" y="225" width="55" height="30" fill="#1e3a8a" rx="2"/>
    <text x="182" y="244" fill="#93c5fd" font-size="8" text-anchor="middle">TCP Hdr</text>
    <rect x="265" y="225" width="55" height="30" fill="#064e3b" rx="2"/>
    <text x="292" y="244" fill="#86efac" font-size="8" font-weight="bold" text-anchor="middle">FCS Trail</text>

    <!-- Physical Bits -->
    <rect x="25" y="280" width="300" height="35" fill="#0f172a" stroke="#d9a74a" rx="3"/>
    <text x="175" y="302" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">01101001 01101110 01110100 (Physical Bits on Wire)</text>
  </g>

  <!-- Footer Banner -->
  <rect x="40" y="445" width="770" height="32" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="466" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ Mnemonic: All People Seem To Need Data Processing | PDUs: Don't Some People Fear Birthdays (Data, Segment, Packet, Frame, Bit)</text>
</svg>
</div>'''

# 2. Module 02: TCP 3-Way Handshake & Connection Teardown
M02_SVG = '''<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-3321 NETWORK ADMINISTRATION</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">TCP Reliable Connection Architecture: 3-Way Handshake &amp; 4-Step Teardown</text>

  <!-- Left: 3-Way Handshake -->
  <g transform="translate(40, 95)">
    <rect width="380" height="330" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
    <text x="190" y="24" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">TCP 3-Way Handshake (Establishment)</text>

    <!-- Client & Server Columns -->
    <rect x="30" y="45" width="80" height="30" fill="#0f172a" stroke="#cbd5e1" rx="4"/><text x="70" y="65" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">CLIENT</text>
    <rect x="270" y="45" width="80" height="30" fill="#0f172a" stroke="#cbd5e1" rx="4"/><text x="310" y="65" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">SERVER</text>

    <line x1="70" y1="80" x2="70" y2="280" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4"/>
    <line x1="310" y1="80" x2="310" y2="280" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4"/>

    <!-- Step 1 SYN -->
    <line x1="70" y1="110" x2="305" y2="140" stroke="#38bdf8" stroke-width="2.5"/>
    <polygon points="310,140 298,133 300,145" fill="#38bdf8"/>
    <rect x="120" y="105" width="140" height="24" fill="#0f172a" rx="3"/>
    <text x="190" y="121" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">1. SYN (Seq = x)</text>

    <!-- Step 2 SYN-ACK -->
    <line x1="310" y1="165" x2="75" y2="195" stroke="#10b981" stroke-width="2.5"/>
    <polygon points="70,195 82,188 80,200" fill="#10b981"/>
    <rect x="100" y="160" width="180" height="24" fill="#0f172a" rx="3"/>
    <text x="190" y="176" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">2. SYN-ACK (Seq=y, Ack=x+1)</text>

    <!-- Step 3 ACK -->
    <line x1="70" y1="220" x2="305" y2="250" stroke="#d9a74a" stroke-width="2.5"/>
    <polygon points="310,250 298,243 300,255" fill="#d9a74a"/>
    <rect x="120" y="215" width="140" height="24" fill="#0f172a" rx="3"/>
    <text x="190" y="231" fill="#d9a74a" font-size="10" font-weight="bold" text-anchor="middle">3. ACK (Seq=x+1, Ack=y+1)</text>

    <rect x="30" y="285" width="320" height="25" fill="#059669" rx="3"/>
    <text x="190" y="302" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">STATUS: ESTABLISHED (Bidirectional Stream)</text>
  </g>

  <!-- Right: 4-Step Teardown -->
  <g transform="translate(440, 95)">
    <rect width="370" height="330" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" rx="6"/>
    <text x="185" y="24" fill="#f59e0b" font-size="13" font-weight="bold" text-anchor="middle">TCP 4-Step Connection Termination</text>

    <rect x="30" y="45" width="80" height="30" fill="#0f172a" stroke="#cbd5e1" rx="4"/><text x="70" y="65" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">CLIENT</text>
    <rect x="260" y="45" width="80" height="30" fill="#0f172a" stroke="#cbd5e1" rx="4"/><text x="300" y="65" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">SERVER</text>

    <line x1="70" y1="80" x2="70" y2="280" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4"/>
    <line x1="300" y1="80" x2="300" y2="280" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4"/>

    <!-- Step 1 FIN -->
    <line x1="70" y1="105" x2="295" y2="130" stroke="#ef4444" stroke-width="2"/>
    <polygon points="300,130 288,124 290,135" fill="#ef4444"/>
    <text x="185" y="115" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">1. FIN (Client Closes)</text>

    <!-- Step 2 ACK -->
    <line x1="300" y1="145" x2="75" y2="170" stroke="#cbd5e1" stroke-width="2"/>
    <polygon points="70,170 82,164 80,175" fill="#cbd5e1"/>
    <text x="185" y="155" fill="#cbd5e1" font-size="10" text-anchor="middle">2. ACK (Server Confirms)</text>

    <!-- Step 3 FIN -->
    <line x1="300" y1="190" x2="75" y2="215" stroke="#ef4444" stroke-width="2"/>
    <polygon points="70,215 82,209 80,220" fill="#ef4444"/>
    <text x="185" y="200" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">3. FIN (Server Closes)</text>

    <!-- Step 4 ACK -->
    <line x1="70" y1="235" x2="295" y2="260" stroke="#cbd5e1" stroke-width="2"/>
    <polygon points="300,260 288,254 290,265" fill="#cbd5e1"/>
    <text x="185" y="245" fill="#cbd5e1" font-size="10" text-anchor="middle">4. ACK (Client Confirms)</text>

    <rect x="25" y="285" width="320" height="25" fill="#b91c1c" rx="3"/>
    <text x="185" y="302" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">STATUS: CLOSED (TIME_WAIT Expired)</text>
  </g>

  <!-- Footer Banner -->
  <rect x="40" y="435" width="770" height="35" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="457" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ Network+ Rule: UDP has NO handshake, no sequence numbers, and no delivery acknowledgments.</text>
</svg>
</div>'''

# 3. Module 03: IPv4 Subnetting & RFC 1918 Private Ranges
M03_SVG = '''<div style="text-align: center; margin: 24px 0;">
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
</div>'''

# 4. Module 06: Wireless 802.11 Standards & Non-Overlapping Channels
M06_SVG = '''<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-3321 NETWORK ADMINISTRATION</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">Wi-Fi Generations (802.11) &amp; 2.4 GHz vs. 5 GHz Channel Spectrum</text>

  <!-- 2.4 GHz Channels Spectrum -->
  <g transform="translate(40, 95)">
    <rect width="770" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
    <text x="385" y="24" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">2.4 GHz Spectrum: Only 3 Non-Overlapping 20 MHz Channels (1, 6, 11)</text>

    <!-- Channel 1 -->
    <path d="M 60 120 Q 140 45 220 120 Z" fill="rgba(16, 185, 129, 0.3)" stroke="#10b981" stroke-width="2"/>
    <text x="140" y="80" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Channel 1</text>
    <text x="140" y="100" fill="#cbd5e1" font-size="10" text-anchor="middle">2412 MHz</text>

    <!-- Channel 6 -->
    <path d="M 300 120 Q 380 45 460 120 Z" fill="rgba(16, 185, 129, 0.3)" stroke="#10b981" stroke-width="2"/>
    <text x="380" y="80" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Channel 6</text>
    <text x="380" y="100" fill="#cbd5e1" font-size="10" text-anchor="middle">2437 MHz</text>

    <!-- Channel 11 -->
    <path d="M 540 120 Q 620 45 700 120 Z" fill="rgba(16, 185, 129, 0.3)" stroke="#10b981" stroke-width="2"/>
    <text x="620" y="80" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Channel 11</text>
    <text x="620" y="100" fill="#cbd5e1" font-size="10" text-anchor="middle">2462 MHz</text>

    <text x="385" y="140" fill="#fca5a5" font-size="10" text-anchor="middle">Channels 2, 3, 4, 5, 7, 8, 9, 10 overlap and cause severe Co-Channel Interference (CCI)!</text>
  </g>

  <!-- 802.11 Generations Matrix -->
  <g transform="translate(40, 260)">
    <rect width="770" height="160" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="385" y="24" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Wi-Fi Standards Evolution &amp; Maximum Data Rates</text>

    <g transform="translate(25, 40)">
      <!-- Row 1 -->
      <rect x="0" y="0" width="230" height="50" fill="#0f172a" rx="3"/>
      <text x="15" y="20" fill="#38bdf8" font-size="11" font-weight="bold">802.11n (Wi-Fi 4)</text>
      <text x="15" y="38" fill="#94a3b8" font-size="10">2.4 / 5 GHz • Up to 600 Mbps • MIMO</text>

      <!-- Row 2 -->
      <rect x="245" y="0" width="230" height="50" fill="#0f172a" rx="3"/>
      <text x="260" y="20" fill="#10b981" font-size="11" font-weight="bold">802.11ac (Wi-Fi 5)</text>
      <text x="260" y="38" fill="#94a3b8" font-size="10">5 GHz Only • Up to 3.5 Gbps • MU-MIMO</text>

      <!-- Row 3 -->
      <rect x="490" y="0" width="230" height="50" fill="#0f172a" rx="3"/>
      <text x="505" y="20" fill="#d9a74a" font-size="11" font-weight="bold">802.11ax (Wi-Fi 6 / 6E)</text>
      <text x="505" y="38" fill="#94a3b8" font-size="10">2.4 / 5 / 6 GHz • 9.6 Gbps • OFDMA</text>

      <!-- Comparison Summary -->
      <rect x="0" y="60" width="720" height="45" fill="#0f172a" rx="3"/>
      <text x="15" y="80" fill="#cbd5e1" font-size="10"><b>2.4 GHz Band:</b> Greater physical range, superior wall penetration, high congestion from microwaves/Bluetooth.</text>
      <text x="15" y="96" fill="#38bdf8" font-size="10"><b>5.0 GHz Band:</b> Shorter range, reduced wall penetration, vastly larger channel count (24+ non-overlapping 20 MHz channels).</text>
    </g>
  </g>

  <!-- Footer Banner -->
  <rect x="40" y="430" width="770" height="35" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="452" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ Security Standard: WPA3 uses SAE (Simultaneous Authentication of Equals) to defeat offline dictionary attacks.</text>
</svg>
</div>'''

# 5. Module 09: DNS Hierarchy & DHCP DORA Process
M09_SVG = '''<div style="text-align: center; margin: 24px 0;">
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
</div>'''

NET_MODULE_MAP = {
    "Module_01": M01_SVG,
    "Module_02": M02_SVG,
    "Module_03": M03_SVG,
    "Module_06": M06_SVG,
    "Module_09": M09_SVG,
}

def inject_networking():
    print("Beginning systematic SVG injection across CIS-3321 Network Administration...")
    for mod_name, svg_content in NET_MODULE_MAP.items():
        mod_dir = os.path.join(BASE_DIR, mod_name)
        if not os.path.exists(mod_dir):
            continue
        
        # Video Scripts
        vs_files = [f for f in os.listdir(mod_dir) if f.startswith("01_Video_Script")]
        for vs_file in vs_files:
            vs_path = os.path.join(mod_dir, vs_file)
            with open(vs_path, "r", encoding="utf-8") as f:
                content = f.read()
            if "<svg" not in content:
                m = re.search(r'(\[SHOW DIAGRAM:[^\]]+\])', content)
                if m:
                    cue = m.group(1)
                    new_content = content.replace(cue, f"{svg_content}\n\n{cue}", 1)
                    with open(vs_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"  ✓ Injected SVG into Video Script: {mod_name}/{vs_file}")
            else:
                print(f"  - Video script already has SVG: {mod_name}/{vs_file}")

        # Reading Guides
        rg_files = [f for f in os.listdir(mod_dir) if "Reading_Guide" in f]
        for rg_file in rg_files:
            rg_path = os.path.join(mod_dir, rg_file)
            with open(rg_path, "r", encoding="utf-8") as f:
                rg_content = f.read()
            if "TEXAS WESLEYAN UNIVERSITY • CIS-3321 NETWORK ADMINISTRATION" not in rg_content:
                if "## 1." in rg_content:
                    parts = rg_content.split("## 1.", 1)
                    new_rg = parts[0] + f"{svg_content}\n\n## 1." + parts[1]
                elif "### 1." in rg_content:
                    parts = rg_content.split("### 1.", 1)
                    new_rg = parts[0] + f"{svg_content}\n\n### 1." + parts[1]
                else:
                    if "<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->" in rg_content:
                        parts = rg_content.split("<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->", 1)
                        new_rg = parts[0] + "<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->\n\n" + svg_content + parts[1]
                    else:
                        new_rg = svg_content + "\n\n" + rg_content
                with open(rg_path, "w", encoding="utf-8") as f:
                    f.write(new_rg)
                print(f"  ✓ Injected SVG into Reading Guide: {mod_name}/{rg_file}")
            else:
                print(f"  - Reading guide already has SVG: {mod_name}/{rg_file}")

if __name__ == "__main__":
    inject_networking()
