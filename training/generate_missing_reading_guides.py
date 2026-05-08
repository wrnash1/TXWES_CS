import os
import glob

base_dir = "/home/wrnash1/Developer/TXWES_CS/training/Online_Courses"
courses = glob.glob(os.path.join(base_dir, "CIS-*"))

topics = {
    "CIS-3321_Network_Admin": ["OSI Model", "VLANs", "Routing", "Security", "OSPF/BGP", "Wireless", "Monitoring", "Troubleshooting", "WANs", "IPv6", "VoIP", "High Availability", "Datacenter", "Disaster Recovery", "Acronyms", "Final Prep"],
    "CIS-3325_OS_Admin": ["OS Basics", "Command Line", "Users", "Permissions", "Bash Scripting", "Networking", "Archiving", "Boot Process", "Package Management", "Storage", "Awk/Sed", "Cron", "SSH", "Logging", "Review", "Final Prep"],
    "CIS-3326_Windows_Server_Admin": ["Server Core", "AD DS", "GPOs", "File Services", "DNS/DHCP", "IIS", "RDS", "Backups", "WSUS", "AD Trusts", "Print Services", "NPS/RADIUS", "Containers", "Clustering", "PowerShell", "Final Prep"],
    "CIS-4327_Database_Admin": ["Cloud SQL", "Spanner", "Migration", "Security", "TrueTime", "BigQuery", "Terraform", "RTO/RPO", "Firestore", "Datastream", "Performance Tuning", "Bigtable", "Memorystore", "Cross-Region DR", "Review", "Final Prep"],
    "CIS-4328_Information_Security": ["Threats", "Network Sec", "Cryptography", "Operations", "IAM", "PKI", "Risk", "Incident Response", "AppSec (OWASP)", "SDLC", "Cloud/MDM", "IoT Security", "Compliance/GRC", "Forensics", "Review", "Final Prep"],
    "CIS-4329_Google_Cloud": ["Resource Hierarchy", "Compute/Storage", "GKE", "Autoscaling", "VPC", "IAM", "Billing", "CLI Tools", "GKE Deployments", "App Engine/Cloud Run", "Functions/PubSub", "Databases", "Hybrid Cloud", "Security Command Center", "Review", "Final Prep"]
}

for course in courses:
    course_name = os.path.basename(course)
    course_topics = topics.get(course_name, ["Topic"] * 16)
    
    for i in range(1, 17):
        mod_dir = os.path.join(course, f"Module_{i:02d}")
        rg_dir = os.path.join(mod_dir, "02_Reading_Guides")
        
        os.makedirs(rg_dir, exist_ok=True)
        
        # Check if empty
        if not os.listdir(rg_dir):
            topic = course_topics[i-1]
            content = f"""### Reading Guide: {topic}

**Zero Textbook Cost (ZTC) Resource Link:**
Please refer to the `ZTC_OER_Reading_Materials.md` file located in the root of the course for the direct links to the free, official Open Educational Resources (OER) for this module.

**High-Yield Summaries:**
*   **Core Concept:** This module focuses on {topic}. Ensure you understand the primary terminology and how it applies to the certification exam objectives.
*   **Exam Tip:** Memorize the common ports, protocols, and command-line syntax associated with {topic}.
*   **Documentation:** Always refer to the official vendor documentation (Microsoft Learn, Google Cloud Docs, or CompTIA objectives) linked in your ZTC guide for the most up-to-date information.
"""
            with open(os.path.join(rg_dir, f"Reading_Guide_Module_{i:02d}.md"), 'w') as f:
                f.write(content)

print("Generated missing reading guides.")
