# -*- coding: utf-8 -*-
"""
Build and deploy all certification pages to Canvas:
  - CIS-4328 (13090): 5 Cert Guides into Module 87948
  - CIS-3321 (13089): Network+/CCNA Dual Cert Hub into Module 87931
  - CSC-6361 (12666): CCNP Enterprise Guide into Module 88222
"""

import json, time, re, urllib.request
from pathlib import Path

CANVAS_URL = "https://txwes.instructure.com"
TOKEN      = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
BASE_DIR   = Path(__file__).parent

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

from generate_cert_pages import generate_multi_cert_roadmap

# Build remaining page HTML generators
def generate_isc2_cc_guide():
    return '''<div style="font-family:Arial,sans-serif;max-width:980px;margin:0 auto;padding:10px;line-height:1.7;color:#2c3e50;">

<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(139,0,0,0.15);">
  <div style="font-size:12px;font-weight:bold;text-transform:uppercase;letter-spacing:1px;color:#f5a623;margin-bottom:6px;">
    Texas Wesleyan University · Department of Computer Science &amp; IT
  </div>
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">🛡️ ISC2 Certified in Cybersecurity (CC) Exam Prep Guide</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">The 5 Core Domains, ISC2 Code of Ethics &amp; Scenario Practice Bank</p>
</div>

<div style="background:#e8f5e9;border-left:5px solid #2e7d32;padding:18px 22px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <h3 style="margin:0 0 8px 0;color:#1b5e20;font-size:16px;font-weight:bold;">🎓 About the ISC2 CC Credential</h3>
  <p style="margin:0;color:#2e7d32;font-size:14px;">
    The <strong>Certified in Cybersecurity (CC)</strong> credential from ISC2 is an internationally recognized foundational certification. It proves to employers that you possess foundational cybersecurity principles, risk management concepts, network security, and professional ethics. As part of the <em>One Million Certified in Cybersecurity</em> pledge, ISC2 offers 100% free exam vouchers to enrolled students!
  </p>
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:30px;">1. The 5 ISC2 CC Domains &amp; Exam Weights</h2>

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin-top:16px;">
  <div style="background:#ffffff;border:1px solid #e2e8f0;border-left:4px solid #8b0000;padding:16px;border-radius:6px;box-shadow:0 2px 4px rgba(0,0,0,0.05);">
    <h4 style="margin:0 0 6px 0;color:#8b0000;">Domain 1: Security Principles (26%)</h4>
    <p style="margin:0;font-size:13px;color:#475569;">CIA Triad, IAAA (Identification, Authentication, Authorization, Accounting), Non-repudiation, Privacy, Risk Management (Mitigate, Avoid, Transfer, Accept), and the <strong>ISC2 Code of Ethics</strong>.</p>
  </div>
  <div style="background:#ffffff;border:1px solid #e2e8f0;border-left:4px solid #b22222;padding:16px;border-radius:6px;box-shadow:0 2px 4px rgba(0,0,0,0.05);">
    <h4 style="margin:0 0 6px 0;color:#b22222;">Domain 2: Business Continuity, DR &amp; IR (10%)</h4>
    <p style="margin:0;font-size:13px;color:#475569;">Business Impact Analysis (BIA), Maximum Tolerable Downtime (MTD), RTO &amp; RPO, Disaster Recovery sites (Hot, Warm, Cold), and Incident Response phases.</p>
  </div>
  <div style="background:#ffffff;border:1px solid #e2e8f0;border-left:4px solid #f5a623;padding:16px;border-radius:6px;box-shadow:0 2px 4px rgba(0,0,0,0.05);">
    <h4 style="margin:0 0 6px 0;color:#d97706;">Domain 3: Access Controls Concepts (22%)</h4>
    <p style="margin:0;font-size:13px;color:#475569;">Physical vs Logical vs Administrative controls. Discretionary Access Control (DAC), Mandatory Access Control (MAC), Role-Based Access Control (RBAC), and Principle of Least Privilege.</p>
  </div>
  <div style="background:#ffffff;border:1px solid #e2e8f0;border-left:4px solid #2563eb;padding:16px;border-radius:6px;box-shadow:0 2px 4px rgba(0,0,0,0.05);">
    <h4 style="margin:0 0 6px 0;color:#1d4ed8;">Domain 4: Network Security (24%)</h4>
    <p style="margin:0;font-size:13px;color:#475569;">OSI 7 Layers, TCP/IP, common ports (22, 53, 80, 443, 3389), Firewalls, IDS/IPS, Virtual Private Networks (VPNs), Wireless security (WPA3), and Network Attacks (DDoS, MitM, Spoofing).</p>
  </div>
  <div style="background:#ffffff;border:1px solid #e2e8f0;border-left:4px solid #059669;padding:16px;border-radius:6px;box-shadow:0 2px 4px rgba(0,0,0,0.05);">
    <h4 style="margin:0 0 6px 0;color:#047857;">Domain 5: Security Operations (18%)</h4>
    <p style="margin:0;font-size:13px;color:#475569;">Data handling &amp; classification, System hardening, Patch management, Configuration management, Acceptable Use Policies (AUP), and Security awareness training.</p>
  </div>
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">2. The ISC2 Code of Ethics (Mandatory Exam Memory Target!)</h2>

<div style="background:#fffbeb;border:2px solid #fde68a;padding:20px;border-radius:8px;margin-top:16px;">
  <p style="margin:0 0 10px 0;color:#92400e;font-size:14px;font-weight:bold;">⚠️ CRITICAL EXAM RULE: You MUST memorize the 4 Canons of the ISC2 Code of Ethics IN STRICT ORDER:</p>
  <ol style="margin:0;padding-left:22px;color:#78350f;font-size:14px;line-height:1.8;">
    <li><strong>Protect society, the common good, necessary public trust, and the infrastructure.</strong> (Highest priority!)</li>
    <li><strong>Act honorably, honestly, justly, responsibly, and legally.</strong></li>
    <li><strong>Provide diligent and competent service to principals.</strong> (Your employer/clients)</li>
    <li><strong>Advance and protect the profession.</strong></li>
  </ol>
  <p style="margin:10px 0 0 0;color:#92400e;font-size:13px;"><em>Exam Tip: If an employer instructs you to perform an illegal action or conceal a public safety breach, Canon 1 and Canon 2 ALWAYS override Canon 3 (loyalty to employer).</em></p>
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">3. Key Formula &amp; Concept Cheat Sheet</h2>

<table style="width:100%;border-collapse:collapse;margin-top:16px;font-size:13.5px;">
  <thead>
    <tr style="background:#8b0000;color:white;text-align:left;">
      <th style="padding:10px;border:1px solid #700000;">Concept</th>
      <th style="padding:10px;border:1px solid #700000;">Formula / Core Rule</th>
      <th style="padding:10px;border:1px solid #700000;">Scenario Application</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:10px;border:1px solid #e2e8f0;font-weight:bold;">Risk Formula</td><td style="padding:10px;border:1px solid #e2e8f0;">Risk = Threat × Vulnerability × Impact</td><td style="padding:10px;border:1px solid #e2e8f0;">If vulnerability is patched to 0, risk drops to 0.</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:10px;border:1px solid #e2e8f0;font-weight:bold;">Single Loss Expectancy (SLE)</td><td style="padding:10px;border:1px solid #e2e8f0;">SLE = Asset Value (AV) × Exposure Factor (EF)</td><td style="padding:10px;border:1px solid #e2e8f0;">$100,000 server × 0.4 EF = $40,000 SLE.</td></tr>
    <tr><td style="padding:10px;border:1px solid #e2e8f0;font-weight:bold;">Annualized Loss Expectancy (ALE)</td><td style="padding:10px;border:1px solid #e2e8f0;">ALE = SLE × Annualized Rate of Occurrence (ARO)</td><td style="padding:10px;border:1px solid #e2e8f0;">If event happens once every 2 years (ARO = 0.5), ALE = $20,000.</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:10px;border:1px solid #e2e8f0;font-weight:bold;">RTO vs RPO</td><td style="padding:10px;border:1px solid #e2e8f0;">RTO = Downtime Target | RPO = Data Loss Target</td><td style="padding:10px;border:1px solid #e2e8f0;">RTO defines time to restore server; RPO defines how frequent backups must be.</td></tr>
  </tbody>
</table>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">4. Sample Scenario Practice Questions</h2>

<div style="background:#f8fafc;border:1px solid #cbd5e1;padding:18px;border-radius:6px;margin-top:16px;">
  <p style="margin:0 0 8px 0;font-weight:bold;color:#1e293b;">Question 1: A financial analyst discovers an unpatched critical SQL injection vulnerability in a public-facing banking portal. The CEO demands the analyst delay reporting until after quarterly earnings are announced. What should the analyst do under the ISC2 Code of Ethics?</p>
  <p style="margin:0 0 6px 0;color:#475569;font-size:13.5px;">A) Comply with the CEO because Canon 3 mandates diligent service to employers.<br>B) Report the vulnerability immediately through proper regulatory and ethical escalation channels because Canon 1 mandates protecting society and public trust.<br>C) Post the vulnerability anonymously on social media.<br>D) Resign immediately without reporting.</p>
  <p style="margin:8px 0 0 0;font-size:13px;color:#166534;font-weight:bold;">✅ Correct Answer: B. Canon 1 (Protect society and public trust) takes absolute precedence over employer loyalty.</p>
</div>

</div>'''

def generate_cysa_plus_guide():
    return '''<div style="font-family:Arial,sans-serif;max-width:980px;margin:0 auto;padding:10px;line-height:1.7;color:#2c3e50;">

<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(139,0,0,0.15);">
  <div style="font-size:12px;font-weight:bold;text-transform:uppercase;letter-spacing:1px;color:#f5a623;margin-bottom:6px;">
    Texas Wesleyan University · Department of Computer Science &amp; IT
  </div>
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">🔍 CompTIA CySA+ (CS0-003) Analyst Mastery Guide</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">SOC Operations, SIEM Log Analysis, CVSS Scoring &amp; Incident Response</p>
</div>

<div style="background:#eff6ff;border-left:5px solid #2563eb;padding:18px 22px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <h3 style="margin:0 0 8px 0;color:#1d4ed8;font-size:16px;font-weight:bold;">🎯 Blue Team SOC Analyst Preparation</h3>
  <p style="margin:0;color:#1e40af;font-size:14px;">
    The <strong>CompTIA Cybersecurity Analyst (CySA+) CS0-003</strong> certification applies behavioral analytics to networks and devices to prevent, detect, and combat cybersecurity threats. It is heavily weighted toward practical log interpretation, vulnerability management, and incident containment.
  </p>
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:30px;">1. Critical Windows &amp; Linux Security Event IDs</h2>

<table style="width:100%;border-collapse:collapse;margin-top:16px;font-size:13.5px;">
  <thead>
    <tr style="background:#1e293b;color:white;text-align:left;">
      <th style="padding:10px;border:1px solid #0f172a;">Event ID / Log</th>
      <th style="padding:10px;border:1px solid #0f172a;">Meaning</th>
      <th style="padding:10px;border:1px solid #0f172a;">Analyst Investigation Trigger</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:10px;border:1px solid #e2e8f0;font-weight:bold;color:#0369a1;">Windows 4624</td><td style="padding:10px;border:1px solid #e2e8f0;">Successful Logon</td><td style="padding:10px;border:1px solid #e2e8f0;">Logon Type 3 (Network) or Type 10 (Remote Desktop) during off-hours.</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:10px;border:1px solid #e2e8f0;font-weight:bold;color:#b91c1c;">Windows 4625</td><td style="padding:10px;border:1px solid #e2e8f0;">Failed Logon</td><td style="padding:10px;border:1px solid #e2e8f0;">Bursts of failed logons indicate password spraying or brute force.</td></tr>
    <tr><td style="padding:10px;border:1px solid #e2e8f0;font-weight:bold;color:#c2410c;">Windows 4672</td><td style="padding:10px;border:1px solid #e2e8f0;">Special Privileges Assigned</td><td style="padding:10px;border:1px solid #e2e8f0;">Administrator privilege escalation (SeDebugPrivilege).</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:10px;border:1px solid #e2e8f0;font-weight:bold;color:#b91c1c;">Windows 7045</td><td style="padding:10px;border:1px solid #e2e8f0;">New Service Installed</td><td style="padding:10px;border:1px solid #e2e8f0;">Persistence mechanism installed by malware or PsExec execution.</td></tr>
    <tr><td style="padding:10px;border:1px solid #e2e8f0;font-weight:bold;color:#475569;">/var/log/auth.log</td><td style="padding:10px;border:1px solid #e2e8f0;">Linux SSH &amp; Sudo Activity</td><td style="padding:10px;border:1px solid #e2e8f0;">"Accepted publickey for root" or repeated "sudo: authentication failure".</td></tr>
  </tbody>
</table>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">2. CVSS v3.1 / v4 Scoring Breakdown</h2>

<div style="background:#ffffff;border:1px solid #cbd5e1;padding:18px;border-radius:8px;margin-top:16px;">
  <p style="margin:0 0 10px 0;font-weight:bold;color:#1e293b;">CVSS Vector Breakdown: <code>CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H (Score: 9.8 Critical)</code></p>
  <ul style="margin:0;padding-left:20px;font-size:13.5px;line-height:1.7;color:#334155;">
    <li><strong>Attack Vector (AV):</strong> Network (N) &gt; Adjacent (A) &gt; Local (L) &gt; Physical (P). Network has the highest severity.</li>
    <li><strong>Attack Complexity (AC):</strong> Low (L) vs High (H). Low complexity yields a higher vulnerability score.</li>
    <li><strong>Privileges Required (PR):</strong> None (N) &gt; Low (L) &gt; High (H).</li>
    <li><strong>User Interaction (UI):</strong> None (N) &gt; Required (R). (e.g., victim clicking a link).</li>
    <li><strong>Scope (S):</strong> Unchanged (U) vs Changed (C). Changed scope (vulnerability impacts components beyond its security authority) elevates risk.</li>
    <li><strong>CIA Impacts (C/I/A):</strong> High (H), Low (L), None (N).</li>
  </ul>
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">3. Incident Response Playbook (NIST SP 800-61 Rev. 2)</h2>

<div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:16px;">
  <div style="flex:1;min-width:140px;background:#f8fafc;border:1px solid #cbd5e1;padding:12px;border-radius:6px;text-align:center;">
    <strong style="color:#8b0000;">1. Preparation</strong><br><span style="font-size:12px;color:#64748b;">Tooling, playbooks, CSIRT training</span>
  </div>
  <div style="flex:1;min-width:140px;background:#f8fafc;border:1px solid #cbd5e1;padding:12px;border-radius:6px;text-align:center;">
    <strong style="color:#8b0000;">2. Detection &amp; Analysis</strong><br><span style="font-size:12px;color:#64748b;">SIEM alerts, triage, IOC verification</span>
  </div>
  <div style="flex:1;min-width:140px;background:#f8fafc;border:1px solid #cbd5e1;padding:12px;border-radius:6px;text-align:center;">
    <strong style="color:#8b0000;">3. Containment</strong><br><span style="font-size:12px;color:#64748b;">Network isolation, disabling accounts</span>
  </div>
  <div style="flex:1;min-width:140px;background:#f8fafc;border:1px solid #cbd5e1;padding:12px;border-radius:6px;text-align:center;">
    <strong style="color:#8b0000;">4. Eradication &amp; Recovery</strong><br><span style="font-size:12px;color:#64748b;">Malware removal, restoring from backup</span>
  </div>
  <div style="flex:1;min-width:140px;background:#f8fafc;border:1px solid #cbd5e1;padding:12px;border-radius:6px;text-align:center;">
    <strong style="color:#8b0000;">5. Post-Incident Review</strong><br><span style="font-size:12px;color:#64748b;">Lessons learned, updating policies</span>
  </div>
</div>

</div>'''

def generate_google_cyber_guide():
    return '''<div style="font-family:Arial,sans-serif;max-width:980px;margin:0 auto;padding:10px;line-height:1.7;color:#2c3e50;">

<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(139,0,0,0.15);">
  <div style="font-size:12px;font-weight:bold;text-transform:uppercase;letter-spacing:1px;color:#f5a623;margin-bottom:6px;">
    Texas Wesleyan University · Department of Computer Science &amp; IT
  </div>
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">☁️ Google Cybersecurity Certificate &amp; Cloud Security Bridge</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">Python Log Automation, SQL Security Queries, &amp; Cloud SIEM</p>
</div>

<div style="background:#fef3c7;border-left:5px solid #d97706;padding:18px 22px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <h3 style="margin:0 0 8px 0;color:#92400e;font-size:16px;font-weight:bold;">🚀 Google Professional Cybersecurity Alignment</h3>
  <p style="margin:0;color:#78350f;font-size:14px;">
    Google's Cybersecurity Professional Certificate emphasizes hands-on analyst workflows: writing Python scripts to parse authentication logs, querying relational databases with SQL to identify security anomalies, and operating in Google Cloud Platform (GCP) environments with Chronicle SIEM.
  </p>
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:30px;">1. Essential Python Scripting for Security Analysts</h2>

<div style="background:#1e293b;color:#f8fafc;padding:16px 20px;border-radius:8px;font-family:monospace;font-size:13px;line-height:1.6;margin-top:16px;">
<span style="color:#94a3b8;"># Google Cyber Portfolio Task: Automated IP Allowlist Auditor</span><br>
<span style="color:#f43f5e;">import</span> re<br><br>
<span style="color:#38bdf8;">def</span> <span style="color:#4ade80;">audit_allowlist</span>(log_file, remove_ips):<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#f43f5e;">with</span> open(log_file, <span style="color:#facc15;">"r"</span>) <span style="color:#f43f5e;">as</span> file:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_addresses = file.read().split()<br>
&nbsp;&nbsp;&nbsp;&nbsp;updated_ips = [ip <span style="color:#f43f5e;">for</span> ip <span style="color:#f43f5e;">in</span> ip_addresses <span style="color:#f43f5e;">if</span> ip <span style="color:#f43f5e;">not in</span> remove_ips]<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#f43f5e;">with</span> open(log_file, <span style="color:#facc15;">"w"</span>) <span style="color:#f43f5e;">as</span> file:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;file.write(<span style="color:#facc15;">"\n"</span>.join(updated_ips))<br>
&nbsp;&nbsp;&nbsp;&nbsp;print(<span style="color:#facc15;">f"Audit complete: Removed {len(remove_ips)} unauthorized IPs."</span>)
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">2. SQL Queries for Incident Investigation</h2>

<div style="background:#1e293b;color:#f8fafc;padding:16px 20px;border-radius:8px;font-family:monospace;font-size:13px;line-height:1.6;margin-top:16px;">
<span style="color:#94a3b8;">-- Query 1: Detect after-hours logins from outside corporate subnet</span><br>
<span style="color:#38bdf8;">SELECT</span> employee_id, login_time, ip_address, success<br>
<span style="color:#38bdf8;">FROM</span> log_activity<br>
<span style="color:#38bdf8;">WHERE</span> (login_time &gt; <span style="color:#facc15;">'19:00:00'</span> <span style="color:#38bdf8;">OR</span> login_time &lt; <span style="color:#facc15;">'06:00:00'</span>)<br>
&nbsp;&nbsp;<span style="color:#38bdf8;">AND</span> ip_address <span style="color:#38bdf8;">NOT LIKE</span> <span style="color:#facc15;">'192.168.%'</span>;<br><br>
<span style="color:#94a3b8;">-- Query 2: Identify brute force attempts (failed attempts &gt; 5)</span><br>
<span style="color:#38bdf8;">SELECT</span> username, <span style="color:#38bdf8;">COUNT</span>(*) <span style="color:#38bdf8;">AS</span> failed_attempts<br>
<span style="color:#38bdf8;">FROM</span> auth_events<br>
<span style="color:#38bdf8;">WHERE</span> status = <span style="color:#facc15;">'FAIL'</span><br>
<span style="color:#38bdf8;">GROUP BY</span> username<br>
<span style="color:#38bdf8;">HAVING</span> <span style="color:#38bdf8;">COUNT</span>(*) &gt;= 5;
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">3. Google Cloud Platform (GCP) Security Pillars</h2>

<ul style="padding-left:20px;font-size:14px;line-height:1.8;">
  <li><strong>Cloud IAM:</strong> Roles (Viewer, Editor, Owner vs Predefined &amp; Custom). Principle of Least Privilege via Service Accounts.</li>
  <li><strong>Security Command Center (SCC):</strong> Centralized vulnerability and threat detection dashboard for GCP assets and IAM misconfigurations.</li>
  <li><strong>Chronicle SIEM:</strong> Petabyte-scale security telemetry search engine leveraging YARA-L detection rules.</li>
</ul>

</div>'''

def generate_cisco_cyberops_guide():
    return '''<div style="font-family:Arial,sans-serif;max-width:980px;margin:0 auto;padding:10px;line-height:1.7;color:#2c3e50;">

<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(139,0,0,0.15);">
  <div style="font-size:12px;font-weight:bold;text-transform:uppercase;letter-spacing:1px;color:#f5a623;margin-bottom:6px;">
    Texas Wesleyan University · Department of Computer Science &amp; IT
  </div>
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">🌐 Cisco CyberOps Associate (200-201) &amp; Security Operations Guide</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">Snort/Suricata Rule Writing, NetFlow Telemetry, &amp; Intrusion Analysis</p>
</div>

<div style="background:#f0fdf4;border-left:5px solid #16a34a;padding:18px 22px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <h3 style="margin:0 0 8px 0;color:#15803d;font-size:16px;font-weight:bold;">🛡️ Cisco Certified CyberOps Associate (CBROPS)</h3>
  <p style="margin:0;color:#166534;font-size:14px;">
    The <strong>Cisco 200-201 CBROPS</strong> certification certifies candidates to detect cybersecurity breaches, gather forensic evidence, analyze network packet captures (PCAP), configure NetFlow telemetry, and write IDS/IPS signatures.
  </p>
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:30px;">1. Snort &amp; Suricata Rule Syntax Anatomy</h2>

<div style="background:#1e293b;color:#f8fafc;padding:16px 20px;border-radius:8px;font-family:monospace;font-size:13px;line-height:1.6;margin-top:16px;">
<span style="color:#94a3b8;"># Snort Rule: Detecting SQL Injection in HTTP GET Request</span><br>
<span style="color:#f43f5e;">alert</span> tcp $EXTERNAL_NET any -&gt; $HTTP_SERVERS $HTTP_PORTS (<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#38bdf8;">msg:</span><span style="color:#facc15;">"WEB-ATTACK SQL Injection Attempt (UNION SELECT)"</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#38bdf8;">flow:</span>to_server,established;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#38bdf8;">content:</span><span style="color:#facc15;">"UNION"</span>; nocase;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#38bdf8;">content:</span><span style="color:#facc15;">"SELECT"</span>; nocase; distance:1;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#38bdf8;">classtype:</span>web-application-attack;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#38bdf8;">sid:</span>1000042;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#38bdf8;">rev:</span>1;<br>
)
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">2. NetFlow v9 / IPFIX Analysis for SOC Analysts</h2>

<table style="width:100%;border-collapse:collapse;margin-top:16px;font-size:13px;">
  <thead>
    <tr style="background:#1e293b;color:white;text-align:left;">
      <th style="padding:8px 10px;border:1px solid #0f172a;">NetFlow Field</th>
      <th style="padding:8px 10px;border:1px solid #0f172a;">Normal Baseline</th>
      <th style="padding:8px 10px;border:1px solid #0f172a;">Threat Indicator (Anomaly)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">Flow Duration</td><td style="padding:8px;border:1px solid #cbd5e1;">Seconds to minutes</td><td style="padding:8px;border:1px solid #cbd5e1;">Hours-long persistent beaconing (C2 channel).</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">Byte / Packet Ratio</td><td style="padding:8px;border:1px solid #cbd5e1;">Symmetric download/upload</td><td style="padding:8px;border:1px solid #cbd5e1;">Massive outbound volume with tiny inbound (Data Exfiltration).</td></tr>
    <tr><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">TCP Flags</td><td style="padding:8px;border:1px solid #cbd5e1;">SYN, ACK, FIN, PSH</td><td style="padding:8px;border:1px solid #cbd5e1;">High volume of SYN packets without ACK (SYN Flood DDoS or Port Scan).</td></tr>
  </tbody>
</table>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">3. The Diamond Model of Intrusion Analysis</h2>

<div style="background:#ffffff;border:2px solid #e2e8f0;padding:18px;border-radius:8px;margin-top:16px;text-align:center;">
  <p style="margin:0 0 12px 0;font-weight:bold;color:#8b0000;">THE DIAMOND MODEL: 4 CORE VERTICES</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;max-width:500px;margin:0 auto;text-align:left;font-size:13px;">
    <div style="background:#f1f5f9;padding:10px;border-radius:4px;"><strong>1. Adversary:</strong> The threat actor behind the attack.</div>
    <div style="background:#f1f5f9;padding:10px;border-radius:4px;"><strong>2. Capability:</strong> Tools, malware, exploits used.</div>
    <div style="background:#f1f5f9;padding:10px;border-radius:4px;"><strong>3. Infrastructure:</strong> C2 servers, IP domains, botnets.</div>
    <div style="background:#f1f5f9;padding:10px;border-radius:4px;"><strong>4. Victim:</strong> Target organization, asset, or persona.</div>
  </div>
</div>

</div>'''

def generate_network_ccna_guide():
    return '''<div style="font-family:Arial,sans-serif;max-width:980px;margin:0 auto;padding:10px;line-height:1.7;color:#2c3e50;">

<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(139,0,0,0.15);">
  <div style="font-size:12px;font-weight:bold;text-transform:uppercase;letter-spacing:1px;color:#f5a623;margin-bottom:6px;">
    Texas Wesleyan University · Department of Computer Science &amp; IT
  </div>
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">🌐 CompTIA Network+ &amp; Cisco CCNA (200-301) Dual Certification Hub</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">Mastering Subnetting, Routing Protocols, VLANs, &amp; Cisco CLI</p>
</div>

<div style="background:#f8fafc;border-left:5px solid #8b0000;padding:18px 22px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <h3 style="margin:0 0 8px 0;color:#8b0000;font-size:16px;font-weight:bold;">🎓 Dual Credential Strategy: Network+ vs. CCNA</h3>
  <p style="margin:0;color:#475569;font-size:14px;">
    In <strong>CIS-3321 Network Administration</strong>, the curriculum is uniquely mapped so you can sit for both the vendor-neutral <strong>CompTIA Network+ (N10-008/009)</strong> and the industry-standard <strong>Cisco CCNA (200-301)</strong>.
  </p>
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:30px;">1. IPv4 Rapid Subnetting Cheat Sheet</h2>

<table style="width:100%;border-collapse:collapse;margin-top:16px;font-size:13.5px;">
  <thead>
    <tr style="background:#8b0000;color:white;text-align:left;">
      <th style="padding:8px 10px;border:1px solid #700000;">Prefix (CIDR)</th>
      <th style="padding:8px 10px;border:1px solid #700000;">Subnet Mask</th>
      <th style="padding:8px 10px;border:1px solid #700000;">Block Size (Increment)</th>
      <th style="padding:8px 10px;border:1px solid #700000;">Usable Hosts</th>
      <th style="padding:8px 10px;border:1px solid #700000;">Typical Use Case</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">/24</td><td style="padding:8px;border:1px solid #cbd5e1;">255.255.255.0</td><td style="padding:8px;border:1px solid #cbd5e1;">1</td><td style="padding:8px;border:1px solid #cbd5e1;">254</td><td style="padding:8px;border:1px solid #cbd5e1;">Standard Departmental LAN</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">/25</td><td style="padding:8px;border:1px solid #cbd5e1;">255.255.255.128</td><td style="padding:8px;border:1px solid #cbd5e1;">128</td><td style="padding:8px;border:1px solid #cbd5e1;">126</td><td style="padding:8px;border:1px solid #cbd5e1;">Branch Office LAN</td></tr>
    <tr><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">/26</td><td style="padding:8px;border:1px solid #cbd5e1;">255.255.255.192</td><td style="padding:8px;border:1px solid #cbd5e1;">64</td><td style="padding:8px;border:1px solid #cbd5e1;">62</td><td style="padding:8px;border:1px solid #cbd5e1;">Server Subnet</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">/27</td><td style="padding:8px;border:1px solid #cbd5e1;">255.255.255.224</td><td style="padding:8px;border:1px solid #cbd5e1;">32</td><td style="padding:8px;border:1px solid #cbd5e1;">30</td><td style="padding:8px;border:1px solid #cbd5e1;">Management VLAN</td></tr>
    <tr><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">/28</td><td style="padding:8px;border:1px solid #cbd5e1;">255.255.255.240</td><td style="padding:8px;border:1px solid #cbd5e1;">16</td><td style="padding:8px;border:1px solid #cbd5e1;">14</td><td style="padding:8px;border:1px solid #cbd5e1;">DMZ Subnet</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">/29</td><td style="padding:8px;border:1px solid #cbd5e1;">255.255.255.248</td><td style="padding:8px;border:1px solid #cbd5e1;">8</td><td style="padding:8px;border:1px solid #cbd5e1;">6</td><td style="padding:8px;border:1px solid #cbd5e1;">HSRP / VRRP Cluster</td></tr>
    <tr><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">/30</td><td style="padding:8px;border:1px solid #cbd5e1;">255.255.255.252</td><td style="padding:8px;border:1px solid #cbd5e1;">4</td><td style="padding:8px;border:1px solid #cbd5e1;">2</td><td style="padding:8px;border:1px solid #cbd5e1;">Point-to-Point Router Link</td></tr>
  </tbody>
</table>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">2. Cisco IOS CLI Essential Command Reference</h2>

<div style="background:#1e293b;color:#f8fafc;padding:16px 20px;border-radius:8px;font-family:monospace;font-size:13px;line-height:1.6;margin-top:16px;">
<span style="color:#94a3b8;">! Configure 802.1Q Trunk Link on Switch</span><br>
Switch(config)# interface GigabitEthernet0/1<br>
Switch(config-if)# switchport mode trunk<br>
Switch(config-if)# switchport trunk allowed vlan 10,20,30<br>
Switch(config-if)# switchport trunk native vlan 99<br><br>
<span style="color:#94a3b8;">! Configure Single-Area OSPFv2 on Router</span><br>
Router(config)# router ospf 1<br>
Router(config-router)# router-id 1.1.1.1<br>
Router(config-router)# network 10.0.0.0 0.0.255.255 area 0<br>
Router(config-router)# passive-interface GigabitEthernet0/0
</div>

</div>'''

def generate_ccnp_enterprise_guide():
    return '''<div style="font-family:Arial,sans-serif;max-width:980px;margin:0 auto;padding:10px;line-height:1.7;color:#2c3e50;">

<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(139,0,0,0.15);">
  <div style="font-size:12px;font-weight:bold;text-transform:uppercase;letter-spacing:1px;color:#f5a623;margin-bottom:6px;">
    Texas Wesleyan University · Department of Computer Science &amp; IT
  </div>
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">🚀 Cisco CCNP Enterprise (350-401 ENCOR &amp; 300-410 ENARSI) Mastery Guide</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">Graduate Engineering: Multi-Area OSPF, BGP Path Selection, SD-WAN &amp; Automation</p>
</div>

<div style="background:#eff6ff;border-left:5px solid #2563eb;padding:18px 22px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <h3 style="margin:0 0 8px 0;color:#1e40af;font-size:16px;font-weight:bold;">🎓 Graduate Professional Preparation</h3>
  <p style="margin:0;color:#1e3a8a;font-size:14px;">
    In <strong>CSC-6361 Advanced Computer Networks</strong>, the course directly targets the <strong>Cisco CCNP Enterprise Core (350-401 ENCOR)</strong> and <strong>Enterprise Advanced Routing (300-410 ENARSI)</strong> blueprints.
  </p>
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:30px;">1. BGP Best Path Selection Algorithm (Strict Tie-Breaker Order)</h2>

<ol style="padding-left:22px;font-size:14px;line-height:1.8;">
  <li><strong>Weight:</strong> Cisco proprietary (Highest wins; default 32768 for locally originated, 0 for learned).</li>
  <li><strong>Local Preference:</strong> Highest wins (Default 100; shared across iBGP within AS).</li>
  <li><strong>Locally Originated:</strong> Prefer paths originated locally via <code>network</code> or <code>aggregate-address</code>.</li>
  <li><strong>AS-Path Length:</strong> Shortest AS-Path wins.</li>
  <li><strong>Origin Code:</strong> Prefer IGP &gt; EGP &gt; Incomplete (?).</li>
  <li><strong>MED (Multi-Exit Discriminator):</strong> Lowest wins (Metric sent to external AS).</li>
  <li><strong>Neighbor Type:</strong> Prefer eBGP over iBGP.</li>
  <li><strong>IGP Metric:</strong> Lowest metric to next-hop.</li>
  <li><strong>Oldest Route:</strong> Prefer oldest eBGP route.</li>
  <li><strong>Router ID:</strong> Lowest BGP router ID wins.</li>
</ol>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">2. Cisco SD-WAN Architecture Plane Separation</h2>

<table style="width:100%;border-collapse:collapse;margin-top:16px;font-size:13.5px;">
  <thead>
    <tr style="background:#1e293b;color:white;text-align:left;">
      <th style="padding:10px;border:1px solid #0f172a;">Plane</th>
      <th style="padding:10px;border:1px solid #0f172a;">Component</th>
      <th style="padding:10px;border:1px solid #0f172a;">Function &amp; Protocol</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:10px;border:1px solid #cbd5e1;font-weight:bold;color:#0369a1;">Orchestration</td><td style="padding:10px;border:1px solid #cbd5e1;">vBond</td><td style="padding:10px;border:1px solid #cbd5e1;">Authenticates all nodes; facilitates NAT traversal.</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:10px;border:1px solid #cbd5e1;font-weight:bold;color:#15803d;">Management</td><td style="padding:10px;border:1px solid #cbd5e1;">vManage</td><td style="padding:10px;border:1px solid #cbd5e1;">Single pane of glass GUI; configuration templates &amp; REST APIs.</td></tr>
    <tr><td style="padding:10px;border:1px solid #cbd5e1;font-weight:bold;color:#b45309;">Control Plane</td><td style="padding:10px;border:1px solid #cbd5e1;">vSmart</td><td style="padding:10px;border:1px solid #cbd5e1;">Distributes routing, policy &amp; crypto keys via OMP (Overlay Management Protocol).</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:10px;border:1px solid #cbd5e1;font-weight:bold;color:#b91c1c;">Data Plane</td><td style="padding:10px;border:1px solid #cbd5e1;">vEdge / cEdge</td><td style="padding:10px;border:1px solid #cbd5e1;">Physical/virtual routers forwarding user traffic over IPsec tunnels.</td></tr>
  </tbody>
</table>

</div>'''


def deploy_all_certification_materials():
    print("="*75)
    print("DEPLOYING MULTI-CERTIFICATION ECOSYSTEM TO CANVAS")
    print("="*75)

    # 1. CIS-4328 (Course 13090)
    print("\n--- Deploying CIS-4328 Certification Pages ---")
    cid_4328 = 13090
    mid_4328 = 87948 # Getting Started & Course Orientation

    pages_4328 = [
        ("🎓 Multi-Certification Master Roadmap & Domain Crosswalk", generate_multi_cert_roadmap()),
        ("🛡️ ISC2 Certified in Cybersecurity (CC) Exam Prep Guide", generate_isc2_cc_guide()),
        ("🔍 CompTIA CySA+ (CS0-003) Analyst Mastery Guide", generate_cysa_plus_guide()),
        ("☁️ Google Cybersecurity Certificate & Cloud Security Bridge", generate_google_cyber_guide()),
        ("🌐 Cisco CyberOps Associate & Security Operations Guide", generate_cisco_cyberops_guide()),
    ]

    for idx, (title, html) in enumerate(pages_4328, start=7):
        url = create_or_update_page(cid_4328, title, html)
        add_item_to_module(cid_4328, mid_4328, title, url, pos=idx)
        print(f"  ✅ CIS-4328: Deployed '{title}'")
        time.sleep(0.4)

    # 2. CIS-3321 (Course 13089)
    print("\n--- Deploying CIS-3321 Certification Hub ---")
    cid_3321 = 13089
    mid_3321 = 87931 # Getting Started & Course Orientation
    net_title = "🌐 CompTIA Network+ & Cisco CCNA (200-301) Dual Certification Hub"
    net_url = create_or_update_page(cid_3321, net_title, generate_network_ccna_guide())
    add_item_to_module(cid_3321, mid_3321, net_title, net_url, pos=7)
    print(f"  ✅ CIS-3321: Deployed '{net_title}'")

    # 3. CSC-6361 (Course 12666)
    print("\n--- Deploying CSC-6361 CCNP Enterprise Guide ---")
    cid_6361 = 12666
    mid_6361 = 88222 # Course Information & Resources
    ccnp_title = "🚀 Cisco CCNP Enterprise (350-401 ENCOR & 300-410 ENARSI) Mastery Guide"
    ccnp_url = create_or_update_page(cid_6361, ccnp_title, generate_ccnp_enterprise_guide())
    add_item_to_module(cid_6361, mid_6361, ccnp_title, ccnp_url, pos=6)
    print(f"  ✅ CSC-6361: Deployed '{ccnp_title}'")

    print("\n" + "="*75)
    print("✅ ALL CERTIFICATION MATERIALS DEPLOYED AND LINKED!")
    print("="*75)

if __name__ == '__main__':
    deploy_all_certification_materials()
