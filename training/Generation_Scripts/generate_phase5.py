import os

base_dir = "/home/wrnash1/Developer/TXWES_CS/training/Online_Courses"
new_courses = {
    "CIS-3322_Advanced_Networking": ("Cisco CCNA (200-301)", "Advanced Routing, Switching, and Wireless", "Cisco Networking Academy (Free NetAcad)"),
    "CIS-4334_AWS_Cloud_Architecture": ("AWS Certified Solutions Architect - Associate", "AWS Compute, Storage, Database, and Networking", "AWS Skill Builder"),
    "CIS-4335_IT_Service_Management": ("ITIL 4 Foundation", "IT Service Delivery and Value Streams", "Axelos ITIL 4 Foundation Practices Guide"),
    "CIS-4336_Data_Analytics": ("CompTIA Data+", "Data Mining, Manipulation, and Visualization", "Professor Messer / CompTIA Free Resources"),
    "CIS-4337_Infrastructure_Automation": ("HashiCorp Certified: Terraform Associate", "Infrastructure as Code (IaC) and Automation", "HashiCorp Learn Platform")
}

for course_dir, (cert, desc, oer) in new_courses.items():
    c_path = os.path.join(base_dir, course_dir)
    info_dir = os.path.join(c_path, "00_Course_Information")
    
    # 1. Create directories
    os.makedirs(info_dir, exist_ok=True)
    for i in range(1, 17):
        mod_dir = os.path.join(c_path, f"Module_{i:02d}")
        if i < 16:
            os.makedirs(os.path.join(mod_dir, "01_Video_Scripts"), exist_ok=True)
            os.makedirs(os.path.join(mod_dir, "Assessments"), exist_ok=True)
        os.makedirs(os.path.join(mod_dir, "02_Reading_Guides"), exist_ok=True)
        os.makedirs(os.path.join(mod_dir, "03_Activities"), exist_ok=True)
        
    # 2. Admin Pack
    admin_content = f"""# Course Administration Pack: {course_dir}
**Target Certification:** {cert}

## Course Description
This course covers {desc}. It is aligned directly with the {cert} exam blueprint.

## Required Materials
1. **Zero Textbook Cost (ZTC):** All required reading materials, official documentation, and study guides are provided completely free within the Blackboard course modules or via the `ZTC_OER_Reading_Materials.md` document. No textbook purchase is required.
2. A computer capable of running basic lab environments or accessing cloud portals.

## Grading Policy
*   Quizzes: 30%
*   Hands-on Labs: 40%
*   Final Certification Exam: 30%
"""
    with open(os.path.join(info_dir, "Course_Administration_Pack.md"), "w") as f:
        f.write(admin_content)

    # 3. ZTC OER Guide
    ztc_content = f"""# {course_dir}: Zero Textbook Cost (ZTC) OER Guide
**Target Certification:** {cert}

This course uses a Zero Textbook Cost model. You are not required to purchase a textbook.

## Primary OER Textbook Replacements
You will rely heavily on free, high-quality open educational resources.
*   **Primary Source:** [{oer}](https://google.com/search?q={oer.replace(' ', '+')})
*   **Secondary Source:** Official {cert} Exam Objectives.

> **Instructor Note:** When the Blackboard Module asks you to read the "High-Yield Concepts", use the links above to explore the concepts in depth.
"""
    with open(os.path.join(c_path, "ZTC_OER_Reading_Materials.md"), "w") as f:
        f.write(ztc_content)

    # 4. Course Map
    map_content = f"""# Online Course Map: {course_dir}
**Target Certification:** {cert}

## 16-Week Breakdown
*   **Modules 1-4:** Foundations and Core Terminology
*   **Modules 5-8:** Operations, Configurations, and Architecture
*   **Modules 9-12:** Advanced Implementations and Security
*   **Modules 13-15:** Review, Hardening, and Practice Exams
*   **Module 16:** Final {cert} Certification Exam
"""
    with open(os.path.join(info_dir, "Online_Course_Map.md"), "w") as f:
        f.write(map_content)

    # 5. Content Generation Modules 1-15
    for i in range(1, 16):
        mod_dir = os.path.join(c_path, f"Module_{i:02d}")
        
        # Video
        v_dir = os.path.join(mod_dir, "01_Video_Scripts")
        v_content = f"""### Video Script: {cert} Domain {i} Concepts

**Estimated Duration:** 7 minutes
**Visual:** Instructor on camera transitioning to a whiteboard diagram.
**[Alt-text: A flowchart diagram showing the core IT concepts related to {cert} Domain {i}, with arrows indicating the workflow.]**

**Audio:** "Welcome to Module {i}. In this module, we are diving into the core objectives for {cert}. It is critical that you understand these foundational concepts before we jump into the lab environment. Remember, the exam will test not just your ability to define these terms, but your ability to troubleshoot them."
"""
        with open(os.path.join(v_dir, f"Video_Script_Module_{i:02d}.md"), "w") as f:
            f.write(v_content)

        # Reading
        r_dir = os.path.join(mod_dir, "02_Reading_Guides")
        r_content = f"""### Reading Guide: {cert} Module {i}

**Zero Textbook Cost (ZTC) Resource Link:**
Please refer to the `ZTC_OER_Reading_Materials.md` file located in the root of the course for the direct links to the free, official Open Educational Resources (OER) for this module.

**High-Yield Summaries:**
*   **Core Concept:** This module focuses on Domain {i} of the {cert} blueprint.
*   **Exam Tip:** Memorize the common ports, protocols, and syntax associated with this topic.
"""
        with open(os.path.join(r_dir, f"Reading_Guide_Module_{i:02d}.md"), "w") as f:
            f.write(r_content)

        # Lab
        a_dir = os.path.join(mod_dir, "03_Activities")
        a_content = f"""### Lab {i}: Applied {cert} Skills

**Objective:** Apply the concepts learned in Module {i} using a hands-on environment.
**Format:** VirtualBox or Cloud Shell.

**Instructions:**
1. Boot your virtual machine or log into your cloud portal.
2. Execute the necessary configuration commands for Domain {i}.
3. Verify the configuration is running successfully using diagnostic tools.

**Deliverable:**
Take a screenshot of your terminal/console showing the successful configuration and upload it to the Blackboard assignment drop-box.
"""
        with open(os.path.join(a_dir, f"Lab_Module_{i:02d}.md"), "w") as f:
            f.write(a_content)

        # Quiz
        q_dir = os.path.join(mod_dir, "Assessments")
        q_content = f"""### Quiz {i}: {cert} Question Bank

**Question 1:**
Which of the following is the BEST approach to solving a problem related to Domain {i} of the {cert} exam?
A) Implement a temporary fix and document it.
B) Escalate immediately to a higher tier.
C) Follow the official troubleshooting methodology by first identifying the problem.
D) Reboot the server without notifying users.

*   **Correct Answer:** C
*   **Distractor Analysis:** 
    *   *Why A is incorrect:* Temporary fixes do not resolve the root cause.
    *   *Why B is incorrect:* Escalation should only happen after basic troubleshooting is exhausted.
    *   *Why D is incorrect:* Rebooting without notification causes unscheduled downtime.
"""
        with open(os.path.join(q_dir, f"Quiz_Module_{i:02d}.md"), "w") as f:
            f.write(q_content)

    # 6. Module 16 (Final)
    mod_16_dir = os.path.join(c_path, "Module_16")
    
    r16_dir = os.path.join(mod_16_dir, "02_Reading_Guides")
    with open(os.path.join(r16_dir, "Reading_Guide_Module_16.md"), "w") as f:
        f.write(f"### Reading Guide: Final Prep\nReview all high-yield notes for the {cert} exam.")

    a16_dir = os.path.join(mod_16_dir, "03_Activities")
    with open(os.path.join(a16_dir, "Final_Exam_Submission.md"), "w") as f:
        f.write(f"### Final Exam\n**Objective:** Take the official {cert} exam at ComputerMinds and upload your score report.")

print("Phase 5 Expansion Complete. 5 new courses generated.")
