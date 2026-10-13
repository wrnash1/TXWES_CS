# -*- coding: utf-8 -*-
"""
Comprehensive Lab Overhaul Script:
1. Publishes Central Lab Setup Guides to Course Orientation modules in CIS-3321, CIS-4328, and CSC-6361
2. Updates all 39 lab assignments with clean titles and Quick-Start Checklists
3. Updates Module Item titles in Canvas
4. Posts reassuring announcements to CIS-3321 and CIS-4328
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

# ==============================================================================
# 1. CENTRAL LAB SETUP GUIDES (HTML GENERATORS)
# ==============================================================================

def generate_packet_tracer_guide_html():
    return '''<div style="font-family:Arial,sans-serif;max-width:980px;margin:0 auto;padding:10px;line-height:1.7;color:#2c3e50;">

<div style="background:linear-gradient(135deg,#1b365d,#002855);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(27,54,93,0.25);">
  <div style="font-size:12px;font-weight:bold;text-transform:uppercase;letter-spacing:1px;color:#f5a623;margin-bottom:6px;">
    Texas Wesleyan University · Department of Computer Science &amp; IT
  </div>
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">🛠️ Hands-On Lab Setup &amp; Cisco Packet Tracer Installation Guide</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">Complete Step-by-Step Instructions: Free Download, Installation, Topology Building, &amp; Submissions</p>
</div>

<div style="background:#e8f4f8;border-left:5px solid #0056b3;padding:18px 22px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <h3 style="margin:0 0 8px 0;color:#003d80;font-size:16px;font-weight:bold;">📌 Welcome to Your Hands-On Network Simulation Environment!</h3>
  <p style="margin:0;color:#004085;font-size:14px;line-height:1.6;">
    In this course, you will build real-world enterprise network topologies, configure routers and switches, inspect data packet encapsulations, and troubleshoot communication failures using <strong>Cisco Packet Tracer</strong>. Cisco Packet Tracer is the industry-standard network simulation software created by Cisco Systems, and it is <strong>100% free</strong> for all students.
  </p>
</div>

<h2 style="color:#1b365d;border-bottom:2px solid #1b365d;padding-bottom:8px;margin-top:30px;">Step 1: Download Cisco Packet Tracer (100% Free Official Link)</h2>

<div style="background:#ffffff;border:1px solid #cbd5e1;padding:20px;border-radius:8px;margin-top:14px;box-shadow:0 2px 4px rgba(0,0,0,0.05);">
  <p style="margin:0 0 12px 0;font-size:14.5px;color:#1e293b;">
    Cisco provides Packet Tracer free through its official <em>Skills for All</em> / <em>Networking Academy</em> educational portal:
  </p>
  <div style="background:#f1f5f9;border:1px solid #cbd5e1;padding:14px 18px;border-radius:6px;margin-bottom:14px;">
    👉 <strong>Official Download Link:</strong> <a href="https://skillsforall.com/course/getting-started-cisco-packet-tracer" target="_blank" style="color:#0056b3;font-weight:bold;text-decoration:underline;">Cisco Skills for All: Getting Started with Cisco Packet Tracer</a>
  </div>
  <ol style="margin:0;padding-left:22px;font-size:14px;line-height:1.8;color:#334155;">
    <li>Click the link above and click <strong>"Get Started"</strong> or <strong>"Sign In"</strong>.</li>
    <li>Create a free account using your Texas Wesleyan student email (or log in with an existing Google or Cisco account).</li>
    <li>Navigate to the download page and select the installer for your operating system:
      <ul>
        <li><strong>Windows:</strong> <code>Cisco Packet Tracer 8.2+ (64-bit Desktop)</code></li>
        <li><strong>macOS:</strong> <code>Cisco Packet Tracer 8.2+ for macOS (Intel or Apple Silicon M1/M2/M3)</code></li>
        <li><strong>Linux:</strong> <code>Ubuntu 64-bit (.deb package)</code></li>
      </ul>
    </li>
    <li>Run the installer and follow the standard on-screen prompts.</li>
  </ol>
</div>

<h2 style="color:#1b365d;border-bottom:2px solid #1b365d;padding-bottom:8px;margin-top:36px;">Step 2: First-Time Launch &amp; Login</h2>

<div style="background:#ffffff;border:1px solid #cbd5e1;padding:20px;border-radius:8px;margin-top:14px;">
  <p style="margin:0 0 10px 0;font-size:14px;color:#334155;">
    When you open Packet Tracer for the first time, you will see a login prompt:
  </p>
  <ul style="margin:0;padding-left:22px;font-size:14px;line-height:1.8;color:#334155;">
    <li>Select <strong>"Skills for All"</strong> (green logo) or <strong>"Cisco Networking Academy"</strong> (blue logo).</li>
    <li>Check the box <strong>"Keep me logged in"</strong> (this ensures you won't have to log in again for 3 months).</li>
    <li>Enter the credentials you created in Step 1. The main Packet Tracer workspace will open!</li>
  </ul>
</div>

<h2 style="color:#1b365d;border-bottom:2px solid #1b365d;padding-bottom:8px;margin-top:36px;">Step 3: Understanding the Packet Tracer Interface</h2>

<table style="width:100%;border-collapse:collapse;margin-top:14px;font-size:13.5px;">
  <thead>
    <tr style="background:#1e293b;color:white;text-align:left;">
      <th style="padding:10px;border:1px solid #0f172a;">Area / Tool</th>
      <th style="padding:10px;border:1px solid #0f172a;">Location</th>
      <th style="padding:10px;border:1px solid #0f172a;">What It Does</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:10px;border:1px solid #cbd5e1;font-weight:bold;color:#0369a1;">Logical Workspace</td><td style="padding:10px;border:1px solid #cbd5e1;">Center large white area</td><td style="padding:10px;border:1px solid #cbd5e1;">Where you drag and drop devices, draw cables, and build topologies.</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:10px;border:1px solid #cbd5e1;font-weight:bold;color:#0369a1;">Device Panel</td><td style="padding:10px;border:1px solid #cbd5e1;">Bottom-left corner</td><td style="padding:10px;border:1px solid #cbd5e1;">Contains Routers, Switches, End Devices (PCs/Laptops/Servers), and Connections (cables).</td></tr>
    <tr><td style="padding:10px;border:1px solid #cbd5e1;font-weight:bold;color:#0369a1;">Connections (Cables)</td><td style="padding:10px;border:1px solid #cbd5e1;">Lightning bolt icon (bottom-left)</td><td style="padding:10px;border:1px solid #cbd5e1;">Select Copper Straight-Through (solid black line) or Copper Crossover (dashed black line).</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:10px;border:1px solid #cbd5e1;font-weight:bold;color:#0369a1;">Realtime vs. Simulation Mode</td><td style="padding:10px;border:1px solid #cbd5e1;">Bottom-right corner tabs</td><td style="padding:10px;border:1px solid #cbd5e1;"><strong>Realtime:</strong> Normal network operation.<br><strong>Simulation:</strong> Allows you to pause time, step through packet transmissions, and inspect OSI layer encapsulation!</td></tr>
  </tbody>
</table>

<h2 style="color:#1b365d;border-bottom:2px solid #1b365d;padding-bottom:8px;margin-top:36px;">Step 4: Completing &amp; Submitting Your Weekly Lab</h2>

<div style="background:#f8fafc;border:2px solid #1b365d;padding:20px;border-radius:8px;margin-top:14px;">
  <p style="margin:0 0 10px 0;font-weight:bold;color:#1b365d;font-size:15px;">Every lab assignment requires TWO deliverables:</p>
  <ol style="margin:0;padding-left:22px;font-size:14px;line-height:1.8;color:#1e293b;">
    <li><strong>Deliverable 1 — Your Packet Tracer Topology File (<code>.pkt</code>):</strong>
      <br>In Packet Tracer, click <strong>File &rarr; Save As</strong>. Name your file using the standard format:
      <br><code style="background:#1e293b;color:#f8fafc;padding:3px 8px;border-radius:4px;">LastName_FirstName_Course_MXX_Lab.pkt</code> (e.g. <code>Smith_John_CIS3321_M01_Lab.pkt</code>).
    </li>
    <li><strong>Deliverable 2 — Your Written Lab Report / Answers (<code>.pdf</code>):</strong>
      <br>Open Microsoft Word or Google Docs. Copy the questions/verification steps from the lab assignment. Type your answers, paste screenshots of successful <code>ping</code> tests or Simulation Mode PDUs, and click <strong>File &rarr; Export / Save As &rarr; PDF</strong>.
      <br><code style="background:#1e293b;color:#f8fafc;padding:3px 8px;border-radius:4px;">LastName_FirstName_Course_MXX_LabReport.pdf</code>
    </li>
    <li><strong>Upload to Canvas:</strong> Go to the Canvas assignment page, click <strong>Submit Assignment</strong>, and upload BOTH files before submitting.</li>
  </ol>
</div>

<h2 style="color:#1b365d;border-bottom:2px solid #1b365d;padding-bottom:8px;margin-top:36px;">Troubleshooting &amp; Frequently Asked Questions (FAQ)</h2>

<div style="background:#fffbeb;border:1px solid #fde68a;padding:18px 22px;border-radius:8px;margin-top:14px;">
  <p style="margin:0 0 8px 0;font-weight:bold;color:#92400e;font-size:14.5px;">Q: My link lights between the switch and PC are orange, not green. Is something broken?</p>
  <p style="margin:0 0 14px 0;font-size:13.5px;color:#78350f;"><strong>A:</strong> No! Cisco switches run Spanning Tree Protocol (STP). When a cable is plugged in, the switch port stays orange for 30–50 seconds while listening and learning. Click the "Fast Forward Time" button (two right arrows in the bottom toolbar) or wait 30 seconds, and the link light will turn green.</p>

  <p style="margin:0 0 8px 0;font-weight:bold;color:#92400e;font-size:14.5px;">Q: I got a timeout on my first ping in Packet Tracer. Did I configure it wrong?</p>
  <p style="margin:0 0 14px 0;font-size:13.5px;color:#78350f;"><strong>A:</strong> The first ping across a switch often times out because the switch and host need to perform an ARP (Address Resolution Protocol) broadcast to resolve the destination MAC address. Run the ping command a second time — all 4 packets will succeed!</p>

  <p style="margin:0 0 8px 0;font-weight:bold;color:#92400e;font-size:14.5px;">Q: Can I complete these labs on a Mac or Chromebook?</p>
  <p style="margin:0;font-size:13.5px;color:#78350f;"><strong>A:</strong> Packet Tracer runs natively on macOS (Apple Silicon M1/M2/M3 and Intel). On a Chromebook, you can run the Android APK version from Google Play or install the Linux (.deb) version inside ChromeOS Linux Development environment.</p>
</div>

</div>'''

def generate_security_lab_guide_html():
    return '''<div style="font-family:Arial,sans-serif;max-width:980px;margin:0 auto;padding:10px;line-height:1.7;color:#2c3e50;">

<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(139,0,0,0.15);">
  <div style="font-size:12px;font-weight:bold;text-transform:uppercase;letter-spacing:1px;color:#f5a623;margin-bottom:6px;">
    Texas Wesleyan University · Department of Computer Science &amp; IT
  </div>
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">🛠️ Security Analyst Lab Guide &amp; Deliverable Submission Template</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">How to Complete Your Weekly Security Case Study &amp; PBQ Worksheets (No Special Tools Required!)</p>
</div>

<div style="background:#f0fdf4;border-left:5px solid #22c55e;padding:18px 22px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <h3 style="margin:0 0 8px 0;color:#15803d;font-size:16px;font-weight:bold;">🎉 Good News: NO Complex Software Installation Required!</h3>
  <p style="margin:0;color:#166534;font-size:14px;line-height:1.6;">
    Students often ask: <em>"Do I need to install Kali Linux, Wireshark, or hacking tools on my computer for this course?"</em><br>
    <strong>The answer is NO!</strong> In <strong>CIS-4328 Information Security</strong>, the labs are structured as professional <strong>Security Analyst Case Studies &amp; Performance-Based Question (PBQ) Investigations</strong>. You act as an enterprise cybersecurity consultant analyzing real incidents, classifying threat vectors, calculating risk metrics, and designing mitigation policies.
  </p>
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:30px;">1. What Every Security Lab Consists Of</h2>

<p>Each weekly lab assignment presents a realistic enterprise scenario (such as a financial institution, healthcare clinic, or SaaS provider) and provides structured investigation prompts divided into 2 to 3 parts:</p>

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin-top:14px;">
  <div style="background:#ffffff;border:1px solid #e2e8f0;border-left:4px solid #8b0000;padding:16px;border-radius:6px;box-shadow:0 2px 4px rgba(0,0,0,0.05);">
    <h4 style="margin:0 0 6px 0;color:#8b0000;">Part A: Scenario &amp; Threat Classification</h4>
    <p style="margin:0;font-size:13px;color:#475569;">Analyze 5 specific incident logs or event descriptions. Identify the Threat Actor (Nation-State, Insider, Hacktivist), the CIA Triad property impacted, and the attack type.</p>
  </div>
  <div style="background:#ffffff;border:1px solid #e2e8f0;border-left:4px solid #b22222;padding:16px;border-radius:6px;box-shadow:0 2px 4px rgba(0,0,0,0.05);">
    <h4 style="margin:0 0 6px 0;color:#b22222;">Part B: Security Control Mapping</h4>
    <p style="margin:0;font-size:13px;color:#475569;">Map recommended countermeasures across Control Categories (Physical, Technical, Administrative) and Control Functions (Preventive, Detective, Corrective, Compensating).</p>
  </div>
  <div style="background:#ffffff;border:1px solid #e2e8f0;border-left:4px solid #059669;padding:16px;border-radius:6px;box-shadow:0 2px 4px rgba(0,0,0,0.05);">
    <h4 style="margin:0 0 6px 0;color:#047857;">Part C: Executive Analysis &amp; Security+ Reflection</h4>
    <p style="margin:0;font-size:13px;color:#475569;">Synthesize your findings into a 250–400 word executive memo explaining the organizational risk posture and connecting the case study to CompTIA Security+ exam logic.</p>
  </div>
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">2. Standard Lab Report Template (Copy &amp; Paste into Word / Docs)</h2>

<div style="background:#1e293b;color:#f8fafc;padding:18px 22px;border-radius:8px;font-family:monospace;font-size:13px;line-height:1.6;margin-top:14px;">
================================================================================<br>
CIS-4328 Information Security — Lab Report: Module [XX]<br>
Student Name: [Your First and Last Name]<br>
Date: [Submission Date]<br>
Lab Title: [Module Lab Title from Canvas]<br>
================================================================================<br><br>
1. EXECUTIVE SUMMARY<br>
[2–3 paragraphs summarizing the organization's security posture, the primary threat<br>
vectors identified, and the strategic direction of your recommendations.]<br><br>
2. INCIDENT ANALYSIS &amp; CLASSIFICATION TABLE<br>
| Incident # | Threat Actor Type | CIA Triad Violated | Attack Category | Recommended Control |<br>
| Incident 1 | [e.g. Insider]     | [e.g. Integrity]   | [e.g. Tampering]| [e.g. FIM / Hashing]|<br>
| Incident 2 | [e.g. Hacktivist]  | [e.g. Availability]| [e.g. DDoS]     | [e.g. Cloudflare]   |<br><br>
3. TECHNICAL CONTROL RECOMMENDATIONS &amp; JUSTIFICATION<br>
[Detail each recommended control. Explain whether it is Physical, Technical, or<br>
Administrative, and justify why it solves the specific root cause.]<br><br>
4. COMPTIA SECURITY+ (SY0-701) EXAM REFLECTION<br>
[Explain how the concepts in this case study appear on the Security+ exam and how<br>
you reasoned through the trade-offs.]
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">3. Step-by-Step Submission Guide</h2>

<ol style="padding-left:22px;font-size:14px;line-height:1.8;color:#334155;">
  <li><strong>Open Word, Google Docs, or Pages:</strong> Copy the scenario questions and template headers into your document.</li>
  <li><strong>Read the Module Incident Descriptions:</strong> Refer back to the Module Reading Guide to apply the exact technical definitions.</li>
  <li><strong>Complete Your Analysis:</strong> Fill out the classification tables and write complete, professional sentences for your executive recommendations.</li>
  <li><strong>Export as PDF:</strong> In your word processor, click <strong>File &rarr; Save As / Export &rarr; PDF (.pdf)</strong>.</li>
  <li><strong>Submit to Canvas:</strong> Go to the assignment in Canvas, click <strong>Submit Assignment</strong>, attach your PDF, and submit before Sunday at 11:59 PM CST.</li>
</ol>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">Grading Rubric &amp; How to Earn 100/100 Points</h2>

<table style="width:100%;border-collapse:collapse;margin-top:14px;font-size:13px;">
  <thead>
    <tr style="background:#8b0000;color:white;text-align:left;">
      <th style="padding:10px;border:1px solid #700000;">Rubric Criterion</th>
      <th style="padding:10px;border:1px solid #700000;">Points</th>
      <th style="padding:10px;border:1px solid #700000;">Requirements for Full Marks</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:8px 10px;border:1px solid #cbd5e1;font-weight:bold;">Threat &amp; Incident Classification</td><td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:center;font-weight:bold;">40 pts</td><td style="padding:8px 10px;border:1px solid #cbd5e1;">All incidents correctly categorized by Threat Actor, CIA property, and Attack Vector.</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:8px 10px;border:1px solid #cbd5e1;font-weight:bold;">Control Selection &amp; Justification</td><td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:center;font-weight:bold;">35 pts</td><td style="padding:8px 10px;border:1px solid #cbd5e1;">Recommended controls correctly mapped to category (Tech/Admin/Phys) with technical justification.</td></tr>
    <tr><td style="padding:8px 10px;border:1px solid #cbd5e1;font-weight:bold;">Executive Memo &amp; Exam Reflection</td><td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:center;font-weight:bold;">25 pts</td><td style="padding:8px 10px;border:1px solid #cbd5e1;">250+ words of clear, professional synthesis citing course concepts and Security+ exam domains.</td></tr>
  </tbody>
</table>

</div>'''

print("Central Lab Guides HTML generators ready.")

# ==============================================================================
# 2. QUICK-START BANNER HTML GENERATORS
# ==============================================================================

def get_packet_tracer_banner_html(course_id: int) -> str:
    return f'''
<div style="background: #eff6ff; border: 2px solid #3b82f6; border-radius: 8px; padding: 20px 24px; margin-bottom: 24px; box-shadow: 0 4px 12px rgba(59, 130, 246, 0.1);">
  <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
    <span style="font-size: 24px;">🛠️</span>
    <h2 style="margin: 0; color: #1d4ed8; font-size: 18px; font-weight: bold;">
      PACKET TRACER LAB QUICK-START &amp; SUBMISSION CHECKLIST
    </h2>
  </div>
  <p style="margin: 0 0 12px 0; font-size: 14px; color: #1e3a8a; line-height: 1.6;">
    This is a hands-on network simulation lab using <strong>Cisco Packet Tracer</strong>. Please review these simple instructions before beginning:
  </p>
  <div style="background: white; border: 1px solid #bfdbfe; border-radius: 6px; padding: 14px 18px; margin-bottom: 12px; font-size: 13.5px; line-height: 1.7; color: #1e293b;">
    <strong>1. Required Software:</strong> Cisco Packet Tracer (Free via <a href="https://skillsforall.com/course/getting-started-cisco-packet-tracer" target="_blank" style="color: #2563eb; font-weight: bold; text-decoration: underline;">Cisco Skills for All / NetAcad</a>).<br>
    <strong>2. Setup Instructions:</strong> See the <a href="/courses/{course_id}/pages/hands-on-lab-setup-and-cisco-packet-tracer-installation-guide" style="color: #2563eb; font-weight: bold; text-decoration: underline;">🛠️ Lab Setup &amp; Packet Tracer Guide</a> in the Course Orientation module for a complete download &amp; installation walkthrough.<br>
    <strong>3. Deliverables to Submit:</strong>
    <ul style="margin: 6px 0 0 20px; padding: 0;">
      <li>Your completed Cisco Packet Tracer network topology file (<strong>.pkt</strong> format).</li>
      <li>Your written lab report / verification answers saved as a <strong>PDF</strong> document.</li>
    </ul>
  </div>
  <div style="font-size: 12.5px; color: #1e40af;">
    💡 <em>Need help getting started? Check the Lab Setup Guide in the Course Orientation module or reach out to Professor Nash via Canvas Inbox!</em>
  </div>
</div>
'''

def get_security_lab_banner_html(course_id: int) -> str:
    return f'''
<div style="background: #f0fdf4; border: 2px solid #22c55e; border-radius: 8px; padding: 20px 24px; margin-bottom: 24px; box-shadow: 0 4px 12px rgba(34, 197, 94, 0.1);">
  <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
    <span style="font-size: 24px;">📝</span>
    <h2 style="margin: 0; color: #15803d; font-size: 18px; font-weight: bold;">
      SECURITY ANALYST LAB QUICK-START &amp; SUBMISSION CHECKLIST
    </h2>
  </div>
  <p style="margin: 0 0 12px 0; font-size: 14px; color: #166534; line-height: 1.6;">
    This is an analytical <strong>Security Case Study &amp; PBQ Worksheet</strong>. Please review these simple instructions before beginning:
  </p>
  <div style="background: white; border: 1px solid #bbf7d0; border-radius: 6px; padding: 14px 18px; margin-bottom: 12px; font-size: 13.5px; line-height: 1.7; color: #1e293b;">
    <strong>1. Software Required:</strong> <strong>NO complex tools or software required!</strong> All work is completed using standard word processing software (Microsoft Word, Google Docs, or Pages).<br>
    <strong>2. How to Complete:</strong> Copy the scenario questions/tables below into your word processor, complete your threat analysis and technical recommendations, and export the document.<br>
    <strong>3. Deliverables to Submit:</strong> Upload your completed analysis report as a <strong>PDF (.pdf)</strong> or Word document (<strong>.docx</strong>) to this Canvas assignment before the deadline.<br>
    <strong>4. Lab Guide &amp; Template:</strong> See the <a href="/courses/{course_id}/pages/security-analyst-lab-guide-and-deliverable-submission-template" style="color: #15803d; font-weight: bold; text-decoration: underline;">🛠️ Security Analyst Lab Guide &amp; Template</a> in the Course Orientation module for an exemplar report format.
  </div>
  <div style="font-size: 12.5px; color: #166534;">
    💡 <em>This lab trains you directly on the Performance-Based Question (PBQ) scenario format used in the CompTIA Security+ (SY0-701) and CySA+ exams!</em>
  </div>
</div>
'''


# ==============================================================================
# 3. LAB TITLES MAP
# ==============================================================================

CLEAN_TITLES_CIS3321 = {
    1: "Lab (M01): OSI Model Observation & Star Topology (Packet Tracer)",
    2: "Lab (M02): Protocol Identification & Command-Line Diagnostics (Packet Tracer)",
    3: "Lab (M03): IPv4 Subnetting Calculations & Verification (Packet Tracer)",
    4: "Lab (M04): IPv6 Addressing & EUI-64 Configuration (Packet Tracer)",
    5: "Lab (M05): Switch MAC Address Tables & Traffic Flow (Packet Tracer)",
    6: "Lab (M06): Wireless Networking & WPA3 Security (Packet Tracer)",
    7: "Lab (M07): Network Monitoring, SNMP & Syslog (Packet Tracer)",
    8: "Lab (M08): Network Security Concepts & ACLs (Packet Tracer)",
    9: "Lab (M09): Network Services: DNS, DHCP, and NTP (Packet Tracer)",
    10: "Lab (M10): Routing Protocols: Static Routes & OSPF (Packet Tracer)",
    11: "Lab (M11): Switching: VLANs, 802.1Q Trunks & STP (Packet Tracer)",
    12: "Lab (M12): Wide Area Networks & IPsec VPNs (Packet Tracer)",
    13: "Lab (M13): Unified Communications, VoIP & QoS (Packet Tracer)",
    14: "Lab (M14): Network Troubleshooting Methodology (Packet Tracer)",
    15: "Lab (M15): Network Documentation & Topology Baselines (Packet Tracer)",
    16: "Lab (M16): Comprehensive Network+ Capstone Review (Packet Tracer)",
}

CLEAN_TITLES_CIS4328 = {
    1: "Lab (M01): Threat & Control Classification (Security Case Study)",
    2: "Lab (M02): Social Engineering Analysis & Countermeasures (Security Case Study)",
    3: "Lab (M03): Application Attacks & Cryptographic Analysis (Security Case Study)",
    4: "Lab (M04): Threat Analysis & IoC Investigation (Security Case Study)",
    5: "Lab (M05): Cryptography, Hash Verification & PKI (Security Case Study)",
    6: "Lab (M06): Identity & Access Management Design (Security Case Study)",
    7: "Lab (M07): Network Security Architecture & Firewalls (Security Case Study)",
    8: "Lab (M08): Endpoint Security Assessment & Hardening (Security Case Study)",
    9: "Lab (M09): Cloud Security & Shared Responsibility (Security Case Study)",
    10: "Lab (M10): Application Security & OWASP Top 10 (Security Case Study)",
    11: "Lab (M11): Incident Response Playbook Simulation (Security Case Study)",
    12: "Lab (M12): Digital Forensics & Evidence Handling (Security Case Study)",
    13: "Lab (M13): Risk Management, BIA & Quantitative Analysis (Security Case Study)",
    14: "Lab (M14): Governance, Compliance & Regulatory Frameworks (Security Case Study)",
    15: "Lab (M15): Security Operations & SIEM Log Triage (Security Case Study)",
    16: "Lab (M16): Comprehensive Security+ Capstone PBQ (Security Case Study)",
}

CLEAN_TITLES_CSC6361 = {
    1: "Lab (M01): Multi-Area OSPF & EIGRP Redistribution (Packet Tracer)",
    2: "Lab (M02): Campus Switching: VLANs, STP & EtherChannel (Packet Tracer)",
    3: "Lab (M03): WAN Technologies: GRE over IPsec with OSPF (Packet Tracer)",
    4: "Lab (M04): Enterprise Security & Infrastructure Hardening (Packet Tracer)",
    5: "Lab (M05): QoS & HSRP High Availability Configuration (Packet Tracer)",
    6: "Lab (M06): Cloud Networking & Hybrid Architectures (Packet Tracer)",
    7: "Lab (M07): Capstone Enterprise Troubleshooting Lab (Packet Tracer)",
}


# ==============================================================================
# 4. EXECUTE OVERHAUL
# ==============================================================================

def overhaul_course_labs(cid: int, mid_orient: int, titles_map: dict, is_network: bool):
    print(f"\n{'='*75}")
    print(f"OVERHAULING LABS FOR COURSE ID: {cid}")
    print(f"{'='*75}")

    # 1. Publish Central Guide
    if is_network:
        guide_title = "🛠️ Hands-On Lab Setup & Cisco Packet Tracer Installation Guide"
        guide_html = generate_packet_tracer_guide_html()
    else:
        guide_title = "🛠️ Security Analyst Lab Guide & Deliverable Submission Template"
        guide_html = generate_security_lab_guide_html()

    guide_url = create_or_update_page(cid, guide_title, guide_html)
    add_item_to_module(cid, mid_orient, guide_title, guide_url, pos=4)
    print(f"  ✅ Published & Linked Central Guide: {guide_title}")

    # 2. Fetch all assignments in course
    assignments = api_get(f"/courses/{cid}/assignments?per_page=100")
    if not isinstance(assignments, list):
        print(f"  ❌ Failed to fetch assignments for {cid}")
        return

    # Map assignments by module number
    lab_assignments = {}
    for a in assignments:
        if 'lab' in a['name'].lower():
            m_match = re.search(r'M0?(\d+)', a['name'])
            if m_match:
                mod_num = int(m_match.group(1))
                lab_assignments[mod_num] = a

    # 3. Update each lab assignment
    banner_html = get_packet_tracer_banner_html(cid) if is_network else get_security_lab_banner_html(cid)

    for mod_num, clean_title in sorted(titles_map.items()):
        asgn = lab_assignments.get(mod_num)
        if not asgn:
            print(f"  ⚠️ No lab assignment found for Module {mod_num}")
            continue

        aid = asgn['id']
        curr_desc = asgn.get('description', '')

        # Prepend banner if not already present
        if 'QUICK-START & SUBMISSION CHECKLIST' not in curr_desc:
            new_desc = banner_html + curr_desc
        else:
            new_desc = curr_desc

        payload = {
            'assignment': {
                'name': clean_title,
                'description': new_desc,
            }
        }
        res = api_put(f"/courses/{cid}/assignments/{aid}", payload)
        if res.get('id'):
            print(f"  ✅ Updated M{mod_num:02d} Lab: {clean_title}")
        else:
            print(f"  ❌ Failed to update M{mod_num:02d} Lab ({aid})")
        time.sleep(0.3)

    # 4. Sync module item titles
    modules = api_get(f"/courses/{cid}/modules?per_page=50&include[]=items")
    if isinstance(modules, list):
        for m in modules:
            for it in m.get('items', []):
                if it['type'] == 'Assignment' and 'lab' in it['title'].lower():
                    m_match = re.search(r'M0?(\d+)', it['title'])
                    if m_match:
                        mod_num = int(m_match.group(1))
                        clean_t = titles_map.get(mod_num)
                        if clean_t and it['title'] != clean_t:
                            api_put(f"/courses/{cid}/modules/{m['id']}/items/{it['id']}", {
                                'module_item': {'title': clean_t}
                            })
                            print(f"    🔄 Synced Module Item Title -> {clean_t}")
                            time.sleep(0.2)


def post_student_announcements():
    print(f"\n{'='*75}")
    print("POSTING CLARIFYING LAB ANNOUNCEMENTS TO STUDENTS")
    print("="*75)

    ann_3321_html = '''<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #1e293b; line-height: 1.7; max-width: 820px; margin: 0 auto;">
  <div style="background: linear-gradient(135deg, #1b365d 0%, #002855 100%); color: #ffffff; padding: 24px 30px; border-radius: 10px; margin-bottom: 24px; box-shadow: 0 4px 12px rgba(27, 54, 93, 0.2);">
    <div style="font-size: 13px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; color: #f5a623; margin-bottom: 6px;">
      Texas Wesleyan University • Department of Computer Science &amp; IT
    </div>
    <h2 style="margin: 0; font-size: 22px; font-weight: 700; color: #ffffff;">
      📢 Important Lab Guidance: Free Cisco Packet Tracer Setup &amp; Submission Walkthrough
    </h2>
    <div style="font-size: 13px; color: #ffcccc; margin-top: 6px;">
      From: Professor William Nash
    </div>
  </div>

  <div style="background: #eff6ff; border-left: 5px solid #2563eb; padding: 18px 22px; border-radius: 6px; margin-bottom: 22px;">
    <h3 style="margin: 0 0 8px 0; color: #1e40af; font-size: 16px; font-weight: bold;">
      🛠️ Everything You Need to Complete Your Hands-On Labs
    </h3>
    <p style="margin: 0; color: #1e3a8a; font-size: 14.5px;">
      Several students reached out asking how to set up and complete the weekly hands-on labs. All lab assignments have been renamed with clear titles and step-by-step checklists to make your workflow crystal clear.
    </p>
  </div>

  <p style="font-size: 15px;">Dear Students,</p>

  <p style="font-size: 15px;">
    Here is everything you need to know to complete your labs with confidence:
  </p>

  <h3 style="color: #1b365d; font-size: 16px; margin-top: 24px; border-bottom: 1px solid #e2e8f0; padding-bottom: 6px;">
    Key Steps &amp; Resources:
  </h3>
  <ul style="padding-left: 20px; font-size: 14.5px; line-height: 1.8;">
    <li><strong>1. Download Free Cisco Packet Tracer:</strong> In the <em>Course Orientation</em> module, check out our new guide: <strong><a href="/courses/13089/pages/hands-on-lab-setup-and-cisco-packet-tracer-installation-guide" style="color: #2563eb; font-weight: bold; text-decoration: underline;">🛠️ Hands-On Lab Setup &amp; Cisco Packet Tracer Installation Guide</a></strong>. It includes official download links and step-by-step installation instructions for Windows, Mac, and Linux.</li>
    <li><strong>2. What to Submit:</strong> Every lab requires two files: (1) your <code>.pkt</code> topology file, and (2) a PDF report answering the verification questions.</li>
    <li><strong>3. Flexible Pacing:</strong> If you experienced any setup delay getting Packet Tracer running on your computer for Module 1 or Module 2, you may submit your work without any late penalty while you get comfortable with the environment.</li>
  </ul>

  <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 16px 20px; border-radius: 8px; margin-top: 24px;">
    <p style="margin: 0; font-size: 14px; color: #475569;">
      If you run into any installation questions or need assistance with your Packet Tracer topology, please send me a message through Canvas Inbox or visit during office hours. Have fun building your networks!
    </p>
  </div>

  <p style="margin-top: 24px; font-size: 14.5px;">
    Best regards,<br>
    <strong>Professor William Nash</strong><br>
    <span style="color: #64748b; font-size: 13px;">Department of Computer Science &amp; Information Technology<br>Texas Wesleyan University</span>
  </p>
</div>'''

    ann_4328_html = '''<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #1e293b; line-height: 1.7; max-width: 820px; margin: 0 auto;">
  <div style="background: linear-gradient(135deg, #8b0000 0%, #4a0000 100%); color: #ffffff; padding: 24px 30px; border-radius: 10px; margin-bottom: 24px; box-shadow: 0 4px 12px rgba(139, 0, 0, 0.2);">
    <div style="font-size: 13px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; color: #f5a623; margin-bottom: 6px;">
      Texas Wesleyan University • Department of Computer Science &amp; IT
    </div>
    <h2 style="margin: 0; font-size: 22px; font-weight: 700; color: #ffffff;">
      📢 Important Lab Guidance: How to Complete Security Analyst Case Study Labs
    </h2>
    <div style="font-size: 13px; color: #ffcccc; margin-top: 6px;">
      From: Professor William Nash
    </div>
  </div>

  <div style="background: #f0fdf4; border-left: 5px solid #22c55e; padding: 18px 22px; border-radius: 6px; margin-bottom: 22px;">
    <h3 style="margin: 0 0 8px 0; color: #15803d; font-size: 16px; font-weight: bold;">
      🎉 Clarification: NO Software Installation Required!
    </h3>
    <p style="margin: 0; color: #166534; font-size: 14.5px;">
      Some students were concerned about needing to install virtual machines or hacking tools on their personal computers. <strong>You do not need any special software!</strong> The labs in this course are structured as professional <strong>Security Analyst Case Studies &amp; PBQ Worksheets</strong> completed in Microsoft Word or Google Docs.
    </p>
  </div>

  <p style="font-size: 15px;">Dear Students,</p>

  <p style="font-size: 15px;">
    To make your lab workflow simple, clear, and structured, here is what you need to know:
  </p>

  <h3 style="color: #8b0000; font-size: 16px; margin-top: 24px; border-bottom: 1px solid #e2e8f0; padding-bottom: 6px;">
    How to Complete Your Labs:
  </h3>
  <ul style="padding-left: 20px; font-size: 14.5px; line-height: 1.8;">
    <li><strong>1. Central Lab Guide &amp; Template:</strong> Check out the new guide in the <em>Course Orientation</em> module: <strong><a href="/courses/13090/pages/security-analyst-lab-guide-and-deliverable-submission-template" style="color: #8b0000; font-weight: bold; text-decoration: underline;">🛠️ Security Analyst Lab Guide &amp; Deliverable Submission Template</a></strong>. It provides an exact report template and sample exemplar showing how to earn full points.</li>
    <li><strong>2. Completing the Work:</strong> Open Microsoft Word or Google Docs, copy the incident analysis questions and tables from the lab assignment, write your threat classifications and mitigation recommendations, and save as a <strong>PDF (.pdf)</strong>.</li>
    <li><strong>3. What to Submit:</strong> Upload your completed PDF or Word document directly to the Canvas lab assignment.</li>
    <li><strong>4. Flexible Pacing:</strong> If you had any confusion regarding the format for Module 1 or Module 2, you may submit your lab without penalty.</li>
  </ul>

  <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 16px 20px; border-radius: 8px; margin-top: 24px;">
    <p style="margin: 0; font-size: 14px; color: #475569;">
      These case studies directly reflect the Performance-Based Questions (PBQs) you will see on the CompTIA Security+ (SY0-701) exam. If you have any questions on how to classify an incident, feel free to reach out via Canvas Inbox!
    </p>
  </div>

  <p style="margin-top: 24px; font-size: 14.5px;">
    Best regards,<br>
    <strong>Professor William Nash</strong><br>
    <span style="color: #64748b; font-size: 13px;">Department of Computer Science &amp; Information Technology<br>Texas Wesleyan University</span>
  </p>
</div>'''

    # Post CIS-3321 Announcement
    api_post("/courses/13089/discussion_topics", {
        'title': '📢 Important Lab Guidance: Free Cisco Packet Tracer Setup & Submission Walkthrough',
        'message': ann_3321_html,
        'is_announcement': True,
        'published': True
    })
    print("  ✅ Posted Announcement to CIS-3321 (13089)")

    # Post CIS-4328 Announcement
    api_post("/courses/13090/discussion_topics", {
        'title': '📢 Important Lab Guidance: How to Complete Security Analyst Case Study Labs',
        'message': ann_4328_html,
        'is_announcement': True,
        'published': True
    })
    print("  ✅ Posted Announcement to CIS-4328 (13090)")


if __name__ == '__main__':
    # 1. Overhaul CIS-3321
    overhaul_course_labs(13089, 87931, CLEAN_TITLES_CIS3321, is_network=True)
    
    # 2. Overhaul CIS-4328
    overhaul_course_labs(13090, 87948, CLEAN_TITLES_CIS4328, is_network=False)
    
    # 3. Overhaul CSC-6361
    overhaul_course_labs(12666, 88222, CLEAN_TITLES_CSC6361, is_network=True)

    # 4. Post Announcements
    post_student_announcements()

    print("\n" + "="*75)
    print("✅ COMPREHENSIVE LAB OVERHAUL COMPLETE ACROSS ALL COURSES!")
    print("="*75)
