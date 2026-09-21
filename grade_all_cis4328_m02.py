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

def grade_submission(assign_id, user_id, grade, comment):
    url = f"{API_BASE}/courses/{COURSE_ID}/assignments/{assign_id}/submissions/{user_id}"
    payload = {
        "submission": {"posted_grade": str(grade)},
        "comment": {"text_comment": comment}
    }
    res = api_call(url, data=payload, method="PUT")
    if res:
        print(f"  ✅ Graded User {user_id} on Assignment {assign_id} -> {grade} pts")
    return res

def post_discussion_reply(topic_id, entry_id, html_message):
    url = f"{API_BASE}/courses/{COURSE_ID}/discussion_topics/{topic_id}/entries/{entry_id}/replies"
    payload = {"message": html_message}
    res = api_call(url, data=payload, method="POST")
    if res:
        print(f"  💬 Posted reply to Entry {entry_id}")
    return res

ZERO_COMMENT = "No submission recorded as of the module deadline (September 14, 2026). In accordance with Texas Wesleyan course grading policy, a zero has been entered. Please review the syllabus late work policy and contact Professor Nash promptly if you have documented extenuating circumstances."

# ==============================================================================
# 1. LAB M01 (BENJAMIN FLORES)
# ==============================================================================
def grade_lab_m01():
    print("\n--- Grading Lab M01: Benjamin Flores ---")
    comment = """Benjamin,

Thank you for your submission for Lab (M01): Threat & Control Classification.

Evaluation & Technical Feedback:
1. Threat Identification & Modeling: You demonstrated a solid grasp of threat actor motivations and tactics impacting the Ridgeline scenario.
2. CIA Triad Mapping: You accurately distinguished between breaches of Confidentiality (unauthorized data access) and Availability (ransomware disruption).
3. Security Control Categorization: Your proposed controls span Administrative (policy governance) and Technical (endpoint protection, access controls) categories under NIST SP 800-53.

Well structured and thoughtful analysis!

Grade: 98/100 (A)
— Professor Nash, Ph.D."""
    grade_submission(227499, 4464, 98.0, comment)

# ==============================================================================
# 2. LAB M02 (SOCIAL ENGINEERING & COUNTERMEASURES)
# ==============================================================================
LAB_M02_4328 = [
    {
        "user_id": 2022,
        "name": "Kobee Cain",
        "grade": 98.0,
        "comment": """Kobee,

Superb work on Lab (M02): Social Engineering Analysis & Countermeasures ('Module_02SocialEngineeringLab.docx').

Evaluation & Technical Feedback:
1. Attack Vector Deconstruction: You systematically evaluated the multi-stage social engineering scenarios, identifying spear phishing, voice phishing (vishing), and baiting tactics.
2. Human Factor & Psychological Exploitation: You correctly identified how adversaries leverage cognitive biases—specifically authority, urgency, and social proof—to bypass technical controls.
3. Layered Countermeasures: Your recommendations for technical email authentication (SPF, DKIM, DMARC) paired with recurring simulated phishing campaigns align directly with CompTIA Security+ objectives.

Grade: 98/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 2355,
        "name": "Chasity Gaston",
        "grade": 98.0,
        "comment": """Chasity,

Outstanding technical deliverable for Lab (M02) ('Lab 2 security case study.docx').

Evaluation & Technical Feedback:
1. Scenario Analysis: Your report provides a thorough breakdown of how attackers exploit organizational trust. You correctly identified that human vulnerabilities cannot be patched with software alone.
2. Countermeasure Architecture: You proposed a robust defense-in-depth model: combining administrative policies (mandatory verification callbacks for wire transfers), operational controls (interactive awareness training), and technical controls (out-of-band MFA and banner warnings on external emails).
3. Presentation: Well written, professional, and clear.

Grade: 98/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 2611,
        "name": "Jaalen Williams",
        "grade": 97.0,
        "comment": """Jaalen,

Very well done on Lab (M02) ('CIS-4328-20  Simulation Lab.docx').

Evaluation & Technical Feedback:
1. Threat Vector Identification: You accurately identified the mechanics of business email compromise (BEC) and malicious baiting.
2. Control Functionality: Your analysis of preventive controls (endpoint USB blocklisting via Group Policy) and detective controls (SIEM log correlation for suspicious credential use) was well targeted.
3. Recommendation Depth: You correctly highlighted that technical controls like FIDO2 hardware keys render traditional credential-harvesting phishing obsolete.

Grade: 97/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 4018,
        "name": "Israel Lopez",
        "grade": 98.0,
        "comment": """Israel,

Exceptional analysis in Lab (M02) ('Lab 2 Israel Lopez.docx').

Evaluation & Technical Feedback:
1. Behavioral Breakdown: Your report accurately diagnoses the psychological triggers exploited in the case study—namely scarcity and intimidation.
2. Technical & Policy Alignment: Your proposal to enforce strict administrative separation of duties for financial transactions alongside technical controls (automated quarantine of lookalike domain emails) demonstrates mature information assurance logic.
3. Industry Frameworks: Your recommendations mirror NIST SP 800-53 Personnel Security (PS) and System and Information Integrity (SI) controls.

Grade: 98/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 4464,
        "name": "Benjamin Flores",
        "grade": 98.0,
        "comment": """Benjamin,

Excellent, thorough laboratory report ('Lab (M02) Social Engineering Analysis & Countermeasures Case Study.pdf').

Evaluation & Technical Feedback:
1. Systematic Evaluation: You walked through all attack vectors with analytical precision, classifying threat types and identifying the root psychological vulnerabilities.
2. Countermeasure Mapping: Your recommendations across Technical (DMARC, MFA), Administrative (security training, verification protocols), and Physical (badging, clean desk policy) categories provide an actionable enterprise roadmap.
3. Visuals & Layout: The PDF submission is clean, readable, and structured.

Grade: 98/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 4694,
        "name": "Avarieus Dwin",
        "grade": 96.0,
        "comment": """Avarieus (AD),

Solid work on Lab (M02) ('Lab__2.docx').

Evaluation & Technical Feedback:
1. Attack Classification: You accurately parsed the social engineering scenarios, correctly identifying spear phishing and pretexting.
2. Defense Recommendations: Your proposals for dual-authorization approval on invoice payments and endpoint USB disabled ports provide practical, high-impact risk reduction.
3. Professional Tip: In future deliverables, explicitly categorizing each control as Preventive, Detective, or Corrective will align your documentation with enterprise security auditing benchmarks.

Grade: 96/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 5072,
        "name": "Bryan Lopez",
        "grade": 97.0,
        "comment": """Bryan,

Strong technical submission for Lab (M02) ('Bryan Lopez- Lab (M02).pdf').

Evaluation & Technical Feedback:
1. Forensic Clarity: Your report clearly articulates how social engineering bypasses perimeter firewalls by deceiving authorized personnel.
2. Countermeasure Matrix: You outlined sensible countermeasures spanning security awareness training, endpoint isolation, and spoofed header filtering.
3. Analytical Rigor: Your explanation of why phishing simulations must be educational rather than punitive reflects modern human risk management best practices.

Grade: 97/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 15566,
        "name": "Zaniya Grice",
        "grade": 100.0,
        "comment": """Zaniya,

Another exemplary, doctoral-quality case study evaluation ('M02 Lab – Social Engineering Attack Analysis and Countermeasures.docx').

Evaluation & Technical Feedback:
1. Psychological & Technical Synthesis: You articulated the intersection of human cognitive biases (authority, social proof, urgency) with technical attack surfaces (typosquatting domains, malicious macros, macro-free payload delivery via LNK files).
2. Defense-in-Depth Framework: Your remediation strategy addresses all three NIST control families:
   • Administrative: Strict verification workflows for executive funds transfer and comprehensive role-based phishing training.
   • Technical: DMARC with strict rejection (p=reject), FIDO2 WebAuthn phishing-resistant MFA, and automated endpoint USB disablement.
   • Physical: Anti-tailgating mantrap controls and secure visitor escrow.
3. Executive Ready: Your writing is crisp, scholarly, and ready for C-suite presentation.

Flawless work!

Grade: 100/100 (A+)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 15652,
        "name": "Arinzechukwu Ejeckam",
        "grade": 98.0,
        "comment": """Arinze,

Superb laboratory report ('Security Lab 2.pdf') for Lab (M02).

Evaluation & Technical Feedback:
1. Threat Analysis: Your report thoroughly analyzes how adversaries exploit social engineering to compromise credentials without triggering perimeter alerts.
2. Control Implementation: Your recommendations emphasize technical enforcement—specifically DNS filtering, external sender email banners, and hardware MFA tokens.
3. Governance Connection: You properly linked the technical controls back to organizational security policies and employee accountability.

Grade: 98/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 15899,
        "name": "Christopher King",
        "grade": 99.0,
        "comment": """Christopher,

Exceptional laboratory deliverable ('Lab M02 Cking.docx').

Evaluation & Technical Feedback:
1. Analytical Sophistication: Your evaluation of the social engineering campaign demonstrates sharp threat intelligence acumen. You accurately identified pretexting personas, baiting lures, and target reconnaissance.
2. Countermeasure Rigor: Your proposed controls—including automated email analysis via natural language processing (NLP) to detect linguistic cues of urgency, alongside strict separation of duties—reflect advanced enterprise SOC practices.
3. Clear Articulation: Your report reads like a senior security consultant's post-incident assessment.

Grade: 99/100 (A)
— Professor Nash, Ph.D."""
    }
]

# ==============================================================================
# 3. DISCUSSION M02 (SOCIAL ENGINEERING & PHISHING)
# ==============================================================================
DISC_M02_4328 = [
    {
        "user_id": 15566,
        "entry_id": 470089,
        "name": "Zaniya Grice",
        "grade": 100.0,
        "comment": "Zaniya, masterclass analysis of Scenario A! You completely dismantled the manager's argument by demonstrating that social engineering preys on deception, authority, and urgency rather than malicious employee intent. Your proposed controls—out-of-band verification and phishing-resistant MFA—were perfect. Flawless 100/100!",
        "reply": "<p>Zaniya,</p><p>You hit the nail on the head: the manager's argument conflates <em>employee trust</em> with <em>adversary deception</em>. Even the most trustworthy employee in the company can be misled by a sophisticated pretext or spoofed identity if formal verification protocols are bypassed in the name of 'efficiency.'</p><p>Your point regarding out-of-band verification (such as requiring an authenticated callback or manager sign-off for password resets) is precisely what NIST SP 800-63B recommends for identity proofing. Outstanding analysis!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 4694,
        "entry_id": 470439,
        "name": "Avarieus Dwin",
        "grade": 97.0,
        "comment": "Avarieus (AD), great analysis of Scenario C! You accurately classified the attack as spear phishing and vendor impersonation, explaining how the attacker conducted target reconnaissance to make the email appear authentic. Well reasoned!",
        "reply": "<p>AD,</p><p>You correctly diagnosed Scenario C as targeted spear phishing / vendor impersonation. Unlike bulk phishing, spear phishing relies on pre-attack reconnaissance to harvest legitimate vendor names, project titles, and communication styles.</p><p>To combat this, how can organizations implement cryptographic email verification standards like DMARC, DKIM, and SPF to automatically reject emails spoofing legitimate partner domains? Great post!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 21504,
        "entry_id": 470571,
        "name": "Caleb Olen",
        "grade": 98.0,
        "comment": "Caleb, excellent analysis of Scenario B (USB Drop Campaign)! You correctly identified the technique as baiting and analyzed the psychological triggers of curiosity and greed. Your proposed preventive controls (disabling USB ports via GPO) were spot on. Great job!",
        "reply": "<p>Caleb,</p><p>A very sharp analysis of the USB drop campaign. You accurately identified <em>baiting</em> as the social engineering mechanism, exploiting curiosity and the promise of confidential payroll data.</p><p>Your recommendation to enforce Group Policy Objects (GPO) or endpoint DLP agents that disable unauthorized removable media storage is the definitive technical countermeasure. If USBs must be used, how can organizations enforce hardware-encrypted drives managed by IT? Great job!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 4018,
        "entry_id": 470996,
        "name": "Israel Lopez",
        "grade": 98.0,
        "comment": "Israel, outstanding critique of Scenario A! You clearly articulated why employee trust is irrelevant when an external attacker impersonates an authorized executive, and why technical verification must always supersede informal trust. Excellent post!",
        "reply": "<p>Israel,</p><p>Your critique of the manager's logic is spot on. Trust is not a security control. Attackers intentionally target helpful, well-meaning employees precisely because their instinct is to solve problems quickly rather than scrutinize credentials.</p><p>Enforcing standardized help desk verification protocols—such as sending a one-time push notification to an enrolled authenticator app before executing a password reset—eliminates the human guessing game. Superb contribution!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 2355,
        "entry_id": 471489,
        "name": "Chasity Gaston",
        "grade": 98.0,
        "comment": "Chasity, excellent response to Scenario A. You accurately highlighted that social engineering exploits authority and human helpfulness rather than employee maliciousness. Your countermeasure recommendations were practical and effective. Great work!",
        "reply": "<p>Chasity,</p><p>Very well stated. You correctly recognized that social engineers exploit psychological leverage—specifically authority and urgency. When an attacker claims to be a VP locked out of a critical board meeting, employees feel immense social pressure to comply.</p><p>Establishing clear corporate policies that explicitly protect help desk staff from executive backlash when they enforce identity verification is a vital administrative safeguard. Excellent analysis!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 4464,
        "entry_id": 471572,
        "name": "Benjamin Flores",
        "grade": 98.0,
        "comment": "Benjamin, strong breakdown of Scenario B! You correctly identified baiting as the primary technique and explained how deceptive labeling lures victims into inserting rogue media. Your proposed technical and operational controls were solid. Good job!",
        "reply": "<p>Benjamin,</p><p>Solid technical breakdown of baiting. Physical USB drops remain one of the most effective red team techniques because they bypass external firewalls and email gateways entirely by relying on an employee to carry the payload inside the perimeter.</p><p>In addition to technical endpoint disabling of mass storage classes, establishing a secure drop-box procedure where found devices are submitted directly to the SOC for sandboxed analysis is a great operational control. Well done!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 15652,
        "entry_id": 471922,
        "name": "Arinzechukwu Ejeckam",
        "grade": 98.0,
        "comment": "Arinze, compelling response to Scenario A. You astutely noted that trading security controls for customer service speed creates a critical attack vector that adversaries will reliably exploit. Strong technical reasoning!",
        "reply": "<p>Arinze,</p><p>You identified the classic organizational tension: security versus convenience. When management prioritizes customer service speed over identity verification, they inadvertently establish an open backdoor for credential theft.</p><p>Implementing self-service password reset (SSPR) portals backed by multi-factor authentication relieves help desk burden while dramatically increasing security. Great contribution!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 2022,
        "entry_id": 472544,
        "name": "Kobee Cain",
        "grade": 98.0,
        "comment": "Kobee, very strong analysis of Scenario C! You accurately classified the attack as spear phishing and business email compromise, noting how the attacker used targeted financial pretexts to divert funds. Excellent work!",
        "reply": "<p>Kobee,</p><p>Very perceptive evaluation. Business Email Compromise (BEC) accounts for billions of dollars in enterprise losses annually according to FBI IC3 reports. Attackers monitor vendor payment schedules and inject modified banking details at the exact moment an invoice is expected.</p><p>Enforcing mandatory dual-custody verification via phone using pre-established contact numbers (never the number listed on the invoice) is the gold standard for stopping payment diversion. Great job!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 15899,
        "entry_id": 473244,
        "name": "Christopher King",
        "grade": 99.0,
        "comment": "Christopher, exceptional breakdown of Scenario B! Your exploration of human psychological vulnerabilities (curiosity, desire for compensation data) paired with technical attack execution was outstanding. Top-tier response!",
        "reply": "<p>Christopher,</p><p>Your analysis of the psychological underpinnings in Scenario B is spot on. Labeling a drive 'Executive Compensation' or 'Q4 Layoffs' weaponizes human anxiety and curiosity in a way that technical firewalls cannot defend against.</p><p>Beyond disabling autorun (which Windows does by default now), enforcing Endpoint Detection and Response (EDR) behavioral monitoring to instantly isolate any host executing binaries from removable media is essential modern defense. Outstanding work!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 2611,
        "entry_id": 473309,
        "name": "Jaalen Williams",
        "grade": 98.0,
        "comment": "Jaalen, thorough and well reasoned response to Scenario C! You correctly identified vendor impersonation / BEC spear phishing and proposed comprehensive technical and administrative countermeasures. Great job!",
        "reply": "<p>Jaalen,</p><p>You provided a comprehensive diagnosis of the BEC attack vector in Scenario C. Vendor impersonation attacks are especially insidious because the email often arrives from a lookalike domain (typosquatting) or an actual compromised vendor account.</p><p>Deploying advanced email security solutions that analyze domain age, domain reputation, and stylistic anomalies in the header is a critical defensive layer. Excellent post!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 4806,
        "entry_id": 473765,
        "name": "Chrissean Sias-Rackstraw",
        "grade": 97.0,
        "comment": "Chrissean, very good response to Scenario A. You accurately explained how social engineering succeeds by exploiting trust and helpfulness, and why strict verification rules must apply to all callers regardless of claims. Well reasoned!",
        "reply": "<p>Chrissean,</p><p>Well stated. Social engineering succeeds not because employees are malicious, but because human nature tends toward empathy and assistance. Attackers are skilled actors who know how to manipulate those positive traits against the organization.</p><p>Establishing a 'trust but verify' culture supported by automated verification tools empowers employees to say no to unverified requests without fear of reprimand. Good work!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 5072,
        "entry_id": 473918,
        "name": "Bryan Lopez",
        "grade": 97.0,
        "comment": "Bryan, solid critique of Scenario A. You correctly noted that social engineering attacks primarily depend upon deceiving employees, making the manager's faith in informal trust deeply flawed. Good analysis!",
        "reply": "<p>Bryan,</p><p>Very clear reasoning. You rightly pointed out that social engineers actively impersonate trusted figures (executives, technicians, auditors) to induce panic or compliance.</p><p>Requiring standardized challenge-response protocols or out-of-band push authentication removes the burden of decision-making from the individual help desk technician. Excellent contribution!</p><p>— Professor Nash, Ph.D.</p>"
    }
]

# ==============================================================================
# 4. MISSING SUBMISSIONS TO MARK AS ZERO
# ==============================================================================
MISSING_4328 = [
    # Assignment 227497: Discussion: Introduce Yourself
    {"aid": 227497, "uid": 15899, "name": "Christopher King"},
    # Assignment 227500: Discussion (M01)
    {"aid": 227500, "uid": 15567, "name": "Elijah Kilgore"},
    {"aid": 227500, "uid": 15445, "name": "Voldi Madiadia"},
    {"aid": 227500, "uid": 20444, "name": "Natalie Turrubiartes"},
    # Assignment 227499: Lab (M01)
    {"aid": 227499, "uid": 15567, "name": "Elijah Kilgore"},
    {"aid": 227499, "uid": 15445, "name": "Voldi Madiadia"},
    {"aid": 227499, "uid": 21504, "name": "Caleb Olen"},
    # Assignment 228294: Quiz (M02)
    {"aid": 228294, "uid": 15567, "name": "Elijah Kilgore"},
    {"aid": 228294, "uid": 15445, "name": "Voldi Madiadia"},
    {"aid": 228294, "uid": 20444, "name": "Natalie Turrubiartes"},
    # Assignment 227503: Discussion (M02)
    {"aid": 227503, "uid": 8992, "name": "Anthony Cruz"},
    {"aid": 227503, "uid": 15567, "name": "Elijah Kilgore"},
    {"aid": 227503, "uid": 15445, "name": "Voldi Madiadia"},
    {"aid": 227503, "uid": 20444, "name": "Natalie Turrubiartes"},
    # Assignment 227502: Lab (M02)
    {"aid": 227502, "uid": 8992, "name": "Anthony Cruz"},
    {"aid": 227502, "uid": 15567, "name": "Elijah Kilgore"},
    {"aid": 227502, "uid": 15445, "name": "Voldi Madiadia"},
    {"aid": 227502, "uid": 21504, "name": "Caleb Olen"},
    {"aid": 227502, "uid": 4806, "name": "Chrissean Sias-Rackstraw"},
    {"aid": 227502, "uid": 20444, "name": "Natalie Turrubiartes"}
]

def main():
    print("=" * 80)
    print("GRADING ALL CIS-4328 ASSIGNMENTS UP TO TODAY (SEP 14, 2026)")
    print("=" * 80)

    # 1. Lab M01 late/resubmission
    grade_lab_m01()

    # 2. Lab M02 submissions
    print("\n--- 2. Grading Lab M02 Submissions ---")
    for item in LAB_M02_4328:
        grade_submission(227502, item["user_id"], item["grade"], item["comment"])
        time.sleep(0.4)

    # 3. Discussion M02 submissions
    print("\n--- 3. Grading Discussion M02 Submissions & Replying ---")
    for item in DISC_M02_4328:
        grade_submission(227503, item["user_id"], item["grade"], item["comment"])
        post_discussion_reply(139149, item["entry_id"], item["reply"])
        time.sleep(0.4)

    # 4. Enter Zeros for Missing Submissions
    print("\n--- 4. Recording Zeros for Missing Submissions ---")
    for item in MISSING_4328:
        grade_submission(item["aid"], item["uid"], 0.0, ZERO_COMMENT)
        time.sleep(0.4)

    print("\n" + "=" * 80)
    print("✅ CIS-4328 COMPLETELY GRADED UP TO TODAY!")
    print("=" * 80)

if __name__ == "__main__":
    main()
