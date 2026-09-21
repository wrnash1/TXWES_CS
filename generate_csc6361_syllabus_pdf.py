import subprocess
import os

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CSC-6361-33 Graduate Course Syllabus - Fall 2026</title>
<style>
  @page {
    size: letter;
    margin: 0.8in 0.8in 0.8in 0.8in;
    @bottom-right {
      content: "Page " counter(page) " of " counter(pages);
      font-size: 9pt;
      color: #64748b;
      font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    @bottom-left {
      content: "Texas Wesleyan University • CSC-6361-33 Syllabus";
      font-size: 9pt;
      color: #64748b;
      font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
  }

  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    color: #1e293b;
    line-height: 1.6;
    font-size: 10.5pt;
    margin: 0;
    padding: 0;
  }

  .header-banner {
    background: linear-gradient(135deg, #8b0000 0%, #5b0000 100%);
    color: #ffffff;
    padding: 24px 28px;
    border-radius: 8px;
    margin-bottom: 24px;
  }

  .header-banner h1 {
    margin: 0 0 4px 0;
    font-size: 20pt;
    letter-spacing: 0.5px;
    color: #ffffff;
    border: none;
    padding: 0;
  }

  .header-banner .sub-title {
    font-size: 13pt;
    color: #fca5a5;
    font-weight: 600;
    margin-bottom: 8px;
  }

  .header-banner .course-meta {
    font-size: 10pt;
    color: #f1f5f9;
    border-top: 1px solid rgba(255,255,255,0.25);
    padding-top: 8px;
    margin-top: 8px;
    display: flex;
    justify-content: space-between;
  }

  h2 {
    color: #8b0000;
    font-size: 14pt;
    border-bottom: 1.5px solid #8b0000;
    padding-bottom: 4px;
    margin-top: 22px;
    margin-bottom: 10px;
    page-break-after: avoid;
  }

  h3 {
    color: #0f172a;
    font-size: 11.5pt;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
  }

  p {
    margin: 6px 0;
    line-height: 1.55;
  }

  ul, ol {
    margin: 6px 0 10px 0;
    padding-left: 22px;
  }

  li {
    margin-bottom: 4px;
    line-height: 1.5;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0 16px 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
  }

  th {
    background: #8b0000;
    color: #ffffff;
    padding: 8px 10px;
    text-align: left;
    border: 1px solid #700000;
    font-weight: 600;
  }

  td {
    padding: 7px 10px;
    border: 1px solid #cbd5e1;
    line-height: 1.45;
  }

  tr:nth-child(even) td {
    background: #f8fafc;
  }

  .callout {
    background: #fff8f8;
    border-left: 4px solid #8b0000;
    padding: 10px 14px;
    margin: 12px 0;
    border-radius: 0 6px 6px 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
  }

  .callout strong {
    color: #8b0000;
  }

  .info-grid {
    display: table;
    width: 100%;
    margin-bottom: 16px;
    page-break-inside: avoid;
  }

  .info-row {
    display: table-row;
  }

  .info-cell-label {
    display: table-cell;
    width: 25%;
    font-weight: bold;
    padding: 4px 6px 4px 0;
    color: #334155;
  }

  .info-cell-value {
    display: table-cell;
    padding: 4px 0;
    color: #1e293b;
  }

  .page-break {
    page-break-before: always;
  }

  .footer-note {
    text-align: center;
    font-size: 8.5pt;
    color: #64748b;
    margin-top: 24px;
    border-top: 1px solid #e2e8f0;
    padding-top: 8px;
  }
</style>
</head>
<body>

<div class="header-banner">
  <h1>TEXAS WESLEYAN UNIVERSITY</h1>
  <div class="sub-title">Department of Computer Science &amp; Information Technology</div>
  <div class="course-meta">
    <div><strong>Course:</strong> CSC-6361-33 — Advanced Computer Networks (Graduate Level)</div>
    <div><strong>Term:</strong> Fall 2026 (7-Week 2 Session)</div>
  </div>
</div>

<div class="info-grid">
  <div class="info-row">
    <div class="info-cell-label">Course Section:</div>
    <div class="info-cell-value">CSC-6361-33 (Credit Hours: 3.0)</div>
  </div>
  <div class="info-row">
    <div class="info-cell-label">Term &amp; Dates:</div>
    <div class="info-cell-value">Fall 2026 (7-Week 2 Session: October 19, 2026 – December 11, 2026)</div>
  </div>
  <div class="info-row">
    <div class="info-cell-label">Course Delivery:</div>
    <div class="info-cell-value">100% Online Asynchronous (Canvas LMS)</div>
  </div>
  <div class="info-row">
    <div class="info-cell-label">Instructor:</div>
    <div class="info-cell-value">Professor Nash, Ph.D.</div>
  </div>
  <div class="info-row">
    <div class="info-cell-label">Instructor Email:</div>
    <div class="info-cell-value">nash@txwes.edu</div>
  </div>
  <div class="info-row">
    <div class="info-cell-label">Office Hours:</div>
    <div class="info-cell-value">Online by Appointment (via Microsoft Teams / Zoom)</div>
  </div>
  <div class="info-row">
    <div class="info-cell-label">Academic Level:</div>
    <div class="info-cell-value">Graduate (MS in Computer Science &amp; MS in Information Technology)</div>
  </div>
</div>

<h2>1. Course Overview &amp; Description</h2>
<p>
  <strong>Catalog Description:</strong> CSC-6361 Advanced Computer Networks is a rigorous graduate-level course designed for students pursuing careers in senior network engineering, enterprise architecture, and infrastructure management. The curriculum examines enterprise-scale networking technologies at the depth aligned with the <strong>Cisco Certified Network Professional (CCNP) Enterprise</strong> certification track (ENCOR 350-401 and ENARSI 300-410).
</p>
<p>
  Students analyze, configure, and troubleshoot complex multi-site routed and switched topologies using industry-standard protocols, command-line interfaces, and automation tools.
</p>

<h3>Course Prerequisites</h3>
<ul>
  <li>Undergraduate coursework in computer networking (e.g., CIS-3321 Network Administration or equivalent) <strong>or</strong> Cisco CCNA certification.</li>
  <li>Operational familiarity with the OSI 7-layer model, IPv4/IPv6 addressing, subnetting, dynamic routing protocols (OSPF/EIGRP), and basic switching.</li>
  <li>Graduate standing in the MS in Computer Science or MS in Information Technology degree program.</li>
</ul>

<h3>Student Learning Outcomes (SLOs)</h3>
<p>Upon successful completion of this graduate course, students will be able to:</p>
<ol>
  <li><strong>Enterprise Routing Architecture:</strong> Design, configure, and optimize complex multi-area OSPF, EIGRP, and BGP architectures, including mutual route redistribution and route-tagging policies.</li>
  <li><strong>Campus Network Design:</strong> Implement enterprise campus switching fabrics utilizing advanced 802.1Q VLAN trunking, Rapid Spanning Tree Protocol (RSTP/MSTP), and multi-chassis EtherChannel.</li>
  <li><strong>WAN &amp; Edge Technologies:</strong> Evaluate and deploy Wide Area Network transport mechanisms including MPLS, Cisco SD-WAN (vBond, vSmart, vManage, vEdge), GRE tunnels, and IPsec site-to-site VPNs.</li>
  <li><strong>Enterprise Security Hardening:</strong> Configure infrastructure plane security including Control Plane Policing (CoPP), Dynamic ARP Inspection (DAI), DHCP Snooping, and IP Source Guard.</li>
  <li><strong>Quality of Service &amp; High Availability:</strong> Architect QoS scheduling/marking mechanisms (DSCP/CoS) and first-hop redundancy protocols (HSRP, VRRP) to guarantee mission-critical SLA uptime.</li>
  <li><strong>Network Automation &amp; Programmability:</strong> Synthesize modern network programmability concepts utilizing Python, RESTCONF, NETCONF, YANG data models, and JSON payloads.</li>
  <li><strong>Graduate Scholarly Synthesis:</strong> Author a peer-reviewed style graduate research paper evaluating enterprise network design decisions, backed by authoritative RFCs and industry standards.</li>
</ol>

<h2>2. Required Course Materials (Zero Textbook Cost - ZTC)</h2>
<p>
  <strong>Zero Textbook Cost (ZTC):</strong> This course utilizes Open Educational Resources (OER), technical RFC standards, and vendor documentation. <strong>No textbook purchase is required.</strong>
</p>
<ul>
  <li><strong>Cisco Packet Tracer (Free):</strong> Version 8.2+ (Downloadable free via Cisco Skills for All / NetAcad account).</li>
  <li><strong>IETF Request for Comments (RFCs):</strong> Primary protocol benchmarks (e.g., OSPF RFC 2328, BGP-4 RFC 4271, MPLS RFC 3031).</li>
  <li><strong>Cisco CCNP Enterprise Documentation &amp; DevNet:</strong> Free learning labs and configuration guides via Cisco Learning Network and Cisco DevNet.</li>
  <li><strong>Computing Requirements:</strong> Windows 10/11, macOS 12+, or modern Linux capable of running Cisco Packet Tracer with continuous broadband internet access.</li>
</ul>

<h2>3. Grading Policy &amp; Evaluation Criteria</h2>
<p>
  Grades are calculated based on a weighted 100-point scale. Course components and their respective syllabus weights are summarized below:
</p>

<table>
  <thead>
    <tr>
      <th style="width: 32%;">Assessment Component</th>
      <th style="width: 18%;">Syllabus Weight</th>
      <th style="width: 50%;">Academic Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Weekly Lab Assignments</strong> (Modules 01–06)</td>
      <td><strong>30%</strong></td>
      <td>Hands-on Cisco Packet Tracer configuration topologies (.pkt) accompanied by formal technical analysis reports (PDF).</td>
    </tr>
    <tr>
      <td><strong>Weekly Quizzes</strong> (Modules 01–06)</td>
      <td><strong>20%</strong></td>
      <td>Rigorous CCNP-level multiple-choice and scenario assessments evaluating protocol behavior and design choices.</td>
    </tr>
    <tr>
      <td><strong>Graduate Discussion Boards</strong> (Modules 01–06)</td>
      <td><strong>20%</strong></td>
      <td>Substantive academic discourse (400+ words) requiring citation of RFCs/vendor benchmarks and peer critique.</td>
    </tr>
    <tr>
      <td><strong>Graduate Research Paper</strong> (Module 06)</td>
      <td><strong>10%</strong></td>
      <td>5–7 page technical research paper exploring emerging enterprise networking architectures in IEEE/APA 7 format.</td>
    </tr>
    <tr>
      <td><strong>Capstone Lab &amp; Final Exam</strong> (Module 07)</td>
      <td><strong>20%</strong></td>
      <td>Comprehensive enterprise troubleshooting simulation and culminating graduate technical exam.</td>
    </tr>
    <tr>
      <td><strong>Total</strong></td>
      <td><strong>100.0%</strong></td>
      <td><strong>Standard University Weighted Gradebook</strong></td>
    </tr>
  </tbody>
</table>

<h3>Grading Scale</h3>
<table>
  <thead>
    <tr>
      <th>Letter Grade</th>
      <th>Percentage Threshold</th>
      <th>Academic Performance Level</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>A</strong></td><td>90.0% – 100.0%</td><td>Excellent / Superior Graduate Performance</td></tr>
    <tr><td><strong>B</strong></td><td>80.0% – 89.9%</td><td>Good / Standard Graduate Competency</td></tr>
    <tr><td><strong>C</strong></td><td>70.0% – 79.9%</td><td>Minimum Passing (Lowest Grade for Graduate Credit)</td></tr>
    <tr><td><strong>F</strong></td><td>Below 70.0%</td><td>Failing (Must Retake Course for Degree Credit)</td></tr>
  </tbody>
</table>

<div class="callout">
  <strong>Graduate Academic Credit Mandate:</strong> Per Texas Wesleyan University Graduate Catalog policy, a minimum final course grade of <strong>"C" (70.0%)</strong> is required to earn graduate degree credit. Any final grade below 70.0% constitutes course failure and requires repetition.
</div>

<div class="page-break"></div>

<h2>4. Compressed 7-Week Course Schedule &amp; Blueprint</h2>
<p>
  This course operates on an intensive <strong>7-Week accelerated format</strong> (October 19, 2026 – December 11, 2026). Each module represents one full week of graduate-level study:
</p>

<table>
  <thead>
    <tr>
      <th style="width: 10%;">Module</th>
      <th style="width: 22%;">Session Dates</th>
      <th style="width: 38%;">Core Topics &amp; Learning Objectives</th>
      <th style="width: 30%;">Key Deliverables Due</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Mod 01</strong></td>
      <td>Week 1<br><strong>Oct 19 – Oct 25</strong></td>
      <td><strong>Advanced IP Routing:</strong> Multi-area OSPFv2/v3, EIGRP unequal-cost load balancing, and mutual route redistribution with route tagging.</td>
      <td>• Discussion M01<br>• Lab M01 (.pkt + PDF)<br>• Quiz M01</td>
    </tr>
    <tr>
      <td><strong>Mod 02</strong></td>
      <td>Week 2<br><strong>Oct 26 – Nov 01</strong></td>
      <td><strong>Campus Network Design:</strong> 802.1Q VLAN trunks, Spanning Tree (PVST+, Rapid-PVST, MSTP), LACP/PAgP EtherChannel, and VTP v3.</td>
      <td>• Discussion M02<br>• Lab M02 (.pkt + PDF)<br>• Quiz M02</td>
    </tr>
    <tr>
      <td><strong>Mod 03</strong></td>
      <td>Week 3<br><strong>Nov 02 – Nov 08</strong></td>
      <td><strong>WAN &amp; Edge Technologies:</strong> MPLS label distribution (LDP), BGP path attributes (Weight, Local Pref, AS-Path, MED), and SD-WAN architecture.</td>
      <td>• Discussion M03<br>• Lab M03 (.pkt + PDF)<br>• Quiz M03</td>
    </tr>
    <tr>
      <td><strong>Mod 04</strong></td>
      <td>Week 4<br><strong>Nov 09 – Nov 15</strong></td>
      <td><strong>Enterprise Security Hardening:</strong> Control Plane Policing (CoPP), Dynamic ARP Inspection (DAI), DHCP Snooping, Port Security, and IPsec VPNs.</td>
      <td>• Discussion M04<br>• Lab M04 (.pkt + PDF)<br>• Quiz M04</td>
    </tr>
    <tr>
      <td><strong>Mod 05</strong></td>
      <td>Week 5<br><strong>Nov 16 – Nov 22</strong></td>
      <td><strong>QoS, High Availability &amp; Automation:</strong> First-Hop Redundancy (HSRP/VRRP), QoS DiffServ classification/marking, and Python RESTCONF.</td>
      <td>• Discussion M05<br>• Lab M05 (.pkt + PDF)<br>• Quiz M05</td>
    </tr>
    <tr>
      <td><strong>Mod 06</strong></td>
      <td>Week 6<br><strong>Nov 23 – Nov 29</strong><br><em>(Extended to Dec 1)</em></td>
      <td><strong>Cloud Networking &amp; Research Paper:</strong> AWS DirectConnect, Azure ExpressRoute, hybrid Transit Gateways, and graduate research synthesis.</td>
      <td>• Discussion M06<br>• Lab M06 (.pkt + PDF)<br>• Quiz M06<br>• <strong>Graduate Research Paper</strong></td>
    </tr>
    <tr>
      <td><strong>Mod 07</strong></td>
      <td>Week 7<br><strong>Nov 30 – Dec 11</strong></td>
      <td><strong>Capstone Troubleshooting &amp; Final Exam:</strong> Multi-site enterprise diagnostic simulation, root-cause analysis, and comprehensive final examination.</td>
      <td>• Discussion M07<br>• <strong>Capstone Lab M07</strong><br>• <strong>Comprehensive Final Exam</strong></td>
    </tr>
  </tbody>
</table>

<div class="callout">
  <strong>⚠ Thanksgiving Holiday Schedule Notice (Module 06):</strong> Thanksgiving Break occurs during Week 6. To accommodate the holiday, Module 06 assignments carry an <strong>extended deadline through Sunday, December 1, 2026 at 11:59 PM CST</strong>. Students are advised to begin research paper preparations early.
</div>

<h2>5. University &amp; Graduate Academic Policies</h2>

<h3>Attendance &amp; Substantive Engagement</h3>
<p>
  In accordance with federal regulations and SACSCOC accreditation standards for distance education, attendance in this 100% online asynchronous course is measured by <strong>Regular and Substantive Interaction (RSI)</strong>. Students must submit at least one required academic deliverable (discussion post, lab, or quiz) each week to be certified as "Present." 
</p>
<p>
  Failure to submit academic work for <strong>two consecutive weeks</strong> will trigger immediate departmental academic review and may result in administrative withdrawal per Texas Wesleyan University catalog policy.
</p>

<h3>Late Work Policy</h3>
<p>
  All weekly deliverables are due by <strong>Sunday at 11:59 PM CST</strong>. In an accelerated 7-week curriculum, adhering to pacing is critical. Late submissions are accepted up to <strong>48 hours (2 days) past the posted deadline</strong> with a <strong>15% penalty per 24-hour period</strong>. Submissions received beyond 48 hours will receive a recorded score of zero unless prior arrangements have been approved by the instructor for documented medical or personal emergencies.
</p>

<h3>Academic Integrity &amp; Generative AI Guidelines</h3>
<p>
  Academic honesty is foundational to graduate scholarship. All submitted technical reports, packet traces, discussion responses, and research manuscripts must represent the student's own intellectual analysis.
</p>
<ul>
  <li><strong>Generative AI Use:</strong> AI tools (e.g., ChatGPT, Gemini) are permitted as supplemental research accelerators and error syntax clarifiers. However, submitting AI-generated text verbatim as your own work constitutes academic misconduct.</li>
  <li><strong>Verification:</strong> Students must be prepared to orally defend any technical claim, protocol configuration, or research finding in a one-on-one conference with the instructor upon request.</li>
</ul>

<h3>Student Accommodations &amp; Support Services</h3>
<p>
  Texas Wesleyan University is committed to providing equal access. Students with documented disabilities requesting reasonable academic accommodations should contact the <strong>Office of Disability Services</strong> (located in the Eunice &amp; James L. West Library) at 817-531-4820 at the beginning of the session.
</p>

<div class="footer-note">
  Texas Wesleyan University • Department of Computer Science &amp; Information Technology • Fort Worth, Texas<br>
  Official Syllabus for CSC-6361-33 (Fall 2026) • Approved by Professor Nash, Ph.D.
</div>

</body>
</html>
"""

def generate_pdf():
    html_path = "/home/wrnash1/Developer/TXWES_CS/CSC-6361-33_Syllabus_Fall2026.html"
    pdf_dir = "/home/wrnash1/Developer/TXWES_CS"
    pdf_path = "/home/wrnash1/Developer/TXWES_CS/CSC-6361-33_Syllabus_Fall2026.pdf"
    artifact_dir = "/home/wrnash1/.gemini/antigravity/brain/c1239228-60f2-4111-9f86-91a2627ea801"
    artifact_pdf = os.path.join(artifact_dir, "CSC-6361-33_Syllabus_Fall2026.pdf")

    # 1. Write clean print-ready HTML
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE)
    print(f"✅ Wrote clean syllabus HTML: {html_path}")

    # 2. Convert to PDF using LibreOffice
    cmd = [
        "libreoffice",
        "--headless",
        "--convert-to",
        "pdf",
        html_path,
        "--outdir",
        pdf_dir
    ]
    print("Running command:", " ".join(cmd))
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)

    if os.path.exists(pdf_path):
        size = os.path.getsize(pdf_path)
        print(f"✅ PDF successfully generated! Size: {size} bytes ({size/1024:.1f} KB)")
        
        # 3. Copy to artifacts directory
        subprocess.run(["cp", pdf_path, artifact_pdf])
        print(f"✅ Copied PDF to artifacts directory: {artifact_pdf}")
    else:
        print("❌ PDF generation failed.")

if __name__ == "__main__":
    generate_pdf()
