import urllib.request
import json
import ssl
import sys
import time

API_BASE = "https://txwes.instructure.com/api/v1"
TOKEN = "21284~xyE786Ptv2MR74T33RfreUc2TVtCTyWkhLGHMXMrn84LmGRYMTrTQzntAF4ZWuZT"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

COURSE_ID = 13090
ASSIGN_ID = 227499  # Lab (M01): Threat & Control Classification (Security Case Study)
ctx = ssl.create_default_context()

def api_call(url, data=None, method="GET"):
    req = urllib.request.Request(url, headers=HEADERS, method=method)
    if data is not None:
        req.data = json.dumps(data).encode('utf-8')
    try:
        with urllib.request.urlopen(req, context=ctx) as resp:
            content = resp.read().decode('utf-8')
            return json.loads(content) if content else {}
    except Exception as e:
        print(f"  ❌ API Error ({method} {url}): {e}")
        return None

def grade_submission(user_id, grade, comment):
    url = f"{API_BASE}/courses/{COURSE_ID}/assignments/{ASSIGN_ID}/submissions/{user_id}"
    payload = {
        "submission": {"posted_grade": str(grade)},
        "comment": {"text_comment": comment}
    }
    res = api_call(url, data=payload, method="PUT")
    if res:
        print(f"  ✅ Graded User {user_id} -> {grade} pts")
    return res

LAB_4328_GRADES = [
    {
        "user_id": 2022,
        "name": "Kobee Cain",
        "grade": 98.0,
        "comment": """Kobee,

Thank you for your submission for Lab (M01): Threat & Control Classification ('Ridgeline_Threat_Control_Classification-1.xlsx').

Evaluation & Technical Feedback:
1. Threat & Vulnerability Modeling: Your spreadsheet matrix demonstrates systematic categorization of the threat events impacting the Ridgeline case study. You accurately separated threat sources (adversary motives) from latent vulnerabilities in the software stack.
2. CIA Triad Impact Mapping: Your mapping across Confidentiality, Integrity, and Availability was logically consistent. You recognized that unencrypted backup tapes and unauthorized database queries directly violate Confidentiality, whereas ransomware encrypting critical volumes is an assault on Availability.
3. Security Control Taxonomy: Your recommended controls aligned well with NIST SP 800-53 control families. 
4. Professional Tip: In spreadsheet matrices, explicitly labeling each control's function (Preventive, Detective, Corrective, Deterrent) alongside its category (Administrative, Technical, Physical) provides executive auditors with immediate visibility.

Overall: Rigorous and structured work.

Grade: 98/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 2355,
        "name": "Chasity Gaston",
        "grade": 98.0,
        "comment": """Chasity,

Superb work on Lab (M01): Threat & Control Classification ('CIS Lab 01.docx').

Evaluation & Technical Feedback:
1. Scenario Deconstruction: Your report provides a thorough narrative analysis of Ridgeline's security posture. You accurately diagnosed how rapid corporate growth without governance leads to architectural vulnerabilities.
2. Control Recommendations: Your proposed remediation roadmap—recommending Multi-Factor Authentication (MFA), role-based access control (RBAC), and centralized Endpoint Detection and Response (EDR)—directly targets the primary attack vectors.
3. Scholarly Commendation: Your explanation of why administrative policies (such as an Acceptable Use Policy) must precede technical enforcement demonstrates a mature understanding of information assurance.

Grade: 98/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 2611,
        "name": "Jaalen Williams",
        "grade": 97.0,
        "comment": """Jaalen,

Very well done on Lab (M01): Threat and Control Classification ('Threat and Control Classification Exercise Jaalen_Williams.docx').

Evaluation & Technical Feedback:
1. Classification Accuracy: You properly classified each threat scenario, correctly identifying phishing vectors, unauthorized external transfers, and insider privilege escalation.
2. Defense-in-Depth Implementation: Your recommendations emphasize layered security rather than relying on a single defensive perimeter. You highlighted network segmentation and email gateway filtering as vital first lines of defense.
3. Area for Continued Depth: Ensure that when recommending security controls, you consistently specify the functional type (e.g. distinguishing Detective controls like SIEM log aggregation from Preventive controls like next-gen firewall IPS rules).

Overall: High-quality, professional report.

Grade: 97/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 4018,
        "name": "Israel Lopez",
        "grade": 98.0,
        "comment": """Israel,

Outstanding technical submission for Lab (M01) ('Ridgeline_Threat_and_Control_Classification_Lab_Israel Lopez.docx').

Evaluation & Technical Feedback:
1. Analytical Rigor: Your breakdown of the threat scenarios demonstrates sharp risk evaluation. You accurately highlighted how known CVEs combined with lack of patch management elevate operational risk in the organization.
2. Technical Depth: Your discussion of technical controls—including EDR agents, automated patch deployment via WSUS/SCCM, and least privilege enforcement—reflects practical systems engineering knowledge.
3. Formatting & Presentation: The document is structured logically with clear headings and executive-ready recommendations.

Grade: 98/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 4694,
        "name": "Avarieus Dwin",
        "grade": 96.0,
        "comment": """Avarieus (AD),

Thank you for your multi-part submission ('Lab Part 1.pdf', 'Lab Part 2.pdf', 'Lab Part 3.pdf') for Lab (M01).

Evaluation & Technical Feedback:
1. Threat Identification: Across your three submission files, you addressed the complete spectrum of the Ridgeline case study. You accurately identified both external and internal threat vectors and evaluated the business impact of data loss.
2. Control Justification: Your control suggestions (including biometric access controls, network monitoring, and mandatory employee awareness training) were sound.
3. Professional Tip: In future deliverables, combining your individual PDF sections into a single consolidated executive PDF report will streamline the review process for security compliance audits.

Overall: Solid effort and strong conceptual grasp.

Grade: 96/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 4806,
        "name": "Chrissean Sias-Rackstraw",
        "grade": 96.0,
        "comment": """Chrissean,

Good work on Lab (M01) ('Lab Reading guide.docx').

Evaluation & Technical Feedback:
1. Core Threat Analysis: You effectively worked through the scenario questions, identifying vulnerabilities in Ridgeline's legacy systems and unmanaged endpoint environment.
2. CIA Triad Application: Your analysis correctly connected data theft to Confidentiality breaches and system downtime to Availability loss.
3. Remediation Strategy: Your suggestions regarding antivirus deployment, firewall rules, and password complexity policies provide a solid baseline for risk reduction.

Keep up the disciplined momentum as we move into cryptography and network security architectures!

Grade: 96/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 5072,
        "name": "Bryan Lopez",
        "grade": 97.0,
        "comment": """Bryan,

Strong submission for Lab (M01) ('Lab 1- Bryan Lopez.pdf').

Evaluation & Technical Feedback:
1. Threat Classification: Your evaluation of the case study events was thorough. You properly distinguished between intentional malicious actions (such as credential theft and data exfiltration) versus accidental operational errors.
2. Risk Assessment: Your discussion of likelihood and impact mirrors standard qualitative risk matrices used in enterprise environments.
3. Control Recommendations: Your proposal for network segmentation, regular vulnerability scanning, and incident response preparedness was well articulated.

Grade: 97/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 8992,
        "name": "Anthony Cruz",
        "grade": 97.0,
        "comment": """Anthony,

Very well done on Lab (M01) ('Lab M01-Anthony Cruz.docx').

Evaluation & Technical Feedback:
1. Systematic Analysis: Your report walks through the threat classification exercise with clarity and precision. You accurately diagnosed the risks stemming from unmonitored outbound traffic and lack of multi-factor authentication.
2. Security Controls: Your proposed controls span administrative (acceptable use policies), technical (firewall access lists and DLP), and operational (quarterly audits) categories.
3. Practical Insight: Your note on how human error contributes to social engineering success underscores the necessity of continuous security training.

Grade: 97/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 15566,
        "name": "Zaniya Grice",
        "grade": 100.0,
        "comment": """Zaniya,

An exemplary, doctoral-quality case study evaluation ('Lab MO1.docx').

Evaluation & Technical Feedback:
1. Framework Alignment: Your classification matrix seamlessly incorporates both NIST SP 800-53 and CompTIA Security+ (SY0-701) taxonomies. You accurately classified threats by intent, actor capability, and attack vector.
2. Comprehensive Control Architecture: Your recommendations provide a complete defense-in-depth model:
   • Administrative: Governance frameworks, incident response plan formalization, and vendor risk management.
   • Technical: Centralized SIEM telemetry, EDR agent deployment, automated patch management, and strict egress filtering.
   • Physical: Environmental access control and secure media disposal.
3. Business Context: You articulated how these controls safeguard business continuity and protect Ridgeline from regulatory liability.

Superb work from start to finish!

Grade: 100/100 (A+)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 15652,
        "name": "Arinzechukwu Ejeckam",
        "grade": 98.0,
        "comment": """Arinze,

Outstanding laboratory report ('Security Lab 1 (2).pdf') for Lab (M01).

Evaluation & Technical Feedback:
1. Executive Quality: Your PDF report is formatted cleanly and articulates threat dynamics with high technical precision.
2. Gap Analysis: You identified Ridgeline's primary deficiency: the disconnect between operational expansion and cybersecurity governance. You correctly noted that having only 40% antivirus coverage leaves the organization blind to lateral movement.
3. Remediation Roadmap: Your prioritization of immediate compensating controls (network isolation of vulnerable assets) followed by strategic technical controls (MFA, centralized logging) demonstrates sound security engineering logic.

Grade: 98/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 15899,
        "name": "Christopher King",
        "grade": 99.0,
        "comment": """Christopher,

Exceptional submission for Lab (M01) ('Lab M01 Cking.docx').

Evaluation & Technical Feedback:
1. Analytical Sophistication: Your threat modeling goes beyond surface-level observations. You evaluated threat actor motivations, living-off-the-land techniques, and privilege escalation pathways with impressive realism.
2. Control Taxonomy: You mapped controls with precision across Preventive, Detective, and Corrective functions. Your recommendation to implement User and Entity Behavior Analytics (UEBA) alongside automated host isolation reflects cutting-edge SOC methodologies.
3. Critical Thinking: Your synthesis of technical findings into actionable risk mitigation steps is exemplary.

Grade: 99/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 20444,
        "name": "Natalie Turrubiartes",
        "grade": 97.0,
        "comment": """Natalie,

Very strong laboratory report ('Lab (M1) Natalie Turrubiartes-0522185 (3).pdf') on Threat and Control Classification.

Evaluation & Technical Feedback:
1. Structural Organization: Your PDF submission is well laid out with clear sections addressing each scenario in the Ridgeline exercise.
2. Threat & Risk Identification: You accurately identified vulnerabilities across endpoints, network perimeters, and user behaviors, correctly assessing the risk posed to organizational data confidentiality.
3. Control Recommendations: Your proposals for endpoint security hardening, strict access controls, and regular employee awareness training provide an effective remediation plan.

Great work!

Grade: 97/100 (A)
— Professor Nash, Ph.D."""
    }
]

def main():
    print("=" * 80)
    print("GRADING CIS-4328 LAB (M01): THREAT & CONTROL CLASSIFICATION")
    print("=" * 80)
    for s in LAB_4328_GRADES:
        grade_submission(s["user_id"], s["grade"], s["comment"])
        time.sleep(0.5)
    print("\n" + "=" * 80)
    print("✅ CIS-4328 LAB (M01) FULLY GRADED WITH SCHOLARLY FEEDBACK!")
    print("=" * 80)

if __name__ == "__main__":
    main()
