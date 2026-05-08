import os

base_dir = "/home/wrnash1/Developer/TXWES_CS/training/Online_Courses"
new_courses = {
    "CIS-2320_Hardware_Fund": ("CompTIA A+", "IT Fundamentals and Hardware", "Professor Messer A+ Videos"),
    "CIS-4330_Intro_to_AI": ("Google Cloud Digital Leader", "Intro to AI and Cloud Business Value", "Google Cloud Skills Boost"),
    "CIS-4331_Azure_Cloud": ("Microsoft Azure Fundamentals (AZ-900)", "Azure Cloud Infrastructure and Identity", "Microsoft Learn AZ-900 Path"),
    "CIS-4332_Cyber_Analyst": ("CompTIA CySA+", "Cybersecurity Analyst and Threat Hunting", "CertifyBreakfast CySA+ Series"),
    "CIS-4333_Penetration_Testing": ("CompTIA PenTest+", "Penetration Testing and Ethical Hacking", "TryHackMe PenTest+ Pathway")
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

print("Admin, ZTC, and Course Maps generated for all 5 new courses.")
