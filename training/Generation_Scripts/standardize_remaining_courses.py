#!/usr/bin/env python3
import os
import re

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
    
    # Let's locate where the horizontal rule (---) or content starts
    # We want to replace the first few header lines with standard headers.
    lines = content.split('\n')
    
    # Find the line that separates the original header from the body (e.g. --- or start of content)
    separator_idx = -1
    for idx, line in enumerate(lines[:10]):
        if line.strip() == "---":
            separator_idx = idx
            break
            
    if separator_idx != -1:
        body = "\n".join(lines[separator_idx + 1:])
    else:
        # Fallback if no separator found: skip lines that look like headers
        start_line = 0
        for idx, line in enumerate(lines[:6]):
            if line.strip().startswith('#') or line.strip().startswith('**') or not line.strip():
                start_line = idx + 1
        body = "\n".join(lines[start_line:])
        
    # Generate standardized header
    new_header = ""
    if file_type == "video":
        part_str = f" (Part {part_idx})" if part_idx else ""
        new_header = f"""# Video Script: {code} ({cert})
## Module {mod_num} - {topic}{part_str}

---
"""
    elif file_type == "reading":
        new_header = f"""# Reading Guide: Module {mod_num} - {topic}
## Course: {code} ({cert})

---
"""
    elif file_type == "lab":
        new_header = f"""# Lab Activity: Module {mod_num} - {topic}
## Course: {code} ({cert})

---
"""
    elif file_type == "quiz":
        new_header = f"""# Quiz: Module {mod_num} - {topic}
## Course: {code} ({cert})

---
"""
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_header + "\n" + body.strip() + "\n")

def main():
    for code, data in REMAINING_COURSES.items():
        print(f"Standardizing {code}...")
        course_path = os.path.join(BASE_DIR, code)
        
        for mod_idx in range(1, 17):
            mod_dir = os.path.join(course_path, f"Module_{mod_idx:02d}")
            if not os.path.exists(mod_dir):
                continue
                
            files = sorted(os.listdir(mod_dir))
            
            # Find and rename Video Scripts (01_)
            video_files = [f for f in files if f.startswith("01_")]
            if len(video_files) == 1:
                old_path = os.path.join(mod_dir, video_files[0])
                new_name = f"01_Video_Script_Module_{mod_idx:02d}.md"
                new_path = os.path.join(mod_dir, new_name)
                os.rename(old_path, new_path)
                clean_file_content(new_path, code, data, mod_idx, "video")
            elif len(video_files) > 1:
                for idx, v_file in enumerate(video_files):
                    old_path = os.path.join(mod_dir, v_file)
                    new_name = f"01_Video_Script_Module_{mod_idx:02d}_Part_{idx+1}.md"
                    new_path = os.path.join(mod_dir, new_name)
                    os.rename(old_path, new_path)
                    clean_file_content(new_path, code, data, mod_idx, "video", part_idx=idx+1)
            
            # Re-read directory contents after renames
            files = sorted(os.listdir(mod_dir))
            
            # Find and rename Reading Guides (02_)
            reading_files = [f for f in files if f.startswith("02_")]
            for r_file in reading_files:
                old_path = os.path.join(mod_dir, r_file)
                new_name = f"02_Reading_Guide_Module_{mod_idx:02d}.md"
                new_path = os.path.join(mod_dir, new_name)
                # Handle possible edge cases where there are multiple (e.g. OS Admin Mod 5)
                if len(reading_files) > 1:
                    # If there's already a standard one, keep the second with suffix or merge
                    if r_file == "02_Reading_Guide_Module_05.md":
                        clean_file_content(old_path, code, data, mod_idx, "reading")
                        continue
                    else:
                        new_name = f"02_Reading_Guide_Module_{mod_idx:02d}_Extra.md"
                        new_path = os.path.join(mod_dir, new_name)
                os.rename(old_path, new_path)
                clean_file_content(new_path, code, data, mod_idx, "reading")
                
            # Re-read directory contents after renames
            files = sorted(os.listdir(mod_dir))
            
            # Find and rename Labs (03_)
            lab_files = [f for f in files if f.startswith("03_")]
            for l_file in lab_files:
                old_path = os.path.join(mod_dir, l_file)
                new_name = f"03_Lab_Module_{mod_idx:02d}.md"
                new_path = os.path.join(mod_dir, new_name)
                os.rename(old_path, new_path)
                clean_file_content(new_path, code, data, mod_idx, "lab")
                
            # Re-read directory contents after renames
            files = sorted(os.listdir(mod_dir))
            
            # Find and rename Quizzes (04_)
            quiz_files = [f for f in files if f.startswith("04_")]
            for q_file in quiz_files:
                old_path = os.path.join(mod_dir, q_file)
                new_name = f"04_Quiz_Module_{mod_idx:02d}.md"
                new_path = os.path.join(mod_dir, new_name)
                os.rename(old_path, new_path)
                clean_file_content(new_path, code, data, mod_idx, "quiz")

    print("=== STANDARDIZATION COMPLETE ===")

if __name__ == "__main__":
    main()
