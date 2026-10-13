import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    """Two-pass canvas to dynamically compute and print 'Page X of Y'"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8.5)
        self.setFillColor(colors.HexColor("#475569"))
        
        # Header (pages 2+)
        if self._pageNumber > 1:
            self.drawString(54, 750, "Texas Wesleyan University • CSC-6361-33: Advanced Computer Networks")
            self.setStrokeColor(colors.HexColor("#d9a74a"))
            self.setLineWidth(0.5)
            self.line(54, 744, 558, 744)

        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(54, 45, 558, 45)
        
        footer_text = "Official Graduate Course Syllabus • Fall 2026 • Department of Computer Science & IT"
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawString(54, 32, footer_text)
        self.drawRightString(558, 32, page_str)
        self.restoreState()

def generate_syllabus_pdf():
    pdf_path = "/home/wrnash1/Developer/TXWES_CS/CSC-6361-33_Syllabus_Fall2026.pdf"
    artifact_path = "/home/wrnash1/.gemini/antigravity/brain/c1239228-60f2-4111-9f86-91a2627ea801/CSC-6361-33_Syllabus_Fall2026.pdf"

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    # Custom Styles
    primary_color = colors.HexColor("#1b365d") # Texas Wesleyan Navy Blue
    accent_gold = colors.HexColor("#d9a74a")   # Texas Wesleyan Gold
    dark_slate = colors.HexColor("#0f172a")
    text_color = colors.HexColor("#1e293b")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.white,
        alignment=0
    )
    
    sub_title_style = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#d9a74a"),
        alignment=0
    )

    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#f8fafc")
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=primary_color,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=dark_slate,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=text_color,
        spaceBefore=3,
        spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=text_color,
        leftIndent=15,
        firstLineIndent=-10,
        spaceBefore=2,
        spaceAfter=2
    )

    callout_style = ParagraphStyle(
        'Callout_Text',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#334155")
    )

    tbl_header = ParagraphStyle(
        'TblHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    tbl_body = ParagraphStyle(
        'TblBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=text_color
    )

    story = []

    # 1. Header Banner Box
    banner_content = [
        [Paragraph("TEXAS WESLEYAN UNIVERSITY", title_style)],
        [Paragraph("Department of Computer Science &amp; Information Technology", sub_title_style)],
        [Paragraph("<strong>Course:</strong> CSC-6361-33 — Advanced Computer Networks (Graduate Level) &nbsp;|&nbsp; <strong>Term:</strong> Fall 2026 (7-Week 2)", meta_style)]
    ]
    banner_table = Table(banner_content, colWidths=[504])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), primary_color),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
        ('RIGHTPADDING', (0,0), (-1,-1), 14),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMBORDER', (0,1), (-1,1), 1, colors.HexColor("#fca5a5"))
    ]))
    story.append(banner_table)
    story.append(Spacer(1, 10))

    # 2. Course & Instructor Metadata Grid
    meta_data = [
        [Paragraph("<strong>Course Section:</strong>", tbl_body), Paragraph("CSC-6361-33 (Credit Hours: 3.0)", tbl_body),
         Paragraph("<strong>Instructor:</strong>", tbl_body), Paragraph("Professor Nash, Ph.D.", tbl_body)],
        [Paragraph("<strong>Term Dates:</strong>", tbl_body), Paragraph("Oct 19, 2026 – Dec 11, 2026 (7-Week 2)", tbl_body),
         Paragraph("<strong>Email:</strong>", tbl_body), Paragraph("nash@txwes.edu", tbl_body)],
        [Paragraph("<strong>Delivery Format:</strong>", tbl_body), Paragraph("100% Online Asynchronous (Canvas LMS)", tbl_body),
         Paragraph("<strong>Office Hours:</strong>", tbl_body), Paragraph("Online by appointment (MS Teams/Zoom)", tbl_body)],
        [Paragraph("<strong>Academic Level:</strong>", tbl_body), Paragraph("Graduate (MS in CS / MS in IT)", tbl_body),
         Paragraph("<strong>Response Time:</strong>", tbl_body), Paragraph("Within 24–48 hours on weekdays", tbl_body)]
    ]
    meta_table = Table(meta_data, colWidths=[100, 152, 90, 162])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 8))

    # 3. Course Overview
    story.append(Paragraph("1. Course Overview &amp; Learning Outcomes", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#d9a74a"), spaceBefore=1, spaceAfter=6))
    
    story.append(Paragraph("<strong>Catalog Description:</strong> CSC-6361 Advanced Computer Networks is a rigorous graduate-level course designed for students pursuing careers in senior network engineering, cloud architecture, and infrastructure management. The curriculum examines enterprise-scale networking technologies at the depth and rigor aligned with the <strong>Cisco Certified Network Professional (CCNP) Enterprise</strong> track (ENCOR 350-401 and ENARSI 300-410). Students analyze, configure, and troubleshoot complex multi-site routed and switched topologies using industry-standard protocols, command-line interfaces, and automation frameworks.", body_style))
    
    story.append(Paragraph("<strong>Course Prerequisites:</strong> Undergraduate coursework in computer networking (e.g., CIS-3321 Network Administration or equivalent) <em>or</em> Cisco CCNA certification; operational familiarity with the OSI model, IP addressing, subnetting, dynamic routing protocols (OSPF/EIGRP), and basic switching; graduate standing in the MS in CS or MS in IT program.", body_style))

    story.append(Paragraph("<strong>Student Learning Outcomes (SLOs):</strong> Upon successful completion of this graduate course, students will be able to:", body_style))
    slos = [
        "<strong>Enterprise Routing Architecture:</strong> Design, configure, and optimize complex multi-area OSPF, EIGRP, and BGP routing architectures, including mutual route redistribution and route-tagging policies.",
        "<strong>Campus Network Design:</strong> Implement enterprise campus switching fabrics utilizing advanced 802.1Q VLAN trunking, Rapid Spanning Tree (RSTP/MSTP), and multi-chassis EtherChannel.",
        "<strong>WAN &amp; Edge Technologies:</strong> Evaluate and deploy Wide Area Network transport mechanisms including MPLS, Cisco SD-WAN (vBond, vSmart, vManage, vEdge), GRE tunnels, and IPsec site-to-site VPNs.",
        "<strong>Enterprise Security Hardening:</strong> Configure infrastructure plane security including Control Plane Policing (CoPP), Dynamic ARP Inspection (DAI), DHCP Snooping, Port Security, and ACL filtering.",
        "<strong>Quality of Service &amp; High Availability:</strong> Architect QoS scheduling/marking mechanisms (DSCP/CoS) and first-hop redundancy protocols (HSRP/VRRP) to guarantee mission-critical SLA uptime.",
        "<strong>Network Automation &amp; Programmability:</strong> Synthesize modern network programmability concepts utilizing Python, RESTCONF, NETCONF, YANG data models, and JSON payloads.",
        "<strong>Graduate Scholarly Synthesis:</strong> Author a peer-reviewed style graduate research paper evaluating enterprise network design decisions, backed by authoritative RFC standards and industry benchmarks."
    ]
    for slo in slos:
        story.append(Paragraph(f"• {slo}", bullet_style))

    # 4. Required Materials (ZTC)
    story.append(Spacer(1, 6))
    story.append(Paragraph("2. Required Materials (Zero Textbook Cost — ZTC)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#d9a74a"), spaceBefore=1, spaceAfter=6))
    story.append(Paragraph("<strong>Zero Textbook Cost (ZTC):</strong> This is a designated ZTC course. All required readings, video lecture scripts, lab topologies, and documentation are provided completely free within the Canvas LMS course shell. <strong>No textbook purchase is required.</strong>", body_style))
    materials = [
        "<strong>Cisco Packet Tracer (Free):</strong> Version 8.2+ (Downloadable free via Cisco Skills for All introductory course). All weekly labs run natively in Packet Tracer. No ongoing NetAcad course logins required.",
        "<strong>IETF Request for Comments (RFCs):</strong> Authoritative technical references (e.g., OSPF RFC 2328, BGP-4 RFC 4271, MPLS RFC 3031, IPv6 RFC 8200).",
        "<strong>Cisco CCNP Enterprise Documentation &amp; DevNet:</strong> Free official configuration blueprints and programmability labs via Cisco Learning Network and DevNet.",
        "<strong>Hardware &amp; Software Requirements:</strong> Windows 10/11, macOS 12+, or modern Linux system capable of running Cisco Packet Tracer with continuous broadband internet connectivity."
    ]
    for mat in materials:
        story.append(Paragraph(f"• {mat}", bullet_style))

    story.append(PageBreak())

    # 5. Grading Policy & Evaluation
    story.append(Paragraph("3. Grading Policy &amp; Evaluation Criteria", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#d9a74a"), spaceBefore=1, spaceAfter=6))
    story.append(Paragraph("Your final course grade is determined by performance across five weighted assignment categories:", body_style))

    grading_table_data = [
        [Paragraph("Assessment Category", tbl_header), Paragraph("Syllabus Weight", tbl_header), Paragraph("Academic Description &amp; Rigor", tbl_header)],
        [Paragraph("<strong>Weekly Lab Assignments</strong> (Modules 01–06)", tbl_body), Paragraph("<strong>30.0%</strong>", tbl_body), Paragraph("Applied Cisco Packet Tracer topology configurations (.pkt) accompanied by formal technical analysis reports (PDF).", tbl_body)],
        [Paragraph("<strong>Weekly Quizzes</strong> (Modules 01–06)", tbl_body), Paragraph("<strong>20.0%</strong>", tbl_body), Paragraph("Rigorous CCNP-level multiple-choice and scenario problem sets evaluating protocol mechanics and design choices.", tbl_body)],
        [Paragraph("<strong>Graduate Discussion Boards</strong> (Modules 01–06)", tbl_body), Paragraph("<strong>20.0%</strong>", tbl_body), Paragraph("Substantive academic discourse (400+ words) requiring external citation of RFCs/vendor benchmarks and two peer critiques.", tbl_body)],
        [Paragraph("<strong>Graduate Research Paper</strong> (Module 06)", tbl_body), Paragraph("<strong>10.0%</strong>", tbl_body), Paragraph("5–7 page technical research paper exploring emerging enterprise networking architectures formatted in IEEE/APA 7 style.", tbl_body)],
        [Paragraph("<strong>Capstone Lab &amp; Final Exam</strong> (Module 07)", tbl_body), Paragraph("<strong>20.0%</strong>", tbl_body), Paragraph("Comprehensive multi-site enterprise troubleshooting simulation lab and culminating graduate technical exam.", tbl_body)],
        [Paragraph("<strong>Total</strong>", tbl_header), Paragraph("<strong>100.0%</strong>", tbl_header), Paragraph("<strong>Standard University Weighted Gradebook</strong>", tbl_header)]
    ]
    grade_table = Table(grading_table_data, colWidths=[160, 84, 260])
    grade_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1b365d')),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor("#334155")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.white, colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(grade_table)
    story.append(Spacer(1, 6))

    # Grading Scale
    scale_data = [
        [Paragraph("Letter Grade", tbl_header), Paragraph("Percentage Threshold", tbl_header), Paragraph("Academic Performance Level", tbl_header)],
        [Paragraph("<strong>A</strong>", tbl_body), Paragraph("90.0% – 100.0%", tbl_body), Paragraph("Excellent / Superior Graduate Performance", tbl_body)],
        [Paragraph("<strong>B</strong>", tbl_body), Paragraph("80.0% – 89.9%", tbl_body), Paragraph("Good / Standard Graduate Competency", tbl_body)],
        [Paragraph("<strong>C</strong>", tbl_body), Paragraph("70.0% – 79.9%", tbl_body), Paragraph("Minimum Passing (Lowest Grade for Graduate Degree Credit)", tbl_body)],
        [Paragraph("<strong>F</strong>", tbl_body), Paragraph("Below 70.0%", tbl_body), Paragraph("Failing Grade (Course Must Be Retaken for Graduate Credit)", tbl_body)]
    ]
    scale_table = Table(scale_data, colWidths=[90, 130, 284])
    scale_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#475569")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(scale_table)

    # Graduate Credit Alert Callout
    callout_content = [
        [Paragraph("<strong>Graduate Academic Credit Mandate:</strong> Per Texas Wesleyan University Graduate Catalog policy, a minimum final course grade of <strong>\"C\" (70.0%)</strong> is required to earn graduate degree credit. Any final grade below 70.0% constitutes course failure and requires repeating the course.", callout_style)]
    ]
    callout_tbl = Table(callout_content, colWidths=[504])
    callout_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#fff1f2")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#fda4af")),
        ('LINELEFT', (0,0), (0,-1), 3, primary_color),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(Spacer(1, 6))
    story.append(callout_tbl)
    story.append(Spacer(1, 8))

    # 6. Compressed 7-Week Course Schedule
    story.append(Paragraph("4. Compressed 7-Week Course Schedule &amp; Blueprint", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#d9a74a"), spaceBefore=1, spaceAfter=6))
    story.append(Paragraph("This course operates on an intensive <strong>7-Week accelerated format</strong> (October 19 – December 11, 2026). Each module represents one full week of graduate-level study:", body_style))

    sched_data = [
        [Paragraph("Module", tbl_header), Paragraph("Dates", tbl_header), Paragraph("Core Topics &amp; Technical Coverage", tbl_header), Paragraph("Required Deliverables Due", tbl_header)],
        [Paragraph("<strong>Mod 01</strong>", tbl_body), Paragraph("Week 1<br/><strong>Oct 19 – Oct 25</strong>", tbl_body),
         Paragraph("<strong>Advanced IP Routing:</strong> Multi-area OSPFv2/v3, EIGRP unequal-cost load balancing, mutual route redistribution with route tagging.", tbl_body),
         Paragraph("• Discussion M01<br/>• Lab M01 (.pkt + PDF)<br/>• Quiz M01 (100 pts)", tbl_body)],
        [Paragraph("<strong>Mod 02</strong>", tbl_body), Paragraph("Week 2<br/><strong>Oct 26 – Nov 01</strong>", tbl_body),
         Paragraph("<strong>Campus Network Design:</strong> 802.1Q VLAN trunking, Spanning Tree (PVST+, Rapid-PVST, MSTP), LACP EtherChannel, VTP v3.", tbl_body),
         Paragraph("• Discussion M02<br/>• Lab M02 (.pkt + PDF)<br/>• Quiz M02 (100 pts)", tbl_body)],
        [Paragraph("<strong>Mod 03</strong>", tbl_body), Paragraph("Week 3<br/><strong>Nov 02 – Nov 08</strong>", tbl_body),
         Paragraph("<strong>WAN &amp; Edge Technologies:</strong> MPLS label distribution (LDP), BGP path attributes (Weight, Local Pref, AS-Path, MED), SD-WAN architecture.", tbl_body),
         Paragraph("• Discussion M03<br/>• Lab M03 (.pkt + PDF)<br/>• Quiz M03 (100 pts)", tbl_body)],
        [Paragraph("<strong>Mod 04</strong>", tbl_body), Paragraph("Week 4<br/><strong>Nov 09 – Nov 15</strong>", tbl_body),
         Paragraph("<strong>Enterprise Security Hardening:</strong> Control Plane Policing (CoPP), Dynamic ARP Inspection (DAI), DHCP Snooping, Port Security, IPsec VPNs.", tbl_body),
         Paragraph("• Discussion M04<br/>• Lab M04 (.pkt + PDF)<br/>• Quiz M04 (100 pts)", tbl_body)],
        [Paragraph("<strong>Mod 05</strong>", tbl_body), Paragraph("Week 5<br/><strong>Nov 16 – Nov 22</strong>", tbl_body),
         Paragraph("<strong>QoS, High Availability &amp; Automation:</strong> First-Hop Redundancy (HSRP/VRRP), QoS DiffServ marking/queuing, Python RESTCONF/YANG.", tbl_body),
         Paragraph("• Discussion M05<br/>• Lab M05 (.pkt + PDF)<br/>• Quiz M05 (100 pts)", tbl_body)],
        [Paragraph("<strong>Mod 06</strong>", tbl_body), Paragraph("Week 6<br/><strong>Nov 23 – Nov 29</strong><br/><em>(Ext. Dec 1)</em>", tbl_body),
         Paragraph("<strong>Cloud Networking &amp; Research:</strong> AWS DirectConnect, Azure ExpressRoute, Transit Gateways, and graduate research synthesis.", tbl_body),
         Paragraph("• Discussion M06<br/>• Lab M06 (.pkt + PDF)<br/>• Quiz M06 (100 pts)<br/>• <strong>Graduate Research Paper</strong>", tbl_body)],
        [Paragraph("<strong>Mod 07</strong>", tbl_body), Paragraph("Week 7<br/><strong>Nov 30 – Dec 11</strong>", tbl_body),
         Paragraph("<strong>Capstone Troubleshooting &amp; Final Exam:</strong> Multi-site enterprise diagnostic simulation, root-cause analysis, and comprehensive final exam.", tbl_body),
         Paragraph("• Discussion M07<br/>• <strong>Capstone Lab M07</strong><br/>• <strong>Comprehensive Final Exam</strong>", tbl_body)]
    ]
    sched_table = Table(sched_data, colWidths=[48, 86, 210, 160])
    sched_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1b365d')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(sched_table)

    # Thanksgiving notice
    tg_content = [
        [Paragraph("<strong>⚠ Thanksgiving Holiday Schedule Notice (Module 06):</strong> Thanksgiving Break occurs during Week 6. To accommodate the holiday, Module 06 assignments carry an <strong>extended deadline through Sunday, December 1, 2026 at 11:59 PM CST</strong>. Students are advised to begin research paper preparations early.", callout_style)]
    ]
    tg_tbl = Table(tg_content, colWidths=[504])
    tg_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#fefce8")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#fef08a")),
        ('LINELEFT', (0,0), (0,-1), 3, colors.HexColor("#ca8a04")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(Spacer(1, 6))
    story.append(tg_tbl)

    story.append(PageBreak())

    # 7. University & Departmental Policies
    story.append(Paragraph("5. University &amp; Graduate Academic Policies", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#d9a74a"), spaceBefore=1, spaceAfter=6))

    story.append(Paragraph("Attendance &amp; Substantive Engagement Policy", h2_style))
    story.append(Paragraph("In accordance with federal regulations and SACSCOC accreditation standards for distance education, attendance in this 100% online asynchronous course is measured through <strong>Regular and Substantive Interaction (RSI)</strong>. Students must submit at least one required academic deliverable (discussion post, lab, or quiz) each week to be certified as 'Present.' Failure to submit academic work for <strong>two consecutive weeks</strong> will trigger immediate departmental academic review and may result in administrative withdrawal per Texas Wesleyan University catalog policy.", body_style))

    story.append(Paragraph("Late Work Policy", h2_style))
    story.append(Paragraph("All weekly deliverables are due by <strong>Sunday at 11:59 PM CST</strong>. In an accelerated 7-week graduate curriculum, adhering to pacing is critical. Late submissions are accepted up to <strong>48 hours (2 days) past the posted deadline</strong> with a <strong>15% penalty per 24-hour period</strong>. Submissions received beyond 48 hours will receive a recorded score of zero unless prior arrangements have been approved by the instructor for documented medical or personal emergencies.", body_style))

    story.append(Paragraph("Academic Integrity &amp; Generative AI Guidelines", h2_style))
    story.append(Paragraph("Academic honesty is foundational to graduate scholarship. All submitted technical reports, packet traces, discussion responses, and research manuscripts must represent the student's own intellectual analysis. Plagiarism, cheating, or unauthorized collaboration will result in an immediate zero and disciplinary referral.", body_style))
    ai_guidelines = [
        "<strong>Generative AI Use:</strong> AI tools (e.g., ChatGPT, Gemini) are permitted as supplemental research accelerators and error syntax clarifiers. However, submitting AI-generated text verbatim as your own work constitutes academic misconduct.",
        "<strong>Defense of Work:</strong> Students must be prepared to orally defend any technical claim, protocol configuration, or research finding in a one-on-one conference with the instructor upon request."
    ]
    for g in ai_guidelines:
        story.append(Paragraph(f"• {g}", bullet_style))

    story.append(Paragraph("ADA &amp; Disability Accommodations Statement", h2_style))
    story.append(Paragraph("Texas Wesleyan University is committed to providing equal educational opportunities. In accordance with Section 504 of the Rehabilitation Act of 1973 and the Americans with Disabilities Act (ADA), students with documented disabilities requesting academic accommodations should contact the <strong>Office of Disability Services</strong> (located in the Eunice and James L. West Library) at 817-531-4820 as early in the session as possible.", body_style))

    story.append(Paragraph("Title IX &amp; Non-Discrimination Policy", h2_style))
    story.append(Paragraph("Texas Wesleyan University is committed to maintaining a learning environment free from all forms of discrimination, harassment, and sexual misconduct. If you experience or witness discrimination, sexual harassment, or assault, please report it to the Title IX Coordinator or consult the university student handbook for confidential support services.", body_style))

    story.append(Paragraph("Graduate Academic Support Resources", h2_style))
    support_items = [
        "<strong>University Library (West Library):</strong> Access to IEEE Xplore, ACM Digital Library, peer-reviewed engineering journals, and research consultation.",
        "<strong>Graduate Academic Advising:</strong> Guidance on degree progression, graduation clearance, and prerequisite planning.",
        "<strong>Writing Center:</strong> Specialized assistance for graduate scholars on technical documentation formatting, research synthesis, and IEEE/APA 7 style."
    ]
    for s in support_items:
        story.append(Paragraph(f"• {s}", bullet_style))

    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cbd5e1"), spaceBefore=6, spaceAfter=8))
    story.append(Paragraph("<font size=8 color='#64748b'>Texas Wesleyan University • Department of Computer Science &amp; Information Technology • Fort Worth, Texas<br/>Official Graduate Syllabus for CSC-6361-33 (Fall 2026) • Approved by Professor Nash, Ph.D.</font>", ParagraphStyle('CenterFooter', parent=styles['Normal'], alignment=1)))

    # Build Document
    doc.build(story, canvasmaker=NumberedCanvas)
    
    # Copy to artifacts
    if os.path.exists(pdf_path):
        import shutil
        shutil.copy2(pdf_path, artifact_path)
        size = os.path.getsize(pdf_path)
        print(f"✅ Successfully built publication-grade PDF: {pdf_path} ({size/1024:.1f} KB)")
        print(f"✅ Copied to artifacts directory: {artifact_path}")

if __name__ == "__main__":
    generate_syllabus_pdf()
