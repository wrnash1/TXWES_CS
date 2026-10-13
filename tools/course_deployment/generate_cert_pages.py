# -*- coding: utf-8 -*-
"""
Generates rich HTML for all Certification Guides
"""

def generate_multi_cert_roadmap():
    return '''<div style="font-family:Arial,sans-serif;max-width:980px;margin:0 auto;padding:10px;line-height:1.7;color:#2c3e50;">

<div style="background:linear-gradient(135deg,#8b0000,#b22222);padding:24px 32px;border-radius:8px;margin-bottom:24px;box-shadow:0 4px 12px rgba(139,0,0,0.15);">
  <div style="font-size:12px;font-weight:bold;text-transform:uppercase;letter-spacing:1px;color:#f5a623;margin-bottom:6px;">
    Texas Wesleyan University · Department of Computer Science &amp; IT
  </div>
  <h1 style="color:white;margin:0;font-size:24px;font-weight:bold;">🎓 Multi-Certification Master Roadmap &amp; Domain Crosswalk</h1>
  <p style="color:#ffcccc;margin:8px 0 0;font-size:14px;">Your Pathway to Earning ISC2 CC, CompTIA Security+, CompTIA CySA+, Google Cyber, &amp; Cisco CyberOps</p>
</div>

<div style="background:#e8f5e9;border-left:5px solid #2e7d32;padding:18px 22px;border-radius:0 8px 8px 0;margin-bottom:24px;">
  <h3 style="margin:0 0 8px 0;color:#1b5e20;font-size:16px;font-weight:bold;">🏆 Complete Industry Certification Readiness</h3>
  <p style="margin:0;color:#2e7d32;font-size:14px;line-height:1.6;">
    This course is deliberately engineered to prepare you for not just a single exam, but <strong>five premier, industry-recognized cybersecurity credentials</strong>. By completing our 16 modules, labs, and scenario assessments, you will master the foundational, operational, and analytical competencies tested on global certification blueprints.
  </p>
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:30px;">1. Target Certification Comparison &amp; Exam Blueprints</h2>

<table style="width:100%;border-collapse:collapse;margin-top:16px;font-size:13.5px;">
  <thead>
    <tr style="background:#8b0000;color:white;text-align:left;">
      <th style="padding:10px 12px;border:1px solid #700000;">Certification</th>
      <th style="padding:10px 12px;border:1px solid #700000;">Vendor / Body</th>
      <th style="padding:10px 12px;border:1px solid #700000;">Format &amp; Questions</th>
      <th style="padding:10px 12px;border:1px solid #700000;">Passing Score</th>
      <th style="padding:10px 12px;border:1px solid #700000;">Student Cost / Voucher</th>
      <th style="padding:10px 12px;border:1px solid #700000;">Career Role</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#ffffff;">
      <td style="padding:10px 12px;border:1px solid #e2e8f0;font-weight:bold;color:#003366;">ISC2 Certified in Cybersecurity (CC)</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">ISC2 (Global)</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">100 MCQs (120 mins)</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">700 / 1000</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;color:#2e7d32;font-weight:bold;">FREE (1M CC Initiative) + $50 AMF</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">Junior Security Analyst, Help Desk Tier 2</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:10px 12px;border:1px solid #e2e8f0;font-weight:bold;color:#b22222;">CompTIA Security+ (SY0-701)</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">CompTIA (DoD 8140)</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">Max 90 Qs (PBQs + MCQs, 90 mins)</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">750 / 900</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">~$260 (50% Academic Discount)</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">Security Specialist, Systems Administrator</td>
    </tr>
    <tr style="background:#ffffff;">
      <td style="padding:10px 12px;border:1px solid #e2e8f0;font-weight:bold;color:#b22222;">CompTIA CySA+ (CS0-003)</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">CompTIA (DoD 8140)</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">Max 85 Qs (PBQs + MCQs, 165 mins)</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">750 / 900</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">~$260 (Academic Discount)</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">SOC Analyst (Tier 1/2), Threat Hunter</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:10px 12px;border:1px solid #e2e8f0;font-weight:bold;color:#ea4335;">Google Cybersecurity Certificate</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">Google / Coursera</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">8 Course Assessments + Hands-on Labs</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">80% per module</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">Free trial / $49/mo (Includes Sec+ discount)</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">Information Security Analyst</td>
    </tr>
    <tr style="background:#ffffff;">
      <td style="padding:10px 12px;border:1px solid #e2e8f0;font-weight:bold;color:#0070ba;">Cisco CyberOps Associate (200-201)</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">Cisco Systems</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">95–105 Qs (120 mins)</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">~825 / 1000</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">$300 (NetAcad discounts available)</td>
      <td style="padding:10px 12px;border:1px solid #e2e8f0;">Cisco SOC Analyst, Network Security Engineer</td>
    </tr>
  </tbody>
</table>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">2. Recommended Certification Sequence</h2>

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px;margin-top:16px;">
  <div style="background:#f1f5f9;border-top:4px solid #003366;padding:16px;border-radius:6px;">
    <span style="background:#003366;color:white;padding:2px 8px;border-radius:4px;font-size:11px;font-weight:bold;">STEP 1</span>
    <h4 style="margin:8px 0 4px 0;color:#003366;font-size:15px;">ISC2 CC</h4>
    <p style="margin:0;font-size:12.5px;color:#475569;">Take during Modules 1–6. Free registration, builds immediate exam confidence and introduces professional ethics.</p>
  </div>
  <div style="background:#f1f5f9;border-top:4px solid #b22222;padding:16px;border-radius:6px;">
    <span style="background:#b22222;color:white;padding:2px 8px;border-radius:4px;font-size:11px;font-weight:bold;">STEP 2</span>
    <h4 style="margin:8px 0 4px 0;color:#b22222;font-size:15px;">CompTIA Sec+</h4>
    <p style="margin:0;font-size:12.5px;color:#475569;">Take right after Module 16 Capstone. The universal baseline for DoD 8140/8570 and enterprise roles.</p>
  </div>
  <div style="background:#f1f5f9;border-top:4px solid #ea4335;padding:16px;border-radius:6px;">
    <span style="background:#ea4335;color:white;padding:2px 8px;border-radius:4px;font-size:11px;font-weight:bold;">STEP 3</span>
    <h4 style="margin:8px 0 4px 0;color:#ea4335;font-size:15px;">Google Cyber</h4>
    <p style="margin:0;font-size:12.5px;color:#475569;">Validate Linux bash scripts, SQL security audits, and hands-on portfolio artifacts on Coursera.</p>
  </div>
  <div style="background:#f1f5f9;border-top:4px solid #8b0000;padding:16px;border-radius:6px;">
    <span style="background:#8b0000;color:white;padding:2px 8px;border-radius:4px;font-size:11px;font-weight:bold;">STEP 4</span>
    <h4 style="margin:8px 0 4px 0;color:#8b0000;font-size:15px;">CompTIA CySA+</h4>
    <p style="margin:0;font-size:12.5px;color:#475569;">Specialize in SOC Blue Team operations, SIEM log triage, and vulnerability management.</p>
  </div>
  <div style="background:#f1f5f9;border-top:4px solid #0070ba;padding:16px;border-radius:6px;">
    <span style="background:#0070ba;color:white;padding:2px 8px;border-radius:4px;font-size:11px;font-weight:bold;">STEP 5</span>
    <h4 style="margin:8px 0 4px 0;color:#0070ba;font-size:15px;">Cisco CyberOps</h4>
    <p style="margin:0;font-size:12.5px;color:#475569;">Master Cisco enterprise telemetry, NetFlow, Snort rule writing, and network attack forensics.</p>
  </div>
</div>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">3. Course Module to Certification Domain Mapping</h2>

<table style="width:100%;border-collapse:collapse;margin-top:16px;font-size:13px;">
  <thead>
    <tr style="background:#1e293b;color:white;text-align:left;">
      <th style="padding:8px 10px;border:1px solid #0f172a;">Course Module</th>
      <th style="padding:8px 10px;border:1px solid #0f172a;">ISC2 CC (5 Domains)</th>
      <th style="padding:8px 10px;border:1px solid #0f172a;">CompTIA Sec+ (SY0-701)</th>
      <th style="padding:8px 10px;border:1px solid #0f172a;">CompTIA CySA+ (CS0-003)</th>
      <th style="padding:8px 10px;border:1px solid #0f172a;">Cisco CyberOps (200-201)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">M01: Threats &amp; Vulns</td><td style="padding:8px;border:1px solid #cbd5e1;">D1: Security Principles</td><td style="padding:8px;border:1px solid #cbd5e1;">2.0 Threats, Attacks &amp; Vulns</td><td style="padding:8px;border:1px solid #cbd5e1;">2.0 Vulnerability Mgmt</td><td style="padding:8px;border:1px solid #cbd5e1;">1.0 Security Concepts</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">M02: Social Engineering</td><td style="padding:8px;border:1px solid #cbd5e1;">D1: Security Principles</td><td style="padding:8px;border:1px solid #cbd5e1;">2.0 Social Engineering</td><td style="padding:8px;border:1px solid #cbd5e1;">1.0 Threat Intelligence</td><td style="padding:8px;border:1px solid #cbd5e1;">1.0 Attack Vectors</td></tr>
    <tr><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">M03: App Attacks</td><td style="padding:8px;border:1px solid #cbd5e1;">D5: Security Operations</td><td style="padding:8px;border:1px solid #cbd5e1;">2.0 App Attacks (OWASP)</td><td style="padding:8px;border:1px solid #cbd5e1;">2.0 Web App Scanning</td><td style="padding:8px;border:1px solid #cbd5e1;">4.0 Web Attacks</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">M04: Malware &amp; IOCs</td><td style="padding:8px;border:1px solid #cbd5e1;">D5: Security Operations</td><td style="padding:8px;border:1px solid #cbd5e1;">2.0 Indicators of Malware</td><td style="padding:8px;border:1px solid #cbd5e1;">1.0 Threat Hunting &amp; IOCs</td><td style="padding:8px;border:1px solid #cbd5e1;">3.0 Host Analysis (PE/Hashes)</td></tr>
    <tr><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">M05: Cryptography &amp; PKI</td><td style="padding:8px;border:1px solid #cbd5e1;">D1 Principles &amp; D4 NetSec</td><td style="padding:8px;border:1px solid #cbd5e1;">1.0 Cryptographic Ciphers</td><td style="padding:8px;border:1px solid #cbd5e1;">1.0 TLS/Certificate Triage</td><td style="padding:8px;border:1px solid #cbd5e1;">1.0 PKI &amp; Digital Signatures</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">M06: Identity &amp; Access</td><td style="padding:8px;border:1px solid #cbd5e1;">D3: Access Controls</td><td style="padding:8px;border:1px solid #cbd5e1;">3.0 IAM Architecture</td><td style="padding:8px;border:1px solid #cbd5e1;">1.0 Identity Auditing</td><td style="padding:8px;border:1px solid #cbd5e1;">1.0 AAA, RADIUS, TACACS+</td></tr>
    <tr><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">M07: Network Security</td><td style="padding:8px;border:1px solid #cbd5e1;">D4: Network Security</td><td style="padding:8px;border:1px solid #cbd5e1;">3.0 Sec Architecture</td><td style="padding:8px;border:1px solid #cbd5e1;">1.0 Network Telemetry</td><td style="padding:8px;border:1px solid #cbd5e1;">2.0 NetFlow, PCAP, Snort</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">M08: Endpoint Security</td><td style="padding:8px;border:1px solid #cbd5e1;">D5: Security Operations</td><td style="padding:8px;border:1px solid #cbd5e1;">3.0 EDR/XDR &amp; Hardening</td><td style="padding:8px;border:1px solid #cbd5e1;">1.0 Endpoint Forensics</td><td style="padding:8px;border:1px solid #cbd5e1;">3.0 Windows &amp; Linux Artifacts</td></tr>
    <tr><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">M09: Cloud Security</td><td style="padding:8px;border:1px solid #cbd5e1;">D4: Network Security</td><td style="padding:8px;border:1px solid #cbd5e1;">3.0 Cloud &amp; Virtualization</td><td style="padding:8px;border:1px solid #cbd5e1;">1.0 Cloud Security Logging</td><td style="padding:8px;border:1px solid #cbd5e1;">1.0 Cloud Service Models</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">M10: App Security</td><td style="padding:8px;border:1px solid #cbd5e1;">D5: Security Operations</td><td style="padding:8px;border:1px solid #cbd5e1;">3.0 DevSecOps &amp; Code</td><td style="padding:8px;border:1px solid #cbd5e1;">2.0 Software Security</td><td style="padding:8px;border:1px solid #cbd5e1;">4.0 App Vulnerabilities</td></tr>
    <tr><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">M11: Incident Response</td><td style="padding:8px;border:1px solid #cbd5e1;">D2: BC/DR &amp; IR</td><td style="padding:8px;border:1px solid #cbd5e1;">4.0 Incident Response</td><td style="padding:8px;border:1px solid #cbd5e1;">3.0 Incident Response (NIST)</td><td style="padding:8px;border:1px solid #cbd5e1;">5.0 CSIRT &amp; Playbooks</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">M12: Digital Forensics</td><td style="padding:8px;border:1px solid #cbd5e1;">D2: BC/DR &amp; IR</td><td style="padding:8px;border:1px solid #cbd5e1;">4.0 Forensic Artifacts</td><td style="padding:8px;border:1px solid #cbd5e1;">3.0 Forensics &amp; Memory</td><td style="padding:8px;border:1px solid #cbd5e1;">3.0 Evidence &amp; Volatility</td></tr>
    <tr><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">M13: Risk Management</td><td style="padding:8px;border:1px solid #cbd5e1;">D1: Security Principles</td><td style="padding:8px;border:1px solid #cbd5e1;">5.0 Risk Analysis &amp; BIA</td><td style="padding:8px;border:1px solid #cbd5e1;">4.0 Risk Reporting</td><td style="padding:8px;border:1px solid #cbd5e1;">5.0 Risk &amp; Compliance</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">M14: Governance &amp; Regs</td><td style="padding:8px;border:1px solid #cbd5e1;">D1: Ethics &amp; Regulations</td><td style="padding:8px;border:1px solid #cbd5e1;">5.0 Compliance &amp; Laws</td><td style="padding:8px;border:1px solid #cbd5e1;">4.0 Compliance Audits</td><td style="padding:8px;border:1px solid #cbd5e1;">5.0 Policies &amp; Procedures</td></tr>
    <tr><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">M15: Security Operations</td><td style="padding:8px;border:1px solid #cbd5e1;">D5: Security Operations</td><td style="padding:8px;border:1px solid #cbd5e1;">4.0 Security Operations</td><td style="padding:8px;border:1px solid #cbd5e1;">1.0 SecOps (33% of exam)</td><td style="padding:8px;border:1px solid #cbd5e1;">2.0 SOC Monitoring &amp; SIEM</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;">M16: Capstone &amp; Prep</td><td style="padding:8px;border:1px solid #cbd5e1;">All 5 CC Domains</td><td style="padding:8px;border:1px solid #cbd5e1;">All 5 Sec+ Domains</td><td style="padding:8px;border:1px solid #cbd5e1;">All 4 CySA+ Domains</td><td style="padding:8px;border:1px solid #cbd5e1;">All 5 CyberOps Domains</td></tr>
  </tbody>
</table>

<h2 style="color:#8b0000;border-bottom:2px solid #8b0000;padding-bottom:8px;margin-top:36px;">4. Student Voucher &amp; Discount Guide</h2>

<div style="background:#eff6ff;border:1px solid #bfdbfe;padding:20px;border-radius:8px;margin-top:16px;">
  <h4 style="margin:0 0 10px 0;color:#1e40af;font-size:15px;">💰 How to Save Hundreds of Dollars on Exam Vouchers:</h4>
  <ul style="margin:0;padding-left:20px;color:#1e3a8a;font-size:14px;line-height:1.8;">
    <li><strong>ISC2 CC 100% Free Voucher:</strong> Sign up for the <a href="https://www.isc2.org/1mcc" target="_blank" style="color:#1d4ed8;font-weight:bold;">ISC2 One Million Certified in Cybersecurity Initiative</a>. You receive free online training and an official Pearson VUE exam voucher code!</li>
    <li><strong>CompTIA 50% Academic Discount:</strong> Never pay full retail for CompTIA exams! Use your Texas Wesleyan student email (<code>@txwes.edu</code>) at the <a href="https://academic-store.comptia.org/" target="_blank" style="color:#1d4ed8;font-weight:bold;">CompTIA Academic Marketplace</a> to purchase Security+ and CySA+ vouchers at roughly half price.</li>
    <li><strong>Google Cybersecurity Certificate:</strong> Enrolling in the Google Certificate provides a voucher code for <strong>30% off</strong> the CompTIA Security+ exam upon completion of the 8 modules!</li>
  </ul>
</div>

</div>'''

print("Multi-cert roadmap generator ready.")
