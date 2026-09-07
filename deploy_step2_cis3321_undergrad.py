# -*- coding: utf-8 -*-
"""
Step 2: Deploy Network+ & Cisco CCNA Professional Preparation to CIS-3321
1. Publish Cisco IOS CLI & PBQ Exam Simulation Handbook to Module 87931
2. Inject Network+ & CCNA Exam Focus callout blocks into all 16 Reading Guides
"""

import json, time, re, urllib.request
from pathlib import Path
from csc6361_builder_core import md2html
from canvas_native_visuals import get_native_visual

CANVAS_URL = "https://txwes.instructure.com"
TOKEN      = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
CID        = 13089
MID_ORIENT = 87931
BASE_DIR   = Path(__file__).parent / 'completed' / 'CIS-3321_Network_Admin'

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type':  'application/json',
}

def api_call(method: str, path: str, data: dict = None):
    url = f"{CANVAS_URL}/api/v1{path}"
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            res = r.read()
            return json.loads(res) if res else {}
    except urllib.error.HTTPError as e:
        err = e.read()[:300].decode('utf-8', errors='replace')
        print(f"    [{method} ERROR] {path}: {e.code} -> {err}")
        return {}
    except Exception as ex:
        print(f"    [{method} EXCEPTION] {path}: {ex}")
        return {}

def api_get(path): return api_call('GET', path)
def api_post(path, data): return api_call('POST', path, data)
def api_put(path, data): return api_call('PUT', path, data)

def create_or_update_page(cid: int, title: str, html_body: str) -> str:
    url_slug = re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')[:70]
    payload = {
        'wiki_page': {
            'title': title,
            'body': html_body,
            'published': True,
        }
    }
    res = api_put(f"/courses/{cid}/pages/{url_slug}", payload)
    if not res.get('url'):
        res = api_post(f"/courses/{cid}/pages", payload)
    return res.get('url', url_slug)

def add_item_to_module(cid: int, mid: int, title: str, page_url: str, pos: int = 1):
    items = api_get(f"/courses/{cid}/modules/{mid}/items?per_page=50")
    if isinstance(items, list):
        for it in items:
            if it.get('page_url') == page_url or it.get('title') == title:
                print(f"  ℹ Item '{title}' already in module {mid}")
                return it

    payload = {
        'module_item': {
            'title': title,
            'type': 'Page',
            'page_url': page_url,
            'position': pos,
        }
    }
    res = api_post(f"/courses/{cid}/modules/{mid}/items", payload)
    print(f"  ✅ Added '{title}' to Module {mid}")
    time.sleep(0.3)
    return res

def build_cli_pbq_handbook_html():
    return '''<div style="font-family:Arial,sans-serif;max-width:980px;margin:0 auto;padding:10px;line-height:1.7;color:#2c3e50;">

<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(139,0,0,0.15);">
  <div style="font-size:12px;font-weight:bold;text-transform:uppercase;letter-spacing:1px;color:#f5a623;margin-bottom:6px;">
    Texas Wesleyan University · Department of Computer Science &amp; IT
  </div>
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">💻 Cisco IOS CLI &amp; Performance-Based Question (PBQ) Exam Simulation Handbook</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">Mastering Cisco Router/Switch Configuration, Troubleshooting Syntax, &amp; CompTIA PBQs</p>
</div>

<div style="background:#e8f5e9;border-left:5px solid #2e7d32;padding:18px 22px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <h3 style="margin:0 0 8px 0;color:#1b5e20;font-size:16px;font-weight:bold;">🎯 About Performance-Based Questions (PBQs)</h3>
  <p style="margin:0;color:#2e7d32;font-size:14px;">
    On both <strong>CompTIA Network+ (N10-008/009)</strong> and <strong>Cisco CCNA (200-301)</strong>, the highest-weighted questions appear at the beginning as interactive simulations: configuring switch ports, fixing routing table loops, resolving subnet mismatches, and terminating cable pinouts. This handbook equips you with the exact terminal syntax and diagnostic sequences needed to achieve a perfect score.
  </p>
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:30px;">1. Cisco Switch Switching &amp; VLAN Configuration Matrix</h2>

<div style="background:#1e293b;color:#f8fafc;padding:16px 20px;border-radius:8px;font-family:monospace;font-size:13px;line-height:1.6;margin-top:12px;">
<span style="color:#94a3b8;">! PBQ Task 1: Create VLANs and Assign Access Ports</span><br>
Switch(config)# vlan 10<br>
Switch(config-vlan)# name ENGINEERING<br>
Switch(config-vlan)# vlan 20<br>
Switch(config-vlan)# name MARKETING<br>
Switch(config-vlan)# exit<br><br>
Switch(config)# interface range FastEthernet0/1 - 10<br>
Switch(config-if-range)# switchport mode access<br>
Switch(config-if-range)# switchport access vlan 10<br>
Switch(config-if-range)# spanning-tree portfast<br>
Switch(config-if-range)# spanning-tree bpduguard enable<br><br>
<span style="color:#94a3b8;">! PBQ Task 2: Configure 802.1Q Trunk with Native VLAN Security</span><br>
Switch(config)# interface GigabitEthernet0/1<br>
Switch(config-if)# switchport mode trunk<br>
Switch(config-if)# switchport trunk allowed vlan 10,20,99<br>
Switch(config-if)# switchport trunk native vlan 99<br>
Switch(config-if)# switchport nonegotiate
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">2. Inter-VLAN Routing (Router-on-a-Stick) Configuration</h2>

<div style="background:#1e293b;color:#f8fafc;padding:16px 20px;border-radius:8px;font-family:monospace;font-size:13px;line-height:1.6;margin-top:12px;">
<span style="color:#94a3b8;">! Configure Subinterfaces on Router for Inter-VLAN Routing</span><br>
Router(config)# interface GigabitEthernet0/0<br>
Router(config-if)# no shutdown<br><br>
Router(config)# interface GigabitEthernet0/0.10<br>
Router(config-subif)# encapsulation dot1Q 10<br>
Router(config-subif)# ip address 192.168.10.1 255.255.255.0<br><br>
Router(config)# interface GigabitEthernet0/0.20<br>
Router(config-subif)# encapsulation dot1Q 20<br>
Router(config-subif)# ip address 192.168.20.1 255.255.255.0
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">3. CompTIA 7-Step Troubleshooting Model Applied to PBQs</h2>

<table style="width:100%;border-collapse:collapse;margin-top:16px;font-size:13.5px;">
  <thead>
    <tr style="background:#8b0000;color:white;text-align:left;">
      <th style="padding:10px;border:1px solid #700000;">Step #</th>
      <th style="padding:10px;border:1px solid #700000;">Official CompTIA Step</th>
      <th style="padding:10px;border:1px solid #700000;">Terminal Commands &amp; Practical Action</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:8px 10px;border:1px solid #cbd5e1;font-weight:bold;">1</td><td style="padding:8px 10px;border:1px solid #cbd5e1;">Identify the problem</td><td style="padding:8px 10px;border:1px solid #cbd5e1;">Gather user info, determine scope, review logs (syslog, Event Viewer).</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:8px 10px;border:1px solid #cbd5e1;font-weight:bold;">2</td><td style="padding:8px 10px;border:1px solid #cbd5e1;">Establish a theory of probable cause</td><td style="padding:8px 10px;border:1px solid #cbd5e1;">Question the obvious: link lights, cable seated, APIPA address (169.254.x.x)?</td></tr>
    <tr><td style="padding:8px 10px;border:1px solid #cbd5e1;font-weight:bold;">3</td><td style="padding:8px 10px;border:1px solid #cbd5e1;">Test the theory to determine cause</td><td style="padding:8px 10px;border:1px solid #cbd5e1;"><code>ping 127.0.0.1</code> (NIC), <code>ping Gateway</code> (LAN), <code>nslookup</code> (DNS).</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:8px 10px;border:1px solid #cbd5e1;font-weight:bold;">4</td><td style="padding:8px 10px;border:1px solid #cbd5e1;">Establish a plan of action &amp; identify effects</td><td style="padding:8px 10px;border:1px solid #cbd5e1;">Formulate fix, assess business downtime risk, schedule change window.</td></tr>
    <tr><td style="padding:8px 10px;border:1px solid #cbd5e1;font-weight:bold;">5</td><td style="padding:8px 10px;border:1px solid #cbd5e1;">Implement the solution or escalate</td><td style="padding:8px 10px;border:1px solid #cbd5e1;">Apply configuration changes or replace faulty transceiver/patch cable.</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:8px 10px;border:1px solid #cbd5e1;font-weight:bold;">6</td><td style="padding:8px 10px;border:1px solid #cbd5e1;">Verify full system functionality</td><td style="padding:8px 10px;border:1px solid #cbd5e1;">Have end-user test application, ping external FQDN, verify throughput.</td></tr>
    <tr><td style="padding:8px 10px;border:1px solid #cbd5e1;font-weight:bold;">7</td><td style="padding:8px 10px;border:1px solid #cbd5e1;">Document findings, actions, and outcomes</td><td style="padding:8px 10px;border:1px solid #cbd5e1;">Update topology diagrams, ticketing system (Jira/ServiceNow), and wiki.</td></tr>
  </tbody>
</table>

</div>'''

CIS3321_EXAM_FOCUS = {
    1: {
        "net": "Domain 1.0: Networking Concepts — Encapsulation/De-encapsulation PDU names: Bits (L1) -> Frames (L2) -> Packets (L3) -> Segments (L4) -> Data (L5-7).",
        "ccna": "Domain 1.0: Network Fundamentals — Function of routers, layer 2/3 switches, next-gen firewalls, wireless LAN controllers (WLC), and endpoints in 2-tier / 3-tier architectures.",
        "trap": "Exam Trap: Hubs operate at Layer 1 and form a single collision domain. Switches operate at Layer 2 and break up collision domains per port, but share a single broadcast domain."
    },
    2: {
        "net": "Domain 1.0: Protocol Ports — Memorize core well-known ports: FTP (20/21), SSH (22), Telnet (23), SMTP (25), DNS (53), DHCP (67/68), HTTP (80), NTP (123), HTTPS (443), RDP (3389).",
        "ccna": "Domain 1.0: TCP vs UDP — TCP (connection-oriented, 3-way handshake SYN-SYN/ACK-ACK, sequence numbers, windowing) vs UDP (connectionless, best effort, voice/video).",
        "trap": "Exam Trap: DNS uses UDP port 53 for standard client queries, but TCP port 53 for zone transfers between DNS servers!"
    },
    3: {
        "net": "Domain 1.0: IPv4 Subnetting — Rapid subnetting math: Given 192.168.1.0/27, increment is 32 (256-224=32), usable hosts = 30 (2^5 - 2). Subnets: .0, .32, .64, .96, etc.",
        "ccna": "Domain 1.0: IP Addressing — Variable Length Subnet Masking (VLSM) allocation to conserve IP space on point-to-point links (/30 or /31).",
        "trap": "Exam Trap: First address is the Network ID, last address is the Directed Broadcast. Neither can be assigned to a host interface!"
    },
    4: {
        "net": "Domain 1.0: IPv6 Fundamentals — Address types: Unicast (Global 2000::/3, Link-Local FE80::/10, Unique Local FC00::/7, Loopback ::1), Multicast (FF00::/8), Anycast. (No broadcast in IPv6!)",
        "ccna": "Domain 1.0: IPv6 Auto-Configuration — EUI-64 process: Split 48-bit MAC in half, insert FFFE in middle, flip the 7th bit (Universal/Local bit).",
        "trap": "Exam Trap: Link-local addresses (FE80::/10) are required on every IPv6-enabled interface and are non-routable beyond the local link."
    },
    5: {
        "net": "Domain 2.0: Infrastructure — Copper cable categories: Cat 5e (1 Gbps, 100m), Cat 6 (10 Gbps up to 55m), Cat 6a (10 Gbps at 100m). T568A vs T568B pinout color coding.",
        "ccna": "Domain 1.0: Physical Cabling — Single-Mode Fiber (SMF: 9-micron core, laser, long distance km) vs Multi-Mode Fiber (MMF: 50/62.5-micron core, LED, short distance campus).",
        "trap": "Exam Trap: Straight-through cables connect unlike devices (PC to Switch). Crossover cables connect like devices (Switch to Switch, PC to Router)."
    },
    6: {
        "net": "Domain 2.0: Wireless Standards — 802.11b (11 Mbps, 2.4GHz), 802.11g (54 Mbps, 2.4GHz), 802.11n/Wi-Fi 4 (600 Mbps, 2.4/5GHz), 802.11ac/Wi-Fi 5 (6.9 Gbps, 5GHz), 802.11ax/Wi-Fi 6 (9.6 Gbps, 2.4/5/6GHz).",
        "ccna": "Domain 2.0: Wireless Architectures — Autonomous APs vs Lightweight APs (LAP) with Split-MAC architecture communicating via CAPWAP tunnels to a Wireless LAN Controller (WLC).",
        "trap": "Exam Trap: 2.4 GHz only has 3 non-overlapping channels in North America: Channel 1, Channel 6, and Channel 11 (each 20 MHz wide, 5 MHz channel spacing)."
    },
    7: {
        "net": "Domain 1.0: WAN Technologies — Leased lines (T1: 1.544 Mbps, T3: 44.736 Mbps), Metro Ethernet, DSL, Cable broadband, and Cellular LTE/5G failover.",
        "ccna": "Domain 1.0: Cloud & Virtualization — Virtualization components: Type 1 Hypervisor (Bare-metal: ESXi, KVM) vs Type 2 Hypervisor (Hosted: VirtualBox, VMware Workstation).",
        "trap": "Exam Trap: MPLS labels packets with 20-bit labels for high-speed forwarding between Label Edge Routers (LER) and Label Switch Routers (LSR), bypassing IP route lookups."
    },
    8: {
        "net": "Domain 4.0: Network Security — Attack types: DoS/DDoS, Man-in-the-Middle (MitM), DNS spoofing, ARP poisoning, and rogue DHCP servers.",
        "ccna": "Domain 5.0: Security Fundamentals — Layer 2 defense mechanisms: Port Security (max MACs, violation shutdown/restrict/protect), DHCP Snooping, Dynamic ARP Inspection (DAI).",
        "trap": "Exam Trap: Port Security 'restrict' drops unauthorized frames and logs a syslog alert, while 'protect' drops frames silently, and 'shutdown' error-disables the port."
    },
    9: {
        "net": "Domain 1.0: Network Services — DHCP DORA Process: Discover (Broadcast), Offer (Unicast/Broadcast), Request (Broadcast), Acknowledge (Unicast/Broadcast).",
        "ccna": "Domain 4.0: IP Services — DHCP Relay Agent (`ip helper-address <server-ip>`) required on the router interface to forward client DHCP broadcast Discover packets as unicast across subnets.",
        "trap": "Exam Trap: If a client cannot reach a DHCP server and receives an IP in the 169.254.0.0/16 range, it was assigned via APIPA (Automatic Private IP Addressing)."
    },
    10: {
        "net": "Domain 1.0: Routing Protocols — Interior Gateway Protocols (OSPF, EIGRP, RIP) vs Exterior Gateway Protocol (BGP). Distance Vector vs Link-State routing.",
        "ccna": "Domain 3.0: IP Routing — Administrative Distance (AD) hierarchy: Connected (0) > Static (1) > EIGRP Internal (90) > OSPF (110) > RIP (120) > External EIGRP (170) > eBGP (20).",
        "trap": "Exam Trap: Floating Static Routes use an administrative distance higher than the dynamic routing protocol (e.g. `ip route 0.0.0.0 0.0.0.0 10.1.1.2 115`) to provide backup failover."
    },
    11: {
        "net": "Domain 2.0: Switching — 802.1Q VLAN trunking encapsulation adds a 4-byte tag containing the 12-bit VLAN ID (supports up to 4,094 VLANs).",
        "ccna": "Domain 2.0: Network Access — Spanning Tree Protocol (STP) port roles: Root Port (lowest cost to Root Bridge), Designated Port (lowest cost on segment), Blocking/Alternate Port.",
        "trap": "Exam Trap: The switch with the LOWEST Bridge ID (Bridge Priority + MAC address) becomes the Root Bridge. Default priority is 32768."
    },
    12: {
        "net": "Domain 4.0: Remote Access — IPsec architecture: Authentication Header (AH: integrity/authentication, no encryption) vs Encapsulating Security Payload (ESP: confidentiality, integrity, authentication).",
        "ccna": "Domain 5.0: Secure Remote Access — Client-to-Site VPN (Cisco AnyConnect over SSL/TLS port 443) vs Site-to-Site VPN (IPsec IKEv1/IKEv2 tunnels over UDP 500/4500).",
        "trap": "Exam Trap: In IPsec Transport Mode, only the payload is encrypted. In IPsec Tunnel Mode, the entire original IP packet is encrypted and enclosed in a new IP header."
    },
    13: {
        "net": "Domain 1.0: QoS & VoIP — Real-time transport requirements: Latency (<150ms one-way), Jitter (<30ms), Packet Loss (<1%). Protocols: SIP (signaling, UDP/TCP 5060) and RTP (voice payload, UDP).",
        "ccna": "Domain 1.0: Quality of Service — Classification and Marking: Layer 2 CoS (802.1p, 3 bits in 802.1Q header) vs Layer 3 DSCP (6 bits in IPv4 ToS byte, e.g. EF = Expedited Forwarding for voice).",
        "trap": "Exam Trap: Traffic Shaping buffers excess packets in queue (smoothes bursts), while Traffic Policing drops or re-marks packets that exceed the committed rate."
    },
    14: {
        "net": "Domain 5.0: Network Troubleshooting — Hardware testing tools: Cable certifier, Tone generator and probe (fox & hound), Time-Domain Reflectometer (TDR), optical power meter.",
        "ccna": "Domain 4.0: Network Diagnostics — CLI verification commands: `show ip interface brief` (status/protocol up/up), `show cdp neighbors detail`, `traceroute`, `debug ip packet`.",
        "trap": "Exam Trap: An interface status of 'up / line protocol down' almost always indicates a Layer 2 framing, encapsulation, or clock rate mismatch!"
    },
    15: {
        "net": "Domain 3.0: Network Operations — Configuration baselines, standard operating procedures (SOP), Network diagrams (Physical vs Logical), and Business Impact Analysis.",
        "ccna": "Domain 3.0: Network Management — SNMP Architecture: SNMP Manager (NMS), SNMP Agent, Management Information Base (MIB), and SNMP Traps (UDP 162). SNMPv3 adds auth & encryption.",
        "trap": "Exam Trap: Syslog severity levels from highest to lowest: 0 (Emergency) > 1 (Alert) > 2 (Critical) > 3 (Error) > 4 (Warning) > 5 (Notice) > 6 (Informational) > 7 (Debug)."
    },
    16: {
        "net": "All Domains: Network+ Capstone — Pacing strategy: Skip the 3-5 PBQs at the start of the exam, flag them for review, answer all MCQs, and return with 25-30 minutes remaining.",
        "ccna": "All Domains: CCNA Capstone — Cisco exam rules: NO back button allowed on Cisco exams! Every answer is final once submitted. Practice strict time management (approx. 1 min per question).",
        "trap": "Exam Trap: Carefully verify the subnet mask and default gateway in simulation questions. A single transposed digit in a gateway IP invalidates the entire simulation."
    }
}

def build_cis3321_multicert_callout(mod_num: int) -> str:
    f = CIS3321_EXAM_FOCUS.get(mod_num, {})
    return f'''
<!-- NETWORK+ & CCNA DUAL CERTIFICATION EXAM FOCUS BOX -->
<div style="background:#fdf2f8;border:2px solid #8b0000;border-radius:8px;padding:22px 26px;margin-top:28px;box-shadow:0 3px 10px rgba(139,0,0,0.12);">
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
    <span style="font-size:22px;">🌐</span>
    <h3 style="margin:0;color:#8b0000;font-size:16.5px;font-weight:bold;letter-spacing:0.5px;">
      NETWORK+ (N10-008/009) &amp; CCNA (200-301) EXAM FOCUS · Module {mod_num:02d}
    </h3>
  </div>
  <p style="margin:0 0 14px 0;font-size:13.5px;color:#700000;line-height:1.6;">
    Core objectives tested on CompTIA Network+ and Cisco CCNA certification exams from this module:
  </p>
  <div style="display:grid;grid-template-columns:1fr;gap:10px;font-size:13px;line-height:1.6;">
    <div style="background:white;border-left:4px solid #b22222;padding:10px 14px;border-radius:4px;">
      <strong style="color:#b22222;">🏷️ CompTIA Network+ Focus:</strong> {f.get('net', '')}
    </div>
    <div style="background:white;border-left:4px solid #003366;padding:10px 14px;border-radius:4px;">
      <strong style="color:#003366;">⚡ Cisco CCNA Blueprint Focus:</strong> {f.get('ccna', '')}
    </div>
    <div style="background:#fff8e1;border-left:4px solid #f5a623;padding:10px 14px;border-radius:4px;">
      <strong style="color:#b45309;">⚠️ High-Frequency Exam Trap:</strong> {f.get('trap', '')}
    </div>
  </div>
</div>
'''

def update_cis3321_all():
    print("="*75)
    print("UPDATING CIS-3321 (NETWORK ADMIN) TO NETWORK+ & CCNA DUAL STANDARDS")
    print("="*75)

    # 1. Publish CLI & PBQ Handbook
    print("\n1. Publishing Cisco IOS CLI & PBQ Simulation Handbook...")
    hb_title = "💻 Cisco IOS CLI & Performance-Based Question (PBQ) Exam Simulation Handbook"
    hb_url = create_or_update_page(CID, hb_title, build_cli_pbq_handbook_html())
    add_item_to_module(CID, MID_ORIENT, hb_title, hb_url, pos=8)
    print("  ✅ Published and linked CLI & PBQ Handbook Page!")

    # 2. Enrich all 16 Reading Guides
    print("\n2. Injecting Network+ & CCNA Exam Focus into all 16 Reading Guides...")
    pages = api_get(f"/courses/{CID}/pages?per_page=100")
    page_map = {p['url']: p for p in pages} if isinstance(pages, list) else {}

    for mod_num in range(1, 17):
        mod_dir = BASE_DIR / f"Module_{mod_num:02d}"
        rg_files = sorted(mod_dir.glob("*Reading_Guide*.md"))
        if not rg_files:
            continue

        rg_text = rg_files[0].read_text(encoding='utf-8')
        tm = re.search(r'^#\s+(.+)$', rg_text, re.M)
        topic = re.sub(r'[*_`]', '', tm.group(1)).strip() if tm else f"Module {mod_num:02d} Reading Guide"
        page_title = f"Reading Guide (M{mod_num:02d}): {topic}"

        target_url = None
        for purl, p in page_map.items():
            if f"m{mod_num:02d}" in purl.lower() or f"m{mod_num}-" in purl.lower():
                if "reading" in purl.lower() or "guide" in purl.lower():
                    target_url = purl
                    break

        if not target_url:
            target_url = re.sub(r'[^a-zA-Z0-9]+', '-', page_title.lower()).strip('-')[:60]

        visual_block = get_native_visual(topic, mod_num)
        base_html = md2html(rg_text)
        net_callout = build_cis3321_multicert_callout(mod_num)

        rich_html = f'''<div style="font-family:Arial,sans-serif;max-width:960px;margin:0 auto;padding:10px;">

<!-- BRANDED TEXAS WESLEYAN HEADER -->
<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(139,0,0,0.15);">
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">{page_title}</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">🎓 Texas Wesleyan University · Department of Computer Science &amp; IT · CIS-3321 Network Administration</p>
</div>

<!-- LEARNING OBJECTIVES CALLOUT -->
<div style="background:#fff8e1;border-left:5px solid #f5a623;padding:16px 20px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <p style="margin:0;font-weight:bold;color:#7a5800;font-size:14px;">📌 CORE LEARNING OBJECTIVES (NETWORK+ &amp; CCNA)</p>
  <p style="margin:6px 0 0;color:#7a5800;font-size:13.5px;line-height:1.6;">After completing this reading guide, you will be able to explain underlying theoretical mechanics, evaluate protocol architecture trade-offs, and apply configuration and troubleshooting procedures on enterprise Cisco switches and routers.</p>
</div>

<!-- CANVAS-NATIVE VISUAL ARCHITECTURE BLOCK -->
{visual_block}

<!-- EXPANDED TECHNICAL READING CONTENT -->
<div style="background:white;padding:10px 0;line-height:1.8;color:#2c3e50;font-size:15px;">
{base_html}
</div>

<!-- NETWORK+ & CCNA CALLOUT BLOCK -->
{net_callout}

<!-- STUDY TIP BOX -->
<div style="background:#e8f5e9;border-left:5px solid #4caf50;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:32px;">
  <p style="margin:0;font-weight:bold;color:#2e7d32;">💡 PROFESSOR NASH'S STUDY STRATEGY — Before the Quiz &amp; Lab</p>
  <p style="margin:6px 0 0;color:#2e7d32;font-size:13.5px;line-height:1.6;">Review each major heading, diagram, and the Network+ / CCNA exam focus above. Practice writing Cisco CLI commands from memory before attempting the Packet Tracer lab.</p>
</div>

<!-- KEY TERMS BOX -->
<div style="background:#e3f2fd;border-left:5px solid #2196f3;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:16px;">
  <p style="margin:0;font-weight:bold;color:#0d47a1;">🔑 KEY TERMS &amp; CONCEPTS TO KNOW</p>
  <p style="margin:6px 0 0;color:#0d47a1;font-size:13.5px;line-height:1.6;">Scan this guide and define every term in <strong>bold</strong>. Incorporate these technical terms and standard RFC/IEEE specifications into your weekly discussion board post to earn maximum rubric points.</p>
</div>

<!-- CAREER CONNECTION BOX -->
<div style="background:#fce4ec;border-left:5px solid #e91e63;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:16px;">
  <p style="margin:0;font-weight:bold;color:#880e4f;">🏆 INDUSTRY CERTIFICATION &amp; CAREER IMPACT</p>
  <p style="margin:6px 0 0;color:#880e4f;font-size:13.5px;line-height:1.6;">These concepts appear directly on CompTIA Network+ (N10-008/009) and Cisco CCNA (200-301) exam blueprints and technical interview loops for Network Engineers and Systems Administrators.</p>
</div>

</div>'''

        payload = {
            'wiki_page': {
                'title': page_title,
                'body': rich_html,
                'published': True,
                'notify_of_update': False
            }
        }
        res = api_put(f"/courses/{CID}/pages/{target_url}", payload)
        if res.get('url'):
            print(f"  ✅ M{mod_num:02d}: Injected Network+/CCNA Focus -> {target_url}")
        else:
            print(f"  ⚠ Update may have failed for M{mod_num:02d} ({target_url})")

        time.sleep(0.3)

    print("\n" + "="*75)
    print("✅ CIS-3321 FULLY ELEVATED TO NETWORK+ & CCNA DUAL STANDARDS!")
    print("="*75)

if __name__ == '__main__':
    update_cis3321_all()
