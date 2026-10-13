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

def grade_submission(course_id, assign_id, user_id, grade, comment):
    url = f"{API_BASE}/courses/{course_id}/assignments/{assign_id}/submissions/{user_id}"
    payload = {
        "submission": {"posted_grade": str(grade)},
        "comment": {"text_comment": comment}
    }
    res = api_call(url, data=payload, method="PUT")
    if res:
        print(f"  ✅ Graded User {user_id} on Assignment {assign_id} -> {grade} pts")
    return res

def post_discussion_reply(course_id, topic_id, entry_id, html_message):
    url = f"{API_BASE}/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies"
    payload = {"message": html_message}
    res = api_call(url, data=payload, method="POST")
    if res:
        print(f"  💬 Posted reply to Entry {entry_id}")
    return res

# ==============================================================================
# 1. CIS-4328 INTRODUCE YOURSELF
# ==============================================================================
INTRO_4328 = [
    {
        "user_id": 2022,
        "entry_id": 458340,
        "name": "Kobee Cain",
        "grade": 100.0,
        "comment": "Kobee, welcome to CIS-4328! As a graduating senior in CIS, developing operational fluency in information security architecture, threat intelligence, and risk mitigation will provide the crowning asset on your resume. Great introduction!",
        "reply": "<p>Hello Kobee,</p><p>Welcome to Information Security! In today's digital landscape, enterprise systems administrators and developers must approach every workflow with a security-first posture. You will find that our coverage of CompTIA Security+ and ISC2 CC domains directly complements your CIS degree. Glad to have you in the course!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 4018,
        "entry_id": 458342,
        "name": "Israel Lopez",
        "grade": 100.0,
        "comment": "Israel, welcome to the course! Information security is an essential discipline for all CIS majors. Understanding defense-in-depth, identity management, and threat vectors will prepare you well for the tech industry. Outstanding post!",
        "reply": "<p>Hello Israel,</p><p>Welcome to CIS-4328! You are entering this class at an exciting time. Whether your future career path leads to systems administration, database architecture, or specialized cybersecurity operations, the principles of confidentiality, integrity, and availability we study will be foundational. Welcome aboard!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 8992,
        "entry_id": 458344,
        "name": "Anthony Cruz",
        "grade": 100.0,
        "comment": "Anthony, welcome! Pairing a CIS major with a Music minor is a wonderful combination. The intersection of audio engineering, digital signal processing, and computer systems requires high precision. In security, that same meticulous attention to detail makes an outstanding analyst. Great to have you with us!",
        "reply": "<p>Hello Anthony,</p><p>Welcome to the class! Your combination of CIS and Music is fantastic. In cybersecurity, pattern recognition and anomaly detection in event logs are very similar to recognizing harmonic and rhythmic variations in music theory. I look forward to your contributions this semester!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 15566,
        "entry_id": 458346,
        "name": "Zaniya Grice",
        "grade": 100.0,
        "comment": "Zaniya, welcome to CIS-4328 in your final semester! As someone completing their bachelor's degree, this course will tie together your systems knowledge into a cohesive defense-in-depth framework. Excellent introduction!",
        "reply": "<p>Hello Zaniya,</p><p>Welcome to your final undergraduate semester! Synthesizing threat modeling, cryptographic controls, and governance frameworks in this course will give you the competitive edge needed for senior IT leadership. Let's make this capstone term memorable!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 4806,
        "entry_id": 458356,
        "name": "Chrissean Sias-Rackstraw",
        "grade": 100.0,
        "comment": "Chrissean, welcome! Having genuine curiosity about cybersecurity threats, ransomware mitigation, and defensive controls is the best possible foundation. As a graduating senior, this course will prepare you directly for industry certifications like Security+ and ISC2 CC. Wonderful post!",
        "reply": "<p>Hello Chrissean,</p><p>Welcome to CIS-4328! You don't need years of prior specialized security experience to excel here; our structured labs and analytical case studies are designed specifically to build your threat-hunting intuition step by step. Glad to have you in class!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 4694,
        "entry_id": 458661,
        "name": "Avarieus Dwin",
        "grade": 100.0,
        "comment": "Avarieus (AD), welcome! It is great to have you in class as a senior in CIS. Understanding how adversaries exploit vulnerabilities and how organizations engineer resilient controls is both fascinating and highly marketable. Terrific post!",
        "reply": "<p>Hello AD,</p><p>Welcome to the course! Information security touches every facet of modern business. In our case study labs, you will act as a security consultant evaluating real-world threat scenarios, preparing you for immediate post-graduation roles. Welcome aboard!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 15652,
        "entry_id": 459478,
        "name": "Arinzechukwu Ejeckam",
        "grade": 100.0,
        "comment": "Arinze, welcome to CIS-4328! Your eagerness to delve deeply into information systems security as a junior shows commendable academic foresight. The security architectures we study here will elevate all your future coursework and career opportunities!",
        "reply": "<p>Hello Arinze,</p><p>Welcome to the class! Gaining deep exposure to security engineering during your junior year gives you an enormous advantage for internships and professional certifications. I am excited to see your analytical thinking unfold in our discussions!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 4464,
        "entry_id": 459526,
        "name": "Benjamin Flores",
        "grade": 100.0,
        "comment": "Benjamin, welcome! Completing this security course alongside Network Administration gives you a comprehensive understanding of both infrastructure and defensive architecture. Outstanding introduction!",
        "reply": "<p>Hello Benjamin,</p><p>Welcome to CIS-4328! Taking network administration and information security in parallel is the ideal academic pairing. You will see firsthand how the network protocols configured in CIS-3321 are defended, monitored, and encrypted here in CIS-4328. Looking forward to a great semester!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 2611,
        "entry_id": 460825,
        "name": "Jaalen Williams",
        "grade": 100.0,
        "comment": "Jaalen, welcome to CIS-4328! You rightly noted that cybersecurity is one of the most critical and fast-evolving domains in technology. As a graduating senior, this course will prepare you with hands-on skills in threat classification, cryptography, and incidence response. Great to have you with us!",
        "reply": "<p>Hello Jaalen,</p><p>Welcome to Information Security! Your enthusiasm for the field is fantastic. Organizations across all sectors desperately need professionals who understand both the technical mechanisms of cyberattacks and the risk management frameworks required to defend against them. Welcome!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 15567,
        "entry_id": 461118,
        "name": "Elijah Kilgore",
        "grade": 100.0,
        "comment": "Elijah, welcome! Your career goal of entering the cybersecurity industry post-graduation aligns perfectly with CIS-4328. Everything we study—from CompTIA Security+ domains to incident response playbooks—will build your professional toolkit. Excellent post!",
        "reply": "<p>Hello Elijah,</p><p>Welcome to CIS-4328! With your ambition to break directly into cybersecurity upon graduation, you are in the right place. Be sure to leverage our multi-certification prep guides (covering Security+, CySA+, and ISC2 CC) in the Orientation module to maximize your career trajectory!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 5072,
        "entry_id": 461845,
        "name": "Bryan Lopez",
        "grade": 100.0,
        "comment": "Bryan, welcome! Senior year is an exciting time, and adding cybersecurity proficiency to your CIS major will make you versatile across IT operations, compliance, and systems security. Great introduction!",
        "reply": "<p>Hello Bryan,</p><p>Welcome to the course! Many CIS professionals discover their passion for security once they see how vulnerabilities translate into real-world business risks. The scenario-based case studies we complete will give you practical, job-ready problem-solving experience. Glad to have you!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 21504,
        "entry_id": 462625,
        "name": "Caleb Olen",
        "grade": 100.0,
        "comment": "Caleb, welcome! Your recognition of how crucial security is to databases and modern enterprise technology demonstrates strong systems awareness. Excited to have you in the course for your senior year!",
        "reply": "<p>Hello Caleb,</p><p>Welcome to CIS-4328! You raised a great point regarding database security. Data at rest, data in transit, and role-based access control (RBAC) are central pillars of modern information assurance. I look forward to your perspective in our discussions!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 15445,
        "entry_id": 464672,
        "name": "Voldi Madiadia",
        "grade": 100.0,
        "comment": "Voldi (James), welcome to CIS-4328! Pairing Information Systems with a Business Administration minor gives you an innate understanding of the CIA triad, business continuity, and quantitative risk assessment (ALE/SLE/ARO). Terrific post!",
        "reply": "<p>Hello James,</p><p>Welcome to Information Security! In the corporate world, Chief Information Security Officers (CISOs) must bridge the gap between technical vulnerabilities and executive financial risk. Your business administration background will serve you well when we study risk management frameworks. Welcome aboard!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 2355,
        "entry_id": 464755,
        "name": "Chasity Gaston",
        "grade": 100.0,
        "comment": "Chasity, welcome! It is exciting to have you in your final CIS course before graduation. Finishing your degree with cybersecurity provides the capstone security lens that protects all software and information assets. Outstanding introduction!",
        "reply": "<p>Hello Chasity,</p><p>Welcome to your final CIS course! Concluding your academic program with cybersecurity is the ideal culmination of your degree. You will synthesize systems analysis, data governance, and threat mitigation into a comprehensive professional skill set. Best of luck in your graduating term!</p><p>— Professor Nash, Ph.D.</p>"
    }
]

# ==============================================================================
# 2. CIS-4328 MODULE 01 DISCUSSION: THREATS, ATTACKS & VULNERABILITIES
# ==============================================================================
M01_4328 = [
    {
        "user_id": 4464,
        "entry_id": 464687,
        "name": "Benjamin Flores",
        "grade": 98.0,
        "comment": "Benjamin, excellent analysis of Scenario C (The Controls Gap). You correctly identified the severe deficit in administrative controls (written security policies, acceptable use policies, onboarding/offboarding) and technical controls (centralized endpoint management, disk encryption, EDR). Your recommendations regarding policy creation and endpoint hardening align with NIST SP 800-53. Great work!",
        "reply": "<p>Benjamin,</p><p>You provided a very perceptive evaluation of Scenario C. A rapidly expanding startup frequently suffers from 'technical debt' and 'policy debt.' When 60% of company laptops lack basic endpoint protection and no data classification policy exists, the organization is exposed to severe compliance and breach risks.</p><p>Your distinction between administrative controls (establishing the governance mandate) and technical controls (enforcing the mandate via software agents and firewalls) is essential for CompTIA Security+. How would you prioritize the deployment order between drafting policies versus deploying endpoint detection? Excellent post!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 21504,
        "entry_id": 465034,
        "name": "Caleb Olen",
        "grade": 98.0,
        "comment": "Caleb, thorough and thoughtful response to Scenario B (Suspicious Outbound Transfer). You correctly analyzed the likelihood of insider threat exfiltration given the absence of external malware alerts and the senior accountant's privileged access. Your proposed detective and preventive controls were well targeted. Strong analysis!",
        "reply": "<p>Caleb,</p><p>Your breakdown of Scenario B captures the nuanced reality of insider threats. When an authenticated user with 11 years of tenure initiates an anomalous transfer to an unfamiliar external destination, perimeter defenses (like standard firewalls) often fail because the traffic originates from an authorized identity.</p><p>You correctly highlighted the need for Data Loss Prevention (DLP) and User and Entity Behavior Analytics (UEBA). From an evidentiary perspective, what legal or chain-of-custody steps must the incident response team take before confronting the employee? Outstanding contribution!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 15652,
        "entry_id": 465099,
        "name": "Arinzechukwu Ejeckam",
        "grade": 98.0,
        "comment": "Arinze, comprehensive analysis of Scenario C. You accurately identified the glaring gaps in technical controls (missing antivirus/EDR on 60% of endpoints, unmanaged bring-your-own-device risks) and administrative controls (lack of security awareness training and acceptable use policies). Well structured and technically sound!",
        "reply": "<p>Arinze,</p><p>You did a terrific job diagnosing the root causes of risk in Scenario C. An organization operating with 40% antivirus coverage effectively has zero enterprise visibility—adversaries will naturally target the unprotected nodes as pivot points to establish persistence.</p><p>Your recommendation to enforce centralized Mobile Device Management (MDM) alongside mandatory security awareness training demonstrates a mature understanding of defense-in-depth. Great work!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 4018,
        "entry_id": 465477,
        "name": "Israel Lopez",
        "grade": 98.0,
        "comment": "Israel, outstanding analysis of Scenario A (The Unpatched Server). You articulated the crucial distinction between a vulnerability (an unpatched flaw in an unsupported OS) and risk (the probability of threat exploitation and the resulting impact on patient care). Your proposed compensating controls (network isolation/VLANs and virtual patching) were top-tier!",
        "reply": "<p>Israel,</p><p>Your distinction between a <em>vulnerability</em> (the latent flaw in the legacy OS) and a <em>risk</em> (the likelihood of an active exploit occurring multiplied by the severe impact on patient care) was mathematically and conceptually spot on.</p><p>In healthcare environments governed by HIPAA, taking clinical systems offline is often impossible. Your recommendation to implement compensating controls—specifically placing the imaging system on an isolated VLAN behind an internal firewall with strict access control lists (ACLs)—is standard enterprise best practice. Excellent post!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 15566,
        "entry_id": 465509,
        "name": "Zaniya Grice",
        "grade": 100.0,
        "comment": "Zaniya, this is an exemplary doctoral-level analysis of Scenario C. Your use of formal NIST control taxonomy—distinguishing Managerial/Administrative controls (governance frameworks, security policies), Operational controls (employee awareness training, incident response procedures), and Technical controls (EDR, NAC, disk encryption)—was textbook perfection. A flawless 100/100!",
        "reply": "<p>Zaniya,</p><p>This is a masterclass in security control taxonomy. You properly mapped the startup's vulnerabilities against both managerial (governance, policies) and operational controls (change management, employee training), which many students overlook in favor of pure technical fixes.</p><p>Without managerial policies establishing mandatory standards, technical controls inevitably degrade into unmaintained silos. Your answer reflects the holistic risk-management mindset expected on the CompTIA Security+ and ISC2 CC exams. Outstanding work!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 2355,
        "entry_id": 466408,
        "name": "Chasity Gaston",
        "grade": 98.0,
        "comment": "Chasity, excellent response to Scenario A. You accurately explained that having known CVEs with active exploits in the wild elevates a dormant vulnerability into an immediate, severe operational risk. Your compensating controls—network segmentation and strict host-based isolation—were precisely tailored to healthcare constraints. Great job!",
        "reply": "<p>Chasity,</p><p>Very well articulated. You correctly emphasized that the presence of known, weaponized exploits in the healthcare sector transforms this unpatched OS into an immediate, critical threat vector.</p><p>Your proposal to enforce compensating controls—such as placing the legacy device behind a dedicated micro-segmented firewall that allows only approved medical imaging DICOM traffic—protects patient safety without requiring an impossible OS upgrade. Superb analysis!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 2022,
        "entry_id": 466714,
        "name": "Kobee Cain",
        "grade": 98.0,
        "comment": "Kobee, very strong analysis of Scenario A. You clearly identified the software vulnerability class (unsupported legacy OS) and provided a rigorous justification for why this constitutes active organizational risk under NIST guidelines. Your proposed network isolation controls were technically sound. Excellent work!",
        "reply": "<p>Kobee,</p><p>Solid technical breakdown. You correctly recognized that the inability of the vendor to provide patches means standard vulnerability management workflows are blocked, forcing the hospital to rely entirely on defense-in-depth compensating controls.</p><p>Beyond network segmentation, how might an Intrusion Prevention System (IPS) with virtual patching signatures help neutralize exploit attempts targeting those specific CVEs before packets reach the legacy OS? Great contribution!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 4806,
        "entry_id": 466880,
        "name": "Chrissean Sias-Rackstraw",
        "grade": 97.0,
        "comment": "Chrissean, very strong analysis of Scenario B. You accurately classified the threat actor as an insider threat and correctly identified data exfiltration as the attack vector. Your evaluation of privileged user risk and proposed detective controls were well reasoned. Good job!",
        "reply": "<p>Chrissean,</p><p>You hit upon a critical insight: privileged insider threats are among the most difficult to detect because their actions mirror legitimate business activity. An accountant accessing financial databases is expected behavior; anomalous bulk exfiltration during non-business hours is the red flag.</p><p>Your recommendation to implement User and Entity Behavior Analytics (UEBA) and egress filtering is exactly what enterprise SOCs deploy to catch unauthorized data transfers. Well done!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 4694,
        "entry_id": 466925,
        "name": "Avarieus Dwin",
        "grade": 97.0,
        "comment": "Avarieus (AD), great analysis of Scenario B. You astutely observed that the situation represents either an intentional malicious insider or a compromised account session (such as session hijacking or credential theft). Your proposed remediation controls were well targeted. Strong work!",
        "reply": "<p>AD,</p><p>Your dual hypothesis—that this could either be a malicious insider acting intentionally OR a legitimate user whose session tokens were hijacked by an external adversary—demonstrates advanced threat analysis thinking.</p><p>In both cases, implementing strict egress Data Loss Prevention (DLP) rules that block unauthorized bulk uploads to cloud storage would neutralize the data leak regardless of who controls the keyboard. Great analysis!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 15899,
        "entry_id": 467556,
        "name": "Christopher King",
        "grade": 99.0,
        "comment": "Christopher, exceptional analysis of Scenario B! Your exploration of both intentional insider exfiltration and credential/session hijacking reflects professional incident response acumen. Your recommended controls—combining behavioral baseline monitoring, proxy inspection, and immediate forensic disk isolation—were top tier. Well done!",
        "reply": "<p>Christopher,</p><p>Your evaluation of Scenario B demonstrates exceptional depth. Acknowledging that an authorized identity could be compromised via living-off-the-land techniques or session token theft is exactly how tier-3 SOC analysts approach anomalous telemetry.</p><p>Your recommendation to combine technical DLP enforcement with operational forensic triage (capturing volatile memory before powering down the endpoint) adheres strictly to NIST SP 800-61 Rev. 2 guidelines. Outstanding work!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 2611,
        "entry_id": 468007,
        "name": "Jaalen Williams",
        "grade": 96.0,
        "comment": "Jaalen, solid analysis of Scenario A. You accurately diagnosed the unpatched legacy OS vulnerability and highlighted the acute risk to hospital patient data and operational continuity. Your proposed compensating controls were practical and effective. Good work!",
        "reply": "<p>Jaalen,</p><p>Very clear response. You correctly noted that because the OS cannot be patched without breaking the imaging software, traditional vulnerability remediation fails, requiring immediate compensating controls.</p><p>Restricting physical access, isolating the imaging modality on a protected subnet, and disabling all non-essential network services on that host are vital steps to safeguard the medical environment. Good job!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 5072,
        "entry_id": 468091,
        "name": "Bryan Lopez",
        "grade": 96.0,
        "comment": "Bryan, strong evaluation of Scenario A. You clearly explained why active CVEs in the healthcare sector elevate a software vulnerability into an urgent organizational risk. Your proposed technical isolation controls were well chosen.",
        "reply": "<p>Bryan,</p><p>Well stated. You articulated the core risk equation: Risk = Threat x Vulnerability x Impact. With active threats exploiting the known CVEs and high impact on patient care, the risk is severe.</p><p>Implementing an internal firewall that restricts inbound communication to only authorized radiology viewing stations drastically shrinks the attack surface. Excellent contribution!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 8992,
        "entry_id": 468400,
        "name": "Anthony Cruz",
        "grade": 97.0,
        "comment": "Anthony, very well reasoned breakdown of Scenario B. You accurately identified the insider threat vector and data exfiltration category, noting that the absence of malware alerts points toward abuse of legitimate credentials. Your recommended controls were solid. Great job!",
        "reply": "<p>Anthony,</p><p>Solid analytical reasoning. When an employee with over a decade of tenure initiates suspicious outbound data transfers without triggering signature-based antivirus alerts, it underscores why signature detection alone is obsolete in modern enterprise defense.</p><p>Organizations must deploy behavioral anomaly detection and network traffic analysis (NTA) to spot outbound anomalies regardless of whether malware is present. Excellent work!</p><p>— Professor Nash, Ph.D.</p>"
    }
]

def main():
    print("=" * 80)
    print("GRADING CIS-4328 DISCUSSIONS (INTRO & M01)")
    print("=" * 80)

    # 1. Introduce Yourself
    print("\n--- 1. Grading 'Discussion: Introduce Yourself' (ID: 227497) ---")
    for item in INTRO_4328:
        grade_submission(COURSE_ID, 227497, item["user_id"], item["grade"], item["comment"])
        post_discussion_reply(COURSE_ID, 139147, item["entry_id"], item["reply"])
        time.sleep(0.5)

    # 2. Discussion M01
    print("\n--- 2. Grading 'Discussion (M01)' (ID: 227500) ---")
    for item in M01_4328:
        grade_submission(COURSE_ID, 227500, item["user_id"], item["grade"], item["comment"])
        post_discussion_reply(COURSE_ID, 139148, item["entry_id"], item["reply"])
        time.sleep(0.5)

    print("\n" + "=" * 80)
    print("✅ CIS-4328 DISCUSSIONS FULLY GRADED & REPLIED TO!")
    print("=" * 80)

if __name__ == "__main__":
    main()
