# -*- coding: utf-8 -*-
"""
Step 1: Deploy Professional CCNP ENCOR/ENARSI & Cloud Engineering Knowledge to CSC-6361
1. Publish CCNP Enterprise Engineering Deep-Dive Page to Module 88222
2. Inject Professional Engineering Focus callout blocks into all 7 Weekly Reading Guides
"""

import json, time, re, urllib.request
from pathlib import Path
from csc6361_builder_core import md2html
from canvas_native_visuals import get_native_visual

CANVAS_URL = "https://txwes.instructure.com"
TOKEN      = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
CID        = 12666
MID_ORIENT = 88222
BASE_DIR   = Path(__file__).parent / 'CSC-6361_Computer_Networks'

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

# --- 1. Deep-Dive Page HTML ---
def build_ccnp_deep_dive_html():
    return '''<div style="font-family:Arial,sans-serif;max-width:980px;margin:0 auto;padding:10px;line-height:1.7;color:#2c3e50;">

<div style="background:linear-gradient(135deg,#1b365d,#002855);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(27,54,93,0.25);">
  <div style="font-size:12px;font-weight:bold;text-transform:uppercase;letter-spacing:1px;color:#f5a623;margin-bottom:6px;">
    Texas Wesleyan University · Graduate Computer Science &amp; IT
  </div>
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">🚀 CCNP ENCOR (350-401) &amp; ENARSI (300-410) Professional Engineering Guide</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">Master's Level Network Architecture, Advanced Routing, SD-WAN &amp; Cloud Interconnects</p>
</div>

<div style="background:#e8f4f8;border-left:5px solid #0056b3;padding:18px 22px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <h3 style="margin:0 0 8px 0;color:#003d80;font-size:16px;font-weight:bold;">🏛️ Professional-Tier Graduate Engineering Standard</h3>
  <p style="margin:0;color:#004085;font-size:14px;">
    Graduate study in Advanced Computer Networks demands comprehension beyond configuring commands; it requires reasoning through complex failure states, architectural tradeoffs, and automated control planes. This guide synthesizes core competencies from the <strong>Cisco CCNP Enterprise Core (350-401 ENCOR)</strong>, <strong>Enterprise Advanced Routing (300-410 ENARSI)</strong>, and <strong>AWS Advanced Networking Specialty (ANS-C01)</strong> blueprints.
  </p>
</div>

<h2 style="color:#1b365d;border-bottom:2px solid #1b365d;padding-bottom:8px;margin-top:30px;">1. Advanced Route Redistribution &amp; Loop Prevention</h2>

<p>When redistributing between routing protocols with differing metrics and Administrative Distances (AD) (e.g., OSPF AD 110 vs. EIGRP Internal AD 90 / External AD 170), two mutual redistribution points will cause <strong>suboptimal routing and catastrophic routing loops</strong> unless route tagging and filtering are strictly enforced.</p>

<div style="background:#1e293b;color:#f8fafc;padding:16px 20px;border-radius:8px;font-family:monospace;font-size:13px;line-height:1.6;margin-top:12px;">
<span style="color:#94a3b8;">! Professional Route Tagging on Border Router 1 (Mutual Redistribution)</span><br>
route-map EIGRP_TO_OSPF deny 10<br>
&nbsp;&nbsp;match tag 200<br>
route-map EIGRP_TO_OSPF permit 20<br>
&nbsp;&nbsp;set tag 100<br>
&nbsp;&nbsp;set metric-type type-1<br><br>
route-map OSPF_TO_EIGRP deny 10<br>
&nbsp;&nbsp;match tag 100<br>
route-map OSPF_TO_EIGRP permit 20<br>
&nbsp;&nbsp;set tag 200<br>
&nbsp;&nbsp;default-metric 100000 100 255 1 1500<br><br>
router ospf 1<br>
&nbsp;&nbsp;redistribute eigrp 100 subnets route-map EIGRP_TO_OSPF<br>
router eigrp 100<br>
&nbsp;&nbsp;redistribute ospf 1 route-map OSPF_TO_EIGRP
</div>

<h2 style="color:#1b365d;border-bottom:2px solid #1b365d;padding-bottom:8px;margin-top:36px;">2. Control Plane Policing (CoPP) Implementation</h2>

<p>The router control plane (handling BGP, OSPF, SSH, SNMP) must be protected against Denial-of-Service attacks using Modular QoS CLI (MQC) to filter and rate-limit traffic destined directly to the CPU (Punt Path).</p>

<div style="background:#1e293b;color:#f8fafc;padding:16px 20px;border-radius:8px;font-family:monospace;font-size:13px;line-height:1.6;margin-top:12px;">
class-map match-any COPP_ROUTING<br>
&nbsp;&nbsp;match access-group name ACL_ROUTING_PROTOCOLS<br>
class-map match-any COPP_MGMT<br>
&nbsp;&nbsp;match access-group name ACL_SSH_HTTPS<br><br>
policy-map POLICY_COPP<br>
&nbsp;&nbsp;class COPP_ROUTING<br>
&nbsp;&nbsp;&nbsp;&nbsp;police 1000000 conform-action transmit exceed-action transmit<br>
&nbsp;&nbsp;class COPP_MGMT<br>
&nbsp;&nbsp;&nbsp;&nbsp;police 500000 conform-action transmit exceed-action drop<br>
&nbsp;&nbsp;class class-default<br>
&nbsp;&nbsp;&nbsp;&nbsp;police 100000 conform-action transmit exceed-action drop<br><br>
control-plane<br>
&nbsp;&nbsp;service-policy input POLICY_COPP
</div>

<h2 style="color:#1b365d;border-bottom:2px solid #1b365d;padding-bottom:8px;margin-top:36px;">3. Enterprise Cloud Interconnects: AWS Direct Connect &amp; Transit Gateway</h2>

<table style="width:100%;border-collapse:collapse;margin-top:16px;font-size:13.5px;">
  <thead>
    <tr style="background:#1e293b;color:white;text-align:left;">
      <th style="padding:10px;border:1px solid #0f172a;">Architecture Component</th>
      <th style="padding:10px;border:1px solid #0f172a;">Functionality</th>
      <th style="padding:10px;border:1px solid #0f172a;">Engineering Tradeoff / Best Practice</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:10px;border:1px solid #cbd5e1;font-weight:bold;">AWS Direct Connect (DX)</td><td style="padding:10px;border:1px solid #cbd5e1;">Dedicated 1Gbps / 10Gbps private fiber interconnect via 802.1Q VIFs.</td><td style="padding:10px;border:1px solid #cbd5e1;">Requires BGP peering (eBGP ASN) with MACsec encryption over DX.</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:10px;border:1px solid #cbd5e1;font-weight:bold;">Transit Gateway (TGW)</td><td style="padding:10px;border:1px solid #cbd5e1;">Hub-and-spoke cloud router connecting thousands of VPCs and on-prem routers.</td><td style="padding:10px;border:1px solid #cbd5e1;">Eliminates complex full-mesh VPC peering. Supports multicast and route domain isolation.</td></tr>
    <tr><td style="padding:10px;border:1px solid #cbd5e1;font-weight:bold;">Direct Connect Gateway (DXGW)</td><td style="padding:10px;border:1px solid #cbd5e1;">Global routing entity connecting a DX link to multiple Transit Gateways across AWS regions.</td><td style="padding:10px;border:1px solid #cbd5e1;">BGP prefix limits (max 100 prefixes advertised from on-prem) require prefix summarization.</td></tr>
  </tbody>
</table>

<h2 style="color:#1b365d;border-bottom:2px solid #1b365d;padding-bottom:8px;margin-top:36px;">4. Programmatic Automation: RESTCONF &amp; YANG Data Models</h2>

<div style="background:#1e293b;color:#f8fafc;padding:16px 20px;border-radius:8px;font-family:monospace;font-size:13px;line-height:1.6;margin-top:12px;">
<span style="color:#94a3b8;"># Python RESTCONF (RFC 8040) API Interface Retrieval</span><br>
<span style="color:#f43f5e;">import</span> requests, json<br><br>
url = <span style="color:#facc15;">"https://10.10.10.1/restconf/data/ietf-interfaces:interfaces"</span><br>
headers = {<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#facc15;">"Accept"</span>: <span style="color:#facc15;">"application/yang-data+json"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#facc15;">"Content-Type"</span>: <span style="color:#facc15;">"application/yang-data+json"</span><br>
}<br>
response = requests.get(url, auth=(<span style="color:#facc15;">'cisco'</span>, <span style="color:#facc15;">'cisco123!'</span>), headers=headers, verify=False)<br>
print(json.dumps(response.json(), indent=2))
</div>

</div>'''

GRADUATE_CCNP_FOCUS = {
    1: {
        "encor": "ENCOR 3.1: Layer 3 Technologies — Mutual route redistribution mechanics, EIGRP variance for unequal-cost load balancing, and OSPF Area Types (Stub, Totally Stub, NSSA, Totally NSSA).",
        "enarsi": "ENARSI 1.1: Advanced Routing — Route-map filtering with IP prefix-lists and route tagging (set tag / match tag) to eliminate micro-loops and sub-optimal routing.",
        "cloud": "AWS ANS-C01: BGP Multi-Exit Discriminator (MED) and AS-Path prepending to influence ingress traffic across active/standby hybrid cloud links.",
        "code_snippet": "ip prefix-list RFC1918 permit 10.0.0.0/8 le 24\nroute-map FILTER_OSPF permit 10\n match ip address prefix-list RFC1918\n set tag 100"
    },
    2: {
        "encor": "ENCOR 2.1: Layer 2 Infrastructure — Multiple Spanning Tree Protocol (MST / 802.1s) instance mapping, Rapid PVST+ convergence tuning (Forward Delay 4s, Max-Age 6s), and Root Bridge deterministic placement.",
        "enarsi": "ENARSI 2.1: Campus Switching — LACP (802.3ad) system priority, port priority, and hash distribution algorithms (src-dst-mac vs. src-dst-ip).",
        "cloud": "Enterprise High Availability: Cisco StackWise Virtual vs. Virtual Switching System (VSS) Dual-Active Detection (DAD) via Fast Hello or ePAgP.",
        "code_snippet": "spanning-tree mst configuration\n name CAMPUS_REGION\n revision 1\n instance 1 vlan 10,20\n instance 2 vlan 30,40"
    },
    3: {
        "encor": "ENCOR 3.3: Enterprise WAN — MPLS L3VPN architecture: VRF definition, Route Distinguishers (RD 65000:100), Route Targets (RT import/export), and MP-BGP VPNv4 address-family exchange.",
        "enarsi": "ENARSI 1.4: VPN Technologies — DMVPN Phase 3 with NHRP Shortcut and Redirect, and IPsec Virtual Tunnel Interfaces (VTI) with IKEv2 proposal suites.",
        "cloud": "Cisco SD-WAN Overlay: OMP (Overlay Management Protocol) route advertising, TLOC (Transport Location) composition (System-IP, Color, Encapsulation), and BFD path liveness tracking.",
        "code_snippet": "ip vrf FINANCE\n rd 65000:100\n route-target both 65000:100\ninterface GigabitEthernet0/1.100\n ip vrf forwarding FINANCE"
    },
    4: {
        "encor": "ENCOR 4.1: Network Security & Hardening — Control Plane Policing (CoPP) using MQC rate-limiting, and 802.1X Multi-Auth vs. Multi-Domain for VoIP deployments.",
        "enarsi": "ENARSI 2.2: Layer 2 Hardening — Dynamic ARP Inspection (DAI) trust states, DHCP Snooping Option 82 insertion, and IP Source Guard binding table enforcement.",
        "cloud": "Zero Trust Enterprise Architecture: Cisco TrustSec Security Group Tags (SGTs) and Cisco ISE pxGrid integration with Cloud firewalls.",
        "code_snippet": "ip dhcp snooping\nip dhcp snooping vlan 10,20\nip arp inspection vlan 10,20\ninterface Gi0/1\n ip arp inspection trust"
    },
    5: {
        "encor": "ENCOR 3.2: QoS & High Availability — Modular QoS CLI (MQC): Low Latency Queuing (LLQ) priority command, Class-Based Weighted Fair Queuing (CBWFQ), and WRED congestion avoidance.",
        "enarsi": "ENARSI 1.2: First Hop Redundancy Protocols — HSRPv2 (multicast 224.0.0.102) object tracking with decrement value, VRRPv3 for IPv4/IPv6, and Bidirectional Forwarding Detection (BFD) integration for sub-50ms failover.",
        "cloud": "Enterprise SLA Engineering: Classifying real-time Voice (DSCP EF / 46), Video Conferencing (DSCP AF41 / 34), and Best Effort (DSCP 0).",
        "code_snippet": "track 1 interface GigabitEthernet0/0 line-protocol\ninterface GigabitEthernet0/1\n standby 1 ip 192.168.1.1\n standby 1 priority 110\n standby 1 preempt\n standby 1 track 1 decrement 20"
    },
    6: {
        "encor": "ENCOR 6.1: Automation & Programmability — RESTCONF (RFC 8040) operations (GET, POST, PUT, PATCH, DELETE), YANG data models (RFC 7950), and JSON vs. XML data serializations.",
        "enarsi": "ENARSI 3.1: Hybrid Cloud Interconnects — AWS DirectConnect private virtual interfaces (VIF), Transit Gateway routing tables, and BGP community tagging (e.g., 7224:9100).",
        "cloud": "Infrastructure as Code (IaC): Automating enterprise router configuration rollouts using Python Netmiko and Ansible playbooks.",
        "code_snippet": "from netmiko import ConnectHandler\ncisco_device = {'device_type': 'cisco_ios', 'host': '10.1.1.1', 'username': 'admin', 'password': 'pwd'}\nnet_connect = ConnectHandler(**cisco_device)\noutput = net_connect.send_command('show ip bgp summary')"
    },
    7: {
        "encor": "ENCOR 5.1: Network Assurance & Troubleshooting — Cisco DNA Center / Catalyst Center Assurance, NetFlow v9 telemetry, EEM (Embedded Event Manager) applets, and systematic multi-layer diagnostics.",
        "enarsi": "ENARSI 4.1: Troubleshooting Enterprise Networks — MTU/MSS mismatch packet black hole resolution (`ip tcp adjust-mss 1360`), asymmetric routing detection, and BGP dampening analysis.",
        "cloud": "Capstone Architecture Integration: Formulating root-cause analysis (RCA) executive documentation for enterprise network outages.",
        "code_snippet": "event manager applet INTERFACE_DOWN\n event syslog pattern \"LINEPROTO-5-UPDOWN.*GigabitEthernet0/1.*down\"\n action 1.0 cli command \"enable\"\n action 2.0 cli command \"show ip ospf neighbor\""
    }
}

def build_graduate_multicert_callout(mod_num: int) -> str:
    f = GRADUATE_CCNP_FOCUS.get(mod_num, {})
    return f'''
<!-- GRADUATE CCNP & CLOUD ENGINEERING FOCUS BLOCK -->
<div style="background:#f0f4f8;border:2px solid #003d80;border-radius:8px;padding:22px 26px;margin-top:28px;box-shadow:0 3px 10px rgba(0,61,128,0.15);">
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
    <span style="font-size:22px;">🚀</span>
    <h3 style="margin:0;color:#002855;font-size:16.5px;font-weight:bold;letter-spacing:0.5px;">
      PROFESSIONAL CCNP &amp; CLOUD ENGINEERING FOCUS · Module {mod_num:02d} Architecture
    </h3>
  </div>
  <p style="margin:0 0 14px 0;font-size:13.5px;color:#1e3a8a;line-height:1.6;">
    Master's level mastery requires understanding underlying control-plane mechanisms, enterprise scaling constraints, and Cisco CCNP exam blueprints:
  </p>
  <div style="display:grid;grid-template-columns:1fr;gap:10px;font-size:13px;line-height:1.6;">
    <div style="background:white;border-left:4px solid #1b365d;padding:10px 14px;border-radius:4px;">
      <strong style="color:#1b365d;">🏛️ Cisco CCNP Enterprise Core (350-401 ENCOR):</strong> {f.get('encor', '')}
    </div>
    <div style="background:white;border-left:4px solid #0284c7;padding:10px 14px;border-radius:4px;">
      <strong style="color:#0284c7;">⚡ Cisco Advanced Routing &amp; Services (300-410 ENARSI):</strong> {f.get('enarsi', '')}
    </div>
    <div style="background:white;border-left:4px solid #f5a623;padding:10px 14px;border-radius:4px;">
      <strong style="color:#d97706;">☁️ Enterprise Cloud &amp; High Availability:</strong> {f.get('cloud', '')}
    </div>
  </div>
  <div style="margin-top:14px;background:#1e293b;color:#f8fafc;padding:12px 16px;border-radius:6px;font-family:monospace;font-size:12.5px;line-height:1.5;">
    <span style="color:#94a3b8;">// CCNP Professional IOS Configuration Benchmark:</span><br>
    {f.get('code_snippet', '').replace('\n', '<br>')}
  </div>
</div>
'''

def update_csc6361_all():
    print("="*75)
    print("UPDATING CSC-6361 (MASTER'S COMPUTER NETWORKS) TO PROFESSIONAL CCNP LEVEL")
    print("="*75)

    # 1. Publish Deep Dive Page
    print("\n1. Publishing CCNP Deep Dive Page...")
    dd_title = "🚀 CCNP ENCOR (350-401) & ENARSI (300-410) Professional Engineering Guide"
    dd_url = create_or_update_page(CID, dd_title, build_ccnp_deep_dive_html())
    add_item_to_module(CID, MID_ORIENT, dd_title, dd_url, pos=6)
    print("  ✅ Published and linked CCNP Deep Dive Page!")

    # 2. Enrich all 7 Weekly Reading Guides
    print("\n2. Injecting Professional Engineering Focus into all 7 Weekly Reading Guides...")
    pages = api_get(f"/courses/{CID}/pages?per_page=100")
    page_map = {p['url']: p for p in pages} if isinstance(pages, list) else {}

    for mod_num in range(1, 8):
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
        grad_callout = build_graduate_multicert_callout(mod_num)

        rich_html = f'''<div style="font-family:Arial,sans-serif;max-width:960px;margin:0 auto;padding:10px;">

<!-- BRANDED TEXAS WESLEYAN GRADUATE HEADER -->
<div style="background:linear-gradient(135deg,#1b365d,#002855);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(27,54,93,0.25);">
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">{page_title}</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">🎓 Texas Wesleyan University · Department of Computer Science &amp; IT · CSC-6361 Advanced Computer Networks (Graduate)</p>
</div>

<!-- LEARNING OBJECTIVES CALLOUT -->
<div style="background:#fff8e1;border-left:5px solid #f5a623;padding:16px 20px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <p style="margin:0;font-weight:bold;color:#7a5800;font-size:14px;">📌 GRADUATE LEARNING OBJECTIVES (CCNP ALIGNED)</p>
  <p style="margin:6px 0 0;color:#7a5800;font-size:13.5px;line-height:1.6;">Critically evaluate enterprise routing designs, simulate control-plane convergence behaviors under failure, and formulate production configurations adhering to Cisco enterprise standards.</p>
</div>

<!-- CANVAS-NATIVE VISUAL ARCHITECTURE BLOCK -->
{visual_block}

<!-- EXPANDED TECHNICAL READING CONTENT -->
<div style="background:white;padding:10px 0;line-height:1.8;color:#2c3e50;font-size:15px;">
{base_html}
</div>

<!-- PROFESSIONAL CCNP ENGINEERING CALLOUT BLOCK -->
{grad_callout}

<!-- STUDY TIP BOX -->
<div style="background:#e8f5e9;border-left:5px solid #4caf50;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:32px;">
  <p style="margin:0;font-weight:bold;color:#2e7d32;">💡 PROFESSOR NASH'S GRADUATE ENGINEERING STRATEGY</p>
  <p style="margin:6px 0 0;color:#2e7d32;font-size:13.5px;line-height:1.6;">Trace packet flows across boundary routers. Verify that your route-maps have explicit permit/deny sequence numbers and test your metric tags in Packet Tracer before submitting weekly lab topology reports.</p>
</div>

<!-- KEY TERMS BOX -->
<div style="background:#e3f2fd;border-left:5px solid #2196f3;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:16px;">
  <p style="margin:0;font-weight:bold;color:#0d47a1;">🔑 ADVANCED TERMINOLOGY &amp; RFC SPECIFICATIONS</p>
  <p style="margin:6px 0 0;color:#0d47a1;font-size:13.5px;line-height:1.6;">Cite formal RFCs (e.g., RFC 2328 OSPFv2, RFC 4271 BGP4, RFC 8040 RESTCONF) and IEEE standards in your weekly discussion posts to satisfy graduate rigor rubrics.</p>
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
            print(f"  ✅ M{mod_num:02d}: Injected Graduate CCNP Focus -> {target_url}")
        else:
            print(f"  ⚠ Update may have failed for M{mod_num:02d} ({target_url})")

        time.sleep(0.3)

    print("\n" + "="*75)
    print("✅ CSC-6361 FULLY ELEVATED TO PROFESSIONAL CCNP & CLOUD STANDARDS!")
    print("="*75)

if __name__ == '__main__':
    update_csc6361_all()
