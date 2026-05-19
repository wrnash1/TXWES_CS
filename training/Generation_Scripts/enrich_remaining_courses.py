import os

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

print("=== STARTING RICH CONTENT ENRICHMENT FOR REMAINING 6 COURSES ===")

for code, data in REMAINING_COURSES.items():
    print(f"Enriching {code}...")
    course_dir = os.path.join(BASE_DIR, code)
    if not os.path.exists(course_dir):
        print(f"Directory {course_dir} does not exist. Skipping.")
        continue

    # Generate dynamic weekly schedule blueprint
    weekly_schedule = []
    for w_idx in range(1, 16):
        topic = data["topics"][w_idx - 1]
        weekly_schedule.append(f"*   **Module {w_idx:02d}:** {topic}")
    weekly_schedule.append(f"*   **Module 16:** Final Exam Prep & Certification Exam ({data.get('cert')})")
    weekly_schedule_markdown = "\n".join(weekly_schedule)

    # 1. Update Syllabus in 00_Course_Information
    info_dir = os.path.join(course_dir, "00_Course_Information")
    os.makedirs(info_dir, exist_ok=True)
    syllabus_path = os.path.join(info_dir, "Syllabus.md")
    
    with open(syllabus_path, "w") as f:
        f.write(f"""# TEXAS WESLEYAN UNIVERSITY
## Department of Computer Science & Information Technology
### Course Syllabus: {code} - {data.get('cert')}
**Semester & Year:** Fall 2026
**Course Format:** 100% Online Asynchronous
**Course LMS Portal:** Canvas LMS

---

## Instructor Information
*   **Instructor:** Professor Nash
*   **Department:** Computer Science & Information Technology
*   **Email:** nash@txwes.edu
*   **Office Hours:** Online by appointment (via Zoom/Teams)
*   **Response Time:** Within 24-48 hours on weekdays

---

## Course Overview

### Course Description
{data.get('desc')}

### Course Objectives / Student Learning Outcomes
By the end of this course, students will be able to:
1. Explain and configure core principles of **{data.get('cert')}** in a variety of business and technical scenarios.
2. Formulate, execute, and verify terminal-based commands and administrative configurations matching production-level operations.
3. Critically analyze system failures or security vulnerabilities, and propose mitigation strategies.
4. Prepare for and demonstrate competency aligned with the official **{data.get('cert')}** certification exam blueprint.

### Required Materials
*   **Zero Textbook Cost (ZTC):** All required reading materials, video lectures, and study guides are provided completely free within the Canvas LMS course shell. No textbook purchase is required.
*   **Primary OER Resources:** Reference materials and official vendor documentation are outlined in the [ZTC OER Guide](../ZTC_OER_Reading_Materials.md).
*   **Hardware/Software Requirements:** Access to a computer running Windows, macOS, or Linux with terminal access, standard development tools, and high-speed internet.

---

## Grading & Evaluation

### Grading Policy
Your final grade is calculated based on the following breakdown:
*   **Weekly Quizzes (Modules 01-15):** 20%
*   **Weekly Discussion Boards (Modules 01-15):** 20%
*   **Hands-on Lab Assignments (Modules 01-15):** 30%
*   **Final Certification Exam (Module 16):** 30%

### Grading Scale
*   **A:** 90% - 100% (Excellent)
*   **B:** 80% - 89% (Good)
*   **C:** 70% - 79% (Satisfactory)
*   **D:** 60% - 69% (Passing)
*   **F:** Below 60% (Failure)

---

## Course Calendars & Blueprint
Below is the week-by-week layout of topics and assignments:

{weekly_schedule_markdown}

---

## University & Departmental Policies

### Attendance & Participation Policy
Since this course is conducted 100% online asynchronously, attendance is measured by weekly engagement. Students must log in to Canvas and submit at least one required assignment (discussion post, lab, or quiz) each week to be marked "Present". Failure to submit work for two consecutive weeks will be flagged for departmental review and may lead to administrative withdrawal in accordance with Texas Wesleyan University Catalog policies.

### Academic Integrity & Generative AI Policy
Texas Wesleyan University values academic honesty. Plagiarism, cheating, or any unauthorized collaboration will result in a zero grade for the assignment and potential disciplinary action, up to and including suspension. Refer to the *Texas Wesleyan Student Handbook* for full policies.
*   **Generative AI Guidelines:** In this course, you are encouraged to use AI tools (e.g. ChatGPT, Gemini, Copilot) to brainstorm concepts, understand error messages, and debug script files. However, all submissions (discussion posts, screenshots, explanations) must represent your own cognitive effort. Directly copy-pasting AI outputs without understanding or attribution is considered academic dishonesty.

### ADA & Disability Accommodations Statement
Texas Wesleyan University is committed to providing equal educational opportunities to all students. In accordance with Section 504 of the Rehabilitation Act of 1973 and the Americans with Disabilities Act (ADA), if you have a documented disability and require academic accommodations, please contact the **Office of Disability Services** (located in the Eunice and James L. West Library) as early in the semester as possible.

### Title IX & Harassment Policy
Texas Wesleyan University is committed to maintaining a learning environment free from all forms of discrimination, harassment, and sexual misconduct. If you experience or witness discrimination, sexual harassment, or assault, please report it to the Title IX Coordinator or consult the student handbook for confidential support services.

### Late Work Policy
All weekly assignments (quizzes, discussions, and labs) are due by **Sunday at 11:59 PM CST**. Late work is accepted up to 3 days (72 hours) past the deadline with a **10% penalty per day**. Submissions made after the 3-day grace period will receive a grade of zero unless documented extenuating circumstances are presented.

### Academic Support Services
Texas Wesleyan offers various free support resources to help you succeed:
*   **University Library:** Academic databases, citation guides, and research assistance.
*   **Tutoring & Learning Center (TLC):** Free peer tutoring for computer science and mathematics courses.
*   **Writing Center:** Assistance with structuring essays, documentation reports, and discussion board writing.

### Syllabus Change Notice
The instructor reserves the right to amend this syllabus or schedule at any time during the semester. Students will be notified of any changes immediately via Canvas Announcements.
""")

    # 2. Add Discussions & Midterm Review to Modules
    for week_num in range(1, 16):
        mod_dir = os.path.join(course_dir, f"Module_{week_num:02d}")
        if not os.path.exists(mod_dir):
            os.makedirs(mod_dir, exist_ok=True)
            
        topic = data["topics"][week_num - 1]
        
        # Discussion Prompt
        discussion_path = os.path.join(mod_dir, f"05_Discussion_Module_{week_num:02d}.md")
        with open(discussion_path, "w") as f:
            f.write(f"""# Discussion Forum: Module {week_num} - {topic}
## Course: {code} ({data.get('cert')})

---

## Discussion Prompt
Consider the following real-world scenario or technical concept:
*   **Topic Focus:** **{topic}**

**Your Tasks:**
1.  **Initial Post (Due Wednesday at 11:59 PM):** In 150-200 words, explain how you would apply {topic} in an enterprise system. Address the following:
    *   What is the primary benefit of utilizing this configuration or standard in a production environment?
    *   Identify one common security concern or operational challenge related to this topic, and suggest a best-practice mitigation strategy.
2.  **Peer Responses (Due Sunday at 11:59 PM):** Read through your classmates' posts and write constructive replies (at least 50 words each) to at least two peers. In your replies:
    *   Provide feedback on their proposed mitigation strategy.
    *   Share an alternative approach or add context from your own research or lab exercises.

---

## Discussion Rubric (10 Points Total)
*   **Initial Post (6 Points):**
    *   *5-6 pts:* Thoroughly addresses all prompt questions with technical accuracy, clear explanations, and appropriate terminology. Meets the word count.
    *   *3-4 pts:* Addresses some prompt questions, but lacks detail or technical accuracy.
    *   *0-2 pts:* Incomplete or missing initial post.
*   **Peer Responses (4 Points):**
    *   *4 pts:* Responds constructively to at least two peers, contributing meaningful additions to the conversation.
    *   *2 pts:* Responds to only one peer, or comments are superficial (e.g., "Good post!").
    *   *0 pts:* No peer responses submitted.
""")

        # Midterm Review (Only in Module 08)
        if week_num == 8:
            midterm_path = os.path.join(mod_dir, "Midterm_Review_Module_08.md")
            m1_7_topics = []
            for w_idx in range(7):
                m1_7_topics.append(f"*   **Module 0{w_idx+1}:** {data['topics'][w_idx]}")
            m1_7_topics_str = "\n".join(m1_7_topics)
            
            with open(midterm_path, "w") as f:
                f.write(f"""# Midterm Prep & Review Guide
## Course: {code} ({data.get('cert')})

Congratulations on reaching the halfway point of the semester! This review guide is designed to help you prepare for the upcoming Midterm Exam by summarizing key concepts from Modules 01 through 07.

---

## Core Topics for Review
{m1_7_topics_str}

---

## Study Recommendations
1.  **Revisit the Reading Guides:** Read through the *High-Yield Glossary* and *Certification Exam Tips* in each of the first 7 modules.
2.  **Review Quizzes:** Retake the practice quizzes and pay special attention to the *Distractor Analysis* for any questions you missed.
3.  **Lab Checkpoints:** Review the commands and configuration files you set up during the hands-on lab activities. Make sure you understand the diagnostic utilities you ran.
4.  **Practice Active Recall:** Write brief summaries of each module's core topic from memory and compare them to the Reading Guides.
""")

print("=== RICH CONTENT ENRICHMENT COMPLETE FOR REMAINING 6 COURSES ===")
