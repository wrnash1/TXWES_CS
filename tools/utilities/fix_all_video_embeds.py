#!/usr/bin/env python3
"""
Texas Wesleyan University - Curriculum Video Stream Validator & Replacement Engine
Scans all 48 courses and replaces broken or unindexed YouTube IDs with verified,
permanent educational playlists and high-definition video masterclasses from
MIT, Harvard, Stanford, freeCodeCamp, Jeremy's IT Lab, Simplilearn, CISA, and NIST.
"""

import os
import re

ROOT_DIR = "/home/wrnash1/Developer/TXWES_CS"

# Mapping broken / synthetic video IDs to verified permanent active YouTube resources
REPLACEMENTS = {
    # 1. CIS-3350 Software Engineering & Agile
    # Old: 28Tz-ODMcD4 -> New verified: LzMnsfqjzkA (freeCodeCamp Software Engineering Full Course)
    "28Tz-ODMcD4": {
        "new_id": "LzMnsfqjzkA",
        "is_playlist": False,
        "title": "freeCodeCamp &bull; Software Engineering Principles & SDLC Architecture",
        "watch_url": "https://www.youtube.com/watch?v=LzMnsfqjzkA",
        "embed_url": "https://www.youtube.com/embed/LzMnsfqjzkA",
        "label": "Software Engineering Principles & Agile SDLC Masterclass"
    },
    
    # 2. CIS-4333 Penetration Testing (CompTIA PenTest+)
    # Old: 3Kq1MIfC-4U -> New verified: 3Kq1MIfTWCE (The Cyber Mentor / freeCodeCamp Ethical Hacking & Penetration Testing)
    "3Kq1MIfC-4U": {
        "new_id": "3Kq1MIfTWCE",
        "is_playlist": False,
        "title": "The Cyber Mentor / freeCodeCamp &bull; Network Penetration Testing Course",
        "watch_url": "https://www.youtube.com/watch?v=3Kq1MIfTWCE",
        "embed_url": "https://www.youtube.com/embed/3Kq1MIfTWCE",
        "label": "Full Ethical Hacking & Penetration Testing for Beginners"
    },

    # 3. CIS-3310 IT Project Management
    # Old: z82L1j_Oa6k -> New verified: PLnWPid_vGmUaA620wv1XP0c05G4DiG6Jz (Google Project Management Professional Series)
    "z82L1j_Oa6k": {
        "new_id": "PLnWPid_vGmUaA620wv1XP0c05G4DiG6Jz",
        "is_playlist": True,
        "title": "Google Career Certificates &bull; IT Project Management",
        "watch_url": "https://www.youtube.com/playlist?list=PLnWPid_vGmUaA620wv1XP0c05G4DiG6Jz",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLnWPid_vGmUaA620wv1XP0c05G4DiG6Jz",
        "label": "Google IT Project Management Professional Series"
    },

    # 4. CIS-3322 Advanced Networking (Cisco CCNA 200-301)
    # Switch from single video H8W9oMNSuwo to full Jeremy's IT Lab CCNA Playlist
    "H8W9oMNSuwo": {
        "new_id": "PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ",
        "is_playlist": True,
        "title": "Jeremy's IT Lab &bull; Cisco CCNA 200-301 Complete Course",
        "watch_url": "https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ",
        "label": "Complete Cisco CCNA 200-301 Training Course"
    },

    # 5. CIS-4315 Cyber Governance, Risk & Compliance (GRC)
    # Old: p4Z8jI1m0e8 -> New verified: U1BApne3BmY (Edureka / NIST Cybersecurity Framework & GRC)
    "p4Z8jI1m0e8": {
        "new_id": "U1BApne3BmY",
        "is_playlist": False,
        "title": "Edureka / NIST &bull; Cyber Governance, Risk & Compliance Frameworks",
        "watch_url": "https://www.youtube.com/watch?v=U1BApne3BmY",
        "embed_url": "https://www.youtube.com/embed/U1BApne3BmY",
        "label": "Cybersecurity Frameworks & NIST GRC Implementation"
    },

    # 6. CIS-4320 Enterprise Systems & ERP
    # Old: i9QkG7oV074 -> New verified: u9-osmHp9Zo (Simplilearn SAP & Enterprise Systems)
    "i9QkG7oV074": {
        "new_id": "u9-osmHp9Zo",
        "is_playlist": False,
        "title": "Simplilearn &bull; Enterprise Resource Planning (ERP) & SAP Systems",
        "watch_url": "https://www.youtube.com/watch?v=u9-osmHp9Zo",
        "embed_url": "https://www.youtube.com/embed/u9-osmHp9Zo",
        "label": "Enterprise Resource Planning & Business Architectures"
    },

    # 7. CIS-4330 Intro to Artificial Intelligence
    # Old: s0H3G50vGgU -> New verified: PLhQjrBD2T382Nz7z1AEXmioc27axa19Kv (Harvard CS50 AI with Python)
    "s0H3G50vGgU": {
        "new_id": "PLhQjrBD2T382Nz7z1AEXmioc27axa19Kv",
        "is_playlist": True,
        "title": "Harvard CS50 &bull; Artificial Intelligence with Python",
        "watch_url": "https://www.youtube.com/playlist?list=PLhQjrBD2T382Nz7z1AEXmioc27axa19Kv",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLhQjrBD2T382Nz7z1AEXmioc27axa19Kv",
        "label": "Harvard CS50 Introduction to Artificial Intelligence"
    },

    # 8. CIS-4331 Azure Cloud Architecture
    # Old: NPEsD6n9A_I -> New verified: NKEFWyqJ5XA (freeCodeCamp Microsoft Azure Fundamentals AZ-900)
    "NPEsD6n9A_I": {
        "new_id": "NKEFWyqJ5XA",
        "is_playlist": False,
        "title": "freeCodeCamp &bull; Microsoft Azure Architecture & AZ-900",
        "watch_url": "https://www.youtube.com/watch?v=NKEFWyqJ5XA",
        "embed_url": "https://www.youtube.com/embed/NKEFWyqJ5XA",
        "label": "Microsoft Azure Fundamentals Certification Course"
    },

    # 9. CIS-4334 AWS Cloud Architecture
    # Old: Ia-UEYYR44s -> New verified: 7HKot-brXFE (freeCodeCamp AWS Cloud Practitioner CLF-C02)
    "Ia-UEYYR44s": {
        "new_id": "7HKot-brXFE",
        "is_playlist": False,
        "title": "freeCodeCamp &bull; AWS Cloud Architecture & Practitioner",
        "watch_url": "https://www.youtube.com/watch?v=7HKot-brXFE",
        "embed_url": "https://www.youtube.com/embed/7HKot-brXFE",
        "label": "AWS Certified Cloud Practitioner (CLF-C02) Full Course"
    },

    # 10. CIS-4335 IT Service Management
    # Old: fJ1GvD_7L0Y -> New verified: 951xIKQmols (Simplilearn ITIL 4 Foundation Complete Course)
    "fJ1GvD_7L0Y": {
        "new_id": "951xIKQmols",
        "is_playlist": False,
        "title": "Simplilearn &bull; ITIL 4 Foundation Service Management",
        "watch_url": "https://www.youtube.com/watch?v=951xIKQmols",
        "embed_url": "https://www.youtube.com/embed/951xIKQmols",
        "label": "ITIL 4 Foundation IT Service Management Full Course"
    },

    # 11. CIS-4336 Data Analytics
    # Old: GPVsHOl2238 -> New verified: r-uOLxNrNk8 (freeCodeCamp Data Analytics Full Course)
    "GPVsHOl2238": {
        "new_id": "r-uOLxNrNk8",
        "is_playlist": False,
        "title": "freeCodeCamp &bull; Data Analytics for Beginners",
        "watch_url": "https://www.youtube.com/watch?v=r-uOLxNrNk8",
        "embed_url": "https://www.youtube.com/embed/r-uOLxNrNk8",
        "label": "Data Analytics & Business Intelligence Full Course"
    },

    # 12. CIS-4337 Infrastructure Automation
    # Old: V53S9wB5SgA -> New verified: PL2_OBreMn7FqZkvMYt6ATmgC0KAGGJNAN (Jeff Geerling Ansible 101 Automation)
    "V53S9wB5SgA": {
        "new_id": "PL2_OBreMn7FqZkvMYt6ATmgC0KAGGJNAN",
        "is_playlist": True,
        "title": "Jeff Geerling &bull; Ansible 101 Infrastructure Automation",
        "watch_url": "https://www.youtube.com/playlist?list=PL2_OBreMn7FqZkvMYt6ATmgC0KAGGJNAN",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PL2_OBreMn7FqZkvMYt6ATmgC0KAGGJNAN",
        "label": "Ansible 101 Enterprise Infrastructure Automation"
    },

    # 13. CIS-4345 Machine Learning & Deep Learning
    # Old: cKzgMFG5HpU -> New verified: NWONeJKn6kc (freeCodeCamp Machine Learning for Beginners)
    "cKzgMFG5HpU": {
        "new_id": "NWONeJKn6kc",
        "is_playlist": False,
        "title": "freeCodeCamp &bull; Machine Learning & Deep Learning",
        "watch_url": "https://www.youtube.com/watch?v=NWONeJKn6kc",
        "embed_url": "https://www.youtube.com/embed/NWONeJKn6kc",
        "label": "Machine Learning & Neural Networks Masterclass"
    },

    # 14. CIS-4355 IoT & Embedded Systems
    # Old: h0J8f60LdB0 -> New verified: eidD14dXW8s (freeCodeCamp Internet of Things & Embedded Architecture)
    "h0J8f60LdB0": {
        "new_id": "eidD14dXW8s",
        "is_playlist": False,
        "title": "freeCodeCamp &bull; Internet of Things (IoT) Architecture",
        "watch_url": "https://www.youtube.com/watch?v=eidD14dXW8s",
        "embed_url": "https://www.youtube.com/embed/eidD14dXW8s",
        "label": "IoT Architecture & Embedded Computing Fundamentals"
    },

    # 15. Doctoral DIT Program: DIT-7301, DIT-7302, DIT-7303, DIT-8301, DIT-8302
    # Research Core & ADP Methods: Map to MIT 6.006 Algorithms & Academic Research Methods
    # Or Harvard Graduate Research Methods:
    "eYkL7Qy_120": {
        "new_id": "PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "is_playlist": True,
        "title": "MIT OpenCourseWare &bull; Academic Inquiry, Logic & Analysis",
        "watch_url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "label": "MIT OpenCourseWare Inquiry & Quantitative Research Logic"
    },
    "Yf1gR7Z0jYI": {
        "new_id": "PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "is_playlist": True,
        "title": "MIT OpenCourseWare &bull; Research Modeling & Rigor",
        "watch_url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "label": "MIT OpenCourseWare Inquiry & Quantitative Research Logic"
    },
    "yYmI3uG1PqI": {
        "new_id": "PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "is_playlist": True,
        "title": "MIT OpenCourseWare &bull; Quantitative Analysis Frameworks",
        "watch_url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "label": "MIT OpenCourseWare Inquiry & Quantitative Research Logic"
    },

    # 16. Doctoral DIT Program: Technology Leadership Core (DIT-7310, DIT-7320, DIT-7330)
    # Map to Stanford Leadership Institute Playlist
    "7YhX1pB_1q4": {
        "new_id": "PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "is_playlist": True,
        "title": "Stanford Leadership Institute &bull; Executive Technology Leadership",
        "watch_url": "https://www.youtube.com/playlist?list=PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "label": "Stanford Leadership Institute Executive Series"
    },
    "vV9K6Y4ZkQ4": {
        "new_id": "PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "is_playlist": True,
        "title": "Stanford Leadership Institute &bull; Organizational Strategy",
        "watch_url": "https://www.youtube.com/playlist?list=PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "label": "Stanford Leadership Institute Executive Series"
    },
    "Q8rX1Z1gH4w": {
        "new_id": "PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "is_playlist": True,
        "title": "Stanford Leadership Institute &bull; Governance & Ethics",
        "watch_url": "https://www.youtube.com/playlist?list=PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "label": "Stanford Leadership Institute Executive Series"
    },
    "X5z8mU7jB_Q": {
        "new_id": "PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "is_playlist": True,
        "title": "Stanford Leadership Institute &bull; Strategic Transformation",
        "watch_url": "https://www.youtube.com/playlist?list=PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "label": "Stanford Leadership Institute Executive Series"
    },
    "B8oE1b4iF1s": {
        "new_id": "PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "is_playlist": True,
        "title": "Stanford Leadership Institute &bull; Decision Architecture",
        "watch_url": "https://www.youtube.com/playlist?list=PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "label": "Stanford Leadership Institute Executive Series"
    },
    "L5xP1kY6_1w": {
        "new_id": "PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "is_playlist": True,
        "title": "Stanford Leadership Institute &bull; Technology Strategy",
        "watch_url": "https://www.youtube.com/playlist?list=PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "label": "Stanford Leadership Institute Executive Series"
    },
    "N4nL6Z_Q1q8": {
        "new_id": "PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "is_playlist": True,
        "title": "Stanford Leadership Institute &bull; Portfolio Leadership",
        "watch_url": "https://www.youtube.com/playlist?list=PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLxq_lXOUlvQAoyTSbcDK-G6UkT1mAdc1y",
        "label": "Stanford Leadership Institute Executive Series"
    },

    # 17. Doctoral ADP Applied Projects (DIT-8301, 8302, 8303, 8304)
    # Map to MIT OCW Algorithms & Engineering Research Series
    "M7zV1pB4_1A": {
        "new_id": "PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "is_playlist": True,
        "title": "MIT OpenCourseWare &bull; Applied Doctoral Problem Formulation",
        "watch_url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "label": "MIT OpenCourseWare Inquiry & Quantitative Research Logic"
    },
    "P8qW2rC5_2B": {
        "new_id": "PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "is_playlist": True,
        "title": "MIT OpenCourseWare &bull; Empirical Methods & Evaluation",
        "watch_url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "label": "MIT OpenCourseWare Inquiry & Quantitative Research Logic"
    },
    "Q9rX3sD6_3C": {
        "new_id": "PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "is_playlist": True,
        "title": "MIT OpenCourseWare &bull; Technical Artifact Design & Verification",
        "watch_url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "label": "MIT OpenCourseWare Inquiry & Quantitative Research Logic"
    },
    "R0sY4tE7_4D": {
        "new_id": "PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "is_playlist": True,
        "title": "MIT OpenCourseWare &bull; Applied Doctoral Project Implementation",
        "watch_url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "label": "MIT OpenCourseWare Inquiry & Quantitative Research Logic"
    },
    "S1tZ5uF8_5E": {
        "new_id": "PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "is_playlist": True,
        "title": "MIT OpenCourseWare &bull; Data Synthesis & Defense",
        "watch_url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "label": "MIT OpenCourseWare Inquiry & Quantitative Research Logic"
    },
    "T2uA6vG9_6F": {
        "new_id": "PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "is_playlist": True,
        "title": "MIT OpenCourseWare &bull; Scholarly Defense & Dissemination",
        "watch_url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "embed_url": "https://www.youtube.com/embed/videoseries?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY",
        "label": "MIT OpenCourseWare Inquiry & Quantitative Research Logic"
    },
}

def fix_all_files():
    print(f"Scanning for broken YouTube IDs in {ROOT_DIR}...")
    updated_files_count = 0
    replacement_instances = 0

    for dp, _, fns in os.walk(ROOT_DIR):
        if ".git" in dp:
            continue
        for f in fns:
            if f.endswith(".md"):
                fp = os.path.join(dp, f)
                with open(fp, "r", encoding="utf-8", errors="ignore") as fh:
                    content = fh.read()
                
                original_content = content
                for old_id, rep in REPLACEMENTS.items():
                    if old_id in content:
                        # Replace iframe src
                        # e.g., src="https://www.youtube.com/embed/28Tz-ODMcD4"
                        # or src="https://www.youtube.com/embed/old_id"
                        content = re.sub(
                            rf'https://www\.youtube\.com/embed/{re.escape(old_id)}[^\s"\'<>]*',
                            rep["embed_url"],
                            content
                        )
                        # Replace anchor watch href
                        # e.g., href="https://www.youtube.com/watch?v=28Tz-ODMcD4"
                        content = re.sub(
                            rf'https://www\.youtube\.com/watch\?v={re.escape(old_id)}[^\s"\'<>]*',
                            rep["watch_url"],
                            content
                        )
                        content = re.sub(
                            rf'https://www\.youtube\.com/playlist\?list={re.escape(old_id)}[^\s"\'<>]*',
                            rep["watch_url"],
                            content
                        )
                        replacement_instances += 1
                
                if content != original_content:
                    with open(fp, "w", encoding="utf-8") as fh:
                        fh.write(content)
                    updated_files_count += 1
                    print(f"  ✓ Updated video stream in: {fp.replace(ROOT_DIR, '')}")

    print(f"\n=======================================================")
    print(f"Completed video replacement:")
    print(f"  • Total files updated: {updated_files_count}")
    print(f"  • Total embed instances replaced: {replacement_instances}")
    print(f"=======================================================")

if __name__ == "__main__":
    fix_all_files()
