#!/usr/bin/env python3
import os
import shutil

BASE_DIR = "/home/wrnash1/Developer/TXWES_CS/training/Online_Courses"

REMAINING_COURSES = {
    "CIS-3321_Network_Admin": {
        "cert": "CompTIA Network+ (N10-008)",
        "desc": "This course covers network administration, focusing on the OSI model, IP addressing, routing, switching, wireless technologies, and network security.",
        "oer": "Professor Messer Network+ Videos / Official Documentation",
        "topics": ["OSI Model", "VLANs", "Routing", "Security", "OSPF/BGP", "Wireless", "Monitoring", "Troubleshooting", "WANs", "IPv6", "VoIP", "High Availability", "Datacenter", "Disaster Recovery", "Acronyms", "Final Prep"]
    },
    "CIS-3325_OS_Admin": {
        "cert": "CompTIA Linux+ (XK0-005)",
        "desc": "This course covers operating system administration, including Linux commands, bash scripting, file systems, package management, and system services.",
        "oer": "Official Linux Documentation / CompTIA Linux+ Study Resources",
        "topics": ["OS Basics", "Command Line", "Users", "Permissions", "Bash Scripting", "Networking", "Archiving", "Boot Process", "Package Management", "Storage", "Awk/Sed", "Cron", "SSH", "Logging", "Review", "Final Prep"]
    },
    "CIS-3326_Windows_Server_Admin": {
        "cert": "Microsoft Windows Server Administration (Active Directory)",
        "desc": "This course covers Active Directory Domain Services, Group Policies, DNS/DHCP, IIS web server, and Windows Server storage and clustering.",
        "oer": "Microsoft Learn Windows Server Learning Path",
        "topics": ["Server Core", "AD DS", "GPOs", "File Services", "DNS/DHCP", "IIS", "RDS", "Backups", "WSUS", "AD Trusts", "Print Services", "NPS/RADIUS", "Containers", "Clustering", "PowerShell", "Final Prep"]
    },
    "CIS-4327_Database_Admin": {
        "cert": "Google Cloud Associate Database Engineer",
        "desc": "This course covers Cloud SQL, Spanner, migration, security, BigQuery, Bigtable, and cross-region disaster recovery.",
        "oer": "Google Cloud Database Administrator Path",
        "topics": ["Cloud SQL", "Spanner", "Migration", "Security", "TrueTime", "BigQuery", "Terraform", "RTO/RPO", "Firestore", "Datastream", "Performance Tuning", "Bigtable", "Memorystore", "Cross-Region DR", "Review", "Final Prep"]
    },
    "CIS-4328_Information_Security": {
        "cert": "CompTIA Security+ (SY0-701)",
        "desc": "This course covers information security fundamentals, cryptography, identity access management, cloud security, incident response, and risk governance.",
        "oer": "Professor Messer Security+ Videos / Free CompTIA Resources",
        "topics": ["Threats", "Network Sec", "Cryptography", "Operations", "IAM", "PKI", "Risk", "Incident Response", "AppSec (OWASP)", "SDLC", "Cloud/MDM", "IoT Security", "Compliance/GRC", "Forensics", "Review", "Final Prep"]
    },
    "CIS-4329_Google_Cloud": {
        "cert": "Google Cloud Associate Cloud Engineer",
        "desc": "This course covers Resource Hierarchy, GKE deployment, Autoscaling, IAM, Google Cloud CLI tools, App Engine, and hybrid cloud.",
        "oer": "Google Cloud Skills Boost / Associate Cloud Engineer Path",
        "topics": ["Resource Hierarchy", "Compute/Storage", "GKE", "Autoscaling", "VPC", "IAM", "Billing", "CLI Tools", "GKE Deployments", "App Engine/Cloud Run", "Functions/PubSub", "Databases", "Hybrid Cloud", "Security Command Center", "Review", "Final Prep"]
    }
}

def clean_file_content(filepath, code, data, mod_idx, file_type, part_idx=None):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    topic = data["topics"][mod_idx - 1]
    cert = data["cert"]
    mod_num = f"{mod_idx:02d}"
    
    lines = content.split('\n')
    
    start_idx = 0
    for idx, line in enumerate(lines[:15]):
        l_strip = line.strip()
        if not l_strip:
            continue
        if l_strip.startswith('#') or l_strip.startswith('###'):
            start_idx = idx + 1
            continue
        if l_strip.lower().startswith('**course:**') or l_strip.lower().startswith('course:'):
            start_idx = idx + 1
            continue
        if l_strip.lower().startswith('**certification alignment:**') or l_strip.lower().startswith('certification alignment:'):
            start_idx = idx + 1
            continue
        if l_strip.lower().startswith('**target certification:**') or l_strip.lower().startswith('target certification:'):
            start_idx = idx + 1
            continue
        if l_strip == '---':
            start_idx = idx + 1
            continue
        break
        
    body = "\n".join(lines[start_idx:])
    
    new_header = ""
    if file_type == "video":
        part_str = f" (Part {part_idx})" if part_idx else ""
        new_header = f"""# Video Script: {code} ({cert})
## Module {mod_num} - {topic}{part_str}

---"""
    elif file_type == "reading":
        new_header = f"""# Reading Guide: Module {mod_num} - {topic}
## Course: {code} ({cert})

---"""
    elif file_type == "lab":
        new_header = f"""# Lab Activity: Module {mod_num} - {topic}
## Course: {code} ({cert})

---"""
    elif file_type == "quiz":
        new_header = f"""# Quiz: Module {mod_num} - {topic}
## Course: {code} ({cert})

---"""
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_header + "\n\n" + body.strip() + "\n")

def generate_missing_quiz(filepath, code, data, mod_idx):
    topic = data["topics"][mod_idx - 1]
    cert = data["cert"]
    mod_num = f"{mod_idx:02d}"
    
    if mod_idx == 1:
        content = """# Quiz: Module 01 - OSI Model
## Course: CIS-3321_Network_Admin (CompTIA Network+ (N10-008))

---

**Question 1**
Which layer of the OSI model is responsible for routing packets across multiple logical networks using IP addressing?
A) Layer 2 (Data Link Layer)
B) Layer 3 (Network Layer)
C) Layer 4 (Transport Layer)
D) Layer 7 (Application Layer)
*   **Correct Answer:** B) Layer 3 (Network Layer)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Layer 2 handles MAC addressing and framing on the same physical link, not routing across logical networks.
    *   *Why C is incorrect:* Layer 4 manages end-to-end transport protocols (TCP/UDP) and port numbers, not routing.
    *   *Why D is incorrect:* Layer 7 handles application-specific protocols (HTTP, SMTP), not network routing.

**Question 2**
What is the Protocol Data Unit (PDU) processed at Layer 2 of the OSI model?
A) Segment
B) Packet
C) Frame
D) Bit
*   **Correct Answer:** C) Frame
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Segments are the PDU of Layer 4 (Transport Layer).
    *   *Why B is incorrect:* Packets are the PDU of Layer 3 (Network Layer).
    *   *Why D is incorrect:* Bits are the PDU of Layer 1 (Physical Layer).
"""
    else:  # Module 2
        content = """# Quiz: Module 02 - VLANs & Subnetting
## Course: CIS-3321_Network_Admin (CompTIA Network+ (N10-008))

---

**Question 1**
An administrator wants to segment a switch's ports logically into separate broadcast domains. Which technology should they configure?
A) NAT (Network Address Translation)
B) DHCP (Dynamic Host Configuration Protocol)
C) VLAN (Virtual Local Area Network)
D) STP (Spanning Tree Protocol)
*   **Correct Answer:** C) VLAN (Virtual Local Area Network)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* NAT translates between public and private IP addresses, it does not segment local switch broadcast domains.
    *   *Why B is incorrect:* DHCP assigns IP addresses dynamically, it does not create broadcast boundaries.
    *   *Why D is incorrect:* STP prevents switching loops, it does not segment a switch into logical broadcast domains.

**Question 2**
Which of the following IP addresses falls within the private ranges defined by RFC 1918?
A) 172.32.10.5
B) 192.168.4.25
C) 11.0.0.1
D) 192.169.1.1
*   **Correct Answer:** B) 192.168.4.25
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The private Class B range is 172.16.0.0 to 172.31.255.255. 172.32.x.x is public.
    *   *Why C is incorrect:* The private Class A range is 10.0.0.0/8. 11.0.0.1 is public.
    *   *Why D is incorrect:* The private Class C range is 192.168.0.0/16. 192.169.x.x is public.
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    for code, data in REMAINING_COURSES.items():
        print(f"Standardizing and flattening {code}...")
        course_path = os.path.join(BASE_DIR, code)
        
        for mod_idx in range(1, 17):
            mod_dir = os.path.join(course_path, f"Module_{mod_idx:02d}")
            if not os.path.exists(mod_dir):
                continue
            
            # Find all files recursively in the module folder
            all_md_files = []
            for root, dirs, files in os.walk(mod_dir):
                for f in files:
                    if f.endswith(".md"):
                        all_md_files.append(os.path.join(root, f))
            
            # Group files by category
            videos = []
            readings = []
            labs = []
            quizzes = []
            discussions = []
            midterms = []
            
            for filepath in all_md_files:
                name = os.path.basename(filepath).lower()
                parent_dir = os.path.basename(os.path.dirname(filepath)).lower()
                
                if 'midterm' in name:
                    midterms.append(filepath)
                elif 'discussion' in name:
                    discussions.append(filepath)
                elif 'video' in name or 'video' in parent_dir or name.startswith('1_video') or name.startswith('2_video'):
                    videos.append(filepath)
                elif 'reading' in name or 'summary' in name or 'reading' in parent_dir or name.startswith('3_reading'):
                    readings.append(filepath)
                elif 'lab' in name or 'activity' in name or 'activities' in parent_dir or name.startswith('4_lab') or name.startswith('lab_'):
                    labs.append(filepath)
                elif 'quiz' in name or 'assessment' in name or 'assessments' in parent_dir or name.startswith('5_quiz') or name.startswith('quiz_'):
                    quizzes.append(filepath)
                else:
                    # Fallback classification
                    if name.startswith('01_') or name.startswith('1_'):
                        videos.append(filepath)
                    elif name.startswith('02_') or name.startswith('2_') or name.startswith('3_'):
                        readings.append(filepath)
                    elif name.startswith('03_') or name.startswith('4_'):
                        labs.append(filepath)
                    elif name.startswith('04_') or name.startswith('5_'):
                        quizzes.append(filepath)
                    else:
                        readings.append(filepath)
            
            # 1. Process Video Scripts
            videos = sorted(videos)
            if len(videos) == 1:
                target_path = os.path.join(mod_dir, f"01_Video_Script_Module_{mod_idx:02d}.md")
                shutil.move(videos[0], target_path + ".tmp")
                clean_file_content(target_path + ".tmp", code, data, mod_idx, "video")
                os.rename(target_path + ".tmp", target_path)
            elif len(videos) > 1:
                for idx, vfile in enumerate(videos):
                    target_path = os.path.join(mod_dir, f"01_Video_Script_Module_{mod_idx:02d}_Part_{idx+1}.md")
                    shutil.move(vfile, target_path + ".tmp")
                    clean_file_content(target_path + ".tmp", code, data, mod_idx, "video", part_idx=idx+1)
                    os.rename(target_path + ".tmp", target_path)
                    
            # 2. Process Reading Guides
            readings = sorted(readings)
            for rfile in readings:
                target_path = os.path.join(mod_dir, f"02_Reading_Guide_Module_{mod_idx:02d}.md")
                shutil.move(rfile, target_path + ".tmp")
                clean_file_content(target_path + ".tmp", code, data, mod_idx, "reading")
                os.rename(target_path + ".tmp", target_path)
                
            # 3. Process Labs
            labs = sorted(labs)
            for lfile in labs:
                target_path = os.path.join(mod_dir, f"03_Lab_Module_{mod_idx:02d}.md")
                shutil.move(lfile, target_path + ".tmp")
                clean_file_content(target_path + ".tmp", code, data, mod_idx, "lab")
                os.rename(target_path + ".tmp", target_path)
                
            # 4. Process Quizzes
            quizzes = sorted(quizzes)
            for qfile in quizzes:
                target_path = os.path.join(mod_dir, f"04_Quiz_Module_{mod_idx:02d}.md")
                shutil.move(qfile, target_path + ".tmp")
                clean_file_content(target_path + ".tmp", code, data, mod_idx, "quiz")
                os.rename(target_path + ".tmp", target_path)
                
            # 5. Process Discussions
            for dfile in discussions:
                target_path = os.path.join(mod_dir, f"05_Discussion_Module_{mod_idx:02d}.md")
                if dfile != target_path:
                    shutil.move(dfile, target_path)
                    
            # 6. Process Midterm Reviews
            for mfile in midterms:
                target_path = os.path.join(mod_dir, "Midterm_Review_Module_08.md")
                if mfile != target_path:
                    shutil.move(mfile, target_path)
            
            # Clean up empty subdirectories
            for sub in ["01_Video_Scripts", "02_Reading_Guides", "03_Activities", "Assessments", "04_Assessments"]:
                sub_path = os.path.join(mod_dir, sub)
                if os.path.exists(sub_path):
                    shutil.rmtree(sub_path)
                    
        # Check and write missing quizzes for CIS-3321 Module 01 and 02
        if code == "CIS-3321_Network_Admin":
            for missing_m in [1, 2]:
                qpath = os.path.join(course_path, f"Module_{missing_m:02d}", f"04_Quiz_Module_{missing_m:02d}.md")
                if not os.path.exists(qpath):
                    print(f"Generating missing quiz for CIS-3321 Module_{missing_m:02d}...")
                    generate_missing_quiz(qpath, code, data, missing_m)

    print("=== STANDARDIZATION AND FLATTENING COMPLETE ===")

if __name__ == "__main__":
    main()
