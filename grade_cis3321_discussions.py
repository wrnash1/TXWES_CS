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
# 1. CIS-3321 INTRODUCE YOURSELF DISCUSSIONS
# ==============================================================================
INTRO_DATA_3321 = [
    {
        "user_id": 15566,
        "entry_id": 458349,
        "name": "Zaniya Grice",
        "grade": 100.0,
        "comment": "Zaniya, welcome to CIS-3321! It is wonderful to have you in your graduating semester. You have articulated clear professional ambitions, and the architectural principles covered in this network administration course—from subnetting and VLAN segmentation to robust routing topologies—will serve as the foundational bedrock for your career in enterprise technology. Excellent introduction!",
        "reply": "<p>Hello Zaniya,</p><p>Welcome to your final semester at Texas Wesleyan! As someone who has watched many graduating seniors transition into enterprise IT, I can assure you that mastering the foundational network layer—specifically how traffic traverses Layer 2 switches and Layer 3 routing domains—is what distinguishes competent technologists from true systems leaders. Best of luck in your capstone semester!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 4806,
        "entry_id": 458425,
        "name": "Chrissean Sias-Rackstraw",
        "grade": 100.0,
        "comment": "Chrissean, welcome to the course! Having curiosity and an openness to learning how enterprise infrastructure actually functions is the ideal mindset. As a graduating senior, this course will demystify how packets traverse the internet, giving you tangible systems-thinking skills that bridge software and hardware. Outstanding participation!",
        "reply": "<p>Hello Chrissean,</p><p>Welcome to CIS-3321! You are in an ideal position: approaching network administration with an inquisitive mindset allows you to see the elegance of protocol stacks without preconceived biases. By the time we configure OSPF dynamic routing and 802.1Q trunking in our Packet Tracer labs, you will feel remarkably confident explaining enterprise infrastructure in technical interviews.</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 15652,
        "entry_id": 459502,
        "name": "Arinzechukwu Ejeckam",
        "grade": 100.0,
        "comment": "Arinze, excellent to have you in CIS-3321! Your understanding that computer networking forms the backbone of all advanced information systems is spot on. As a junior, mastering TCP/IP, OSI, and Cisco IOS CLI now will set you apart for internships and senior-level design courses. Keep up the strong engagement!",
        "reply": "<p>Hello Arinze,</p><p>Welcome to the course! You've hit the nail on the head: every distributed system, database cluster, cloud deployment, and cybersecurity defense mechanism ultimately relies on the underlying packet-switched network. I look forward to your contributions throughout our labs and discussion boards this term.</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 4464,
        "entry_id": 459598,
        "name": "Benjamin Flores",
        "grade": 100.0,
        "comment": "Benjamin, welcome! Congratulations on reaching your senior year in Computer Information Systems. The dual focus on Network+ concepts and Cisco CCNA hands-on configurations in this course will directly equip you with the operational fluency needed for immediate post-graduation technical roles. Great post!",
        "reply": "<p>Hello Benjamin,</p><p>Welcome to CIS-3321! As a senior, this is the prime time to synthesize what you've learned across your CIS coursework. The hands-on Packet Tracer labs and multi-vendor troubleshooting methodologies we practice will translate directly into production systems engineering environments.</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 15567,
        "entry_id": 461121,
        "name": "Elijah Kilgore",
        "grade": 100.0,
        "comment": "Elijah, welcome! Combining a CIS major with an Esports minor provides a uniquely practical perspective on high-performance, low-latency network infrastructure. Understanding jitter, packet loss, UDP vs. TCP transport, and QoS bandwidth reservation will bridge your academic focus with cybersecurity and networking. Terrific introduction!",
        "reply": "<p>Hello Elijah,</p><p>Welcome to CIS-3321! Your intersection of CIS and Esports is fascinating from a network engineering standpoint. Competitive gaming infrastructure demands microsecond-level latency, robust DDoS mitigation, and sophisticated Quality of Service (QoS) queueing—all topics we explore in depth this semester. Glad to have you with us!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 21059,
        "entry_id": 461781,
        "name": "Melany Reyes",
        "grade": 100.0,
        "comment": "Melany, welcome to Texas Wesleyan! Transferring from TCC with a computer science background gives you a strong analytical framework. Computer science often treats networking as an abstract API (like socket programming), but this course will show you the real-world physical and data-link realities of enterprise networks. Excellent to have you in class!",
        "reply": "<p>Hello Melany,</p><p>Welcome to Texas Wesleyan and CIS-3321! We are thrilled to have transfer scholars from TCC. Having a computer science background will give you an edge when we analyze protocol header formats and packet flow logic. Don't hesitate to reach out if you need anything as you settle into the semester!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 5072,
        "entry_id": 461848,
        "name": "Bryan Lopez",
        "grade": 100.0,
        "comment": "Bryan, welcome! Graduating seniors in CIS benefit tremendously from hands-on lab experience. Even if you have not worked extensively with enterprise switches and routers in the past, our step-by-step simulations will build your muscle memory quickly. Great to have you aboard!",
        "reply": "<p>Hello Bryan,</p><p>Welcome to the course! Many students enter CIS-3321 with limited formal networking experience, but by building network topologies from scratch in Cisco Packet Tracer, you will quickly develop an intuitive grasp of routing tables, subnet masks, and network troubleshooting. Looking forward to working with you!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 3965,
        "entry_id": 461963,
        "name": "Oke Akpoborie",
        "grade": 100.0,
        "comment": "Oke, welcome! It is wonderful to have you in CIS-3321 as you finish your senior year. Your diverse international background and Houston roots bring great perspective to our academic community. The real-world problem-solving in this class will cap off your degree strongly!",
        "reply": "<p>Hello Oke,</p><p>Welcome to CIS-3321! I appreciate your authentic introduction. As you conclude your degree, this course will provide the architectural and administrative expertise necessary to design resilient networks. I look forward to your active participation in our technical discussions!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 15445,
        "entry_id": 462306,
        "name": "Voldi Madiadia",
        "grade": 100.0,
        "comment": "Voldi (James), welcome to CIS-3321! Pairing CIS with a Business Administration minor is an exceptional strategic combination. Modern network engineering is as much about risk management, business continuity, and ROI as it is about protocols and cables. Wonderful post!",
        "reply": "<p>Hello James,</p><p>Welcome to the course! Your combination of Information Systems and Business Administration is particularly valuable. When enterprise network engineers propose redundancy (like HSRP) or cloud migration, they must articulate the business value and SLA protection to executive leadership. You will see that business-technical intersection throughout our scenarios.</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 18445,
        "entry_id": 462530,
        "name": "Jacori Stubbs",
        "grade": 100.0,
        "comment": "Jacori, welcome! Having past familiarity with CompTIA material (A+, Net+, Sec+) gives you a tremendous launchpad. In this course, we move beyond rote memorization into real terminal diagnostics, packet inspection, and engineering design. Let's get you fully certified and career-ready!",
        "reply": "<p>Hello Jacori,</p><p>Welcome to CIS-3321! It is great that you've had prior exposure to the CompTIA trifecta. Our goal this semester is to activate that knowledge through hands-on labs and scenario PBQs so you can sit for and pass the Network+ and CCNA exams with total confidence. Let's make this semester count!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 21504,
        "entry_id": 462640,
        "name": "Caleb Olen",
        "grade": 100.0,
        "comment": "Caleb, welcome! Your insight that it is vital to 'think in terms of managing a system' is precisely the doctoral perspective we aim to cultivate. Networks are interconnected, interdependent complex systems. Great to have you in class for your senior year!",
        "reply": "<p>Hello Caleb,</p><p>Welcome to the course! Your systems-thinking mindset is exactly what enterprise architecture requires. Isolating root causes across multi-tiered topologies requires understanding how physical links, logical addressing, and transport sessions interact as a unified ecosystem. Glad to have you in the class!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 16186,
        "entry_id": 469351,
        "name": "Wilfredo Lopez",
        "grade": 100.0,
        "comment": "Wilfredo, welcome to CIS-3321! Having practical experience connecting SOHO devices is a great starting point. In this class, we will scale that knowledge into enterprise switching, structured cabling standards, subnetting, and routing protocols. Excellent introduction!",
        "reply": "<p>Hello Wilfredo,</p><p>Welcome to CIS-3321! Moving from residential device connectivity to enterprise network administration is one of the most rewarding transitions in IT. You will find that the foundational principles remain consistent, but the scale, security controls, and redundancy requirements expand significantly. Welcome aboard!</p><p>— Professor Nash, Ph.D.</p>"
    }
]

# ==============================================================================
# 2. CIS-3321 MODULE 01 DISCUSSION: OSI & TROUBLESHOOTING
# ==============================================================================
M01_DATA_3321 = [
    {
        "user_id": 18445,
        "entry_id": 464893,
        "name": "Jacori Stubbs",
        "grade": 98.0,
        "comment": "Jacori, excellent breakdown of Scenario A. You accurately outlined the bottom-up methodology starting at Layer 1 (Physical) before ascending to Layer 2 (Data Link). Your identification of the switch port / NIC interface as the primary suspect for the third workstation is technically sound. To achieve perfection, remember to specify the exact diagnostic commands (such as 'show interface status' or checking duplex mismatches) at Layer 2. Outstanding work!",
        "reply": "<p>Jacori,</p><p>You provided a very clear application of the bottom-up troubleshooting methodology. You correctly noted that because two workstations recovered following cable replacement, the passive patch cable was indeed faulty for those nodes. For the third workstation, when link lights remain unlit even with a verified patch cable, investigating the Network Interface Card (NIC) hardware and the corresponding switch port transceiver at Layer 1 is precisely correct.</p><p>From an enterprise administration standpoint, how would you test whether the fault lies in the workstation's NIC versus the in-wall structured cabling run (horizontal cross-connect) before dispatching a technician to punch down new terminations? Excellent post!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 21504,
        "entry_id": 465089,
        "name": "Caleb Olen",
        "grade": 98.0,
        "comment": "Caleb, thoughtful and rigorous analysis of Scenario A. Your emphasis on testing the patch panel, wall jack, and switch port hardware demonstrates strong practical intuition. Layer 1 encompasses not just the external patch lead, but the entire physical transmission media. Well reasoned and clearly articulated!",
        "reply": "<p>Caleb,</p><p>A very thorough diagnostic breakdown. You rightly pointed out that Layer 1 encompasses the entire physical pathway—including the wall jack, horizontal solid-core UTP cabling, patch panel punch-down block, and switch port transceiver.</p><p>Your point regarding preventing technicians from jumping to higher-layer conclusions (like DHCP or DNS reconfiguration) is paramount. In enterprise environments, adjusting IP configurations when the physical carrier detect signal is absent only introduces configuration drift and complicates root-cause analysis. Keep up the high-caliber analysis!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 15652,
        "entry_id": 465107,
        "name": "Arinzechukwu Ejeckam",
        "grade": 98.0,
        "comment": "Arinze, compelling analysis of Scenario C regarding physical versus logical topologies. You correctly observed that modern Ethernet networks almost universally employ a physical star (or extended star) topology centered around a switch, while the logical data flow depends on the switching fabric. Strong grasp of topology concepts!",
        "reply": "<p>Arinze,</p><p>You tackled Scenario C with genuine architectural insight. While legacy 10BASE-T hubs operated as a physical star but a logical bus (sharing a single collision domain where every frame flooded to all ports), modern Layer 2 switches utilize Content Addressable Memory (CAM) tables to segment collision domains per port.</p><p>Therefore, logically, the switch provides point-to-point dedicated micro-segments between transmitting and receiving MAC addresses. How does the presence of VLANs further alter the logical broadcast topology across that same physical star? Superb contribution!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 15566,
        "entry_id": 465513,
        "name": "Zaniya Grice",
        "grade": 100.0,
        "comment": "Zaniya, this is an exemplary doctoral-quality submission! Your systematic walkthrough of Layer 1 (checking continuity, link pulses, pinouts) and Layer 2 (MAC framing, port speed/duplex negotiation, error counters) was exceptionally thorough. You cited specific diagnostic indicators and avoided common troubleshooting pitfalls. A flawless 100/100!",
        "reply": "<p>Zaniya,</p><p>This is a masterclass in systematic network diagnostics. Your separation between Layer 1 physical carrier detection and Layer 2 frame synchronization / port negotiation was mathematically and architecturally precise.</p><p>You correctly highlighted that replacing cables addresses the most common point of mechanical failure, but when link lights remain dark, the physical layer issue may reside in the NIC hardware, the horizontal cabling run, or a disabled switch port state (such as <em>err-disabled</em> due to port security). Outstanding work!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 4464,
        "entry_id": 467090,
        "name": "Benjamin Flores",
        "grade": 97.0,
        "comment": "Benjamin, strong and practical response to Scenario A. You accurately identified that Layer 1 governs the physical media and signal transmission, and that the third workstation's persistent failure points toward an internal NIC failure or port shut condition. Excellent troubleshooting logic!",
        "reply": "<p>Benjamin,</p><p>Very well argued. You rightly emphasized that before touching network settings, software, or IP addresses, the physical link pulse must be verified. If the PHY chip on the network adapter cannot establish a link pulse with the switch port, no data packets can ever be processed.</p><p>In a production environment, if you suspect the switch port itself might be disabled by the OS, what Cisco IOS command would you issue to inspect whether the port is administrative down or err-disabled? Great job!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 3965,
        "entry_id": 467401,
        "name": "Oke Akpoborie",
        "grade": 97.0,
        "comment": "Oke, great post addressing Scenario A. Your explanation of Layer 1 signal transmission and the rationale for avoiding higher-layer troubleshooting prematurely was spot on. Clear, concise, and technically accurate!",
        "reply": "<p>Oke,</p><p>Solid technical reasoning. Your point about verifying physical seated connections and link lights before even considering higher-level protocol diagnostics illustrates the core discipline of the bottom-up model.</p><p>Technicians who skip Layer 1 and immediately reconfigure IP addresses often introduce secondary misconfigurations that obscure the original hardware fault. Well said!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 21059,
        "entry_id": 467407,
        "name": "Melany Reyes",
        "grade": 100.0,
        "comment": "Melany, outstanding mastery demonstrated on Scenario B (Encapsulation)! Your breakdown of Layer 4 TCP segment headers (source/dest ports, sequence/ACK numbers) down through Layer 3 IP packets (source/dest IP, TTL) and Layer 2 Ethernet frames (MAC addressing, FCS/CRC) was textbook perfection. A flawless 100/100!",
        "reply": "<p>Melany,</p><p>Your breakdown of Protocol Data Unit (PDU) encapsulation in Scenario B was brilliant. You precisely captured how data transforms from application stream to Layer 4 Segment, Layer 3 Packet, Layer 2 Frame, and Layer 1 Bits.</p><p>Your note regarding the Frame Check Sequence (FCS) using a Cyclic Redundancy Check (CRC) at the trailer of Layer 2 is a detail that many students miss. That 4-byte trailer is vital because it allows the receiving NIC to verify frame integrity before passing the payload up to Layer 3. Stellar technical analysis!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 4806,
        "entry_id": 467569,
        "name": "Chrissean Sias-Rackstraw",
        "grade": 96.0,
        "comment": "Chrissean, very clear and logical response to Scenario A. You accurately identified the transition from physical media (Layer 1) to data-link frame parsing (Layer 2) and correctly diagnosed the potential for a burnt-out NIC or damaged switch port. Keep up the solid analytical work!",
        "reply": "<p>Chrissean,</p><p>Strong practical analysis. You noted that bits represent the PDU at the Physical Layer, which is a key CompTIA Network+ exam concept. Your conclusion that the third workstation's persistent link failure suggests a hardware fault in the NIC or the switch port is right on target.</p><p>A great next step in a real office would be swapping the workstation to an adjacent known-working switch port or testing the workstation with a USB-to-Ethernet dongle to isolate the onboard NIC. Well done!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 5072,
        "entry_id": 468151,
        "name": "Bryan Lopez",
        "grade": 96.0,
        "comment": "Bryan, solid response to Scenario A. You correctly delineated between physical inspection (cabling, port LEDs) and data-link evaluation. Your explanation of why lower-layer confirmation saves critical diagnostic time was well framed.",
        "reply": "<p>Bryan,</p><p>Well stated. You walked through the initial Layer 1 physical inspection steps clearly. Demonstrating discipline by confirming Layer 1 continuity before attempting to ping or reconfigure network software is the mark of a seasoned IT professional.</p><p>If link lights are solid green but the computer still cannot communicate on the network, what would be your very first Layer 2 diagnostic check? Excellent contribution!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 16186,
        "entry_id": 468585,
        "name": "Wilfredo Lopez",
        "grade": 96.0,
        "comment": "Wilfredo, very well done on Scenario A. You accurately outlined the bottom-up sequence, correctly flagged the NIC and switch port as primary points of failure, and highlighted the importance of disciplined troubleshooting. Good work!",
        "reply": "<p>Wilfredo,</p><p>Good job walking through the bottom-up diagnostic methodology. You correctly recognized that the failure of two workstations was isolated to physical patch cables, while the third workstation likely suffers from a component failure in the network adapter or the patch panel termination.</p><p>Keeping the OSI layers in mind prevents technicians from chasing phantom software bugs when the wire itself is broken. Nice job!</p><p>— Professor Nash, Ph.D.</p>"
    }
]

# ==============================================================================
# 3. CIS-3321 MODULE 02 DISCUSSION: TCP/IP & NETWORK PROTOCOLS
# ==============================================================================
M02_DATA_3321 = [
    {
        "user_id": 4464,
        "entry_id": 466102,
        "name": "Benjamin Flores",
        "grade": 98.0,
        "comment": "Benjamin, excellent explanation of the DHCP DORA process (Discover, Offer, Request, Acknowledge) in Scenario A. You accurately described why a missing DHCP server leads to the assignment of an Automatic Private IP Addressing (APIPA) link-local address (169.254.0.0/16), leaving clients unable to route beyond their local broadcast domain. Superb technical response!",
        "reply": "<p>Benjamin,</p><p>Your explanation of the 4-step DHCP DORA sequence was spot-on. You correctly explained that without an operative DHCP server responding with an Offer, client operating systems self-assign an APIPA address (169.254.x.x) under RFC 3927.</p><p>From an enterprise design perspective, if your DHCP server is located in a central data center across a routed WAN link, what Layer 3 configuration must be added to the local default gateway router (such as Cisco's <code>ip helper-address</code>) to forward the client's Layer 2 broadcast Discover messages as unicast UDP packets across the router? Excellent post!</p><p>— Professor Nash, Ph.D.</p>"
    },
    {
        "user_id": 18445,
        "entry_id": 469403,
        "name": "Jacori Stubbs",
        "grade": 98.0,
        "comment": "Jacori, outstanding analysis of Scenario B regarding legacy, unencrypted protocols! You accurately matched Port 23 (Telnet), Port 80 (HTTP), and Port 110 (POP3) with their cryptographic replacements: SSH (Port 22), HTTPS (Port 443), and POP3S (Port 995). Your security rationale regarding plaintext transmission vulnerabilities is completely accurate for CompTIA Network+ and Security+. Great job!",
        "reply": "<p>Jacori,</p><p>You did an exceptional job breaking down the severe security risks associated with legacy plaintext protocols in Scenario B. Transmitting credentials over Telnet (Port 23) or POP3 (Port 110) makes organizations trivial targets for packet sniffing and credential harvesting via Wireshark.</p><p>Your recommendations to transition to SSH (Port 22), HTTPS (Port 443 with TLS 1.3), and secure mail protocols are standard enterprise security mandates. When hardening an edge firewall, what default filtering posture (e.g. implicit deny) should be enforced for legacy ports? Excellent contribution!</p><p>— Professor Nash, Ph.D.</p>"
    }
]

def main():
    print("=" * 80)
    print("GRADING CIS-3321 DISCUSSIONS (INTRO, M01, M02)")
    print("=" * 80)

    # 1. Introduce Yourself
    print("\n--- 1. Grading 'Discussion: Introduce Yourself' (ID: 227447) ---")
    for item in INTRO_DATA_3321:
        grade_submission(COURSE_ID, 227447, item["user_id"], item["grade"], item["comment"])
        post_discussion_reply(COURSE_ID, 139131, item["entry_id"], item["reply"])
        time.sleep(0.5)

    # 2. Discussion M01
    print("\n--- 2. Grading 'Discussion (M01)' (ID: 227450) ---")
    for item in M01_DATA_3321:
        grade_submission(COURSE_ID, 227450, item["user_id"], item["grade"], item["comment"])
        post_discussion_reply(COURSE_ID, 139132, item["entry_id"], item["reply"])
        time.sleep(0.5)

    # 3. Discussion M02
    print("\n--- 3. Grading 'Discussion (M02)' (ID: 227453) ---")
    for item in M02_DATA_3321:
        grade_submission(COURSE_ID, 227453, item["user_id"], item["grade"], item["comment"])
        post_discussion_reply(COURSE_ID, 139133, item["entry_id"], item["reply"])
        time.sleep(0.5)

    print("\n" + "=" * 80)
    print("✅ CIS-3321 DISCUSSIONS FULLY GRADED & REPLIED TO!")
    print("=" * 80)

if __name__ == "__main__":
    main()
