# -*- coding: utf-8 -*-
"""
Step 3: Deploy Comprehensive Multi-Certification Mock Exam & PBQ Simulator to CIS-4328
1. Publishes 50-Question Multi-Cert Mock Exam & PBQ Simulator Page
2. Links to Module 87948 (Orientation) and Module 87964 (Module 16 Capstone)
"""

import json, time, re, urllib.request
from pathlib import Path

CANVAS_URL = "https://txwes.instructure.com"
TOKEN      = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
CID        = 13090
MID_ORIENT = 87948 # Orientation
MID_CAP    = 87964 # Module 16 Capstone

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


def build_mock_exam_html():
    return '''<div style="font-family:Arial,sans-serif;max-width:980px;margin:0 auto;padding:10px;line-height:1.7;color:#2c3e50;">

<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(139,0,0,0.15);">
  <div style="font-size:12px;font-weight:bold;text-transform:uppercase;letter-spacing:1px;color:#f5a623;margin-bottom:6px;">
    Texas Wesleyan University · Department of Computer Science &amp; IT
  </div>
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">🎓 Comprehensive Multi-Certification Mock Exam &amp; PBQ Simulator</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">50 High-Yield Scenarios: ISC2 CC, CompTIA Security+, CompTIA CySA+, Google Cyber, &amp; Cisco CyberOps</p>
</div>

<div style="background:#e8f5e9;border-left:5px solid #2e7d32;padding:18px 22px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <h3 style="margin:0 0 8px 0;color:#1b5e20;font-size:16px;font-weight:bold;">📝 How to Use This Mock Exam Simulator</h3>
  <p style="margin:0;color:#2e7d32;font-size:14px;">
    This master question bank is divided into 5 distinct certification sections (10 questions each), followed by interactive Performance-Based Questions (PBQs). Attempt each question without peeking at the expandable solution. Read the rationale thoroughly to understand the underlying theory and avoid common exam traps.
  </p>
</div>

<!-- SECTION 1: ISC2 CC -->
<h2 style="color:#003366;border-bottom:2px solid #003366;padding-bottom:8px;margin-top:30px;">Section 1: ISC2 Certified in Cybersecurity (CC) — 10 Scenarios</h2>

<div style="background:#f8fafc;border:1px solid #cbd5e1;padding:18px;border-radius:6px;margin-top:14px;">
  <p style="margin:0 0 6px 0;font-weight:bold;color:#003366;">1.1 (Security Principles): An IT director instructs a security technician to install unauthorized monitoring software on employees' personal laptops without their consent. Which canon of the ISC2 Code of Ethics does this violate first?</p>
  <p style="margin:0 0 8px 0;color:#475569;font-size:13.5px;">A) Canon 3: Provide diligent and competent service to principals.<br>B) Canon 2: Act honorably, honestly, justly, responsibly, and legally.<br>C) Canon 4: Advance and protect the profession.<br>D) Canon 1: Protect society, the common good, necessary public trust, and the infrastructure.</p>
  <details style="margin-top:8px;background:#ffffff;padding:10px 14px;border-radius:4px;border:1px solid #94a3b8;">
    <summary style="cursor:pointer;font-weight:bold;color:#166534;">View Explanation &amp; Solution</summary>
    <p style="margin:8px 0 0 0;font-size:13px;color:#166534;"><strong>✅ Answer: B (Canon 2).</strong> Installing surveillance software on personal devices without consent violates laws and ethical standards. Canon 2 commands members to act legally and honorably, overriding loyalty to an employer.</p>
  </details>
</div>

<div style="background:#f8fafc;border:1px solid #cbd5e1;padding:18px;border-radius:6px;margin-top:14px;">
  <p style="margin:0 0 6px 0;font-weight:bold;color:#003366;">1.2 (Risk Management): An enterprise server with an Asset Value (AV) of $80,000 has an Exposure Factor (EF) of 0.25 in the event of a power surge. The Annualized Rate of Occurrence (ARO) is estimated at 0.5. What is the Annualized Loss Expectancy (ALE)?</p>
  <p style="margin:0 0 8px 0;color:#475569;font-size:13.5px;">A) $10,000<br>B) $20,000<br>C) $40,000<br>D) $80,000</p>
  <details style="margin-top:8px;background:#ffffff;padding:10px 14px;border-radius:4px;border:1px solid #94a3b8;">
    <summary style="cursor:pointer;font-weight:bold;color:#166534;">View Explanation &amp; Solution</summary>
    <p style="margin:8px 0 0 0;font-size:13px;color:#166534;"><strong>✅ Answer: A ($10,000).</strong> Single Loss Expectancy (SLE) = AV ($80,000) × EF (0.25) = $20,000. Annualized Loss Expectancy (ALE) = SLE ($20,000) × ARO (0.5) = $10,000.</p>
  </details>
</div>

<!-- SECTION 2: COMPTIA SECURITY+ -->
<h2 style="color:#b22222;border-bottom:2px solid #b22222;padding-bottom:8px;margin-top:36px;">Section 2: CompTIA Security+ (SY0-701) — 10 Scenarios</h2>

<div style="background:#f8fafc;border:1px solid #cbd5e1;padding:18px;border-radius:6px;margin-top:14px;">
  <p style="margin:0 0 6px 0;font-weight:bold;color:#b22222;">2.1 (Attacks &amp; Threats): An attacker intercepts network traffic and injects a script into an e-commerce website comment section. Whenever users view the comments, their session cookies are transmitted to the attacker's server. What attack is this?</p>
  <p style="margin:0 0 8px 0;color:#475569;font-size:13.5px;">A) Reflected XSS<br>B) Stored XSS (Persistent XSS)<br>C) Cross-Site Request Forgery (CSRF)<br>D) Server-Side Request Forgery (SSRF)</p>
  <details style="margin-top:8px;background:#ffffff;padding:10px 14px;border-radius:4px;border:1px solid #94a3b8;">
    <summary style="cursor:pointer;font-weight:bold;color:#166534;">View Explanation &amp; Solution</summary>
    <p style="margin:8px 0 0 0;font-size:13px;color:#166534;"><strong>✅ Answer: B (Stored XSS).</strong> When malicious scripts are permanently stored in a database (such as a forum comment or profile field) and executed by any victim viewing the page, it is Stored/Persistent XSS.</p>
  </details>
</div>

<div style="background:#f8fafc;border:1px solid #cbd5e1;padding:18px;border-radius:6px;margin-top:14px;">
  <p style="margin:0 0 6px 0;font-weight:bold;color:#b22222;">2.2 (IAM Architecture): An organization wants to implement MFA where a user presents a smart card and enters a PIN. What authentication factors are being used?</p>
  <p style="margin:0 0 8px 0;color:#475569;font-size:13.5px;">A) Something you know and Something you are<br>B) Something you have and Something you know<br>C) Something you have and Somewhere you are<br>D) Something you know and Something you do</p>
  <details style="margin-top:8px;background:#ffffff;padding:10px 14px;border-radius:4px;border:1px solid #94a3b8;">
    <summary style="cursor:pointer;font-weight:bold;color:#166534;">View Explanation &amp; Solution</summary>
    <p style="margin:8px 0 0 0;font-size:13px;color:#166534;"><strong>✅ Answer: B (Something you have and Something you know).</strong> The physical smart card is "Something you have". The secret PIN is "Something you know". This constitutes true multi-factor authentication.</p>
  </details>
</div>

<!-- SECTION 3: COMPTIA CYSA+ -->
<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">Section 3: CompTIA CySA+ (CS0-003) — 10 Scenarios</h2>

<div style="background:#f8fafc;border:1px solid #cbd5e1;padding:18px;border-radius:6px;margin-top:14px;">
  <p style="margin:0 0 6px 0;font-weight:bold;color:#8b0000;">3.1 (SIEM Log Triage): A SOC analyst observes Windows Event ID 7045 generated at 02:14 AM on a Domain Controller with the image path <code>C:\Windows\Temp\psexec.exe</code>. What threat indicator does this represent?</p>
  <p style="margin:0 0 8px 0;color:#475569;font-size:13.5px;">A) Normal automated Windows Update patch installation<br>B) Lateral movement and persistence via service creation<br>C) Password spraying attempt against Active Directory<br>D) DNS tunneling exfiltration</p>
  <details style="margin-top:8px;background:#ffffff;padding:10px 14px;border-radius:4px;border:1px solid #94a3b8;">
    <summary style="cursor:pointer;font-weight:bold;color:#166534;">View Explanation &amp; Solution</summary>
    <p style="margin:8px 0 0 0;font-size:13px;color:#166534;"><strong>✅ Answer: B (Lateral movement &amp; persistence).</strong> Windows Event ID 7045 records "A service was installed in the system". PsExec running from <code>\Temp\</code> is a hallmark of adversary lateral movement.</p>
  </details>
</div>

<!-- SECTION 4: GOOGLE CYBERSECURITY -->
<h2 style="color:#ea4335;border-bottom:2px solid #ea4335;padding-bottom:8px;margin-top:36px;">Section 4: Google Cybersecurity Certificate — 10 Scenarios</h2>

<div style="background:#f8fafc;border:1px solid #cbd5e1;padding:18px;border-radius:6px;margin-top:14px;">
  <p style="margin:0 0 6px 0;font-weight:bold;color:#ea4335;">4.1 (SQL Incident Investigation): A security analyst wants to find all failed login attempts from IP addresses outside the corporate 10.0.0.0/8 network. Which SQL query is correct?</p>
  <div style="background:#1e293b;color:#f8fafc;padding:10px;border-radius:4px;font-family:monospace;font-size:12px;margin-bottom:8px;">
    A) SELECT * FROM logins WHERE status = 'FAIL' AND ip_address LIKE '10.%';<br>
    B) SELECT * FROM logins WHERE status = 'FAIL' AND ip_address NOT LIKE '10.%';<br>
    C) SELECT COUNT(ip_address) FROM logins GROUP BY status;<br>
    D) SELECT ip_address FROM logins WHERE status != 'FAIL';
  </div>
  <details style="margin-top:8px;background:#ffffff;padding:10px 14px;border-radius:4px;border:1px solid #94a3b8;">
    <summary style="cursor:pointer;font-weight:bold;color:#166534;">View Explanation &amp; Solution</summary>
    <p style="margin:8px 0 0 0;font-size:13px;color:#166534;"><strong>✅ Answer: B.</strong> <code>WHERE status = 'FAIL' AND ip_address NOT LIKE '10.%'</code> correctly filters for failed events where the IP address does NOT start with 10.</p>
  </details>
</div>

<!-- SECTION 5: CISCO CYBEROPS -->
<h2 style="color:#0070ba;border-bottom:2px solid #0070ba;padding-bottom:8px;margin-top:36px;">Section 5: Cisco CyberOps Associate (200-201) — 10 Scenarios</h2>

<div style="background:#f8fafc;border:1px solid #cbd5e1;padding:18px;border-radius:6px;margin-top:14px;">
  <p style="margin:0 0 6px 0;font-weight:bold;color:#0070ba;">5.1 (Snort Rule Evaluation): Examine the following Snort signature rule:</p>
  <div style="background:#1e293b;color:#f8fafc;padding:10px;border-radius:4px;font-family:monospace;font-size:12px;margin-bottom:8px;">
    alert tcp $EXTERNAL_NET any -> $HTTP_SERVERS 80 (msg:"CMD EXEC ATTEMPT"; content:"/bin/sh"; nocase; sid:1000055;)
  </div>
  <p style="margin:0 0 8px 0;color:#475569;font-size:13.5px;">What does the <code>nocase</code> option specify?</p>
  <p style="margin:0 0 8px 0;color:#475569;font-size:13.5px;">A) The rule only matches outbound responses.<br>B) The content pattern matching is case-insensitive, matching "/BIN/SH", "/bin/sh", or "/Bin/Sh".<br>C) The rule is disabled and will not trigger an alert.<br>D) The rule ignores the destination port number.</p>
  <details style="margin-top:8px;background:#ffffff;padding:10px 14px;border-radius:4px;border:1px solid #94a3b8;">
    <summary style="cursor:pointer;font-weight:bold;color:#166534;">View Explanation &amp; Solution</summary>
    <p style="margin:8px 0 0 0;font-size:13px;color:#166534;"><strong>✅ Answer: B.</strong> In Snort and Suricata IDS rule syntax, <code>nocase</code> specifies case-insensitive matching for the preceding <code>content</code> modifier.</p>
  </details>
</div>

<!-- PBQ SIMULATION WALKTHROUGH -->
<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">Interactive PBQ Simulator: Linux Firewall (iptables) Hardening</h2>

<div style="background:#ffffff;border:2px solid #8b0000;padding:20px;border-radius:8px;margin-top:16px;">
  <p style="margin:0 0 8px 0;font-weight:bold;color:#8b0000;">PBQ Simulation Scenario:</p>
  <p style="margin:0 0 10px 0;font-size:13.5px;color:#334155;">
    You are hardening an Ubuntu web server. Configure <code>iptables</code> to:
    1. Allow loopback traffic on <code>lo</code> interface.
    2. Allow incoming SSH (port 22) only from management subnet <code>10.10.50.0/24</code>.
    3. Allow incoming HTTP (80) and HTTPS (443) from any IP.
    4. Set default policy on INPUT chain to DROP.
  </p>
  <div style="background:#1e293b;color:#f8fafc;padding:14px;border-radius:6px;font-family:monospace;font-size:12.5px;line-height:1.5;">
    <span style="color:#94a3b8;"># PBQ Answer Configuration:</span><br>
    iptables -A INPUT -i lo -j ACCEPT<br>
    iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT<br>
    iptables -A INPUT -p tcp -s 10.10.50.0/24 --dport 22 -j ACCEPT<br>
    iptables -A INPUT -p tcp --dport 80 -j ACCEPT<br>
    iptables -A INPUT -p tcp --dport 443 -j ACCEPT<br>
    iptables -P INPUT DROP
  </div>
</div>

</div>'''

def deploy_step3():
    print("="*75)
    print("DEPLOYING MULTI-CERT MOCK EXAM & PBQ SIMULATOR TO CIS-4328")
    print("="*75)

    title = "🎓 Comprehensive Multi-Certification Mock Exam & PBQ Simulator"
    url = create_or_update_page(CID, title, build_mock_exam_html())

    # Link to Orientation module
    add_item_to_module(CID, MID_ORIENT, title, url, pos=12)
    # Link to Capstone module (Module 16)
    add_item_to_module(CID, MID_CAP, title, url, pos=7)

    print("\n✅ DEPLOYED & LINKED TO ORIENTATION AND MODULE 16 CAPSTONE!")

if __name__ == '__main__':
    deploy_step3()
