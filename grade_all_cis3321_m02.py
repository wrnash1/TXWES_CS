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

COURSE_ID = 13089
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

# ZERO COMMENT
ZERO_COMMENT = "No submission recorded as of the module deadline (September 14, 2026). In accordance with Texas Wesleyan course grading policy, a zero has been entered. Please review the syllabus late work policy and contact Professor Nash promptly if you have documented extenuating circumstances."

# ==============================================================================
# 1. LAB M01 (BENJAMIN FLORES)
# ==============================================================================
def grade_lab_m01():
    print("\n--- Grading Lab M01: Benjamin Flores ---")
    comment = """Benjamin,

Thank you for your submission for Lab (M01): OSI Model Observation & Star Topology.

Evaluation & Technical Feedback:
1. Topology Construction: Your Packet Tracer simulation demonstrates a fully functional star topology centered on a Cisco 2960 switch.
2. PDU Encapsulation Analysis: You correctly identified the Layer 2 Ethernet II framing components (Destination/Source MAC addresses) and traced how the switch uses its Content Addressable Memory (CAM) table to forward frames via directed unicast rather than legacy hub broadcasting.
3. Layer 3 Alignment: You accurately differentiated between the 48-bit physical MAC address at Layer 2 and the 32-bit logical IPv4 address at Layer 3.

Great hands-on execution!

Grade: 98/100 (A)
— Professor Nash, Ph.D."""
    grade_submission(227449, 4464, 98.0, comment)

# ==============================================================================
# 2. LAB M02 (PROTOCOL IDENTIFICATION & COMMAND-LINE DIAGNOSTICS)
# ==============================================================================
LAB_M02_GRADES = [
    {
        "user_id": 4464,
        "name": "Benjamin Flores",
        "grade": 98.0,
        "comment": """Benjamin,

Exceptional and exhaustive submission for Lab (M02) ('Lab (M02) Protocol Identification & Command-Line Diagnostics Net Admin.docx' + multi-part screenshots).

Evaluation & Technical Feedback:
1. DNS Resolution (nslookup): Your command output clearly demonstrates authoritative vs. non-authoritative DNS query resolution and the role of A/AAAA records.
2. ICMP Diagnostics (ping & tracert): You accurately analyzed TTL decrements, round-trip time (RTT), and hop-by-hop latency across routing gateways.
3. Socket State Analysis (netstat): Your captures show clear comprehension of active TCP connections (ESTABLISHED, LISTENING, TIME_WAIT) and associated port bindings.

Outstanding attention to detail!

Grade: 98/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 15566,
        "name": "Zaniya Grice",
        "grade": 100.0,
        "comment": """Zaniya,

Another exemplary, doctoral-quality laboratory deliverable ('M2 Lab 2.docx').

Evaluation & Technical Feedback:
1. Diagnostic Methodology: You systematically executed and documented all diagnostic utilities—nslookup, ping, tracert/traceroute, and netstat.
2. Transport & Network Layer Synthesis: Your answers reflect precise understanding of RFC 792 (ICMP), RFC 793 (TCP 3-way handshake), and RFC 1035 (DNS). You clearly explained why routers decrement the IP header TTL field by 1 at each hop and return ICMP Type 11 (Time Exceeded) during path tracing.
3. Socket State Mapping: Your analysis of netstat output correctly linked local IP:Port pairs with foreign sockets and explained the purpose of the TIME_WAIT state in TCP connection teardown.

Flawless work!

Grade: 100/100 (A+)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 15652,
        "name": "Arinzechukwu Ejeckam",
        "grade": 98.0,
        "comment": """Arinze,

Superb laboratory report ('Network Lab 2 (1).pdf') for Lab (M02).

Evaluation & Technical Feedback:
1. Terminal Output & Verification: Your PDF report contains clear, annotated screenshots documenting your command-line executions and packet verifications.
2. Diagnostic Insight: You accurately explained the mechanism of traceroute, identifying how sequential UDP or ICMP probes with incrementing TTL values reveal the Layer 3 path across intermediate routing hops.
3. Protocol Identification: Your socket table analysis demonstrated a strong grasp of standard well-known service ports versus ephemeral client source ports.

Grade: 98/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 18445,
        "name": "Jacori Stubbs",
        "grade": 97.0,
        "comment": """Jacori,

Very well done on Lab (M02) ('Part 1 DNS Queries with nslookup.pdf' + multi-part screenshots).

Evaluation & Technical Feedback:
1. CLI Execution: Your documentation of nslookup queries and netstat port listings is complete and clearly verified.
2. Conceptual Depth: You correctly explained the difference between forward DNS lookups and reverse DNS PTR record lookups, as well as the security implications of open listening ports.
3. Professional Tip: In future deliverables, compiling all image captures into your primary PDF document ensures a unified audit trail for enterprise reporting.

Strong effort!

Grade: 97/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 21059,
        "name": "Melany Reyes",
        "grade": 99.0,
        "comment": """Melany,

Outstanding technical laboratory report ('Melany Reyes - Lab 02.pdf').

Evaluation & Technical Feedback:
1. Academic & Technical Rigor: Your submission is formatted with high structural polish. Each diagnostic tool (nslookup, ping, tracert, netstat) is accompanied by crisp terminal captures and rigorous technical explanations.
2. Protocol Analysis: Your explanation of how ICMP Echo Request (Type 8) and Echo Reply (Type 0) messages function within the IPv4 payload reflects deep theoretical and practical understanding.
3. Troubleshooting Acumen: Your explanation of netstat state transitions—specifically distinguishing passive LISTEN states from active ESTABLISHED sessions—is textbook precision.

Exceptional work!

Grade: 99/100 (A)
— Professor Nash, Ph.D."""
    }
]

# ==============================================================================
# 3. DISCUSSION M02 (TCP/IP & PROTOCOLS)
# ==============================================================================
DISC_M02_GRADES = [
    {
        "user_id": 15566,
        "entry_id": 470124,
        "name": "Zaniya Grice",
        "grade": 100.0,
        "comment": "Zaniya, brilliant analysis of Scenario A (DHCP Outage)! You articulated the DORA exchange with precision, correctly explained why client OSs fall back to APIPA (169.254.0.0/16) link-local addressing, and accurately detailed how an ip helper-address forwards DHCP broadcast discover messages as unicast UDP packets across routed boundaries. Flawless 100/100!",
        "reply": "<p>Zaniya,</p><p>This is a masterclass in TCP/IP protocol analysis. You correctly noted that because DHCP Discover and Request messages are sent to the Layer 2 broadcast address (FF:FF:FF:FF:FF:FF) and Layer 3 broadcast (255.255.255.255), routers naturally drop them to contain the broadcast domain.</p><p>Configuring a DHCP Relay Agent (such as Cisco's <code>ip helper-address</code>) on the client default gateway router interface encapsulates that broadcast into a targeted unicast UDP packet sent directly to the centralized DHCP server on Port 67. Outstanding work!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 21059,
        "entry_id": 470539,
        "name": "Melany Reyes",
        "grade": 99.0,
        "comment": "Melany, outstanding evaluation of Scenario B (Insecure Ports)! You accurately identified the severe eavesdropping vulnerabilities of Telnet (Port 23), HTTP (Port 80), and POP3 (Port 110), and clearly detailed their cryptographic replacements: SSH (Port 22), HTTPS (Port 443 via TLS 1.3), and POP3S (Port 995). Excellent technical depth!",
        "reply": "<p>Melany,</p><p>Your breakdown of unencrypted legacy protocols in Scenario B is spot on. Passing authentication credentials in cleartext over Telnet or legacy HTTP exposes an enterprise to trivial passive sniffing via Wireshark or arpspoofing.</p><p>Beyond upgrading to SSH and HTTPS, how does enforcing strict Transport Layer Security policies like HSTS (HTTP Strict Transport Security) prevent SSL-stripping attacks? Stellar contribution!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 21504,
        "entry_id": 470557,
        "name": "Caleb Olen",
        "grade": 98.0,
        "comment": "Caleb, very strong analysis of Scenario C (Network Boundary Diagnostics)! You correctly interpreted the ping and tracert output, isolating the connection failure to the second-hop default gateway router. Your troubleshooting methodology was logical and disciplined. Great job!",
        "reply": "<p>Caleb,</p><p>You did an excellent job interpreting the diagnostic telemetry in Scenario C. When pings to the local default gateway succeed with low latency but tracert consistently fails at the boundary router, it confirms that local Layer 1/2 switching and ARP are functional, pointing directly to a Layer 3 routing table or upstream WAN interface failure.</p><p>In an enterprise environment, what routing command would you issue on that boundary router to verify whether its default route (0.0.0.0/0) is active? Great post!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 15652,
        "entry_id": 472007,
        "name": "Arinzechukwu Ejeckam",
        "grade": 98.0,
        "comment": "Arinze, excellent breakdown of Scenario A (DHCP DORA Process)! You accurately described Discover, Offer, Request, and Acknowledge, and explained how clients self-assign APIPA addresses when the server fails to respond. Strong grasp of dynamic addressing!",
        "reply": "<p>Arinze,</p><p>Very clear and structured analysis of the DORA sequence. You correctly emphasized that the client cannot obtain an IP address if the DHCP server or the intermediate relay agent fails.</p><p>Under RFC 3927 (APIPA), while the 169.254.x.x address allows hosts on the same physical broadcast domain to communicate locally via ARP, it cannot be routed across a default gateway to access intranet or internet resources. Well done!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 3965,
        "entry_id": 473054,
        "name": "Oke Akpoborie",
        "grade": 97.0,
        "comment": "Oke, strong response to Scenario A. You accurately outlined the DORA cycle, explained the transition to APIPA addresses, and highlighted the resulting loss of routability. Good technical breakdown!",
        "reply": "<p>Oke,</p><p>Solid explanation of DHCP and APIPA dynamics. You correctly recognized that an unrouted 169.254.x.x address is an immediate diagnostic symptom indicating that the host sent a DHCP Discover but received no DHCP Offer.</p><p>Checking whether the DHCP scope is exhausted or the DHCP service daemon has crashed are two prime first steps for a systems administrator. Nice job!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 4806,
        "entry_id": 473186,
        "name": "Chrissean Sias-Rackstraw",
        "grade": 97.0,
        "comment": "Chrissean, very good analysis of Scenario C. You accurately identified that the connection is failing at the default gateway between the university's internal network and the external network, correctly diagnosing the boundary failure. Well reasoned!",
        "reply": "<p>Chrissean,</p><p>Very perceptive diagnostic analysis. Isolating the point of failure to the boundary router based on where traceroute responses cease is the fundamental methodology of network path testing.</p><p>If the boundary router is dropping packets, it could be caused by an expired BGP peering session, a misconfigured Access Control List (ACL), or an interface hardware failure on the ISP handoff. Great work!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 5072,
        "entry_id": 473927,
        "name": "Bryan Lopez",
        "grade": 97.0,
        "comment": "Bryan, solid response to Scenario A. You thoroughly detailed the 4 phases of DHCP DORA and accurately explained the purpose and limitations of APIPA addresses when dynamic leasing fails. Good job!",
        "reply": "<p>Bryan,</p><p>Very thorough breakdown of the DORA process. You correctly highlighted that each phase serves a specific handshake purpose to prevent duplicate IP address allocation across the subnet.</p><p>When a client receives multiple DHCP Offers from different servers, how does the client decide which offer to accept in its subsequent DHCP Request broadcast? Excellent contribution!</p><p>— Professor Nash, Ph.D.</p>"
    }
]

# ==============================================================================
# 4. MISSING SUBMISSIONS TO MARK AS ZERO
# ==============================================================================
MISSING_3321 = [
    # Assignment 228277: Quiz (M01)
    {"aid": 228277, "uid": 15445, "name": "Voldi Madiadia"},
    # Assignment 227450: Discussion (M01)
    {"aid": 227450, "uid": 15567, "name": "Elijah Kilgore"},
    {"aid": 227450, "uid": 15445, "name": "Voldi Madiadia"},
    # Assignment 227449: Lab (M01)
    {"aid": 227449, "uid": 15567, "name": "Elijah Kilgore"},
    {"aid": 227449, "uid": 16186, "name": "Wilfredo Lopez"},
    {"aid": 227449, "uid": 15445, "name": "Voldi Madiadia"},
    {"aid": 227449, "uid": 21504, "name": "Caleb Olen"},
    # Assignment 228278: Quiz (M02)
    {"aid": 228278, "uid": 15567, "name": "Elijah Kilgore"},
    {"aid": 228278, "uid": 16186, "name": "Wilfredo Lopez"},
    {"aid": 228278, "uid": 15445, "name": "Voldi Madiadia"},
    # Assignment 227453: Discussion (M02)
    {"aid": 227453, "uid": 15567, "name": "Elijah Kilgore"},
    {"aid": 227453, "uid": 16186, "name": "Wilfredo Lopez"},
    {"aid": 227453, "uid": 15445, "name": "Voldi Madiadia"},
    # Assignment 227452: Lab (M02)
    {"aid": 227452, "uid": 3965, "name": "Okeoghene Akpoborie"},
    {"aid": 227452, "uid": 15567, "name": "Elijah Kilgore"},
    {"aid": 227452, "uid": 5072, "name": "Bryan Lopez"},
    {"aid": 227452, "uid": 16186, "name": "Wilfredo Lopez"},
    {"aid": 227452, "uid": 15445, "name": "Voldi Madiadia"},
    {"aid": 227452, "uid": 21504, "name": "Caleb Olen"},
    {"aid": 227452, "uid": 4806, "name": "Chrissean Sias-Rackstraw"}
]

def main():
    print("=" * 80)
    print("GRADING ALL CIS-3321 ASSIGNMENTS UP TO TODAY (SEP 14, 2026)")
    print("=" * 80)

    # 1. Lab M01 late/resubmission
    grade_lab_m01()

    # 2. Lab M02 submissions
    print("\n--- 2. Grading Lab M02 Submissions ---")
    for item in LAB_M02_GRADES:
        grade_submission(227452, item["user_id"], item["grade"], item["comment"])
        time.sleep(0.4)

    # 3. Discussion M02 submissions
    print("\n--- 3. Grading Discussion M02 Submissions & Replying ---")
    for item in DISC_M02_GRADES:
        grade_submission(227453, item["user_id"], item["grade"], item["comment"])
        post_discussion_reply(139133, item["entry_id"], item["reply"])
        time.sleep(0.4)

    # 4. Enter Zeros for Missing Submissions
    print("\n--- 4. Recording Zeros for Missing Submissions ---")
    for item in MISSING_3321:
        grade_submission(item["aid"], item["uid"], 0.0, ZERO_COMMENT)
        time.sleep(0.4)

    print("\n" + "=" * 80)
    print("✅ CIS-3321 COMPLETELY GRADED UP TO TODAY!")
    print("=" * 80)

if __name__ == "__main__":
    main()
