# -*- coding: utf-8 -*-
"""
Canvas-Native Visual Architecture Diagrams
Built using HTML/CSS (tables, color-coded cards, badges, gradients, and matrices)
100% compatible with Canvas LMS HTML sanitizer — NEVER stripped, renders on all devices.
"""

def get_native_visual(topic: str, mod_num: int) -> str:
    t = topic.lower()

    # 1. OSI 7-Layer Architecture
    if any(k in t for k in ['osi', 'fundamentals', 'networking fund']):
        return '''<div style="background:#ffffff;border:2px solid #8b0000;border-radius:10px;padding:20px;margin:24px 0;box-shadow:0 4px 12px rgba(139,0,0,0.08);">
  <div style="text-align:center;font-size:17px;font-weight:bold;color:#8b0000;margin-bottom:6px;">📊 OSI 7-Layer Reference Model Architecture &amp; Data Encapsulation</div>
  <div style="text-align:center;font-size:12.5px;color:#666;margin-bottom:16px;">Standard: ISO/IEC 7498-1 · PDU Flow: Application Data ↓ Segments ↓ Packets ↓ Frames ↓ Bits</div>
  <div style="overflow-x:auto;">
    <table style="width:100%;border-collapse:collapse;font-family:Arial,sans-serif;font-size:13px;">
      <thead>
        <tr style="background:#8b0000;color:#ffffff;text-align:left;">
          <th style="padding:10px 12px;border:1px solid #700000;">Layer</th>
          <th style="padding:10px 12px;border:1px solid #700000;">Layer Name</th>
          <th style="padding:10px 12px;border:1px solid #700000;">Protocol Data Unit (PDU)</th>
          <th style="padding:10px 12px;border:1px solid #700000;">Key Protocols &amp; Standards</th>
          <th style="padding:10px 12px;border:1px solid #700000;">Hardware / Addressing</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background:#fff5f5;"><td style="padding:9px 12px;border:1px solid #ddd;font-weight:bold;color:#8b0000;">Layer 7</td><td style="padding:9px 12px;border:1px solid #ddd;font-weight:bold;">Application</td><td style="padding:9px 12px;border:1px solid #ddd;">Data / Payload</td><td style="padding:9px 12px;border:1px solid #ddd;">HTTP/HTTPS, DNS, SSH, DHCP, SMTP, FTP</td><td style="padding:9px 12px;border:1px solid #ddd;">End-user software, APIs, Web Browsers</td></tr>
        <tr style="background:#ffffff;"><td style="padding:9px 12px;border:1px solid #ddd;font-weight:bold;color:#a00000;">Layer 6</td><td style="padding:9px 12px;border:1px solid #ddd;font-weight:bold;">Presentation</td><td style="padding:9px 12px;border:1px solid #ddd;">Formatted Data</td><td style="padding:9px 12px;border:1px solid #ddd;">TLS/SSL Encryption, ASCII, JPEG, MPEG, GIF</td><td style="padding:9px 12px;border:1px solid #ddd;">Data compression, Encryption engines</td></tr>
        <tr style="background:#fff5f5;"><td style="padding:9px 12px;border:1px solid #ddd;font-weight:bold;color:#b22222;">Layer 5</td><td style="padding:9px 12px;border:1px solid #ddd;font-weight:bold;">Session</td><td style="padding:9px 12px;border:1px solid #ddd;">Session Data</td><td style="padding:9px 12px;border:1px solid #ddd;">NetBIOS, RPC, Sockets, SQL Sessions</td><td style="padding:9px 12px;border:1px solid #ddd;">Session setup, sync check-pointing</td></tr>
        <tr style="background:#fef9e7;"><td style="padding:9px 12px;border:1px solid #ddd;font-weight:bold;color:#d4780a;">Layer 4</td><td style="padding:9px 12px;border:1px solid #ddd;font-weight:bold;">Transport</td><td style="padding:9px 12px;border:1px solid #ddd;">Segment (TCP) / Datagram (UDP)</td><td style="padding:9px 12px;border:1px solid #ddd;">TCP (Reliable, Handshake), UDP (Fast, Stream)</td><td style="padding:9px 12px;border:1px solid #ddd;"><strong>Port Numbers</strong> (0–65535), Flow Control</td></tr>
        <tr style="background:#eaf2f8;"><td style="padding:9px 12px;border:1px solid #ddd;font-weight:bold;color:#2a7ab5;">Layer 3</td><td style="padding:9px 12px;border:1px solid #ddd;font-weight:bold;">Network</td><td style="padding:9px 12px;border:1px solid #ddd;">Packet</td><td style="padding:9px 12px;border:1px solid #ddd;">IPv4, IPv6, ICMP, OSPF, BGP, EIGRP, IPsec</td><td style="padding:9px 12px;border:1px solid #ddd;"><strong>Routers, Layer 3 Switches</strong> (Logical IP)</td></tr>
        <tr style="background:#eaf2f8;"><td style="padding:9px 12px;border:1px solid #ddd;font-weight:bold;color:#1a5a8a;">Layer 2</td><td style="padding:9px 12px;border:1px solid #ddd;font-weight:bold;">Data Link</td><td style="padding:9px 12px;border:1px solid #ddd;">Frame</td><td style="padding:9px 12px;border:1px solid #ddd;">Ethernet (802.3), Wi-Fi (802.11), PPP, ARP</td><td style="padding:9px 12px;border:1px solid #ddd;"><strong>Switches, Bridges, NICs</strong> (48-bit MAC)</td></tr>
        <tr style="background:#f4f6f7;"><td style="padding:9px 12px;border:1px solid #ddd;font-weight:bold;color:#555555;">Layer 1</td><td style="padding:9px 12px;border:1px solid #ddd;font-weight:bold;">Physical</td><td style="padding:9px 12px;border:1px solid #ddd;">Bits (0s &amp; 1s)</td><td style="padding:9px 12px;border:1px solid #ddd;">1000BASE-T, Cat6a, Single-mode/Multi-mode Fiber</td><td style="padding:9px 12px;border:1px solid #ddd;"><strong>Cables, Hubs, Transceivers (SFP+)</strong></td></tr>
      </tbody>
    </table>
  </div>
  <div style="margin-top:14px;background:#eef7fc;border-left:4px solid #2a7ab5;padding:10px 14px;font-size:12px;color:#1a5a8a;">
    💡 <strong>Troubleshooting Rule of Thumb:</strong> When diagnosing network outages, adopt a <em>Bottom-Up approach</em> (Physical link light → Data Link MAC table → Network IP routing → Transport Port connectivity).
  </div>
</div>'''

    # 2. TCP/IP Protocol Architecture
    elif any(k in t for k in ['tcp/ip', 'tcp ip', 'protocol']):
        return '''<div style="background:#ffffff;border:2px solid #8b0000;border-radius:10px;padding:20px;margin:24px 0;box-shadow:0 4px 12px rgba(139,0,0,0.08);">
  <div style="text-align:center;font-size:17px;font-weight:bold;color:#8b0000;margin-bottom:6px;">📊 TCP/IP 4-Layer vs. OSI 7-Layer Architecture Suite</div>
  <div style="text-align:center;font-size:12.5px;color:#666;margin-bottom:16px;">Standard: RFC 1122 · The Operational Protocol Model of the Modern Internet</div>
  <div style="overflow-x:auto;">
    <table style="width:100%;border-collapse:collapse;font-family:Arial,sans-serif;font-size:13px;">
      <thead>
        <tr style="background:#8b0000;color:#ffffff;text-align:left;">
          <th style="padding:10px 12px;border:1px solid #700000;">TCP/IP Layer</th>
          <th style="padding:10px 12px;border:1px solid #700000;">Corresponding OSI Layers</th>
          <th style="padding:10px 12px;border:1px solid #700000;">Primary Responsibilities</th>
          <th style="padding:10px 12px;border:1px solid #700000;">Representative Protocols</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background:#fff5f5;"><td style="padding:10px 12px;border:1px solid #ddd;font-weight:bold;color:#8b0000;">1. Application</td><td style="padding:10px 12px;border:1px solid #ddd;">Application (7), Presentation (6), Session (5)</td><td style="padding:10px 12px;border:1px solid #ddd;">User interfaces, data serialization, encryption, formatting</td><td style="padding:10px 12px;border:1px solid #ddd;">HTTP (80), HTTPS (443), DNS (53), SSH (22), DHCP (67/68)</td></tr>
        <tr style="background:#fef9e7;"><td style="padding:10px 12px;border:1px solid #ddd;font-weight:bold;color:#d4780a;">2. Transport</td><td style="padding:10px 12px;border:1px solid #ddd;">Transport (4)</td><td style="padding:10px 12px;border:1px solid #ddd;">Host-to-host communications, reliability, segmentation, port addressing</td><td style="padding:10px 12px;border:1px solid #ddd;">TCP (3-Way Handshake, Windowing, ACK) &amp; UDP (Connectionless)</td></tr>
        <tr style="background:#eaf2f8;"><td style="padding:10px 12px;border:1px solid #ddd;font-weight:bold;color:#2a7ab5;">3. Internet</td><td style="padding:10px 12px;border:1px solid #ddd;">Network (3)</td><td style="padding:10px 12px;border:1px solid #ddd;">Logical packet addressing, routing decisions across internetworks</td><td style="padding:10px 12px;border:1px solid #ddd;">IPv4 (RFC 791), IPv6 (RFC 8200), ICMP (Ping), ARP, IGMP</td></tr>
        <tr style="background:#f4f6f7;"><td style="padding:10px 12px;border:1px solid #ddd;font-weight:bold;color:#555555;">4. Network Access</td><td style="padding:10px 12px;border:1px solid #ddd;">Data Link (2) &amp; Physical (1)</td><td style="padding:10px 12px;border:1px solid #ddd;">Physical transmission of bits onto copper/fiber/radio, framing, MAC filtering</td><td style="padding:10px 12px;border:1px solid #ddd;">IEEE 802.3 Ethernet, IEEE 802.11 Wi-Fi, DOCSIS, LTE, 5G</td></tr>
      </tbody>
    </table>
  </div>
</div>'''

    # 3. IPv4 Subnetting & CIDR Chart
    elif any(k in t for k in ['ipv4', 'subnetting', 'cidr', 'addressing: ipv4']):
        return '''<div style="background:#ffffff;border:2px solid #8b0000;border-radius:10px;padding:20px;margin:24px 0;box-shadow:0 4px 12px rgba(139,0,0,0.08);">
  <div style="text-align:center;font-size:17px;font-weight:bold;color:#8b0000;margin-bottom:6px;">📊 Classless Inter-Domain Routing (CIDR) &amp; Subnet Reference Matrix</div>
  <div style="text-align:center;font-size:12.5px;color:#666;margin-bottom:16px;">Formula: Total Addresses = 2^(32 - Prefix) · Usable Hosts = 2^(32 - Prefix) - 2</div>
  <div style="overflow-x:auto;">
    <table style="width:100%;border-collapse:collapse;font-family:Consolas,Arial,sans-serif;font-size:13px;">
      <thead>
        <tr style="background:#8b0000;color:#ffffff;text-align:left;">
          <th style="padding:9px 12px;border:1px solid #700000;">CIDR Prefix</th>
          <th style="padding:9px 12px;border:1px solid #700000;">Dotted Decimal Subnet Mask</th>
          <th style="padding:9px 12px;border:1px solid #700000;">Wildcard Mask</th>
          <th style="padding:9px 12px;border:1px solid #700000;">Total IP Addresses</th>
          <th style="padding:9px 12px;border:1px solid #700000;">Usable Host Addresses</th>
          <th style="padding:9px 12px;border:1px solid #700000;">Common Enterprise Use Case</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background:#ffffff;"><td style="padding:8px 12px;border:1px solid #ddd;font-weight:bold;color:#8b0000;">/24</td><td style="padding:8px 12px;border:1px solid #ddd;">255.255.255.0</td><td style="padding:8px 12px;border:1px solid #ddd;">0.0.0.255</td><td style="padding:8px 12px;border:1px solid #ddd;">256</td><td style="padding:8px 12px;border:1px solid #ddd;font-weight:bold;">254</td><td style="padding:8px 12px;border:1px solid #ddd;">Standard Office LAN / Department VLAN</td></tr>
        <tr style="background:#f9f9f9;"><td style="padding:8px 12px;border:1px solid #ddd;font-weight:bold;color:#8b0000;">/25</td><td style="padding:8px 12px;border:1px solid #ddd;">255.255.255.128</td><td style="padding:8px 12px;border:1px solid #ddd;">0.0.0.127</td><td style="padding:8px 12px;border:1px solid #ddd;">128</td><td style="padding:8px 12px;border:1px solid #ddd;font-weight:bold;">126</td><td style="padding:8px 12px;border:1px solid #ddd;">Split Floor Subnet / Half-C block</td></tr>
        <tr style="background:#ffffff;"><td style="padding:8px 12px;border:1px solid #ddd;font-weight:bold;color:#8b0000;">/26</td><td style="padding:8px 12px;border:1px solid #ddd;">255.255.255.192</td><td style="padding:8px 12px;border:1px solid #ddd;">0.0.0.63</td><td style="padding:8px 12px;border:1px solid #ddd;">64</td><td style="padding:8px 12px;border:1px solid #ddd;font-weight:bold;">62</td><td style="padding:8px 12px;border:1px solid #ddd;">Medium Branch Office / IT Server Farm</td></tr>
        <tr style="background:#f9f9f9;"><td style="padding:8px 12px;border:1px solid #ddd;font-weight:bold;color:#8b0000;">/27</td><td style="padding:8px 12px;border:1px solid #ddd;">255.255.255.224</td><td style="padding:8px 12px;border:1px solid #ddd;">0.0.0.31</td><td style="padding:8px 12px;border:1px solid #ddd;">32</td><td style="padding:8px 12px;border:1px solid #ddd;font-weight:bold;">30</td><td style="padding:8px 12px;border:1px solid #ddd;">Small Branch / Management VLAN</td></tr>
        <tr style="background:#ffffff;"><td style="padding:8px 12px;border:1px solid #ddd;font-weight:bold;color:#8b0000;">/28</td><td style="padding:8px 12px;border:1px solid #ddd;">255.255.255.240</td><td style="padding:8px 12px;border:1px solid #ddd;">0.0.0.15</td><td style="padding:8px 12px;border:1px solid #ddd;">16</td><td style="padding:8px 12px;border:1px solid #ddd;font-weight:bold;">14</td><td style="padding:8px 12px;border:1px solid #ddd;">DMZ Bastion Subnet / Public Web VIPs</td></tr>
        <tr style="background:#f9f9f9;"><td style="padding:8px 12px;border:1px solid #ddd;font-weight:bold;color:#8b0000;">/29</td><td style="padding:8px 12px;border:1px solid #ddd;">255.255.255.248</td><td style="padding:8px 12px;border:1px solid #ddd;">0.0.0.7</td><td style="padding:8px 12px;border:1px solid #ddd;">8</td><td style="padding:8px 12px;border:1px solid #ddd;font-weight:bold;">6</td><td style="padding:8px 12px;border:1px solid #ddd;">HSRP/VRRP Gateway Failover Cluster</td></tr>
        <tr style="background:#fff3cd;"><td style="padding:8px 12px;border:1px solid #ddd;font-weight:bold;color:#856404;">/30</td><td style="padding:8px 12px;border:1px solid #ddd;">255.255.255.252</td><td style="padding:8px 12px;border:1px solid #ddd;">0.0.0.3</td><td style="padding:8px 12px;border:1px solid #ddd;">4</td><td style="padding:8px 12px;border:1px solid #ddd;font-weight:bold;">2</td><td style="padding:8px 12px;border:1px solid #ddd;"><strong>Point-to-Point WAN Serial/Ethernet Link</strong></td></tr>
        <tr style="background:#d1ecf1;"><td style="padding:8px 12px;border:1px solid #ddd;font-weight:bold;color:#0c5460;">/32</td><td style="padding:8px 12px;border:1px solid #ddd;">255.255.255.255</td><td style="padding:8px 12px;border:1px solid #ddd;">0.0.0.0</td><td style="padding:8px 12px;border:1px solid #ddd;">1</td><td style="padding:8px 12px;border:1px solid #ddd;font-weight:bold;">1 (Host)</td><td style="padding:8px 12px;border:1px solid #ddd;"><strong>Router Loopback Interface (OSPF/BGP Router ID)</strong></td></tr>
      </tbody>
    </table>
  </div>
</div>'''

    # 4. Security CIA Triad & AAA
    elif any(k in t for k in ['security', 'threat', 'vulnerab', 'cia', 'infosec', 'risk', 'incident', 'forensic']):
        return '''<div style="background:#ffffff;border:2px solid #8b0000;border-radius:10px;padding:20px;margin:24px 0;box-shadow:0 4px 12px rgba(139,0,0,0.08);">
  <div style="text-align:center;font-size:17px;font-weight:bold;color:#8b0000;margin-bottom:6px;">📊 Information Security Core Framework: The CIA Triad &amp; Defense-in-Depth</div>
  <div style="text-align:center;font-size:12.5px;color:#666;margin-bottom:16px;">Standard: NIST SP 800-53 / ISO/IEC 27001 · Enterprise Information Assurance Architecture</div>
  
  <div style="display:flex;flex-wrap:wrap;gap:12px;margin-bottom:16px;">
    <div style="flex:1;min-width:200px;background:#fff5f5;border:2px solid #b22222;border-radius:8px;padding:14px;">
      <div style="font-weight:bold;color:#b22222;font-size:14px;margin-bottom:6px;">🔐 CONFIDENTIALITY</div>
      <div style="font-size:12px;color:#333;margin-bottom:8px;">Only authorized entities may access protected sensitive data.</div>
      <div style="font-size:11.5px;color:#555;"><strong>Controls:</strong> AES-256 Encryption, TLS 1.3, RBAC, Data Loss Prevention (DLP), Multi-Factor Authentication.</div>
    </div>
    <div style="flex:1;min-width:200px;background:#eef7fc;border:2px solid #2a7ab5;border-radius:8px;padding:14px;">
      <div style="font-weight:bold;color:#2a7ab5;font-size:14px;margin-bottom:6px;">✅ INTEGRITY</div>
      <div style="font-size:12px;color:#333;margin-bottom:8px;">Data remains complete, authentic, and protected against unauthorized tampering.</div>
      <div style="font-size:11.5px;color:#555;"><strong>Controls:</strong> SHA-256/SHA-3 Hashing, Digital Signatures, HMAC, File Integrity Monitoring (FIM).</div>
    </div>
    <div style="flex:1;min-width:200px;background:#fef8e7;border:2px solid #d4780a;border-radius:8px;padding:14px;">
      <div style="font-weight:bold;color:#d4780a;font-size:14px;margin-bottom:6px;">⚡ AVAILABILITY</div>
      <div style="font-size:12px;color:#333;margin-bottom:8px;">Authorized users have prompt, uninterrupted access to systems and services.</div>
      <div style="font-size:11.5px;color:#555;"><strong>Controls:</strong> RAID Arrays, HSRP/VRRP Failover, DDoS Mitigation (Cloudflare), Redundant Power, Geo-Backups.</div>
    </div>
  </div>

  <div style="background:#f8f9fa;border:1px solid #ddd;border-radius:6px;padding:12px 16px;font-size:12px;">
    <strong>AAA Access Control Model:</strong> 
    <span style="color:#b22222;font-weight:bold;">Authentication</span> (Who are you? → Passwords, PKI, Biometrics) | 
    <span style="color:#d4780a;font-weight:bold;">Authorization</span> (What can you do? → ACLs, Privileges) | 
    <span style="color:#2a7ab5;font-weight:bold;">Accounting</span> (What did you do? → Syslog, TACACS+ Audit Trails).
  </div>
</div>'''

    # Default: 3-Tier Enterprise Cycle
    else:
        return f'''<div style="background:#ffffff;border:2px solid #8b0000;border-radius:10px;padding:20px;margin:24px 0;box-shadow:0 4px 12px rgba(139,0,0,0.08);">
  <div style="text-align:center;font-size:16px;font-weight:bold;color:#8b0000;margin-bottom:6px;">📊 Module {mod_num:02d} Technical Architecture &amp; Workflow Overview</div>
  <div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:14px;">
    <div style="flex:1;min-width:180px;background:#fff5f5;border-left:4px solid #8b0000;padding:12px;border-radius:0 6px 6px 0;">
      <div style="font-weight:bold;color:#8b0000;font-size:13px;">1. Theory &amp; Protocols</div>
      <div style="font-size:12px;color:#555;margin-top:4px;">Master standard specifications, packet formats, and operational states.</div>
    </div>
    <div style="flex:1;min-width:180px;background:#fef9e7;border-left:4px solid #d4780a;padding:12px;border-radius:0 6px 6px 0;">
      <div style="font-weight:bold;color:#d4780a;font-size:13px;">2. Applied Laboratory</div>
      <div style="font-size:12px;color:#555;margin-top:4px;">Configure and troubleshoot topologies in Cisco Packet Tracer.</div>
    </div>
    <div style="flex:1;min-width:180px;background:#eef7fc;border-left:4px solid #2a7ab5;padding:12px;border-radius:0 6px 6px 0;">
      <div style="font-weight:bold;color:#2a7ab5;font-size:13px;">3. Evaluation &amp; Mastery</div>
      <div style="font-size:12px;color:#555;margin-top:4px;">Demonstrate comprehension via auto-graded quizzes and threaded peer discussions.</div>
    </div>
  </div>
</div>'''
