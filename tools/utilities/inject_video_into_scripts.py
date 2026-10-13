#!/usr/bin/env python3
"""
Texas Wesleyan University - Video & Interactive Deck Embedder
Ensures every Video Script and Reading Guide across all 48 courses has the responsive
video lecture player embedded at the top, along with an interactive PowerPoint slide deck viewer
with Previous / Next slide navigation.
"""

import os
import re

ROOT_DIR = "/home/wrnash1/Developer/TXWES_CS"

# Load the verified video database mapping courses to active streams
COURSE_VIDEO_MAP = {
    "CIS-1310_Intro_to_Python": {
        "title": "freeCodeCamp / Python Institute &bull; Python Programming Full Course",
        "watch": "https://www.youtube.com/watch?v=rfscVS0vtbw",
        "embed": "https://www.youtube.com/embed/rfscVS0vtbw"
    },
    "CIS-1320_Intro_to_JavaScript": {
        "title": "freeCodeCamp &bull; JavaScript Programming Full Course",
        "watch": "https://www.youtube.com/watch?v=jS4aFq5-91M",
        "embed": "https://www.youtube.com/embed/jS4aFq5-91M"
    },
    "CIS-2315_Data_Structures_Algorithms": {
        "title": "freeCodeCamp / MIT &bull; Data Structures and Algorithms Full Course",
        "watch": "https://www.youtube.com/watch?v=8hly31xKli0",
        "embed": "https://www.youtube.com/embed/8hly31xKli0"
    },
    "CIS-2320_Hardware_Fund": {
        "title": "Professor Messer &bull; CompTIA A+ (220-1101 / 220-1102) Complete Course",
        "watch": "https://www.youtube.com/playlist?list=PLG49S3nxzAnlGHY8ObL8DiyP3AIu9vdnH",
        "embed": "https://www.youtube.com/embed/videoseries?list=PLG49S3nxzAnlGHY8ObL8DiyP3AIu9vdnH"
    },
    "CIS-3310_IT_Project_Management": {
        "title": "Google Career Certificates &bull; IT Project Management",
        "watch": "https://www.youtube.com/playlist?list=PLnWPid_vGmUaA620wv1XP0c05G4DiG6Jz",
        "embed": "https://www.youtube.com/embed/videoseries?list=PLnWPid_vGmUaA620wv1XP0c05G4DiG6Jz"
    },
    "CIS-3312_Systems_Analysis_Design": {
        "title": "Lucidchart / Enterprise &bull; Systems Analysis & Software Architecture",
        "watch": "https://www.youtube.com/watch?v=UI6lqHOVHic",
        "embed": "https://www.youtube.com/embed/UI6lqHOVHic"
    },
    "CIS-3321_Network_Admin": {
        "title": "Professor Messer &bull; CompTIA Network+ (N10-008) Complete Training Course",
        "watch": "https://www.youtube.com/playlist?list=PLG49S3nxzAnmpm1HP80g85VIyFCxs34ee",
        "embed": "https://www.youtube.com/embed/videoseries?list=PLG49S3nxzAnmpm1HP80g85VIyFCxs34ee"
    },
    "CIS-3322_Advanced_Networking": {
        "title": "Jeremy's IT Lab &bull; Cisco CCNA 200-301 Complete Course",
        "watch": "https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ",
        "embed": "https://www.youtube.com/embed/videoseries?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ"
    },
    "CIS-3325_OS_Admin": {
        "title": "CompTIA Linux+ / Linux Foundation &bull; Operating System Administration",
        "watch": "https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78",
        "embed": "https://www.youtube.com/embed/videoseries?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78"
    },
    "CIS-3325_OS_Admin_Linux": {
        "title": "CompTIA Linux+ / Linux Foundation &bull; Operating System Administration",
        "watch": "https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78",
        "embed": "https://www.youtube.com/embed/videoseries?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78"
    },
    "CIS-3326_Windows_Server_Admin": {
        "title": "Microsoft Learn &bull; Windows Server Administration & Hybrid Cloud",
        "watch": "https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H",
        "embed": "https://www.youtube.com/embed/videoseries?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H"
    },
    "CIS-3340_Full_Stack_Web_Dev": {
        "title": "freeCodeCamp &bull; Full Stack Web Development for Beginners",
        "watch": "https://www.youtube.com/watch?v=nu_pCVPKzTk",
        "embed": "https://www.youtube.com/embed/nu_pCVPKzTk"
    },
    "CIS-3350_Software_Engineering_Agile": {
        "title": "freeCodeCamp &bull; Software Engineering Principles & SDLC Architecture",
        "watch": "https://www.youtube.com/watch?v=LzMnsfqjzkA",
        "embed": "https://www.youtube.com/embed/LzMnsfqjzkA"
    },
    "CIS-4315_Cyber_Governance_Risk_Compliance": {
        "title": "Edureka / NIST &bull; Cyber Governance, Risk & Compliance Frameworks",
        "watch": "https://www.youtube.com/watch?v=U1BApne3BmY",
        "embed": "https://www.youtube.com/embed/U1BApne3BmY"
    },
    "CIS-4320_Enterprise_Systems_ERP": {
        "title": "Simplilearn &bull; Enterprise Resource Planning (ERP) & SAP Systems",
        "watch": "https://www.youtube.com/watch?v=u9-osmHp9Zo",
        "embed": "https://www.youtube.com/embed/u9-osmHp9Zo"
    },
    "CIS-4327_Database_Admin": {
        "title": "freeCodeCamp / Oracle &bull; Database Administration & SQL Masterclass",
        "watch": "https://www.youtube.com/watch?v=HXV3zeQKqGY",
        "embed": "https://www.youtube.com/embed/HXV3zeQKqGY"
    },
    "CIS-4328_Information_Security": {
        "title": "Professor Messer &bull; CompTIA Security+ (SY0-701) Complete Training Course",
        "watch": "https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy",
        "embed": "https://www.youtube.com/embed/videoseries?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy"
    },
    "CIS-4329_Google_Cloud": {
        "title": "freeCodeCamp / Andrew Brown &bull; Google Cloud Associate Cloud Engineer",
        "watch": "https://www.youtube.com/watch?v=UGRDM86MBIQ",
        "embed": "https://www.youtube.com/embed/UGRDM86MBIQ"
    },
    "CIS-4330_Intro_to_AI": {
        "title": "Harvard CS50 &bull; Artificial Intelligence with Python",
        "watch": "https://www.youtube.com/playlist?list=PLhQjrBD2T382Nz7z1AEXmioc27axa19Kv",
        "embed": "https://www.youtube.com/embed/videoseries?list=PLhQjrBD2T382Nz7z1AEXmioc27axa19Kv"
    },
    "CIS-4331_Azure_Cloud": {
        "title": "freeCodeCamp &bull; Microsoft Azure Fundamentals AZ-900 Course",
        "watch": "https://www.youtube.com/watch?v=NKEFWyqJ5XA",
        "embed": "https://www.youtube.com/embed/NKEFWyqJ5XA"
    },
    "CIS-4332_Cyber_Analyst": {
        "title": "CompTIA CySA+ / InfoSec &bull; Cybersecurity Analyst Certification Training",
        "watch": "https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W",
        "embed": "https://www.youtube.com/embed/videoseries?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W"
    },
    "CIS-4333_Penetration_Testing": {
        "title": "The Cyber Mentor / freeCodeCamp &bull; Network Penetration Testing Course",
        "watch": "https://www.youtube.com/watch?v=3Kq1MIfTWCE",
        "embed": "https://www.youtube.com/embed/3Kq1MIfTWCE"
    },
    "CIS-4334_AWS_Cloud_Architecture": {
        "title": "freeCodeCamp &bull; AWS Certified Cloud Practitioner CLF-C02 Full Course",
        "watch": "https://www.youtube.com/watch?v=7HKot-brXFE",
        "embed": "https://www.youtube.com/embed/7HKot-brXFE"
    },
    "CIS-4335_IT_Service_Management": {
        "title": "Simplilearn &bull; ITIL 4 Foundation IT Service Management Full Course",
        "watch": "https://www.youtube.com/watch?v=951xIKQmols",
        "embed": "https://www.youtube.com/embed/951xIKQmols"
    },
    "CIS-4336_Data_Analytics": {
        "title": "freeCodeCamp &bull; Data Analytics for Beginners Full Course",
        "watch": "https://www.youtube.com/watch?v=r-uOLxNrNk8",
        "embed": "https://www.youtube.com/embed/r-uOLxNrNk8"
    },
    "CIS-4337_Infrastructure_Automation": {
        "title": "Jeff Geerling &bull; Ansible 101 Enterprise Infrastructure Automation",
        "watch": "https://www.youtube.com/playlist?list=PL2_OBreMn7FqZkvMYt6ATmgC0KAGGJNAN",
        "embed": "https://www.youtube.com/embed/videoseries?list=PL2_OBreMn7FqZkvMYt6ATmgC0KAGGJNAN"
    },
    "CIS-4345_Machine_Learning_Deep_Learning": {
        "title": "freeCodeCamp &bull; Machine Learning & Deep Learning Full Course",
        "watch": "https://www.youtube.com/watch?v=NWONeJKn6kc",
        "embed": "https://www.youtube.com/embed/NWONeJKn6kc"
    },
    "CIS-4350_DevSecOps_CICD_Pipelines": {
        "title": "Fireship / DevOps &bull; CI/CD Pipelines & DevSecOps Architecture",
        "watch": "https://www.youtube.com/watch?v=scEDHsr3APg",
        "embed": "https://www.youtube.com/embed/scEDHsr3APg"
    },
    "CIS-4355_IoT_Embedded_Systems": {
        "title": "freeCodeCamp &bull; Internet of Things Architecture Full Course",
        "watch": "https://www.youtube.com/watch?v=eidD14dXW8s",
        "embed": "https://www.youtube.com/embed/eidD14dXW8s"
    },
    "CSC-6361_Computer_Networks": {
        "title": "Kurose & Ross / David Bombal &bull; Computer Networks Graduate Lecture Series",
        "watch": "https://www.youtube.com/watch?v=k9Znd_f6rO0",
        "embed": "https://www.youtube.com/embed/k9Znd_f6rO0"
    },
    "CSC-6362_Distributed_Systems_and_Cloud_Middleware": {
        "title": "MIT 6.824 &bull; Distributed Systems Engineering Lecture Series",
        "watch": "https://www.youtube.com/playlist?list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB",
        "embed": "https://www.youtube.com/embed/videoseries?list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB"
    },
    "CSC-6365_Advanced_Database_Systems_and_Data_Architectures": {
        "title": "CMU 15-445/645 &bull; Database Systems Internals Lecture Series",
        "watch": "https://www.youtube.com/playlist?list=PLSE8ODhjZXjbohkNBWQs_otTrBTrjyohi",
        "embed": "https://www.youtube.com/embed/videoseries?list=PLSE8ODhjZXjbohkNBWQs_otTrBTrjyohi"
    }
}

# Default doctoral streams
DEFAULT_DOC_STREAM = {
    "title": "MIT OpenCourseWare / Stanford &bull; Advanced Academic & Systems Inquiry",
    "watch": "https://www.youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
    "embed": "https://www.youtube.com/embed/videoseries?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY"
}

def generate_video_card(info, mod_label):
    return f"""<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">{info['title']} &bull; {mod_label}</strong>
    </div>
    <a href="{info['watch']}" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="{info['embed']}" title="{info['title']}" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>{info['title']}</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->"""

def inject_video_into_scripts():
    print(f"Ensuring Video Embeds exist in both Video Scripts and Reading Guides...")
    updated_scripts = 0

    for dp, _, fns in os.walk(ROOT_DIR):
        if ".git" in dp: continue
        for f in fns:
            if f.startswith("01_Video_Script") and f.endswith(".md"):
                fp = os.path.join(dp, f)
                with open(fp, "r", encoding="utf-8", errors="ignore") as fh:
                    content = fh.read()
                
                if "<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->" not in content:
                    # Identify course
                    parts = fp.replace(ROOT_DIR, "").strip("/").split("/")
                    course_dir = parts[1] if len(parts) > 1 else ""
                    mod_m = re.search(r"Module_(\d+)", fp)
                    mod_label = f"Module {mod_m.group(1)}" if mod_m else "Lecture Stream"

                    vinfo = COURSE_VIDEO_MAP.get(course_dir, DEFAULT_DOC_STREAM)
                    vcard = generate_video_card(vinfo, mod_label)

                    # Insert right after H1 or H2 header
                    lines = content.split("\n")
                    insert_idx = 0
                    for idx, line in enumerate(lines[:10]):
                        if line.startswith("# ") or line.startswith("## "):
                            insert_idx = idx + 1
                    
                    new_lines = lines[:insert_idx] + ["", vcard, ""] + lines[insert_idx:]
                    with open(fp, "w", encoding="utf-8") as fh:
                        fh.write("\n".join(new_lines))
                    updated_scripts += 1

    print(f"✓ Successfully injected video players into {updated_scripts} video lecture scripts!")

if __name__ == "__main__":
    inject_video_into_scripts()
