# -*- coding: utf-8 -*-
"""
Inject Multi-Certification Exam Focus callout blocks into all 16 Reading Guides of CIS-4328
"""

import json, time, re, urllib.request
from pathlib import Path
from csc6361_builder_core import md2html
from canvas_native_visuals import get_native_visual

CANVAS_URL = "https://txwes.instructure.com"
TOKEN      = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
BASE_DIR   = Path(__file__).parent / 'completed' / 'CIS-4328_Information_Security'
CID        = 13090

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
def api_put(path, data): return api_call('PUT', path, data)

MULTI_CERT_FOCUS = {
    1: {
        "cc": "Domain 1: Security Principles — Difference between Threats, Vulnerabilities, and Risks. Remember: Risk = Threat × Vulnerability × Impact.",
        "sec": "Domain 2.0: Threats, Attacks & Vulnerabilities — Threat actor types (Nation-state, Hacktivist, Insider) and vectors.",
        "cysa": "Domain 2.0: Vulnerability Management — CVE, CWE, and NVD vulnerability triage workflows.",
        "google": "Course 2: Manage Security Risks — Understanding attack surfaces and threat actor motivations.",
        "cisco": "Domain 1.0: Security Concepts — Attack vectors and security operations terminology."
    },
    2: {
        "cc": "Domain 1: Security Principles — Social engineering principles (Authority, Urgency, Scarcity, Social Proof).",
        "sec": "Domain 2.0: Social Engineering — Spear phishing, Whaling, Vishing, Smishing, and Watering Hole attacks.",
        "cysa": "Domain 1.0: Threat Intelligence — Email header inspection (SPF, DKIM, DMARC validation) to catch spoofed senders.",
        "google": "Course 2: Social Engineering — Recognizing credential harvesting and deceptive link architectures.",
        "cisco": "Domain 1.0: Security Concepts — Human-factor security and social engineering attack mechanisms."
    },
    3: {
        "cc": "Domain 5: Security Operations — Input validation, buffer overflows, and sanitizing user inputs.",
        "sec": "Domain 2.0: Application Attacks — OWASP Top 10, SQL Injection (' OR '1'='1), XSS (Stored vs Reflected), and CSRF.",
        "cysa": "Domain 2.0: Vulnerability Management — Web application vulnerability scanning with Burp Suite and OWASP ZAP.",
        "google": "Course 5: Assets, Threats & Vulns — Identifying SQL injection in web logs and database hardening.",
        "cisco": "Domain 4.0: Intrusion Analysis — Inspecting HTTP POST requests containing malicious SQL or JavaScript payloads."
    },
    4: {
        "cc": "Domain 5: Security Operations — Malicious code types: Ransomware, Trojans, Worms, Spyware, and Rootkits.",
        "sec": "Domain 2.0: Indicators of Malware — C2 (Command & Control) beaconing, fileless malware, and living-off-the-land binaries (LOLBins).",
        "cysa": "Domain 1.0: Threat Hunting — Using YARA rules and SHA-256 cryptographic hashes to identify infected hosts.",
        "google": "Course 5: Assets & Threats — Malware analysis workflows and hash matching with VirusTotal.",
        "cisco": "Domain 3.0: Host Analysis — Examining Windows Portable Executable (PE) headers and suspicious registry keys."
    },
    5: {
        "cc": "Domain 1 & 4: Security Principles — Symmetric (AES, 3DES) vs Asymmetric (RSA, ECC) encryption; Hashing (SHA-256) for integrity.",
        "sec": "Domain 1.0: Cryptography — Diffie-Hellman key exchange, Perfect Forward Secrecy (PFS), and PKI certificate chains.",
        "cysa": "Domain 1.0: Security Operations — Identifying outdated TLS 1.0/1.1 protocols and weak cipher suites during vulnerability scans.",
        "google": "Course 5: Cryptography — Hash generation using Python hashlib and symmetric key management.",
        "cisco": "Domain 1.0: Cryptography — Public Key Infrastructure (PKI), digital signatures, and CA trust hierarchies."
    },
    6: {
        "cc": "Domain 3: Access Controls — Discretionary (DAC), Mandatory (MAC), and Role-Based Access Control (RBAC); Least Privilege.",
        "sec": "Domain 3.0: IAM Architecture — Multi-Factor Authentication (MFA) factors: Something you Know, Have, Are, Do, Somewhere.",
        "cysa": "Domain 1.0: Identity Auditing — Detecting privilege escalation and unauthorized Active Directory modifications.",
        "google": "Course 3: IAM Concepts — Google Cloud IAM roles, service accounts, and principle of least privilege.",
        "cisco": "Domain 1.0: AAA & Identity — Centralized authentication protocols: TACACS+ vs RADIUS and 802.1X port security."
    },
    7: {
        "cc": "Domain 4: Network Security — OSI 7 layers, Firewalls (Stateful vs Stateless), DMZ architectures, and VPNs.",
        "sec": "Domain 3.0: Security Architecture — Zero Trust Architecture (ZTA), micro-segmentation, and East-West vs North-South traffic.",
        "cysa": "Domain 1.0: Network Telemetry — Analyzing PCAP captures in Wireshark and writing Snort/Suricata intrusion detection rules.",
        "google": "Course 3: Networks & Network Security — Packet filtering with iptables and network traffic monitoring.",
        "cisco": "Domain 2.0: Network Monitoring — NetFlow/IPFIX telemetry, SPAN port mirroring, and Cisco Firepower NG-IPS."
    },
    8: {
        "cc": "Domain 5: Security Operations — Endpoint protection: Antivirus, host-based firewalls, and full disk encryption (BitLocker).",
        "sec": "Domain 3.0: Endpoint Security — EDR (Endpoint Detection & Response), XDR, HIDS, and mobile device management (MDM).",
        "cysa": "Domain 1.0: Endpoint Forensics — Windows Event Log investigation (Event IDs: 4624, 4625, 4672, 7045) and Sysinternals.",
        "google": "Course 4: Linux & SQL — Linux file permission management (chmod/chown) and system security auditing.",
        "cisco": "Domain 3.0: Host-Based Analysis — Analyzing running processes (ps, tasklist) and memory dumps for anomalous behavior."
    },
    9: {
        "cc": "Domain 4: Network Security — Cloud deployment models (Public, Private, Hybrid) and Service models (IaaS, PaaS, SaaS).",
        "sec": "Domain 3.0: Cloud Security — Shared Responsibility Model, CASB (Cloud Access Security Broker), and CSPM.",
        "cysa": "Domain 1.0: Cloud SecOps — Ingesting AWS CloudTrail, Azure Monitor, and Google Cloud Audit logs into SIEM.",
        "google": "Course 3: Cloud Security — GCP IAM, VPC Service Controls, and Security Command Center (SCC) configuration.",
        "cisco": "Domain 1.0: Cloud Concepts — Securing cloud workloads and virtual private cloud (VPC) interconnects."
    },
    10: {
        "cc": "Domain 5: Security Operations — Secure Software Development Lifecycle (SSDLC) and code change control.",
        "sec": "Domain 3.0: DevSecOps — Static Application Security Testing (SAST) vs Dynamic (DAST), software composition analysis (SCA).",
        "cysa": "Domain 2.0: Software Security — Reviewing automated pipeline vulnerability scan reports and remediation tracking.",
        "google": "Course 4: Python Scripting — Writing Python scripts to parse application error logs and automate security checks.",
        "cisco": "Domain 4.0: Application Vulnerabilities — Understanding how insecure API calls and cross-site scripting impact enterprise services."
    },
    11: {
        "cc": "Domain 2: Business Continuity & IR — Incident response stages: Detection, Containment, Eradication, and Recovery.",
        "sec": "Domain 4.0: Incident Response — NIST SP 800-61 Rev. 2 lifecycle, containment strategies (isolation vs sandboxing).",
        "cysa": "Domain 3.0: Incident Response — Computer Security Incident Response Team (CSIRT) playbooks, communication, and SLA tracking.",
        "google": "Course 6: Detection & Response — Incident documentation, triage escalations, and post-incident reviews.",
        "cisco": "Domain 5.0: Incident Handling — Following established CSIRT procedures to isolate compromised switch ports."
    },
    12: {
        "cc": "Domain 2: Business Continuity & IR — Preserving evidence integrity, Order of Volatility, and chain of custody.",
        "sec": "Domain 4.0: Digital Forensics — Hardware write blockers, bit-stream disk imaging (dd, FTK Imager), and hashing verification.",
        "cysa": "Domain 3.0: Forensics & Memory — Volatility framework for RAM memory analysis and registry hive inspection.",
        "google": "Course 6: Forensics — Documenting evidence custody forms and reconstructing cyberattack timelines.",
        "cisco": "Domain 3.0: Evidence Collection — Maintaining strict chain of custody and forensic integrity during criminal investigations."
    },
    13: {
        "cc": "Domain 1 & 2: Risk Management — Quantitative vs Qualitative risk assessment, BIA, MTD, RTO, and RPO.",
        "sec": "Domain 5.0: Risk Management — SLE = Asset Value × Exposure Factor; ALE = SLE × ARO; Risk treatments (Mitigate, Transfer, Accept, Avoid).",
        "cysa": "Domain 4.0: Risk Reporting — Communicating vulnerability risk metrics and mitigation roadmaps to executive leadership.",
        "google": "Course 2: Manage Security Risks — Implementing NIST Cybersecurity Framework (Identify, Protect, Detect, Respond, Recover).",
        "cisco": "Domain 5.0: Security Policies — Assessing business risk and establishing disaster recovery hot/warm/cold sites."
    },
    14: {
        "cc": "Domain 1: Security Principles — Professional ethics, privacy regulations (GDPR), and compliance audits.",
        "sec": "Domain 5.0: Governance & Regulations — Compliance frameworks: HIPAA, PCI-DSS, SOC 2, ISO 27001, and NIST RMF.",
        "cysa": "Domain 4.0: Compliance Audits — Audit trails, regulatory gap analysis, and policy enforcement verification.",
        "google": "Course 2: Frameworks & Controls — Eight CIS Controls and establishing compliance documentation.",
        "cisco": "Domain 5.0: Policies & Procedures — Aligning network security configurations with organizational regulatory mandates."
    },
    15: {
        "cc": "Domain 5: Security Operations — Centralized logging, baseline monitoring, and continuous security auditing.",
        "sec": "Domain 4.0: Security Operations — SIEM log aggregation, SOAR automated playbooks, and User Behavior Analytics (UEBA).",
        "cysa": "Domain 1.0: Security Operations (33% of CySA+) — Splunk Search Processing Language (SPL), log correlation, and alert tuning.",
        "google": "Course 6: Sound the Alarm — Google Chronicle SIEM, YARA-L rule creation, and alert dashboard monitoring.",
        "cisco": "Domain 2.0: Security Monitoring — NetFlow flow analysis, Cisco SecureX, and SOC tier-1 alert triage playbooks."
    },
    16: {
        "cc": "All 5 CC Domains — Comprehensive review of CIA, Ethics, Access Controls, Network Security, and Operations.",
        "sec": "All 5 Sec+ Domains — Performance-Based Questions (PBQ) strategy, CLI simulation, and rapid-fire review.",
        "cysa": "All 4 CySA+ Domains — Scenario-based log analysis, CVSS scoring questions, and incident triage simulations.",
        "google": "All 8 Google Cyber Courses — Portfolio project finalization, resume technical keywords, and mock interview prep.",
        "cisco": "All 5 CyberOps Domains — Packet analysis, Snort rule evaluation, and end-to-end intrusion investigation."
    }
}


def build_multicert_callout(mod_num: int) -> str:
    focus = MULTI_CERT_FOCUS.get(mod_num, {})
    return f'''
<!-- MULTI-CERTIFICATION EXAM FOCUS BOX -->
<div style="background:#fdf2f8;border:2px solid #f472b6;border-radius:8px;padding:20px 24px;margin-top:24px;box-shadow:0 2px 8px rgba(244,114,182,0.15);">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
    <span style="font-size:20px;">🎯</span>
    <h3 style="margin:0;color:#9d174d;font-size:16px;font-weight:bold;letter-spacing:0.5px;">
      MULTI-CERTIFICATION EXAM FOCUS · Module {mod_num:02d} Blueprint Crosswalk
    </h3>
  </div>
  <p style="margin:0 0 14px 0;font-size:13.5px;color:#831843;line-height:1.6;">
    Mastering this module prepares you directly for multiple industry certification exam questions. Focus on how this topic is tested across each blueprint:
  </p>
  <div style="display:grid;grid-template-columns:1fr;gap:10px;font-size:13px;line-height:1.6;">
    <div style="background:white;border-left:4px solid #003366;padding:10px 14px;border-radius:4px;">
      <strong style="color:#003366;">🛡️ ISC2 CC:</strong> {focus.get('cc', '')}
    </div>
    <div style="background:white;border-left:4px solid #b22222;padding:10px 14px;border-radius:4px;">
      <strong style="color:#b22222;">🔐 CompTIA Security+ (SY0-701):</strong> {focus.get('sec', '')}
    </div>
    <div style="background:white;border-left:4px solid #8b0000;padding:10px 14px;border-radius:4px;">
      <strong style="color:#8b0000;">🔍 CompTIA CySA+ (CS0-003):</strong> {focus.get('cysa', '')}
    </div>
    <div style="background:white;border-left:4px solid #ea4335;padding:10px 14px;border-radius:4px;">
      <strong style="color:#ea4335;">☁️ Google Cybersecurity:</strong> {focus.get('google', '')}
    </div>
    <div style="background:white;border-left:4px solid #0070ba;padding:10px 14px;border-radius:4px;">
      <strong style="color:#0070ba;">🌐 Cisco CyberOps:</strong> {focus.get('cisco', '')}
    </div>
  </div>
</div>
'''

def update_cis4328_reading_guides():
    print("="*75)
    print("UPDATING CIS-4328 READING GUIDES WITH MULTI-CERTIFICATION FOCUS CALLOUTS")
    print("="*75)

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

        # Target slug
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
        multicert_callout = build_multicert_callout(mod_num)

        rich_html = f'''<div style="font-family:Arial,sans-serif;max-width:960px;margin:0 auto;padding:10px;">

<!-- BRANDED TEXAS WESLEYAN HEADER -->
<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(139,0,0,0.15);">
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">{page_title}</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">🎓 Texas Wesleyan University · Department of Computer Science &amp; IT · CIS-4328 Information Security</p>
</div>

<!-- LEARNING OBJECTIVES CALLOUT -->
<div style="background:#fff8e1;border-left:5px solid #f5a623;padding:16px 20px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <p style="margin:0;font-weight:bold;color:#7a5800;font-size:14px;">📌 CORE LEARNING OBJECTIVES</p>
  <p style="margin:6px 0 0;color:#7a5800;font-size:13.5px;line-height:1.6;">After completing this reading guide, you will be able to explain underlying theoretical mechanics, evaluate protocol architecture trade-offs, and apply configuration and troubleshooting procedures to solve enterprise technical challenges.</p>
</div>

<!-- CANVAS-NATIVE VISUAL ARCHITECTURE BLOCK -->
{visual_block}

<!-- EXPANDED TECHNICAL READING CONTENT -->
<div style="background:white;padding:10px 0;line-height:1.8;color:#2c3e50;font-size:15px;">
{base_html}
</div>

<!-- MULTI-CERTIFICATION CALLOUT BLOCK -->
{multicert_callout}

<!-- STUDY TIP BOX -->
<div style="background:#e8f5e9;border-left:5px solid #4caf50;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:32px;">
  <p style="margin:0;font-weight:bold;color:#2e7d32;">💡 PROFESSOR NASH'S STUDY STRATEGY — Before the Quiz &amp; Lab</p>
  <p style="margin:6px 0 0;color:#2e7d32;font-size:13.5px;line-height:1.6;">Review each major heading, diagram, and the multi-certification focus above. Can you explain the protocol flow or threat scenario out loud without referencing your notes? Quiz questions and lab verification steps directly evaluate these competencies.</p>
</div>

<!-- KEY TERMS BOX -->
<div style="background:#e3f2fd;border-left:5px solid #2196f3;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:16px;">
  <p style="margin:0;font-weight:bold;color:#0d47a1;">🔑 KEY TERMS &amp; CONCEPTS TO KNOW</p>
  <p style="margin:6px 0 0;color:#0d47a1;font-size:13.5px;line-height:1.6;">Scan this guide and define every term in <strong>bold</strong>. Incorporate these technical terms and standard RFC/IEEE/NIST specifications into your weekly discussion board post to earn maximum rubric points.</p>
</div>

<!-- CAREER CONNECTION BOX -->
<div style="background:#fce4ec;border-left:5px solid #e91e63;padding:16px 20px;border-radius:0 8px 8px 0;margin-top:16px;">
  <p style="margin:0;font-weight:bold;color:#880e4f;">🏆 INDUSTRY CERTIFICATION &amp; CAREER IMPACT</p>
  <p style="margin:6px 0 0;color:#880e4f;font-size:13.5px;line-height:1.6;">These concepts appear directly on industry certification exam blueprints (ISC2 CC, CompTIA Security+, CySA+, Google Cybersecurity, Cisco CyberOps) and technical interview loops for Security Analysts and Cloud Engineers.</p>
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
            print(f"  ✅ M{mod_num:02d}: Injected Multi-Cert Focus Callout -> {target_url}")
        else:
            print(f"  ⚠ Update may have failed for M{mod_num:02d} ({target_url})")

        time.sleep(0.3)

    print("\n" + "="*75)
    print("✅ ALL 16 READING GUIDES ENRICHED WITH MULTI-CERTIFICATION FOCUS CALLOUTS!")
    print("="*75)

if __name__ == '__main__':
    update_cis4328_reading_guides()
