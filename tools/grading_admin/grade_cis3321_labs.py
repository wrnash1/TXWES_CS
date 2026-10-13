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
ASSIGN_ID = 227449  # Lab (M01): OSI Model Observation & Star Topology (Packet Tracer)
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

LAB_3321_GRADES = [
    {
        "user_id": 3965,
        "name": "Okeoghene Akpoborie",
        "grade": 96.0,
        "comment": """Oke,

Thank you for your submission for Lab (M01): OSI Model Observation & Star Topology. 

Evaluation & Technical Feedback:
1. Topology Construction & Simulation Mode: Your embedded screenshots verify an operative physical star topology centered around the Layer 2 switch. The packet animation trace properly captured the ICMP Echo Request / Echo Reply exchange across endpoints.
2. Protocol Data Unit (PDU) Inspection: You correctly identified the Layer 2 Ethernet II framing parameters, specifically distinguishing the 48-bit (6-byte) media access control (MAC) physical addresses from logical Layer 3 IP addressing.
3. Areas for Continued Refinement: In future submissions, ensure you accompany the screenshots with an explicit written summary detailing the preamble, EtherType field (0x0800 for IPv4), and the TTL decrement behavior across routed boundaries. 

Overall: Strong foundational work demonstrating clear comprehension of Layer 1/Layer 2 interactions.

Grade: 96/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 4806,
        "name": "Chrissean Sias-Rackstraw",
        "grade": 96.0,
        "comment": """Chrissean,

Thank you for your multi-image submission for Lab (M01).

Evaluation & Technical Feedback:
1. Diagnostic Sequence: Your series of six high-resolution Packet Tracer captures illustrates the end-to-end packet journey from PC0 through the switch fabric to PC1. You successfully documented both the Inbound PDU and Outbound PDU details.
2. Encapsulation Verification: You captured the Layer 2 frame format and Layer 3 IP header data accurately. 
3. Professional Tip: When submitting future labs, consolidating your PNG screenshots into a single, cohesive PDF technical report with accompanying written descriptions will elevate your documentation to professional enterprise engineering standards.

Overall: Excellent hands-on execution and verification of Ethernet switching.

Grade: 96/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 5072,
        "name": "Bryan Lopez",
        "grade": 98.0,
        "comment": """Bryan,

Outstanding work on Lab (M01): OSI Model Observation & Star Topology.

Evaluation & Technical Feedback:
1. Technical Documentation: Your PDF submission ('Lab 1- Bryan Lopez.pdf') is exceptionally well organized, featuring crisp topology captures alongside clear, concise analytical responses.
2. PDU Header Analysis: You correctly analyzed the transition of data from Layer 3 IP packets (highlighting the 32-bit source and destination addresses) down into Layer 2 Ethernet II frames. Your explanation of why the switch inspects only Layer 2 MAC addresses and ignores Layer 3 IP headers during basic forwarding is architecturally accurate.
3. Conceptual Depth: Your discussion of collision domains versus broadcast domains within a star-wired switched infrastructure reflects solid theoretical comprehension.

Grade: 98/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 15566,
        "name": "Zaniya Grice",
        "grade": 100.0,
        "comment": """Zaniya,

This is an exemplary, doctoral-quality laboratory report.

Evaluation & Technical Feedback:
1. Analytical Rigor: Your comprehensive report ('M1 Lab 1.docx') provides an exhaustive breakdown of each layer of the OSI model as observed through Cisco Packet Tracer's Event Viewer.
2. Bit-Level & Byte-Level Precision: You meticulously documented the Ethernet II frame structure (Preamble, SFD, 6-byte Destination MAC, 6-byte Source MAC, Type 0x0800, Payload, and 4-byte FCS/CRC). Your analysis of the ARP broadcast mechanism preceding the initial ICMP ping was spot on.
3. Star Topology Dynamics: Your explanation of how modern micro-segmented switches eliminate half-duplex CSMA/CD collisions while preserving a unified Layer 2 broadcast domain demonstrates complete mastery of CompTIA Network+ and Cisco CCNA objectives.

Flawless execution.

Grade: 100/100 (A+)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 15652,
        "name": "Arinzechukwu Ejeckam",
        "grade": 98.0,
        "comment": """Arinze,

Superb submission for Lab (M01).

Evaluation & Technical Feedback:
1. Deliverables & Documentation: Your inclusion of the topology diagram ('Cisco Star top.png'), simulation event captures, and the structured PDF analysis ('Source IP 192.pdf') provides complete verification of your lab work.
2. Layer 2 vs. Layer 3 Analysis: You accurately parsed the source and destination IP parameters (192.168.x.x private addressing space under RFC 1918) and traced how the Layer 2 MAC header is encapsulated and de-encapsulated at the network interface card.
3. Scholarly Commendation: Your explanation of why the physical star topology provides fault tolerance (a single severed cable drops only that node without bringing down the enterprise segment) is technically sound.

Grade: 98/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 18445,
        "name": "Jacori Stubbs",
        "grade": 95.0,
        "comment": """Jacori,

Thank you for your text submission addressing the core analytical questions of Lab (M01).

Evaluation & Technical Feedback:
1. Question 1 (MAC Addressing): You correctly identified that the Layer 2 Destination MAC address (00E0.A31B.0924) spans exactly 6 bytes (48 bits), representing the physical hardware address burned into the network interface card.
2. Question 2 (IP Addressing & OSI Layer): You correctly identified that Source and Destination IP addresses operate at Layer 3 (the Network Layer). 
   • Critical Correction: Please note that standard IPv4 addresses comprise exactly 32 bits (4 octets of 8 bits each), rather than 31 bits. Keeping bit-level arithmetic precise is vital when we advance to CIDR variable-length subnet masking (/24 to /30) in Module 03.
3. Question 3 & Forwarding Logic: Your explanation of how switches populate Content Addressable Memory (CAM) tables based on incoming source MAC addresses was accurate.

Overall: Strong grasp of core network concepts. Keep up the solid effort!

Grade: 95/100 (A)
— Professor Nash, Ph.D."""
    },
    {
        "user_id": 21059,
        "name": "Melany Reyes",
        "grade": 99.0,
        "comment": """Melany,

Outstanding technical laboratory report ('Melany Reyes - Lab 01 summary.pdf') accompanied by comprehensive Packet Tracer simulation captures.

Evaluation & Technical Feedback:
1. Structural Clarity: Your report is formatted with academic precision. The annotated screenshots clearly demonstrate the ICMP PDU transmission, switch ingress, CAM table lookup, and directed unicast egress.
2. Protocol Header Deconstruction: You provided a rigorous breakdown of the Layer 3 IP header fields, correctly noting how Time-To-Live (TTL) prevents routing loops and how the Protocol field (value 1) signals the receiving operating system to pass the payload to the ICMP process.
3. Architectural Insight: Your synthesis of physical star cabling versus logical point-to-point switched micro-segmentation aligns directly with enterprise engineering best practices.

Exceptional work!

Grade: 99/100 (A)
— Professor Nash, Ph.D."""
    }
]

def main():
    print("=" * 80)
    print("GRADING CIS-3321 LAB (M01): PACKET TRACER SIMULATION")
    print("=" * 80)
    for s in LAB_3321_GRADES:
        grade_submission(s["user_id"], s["grade"], s["comment"])
        time.sleep(0.5)
    print("\n" + "=" * 80)
    print("✅ CIS-3321 LAB (M01) FULLY GRADED WITH SCHOLARLY FEEDBACK!")
    print("=" * 80)

if __name__ == "__main__":
    main()
