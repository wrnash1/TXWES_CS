import os

base_dir = "/home/wrnash1/Developer/TXWES_CS/training/Online_Courses"
new_courses = {
    "CIS-2320_Hardware_Fund": "CompTIA A+",
    "CIS-4330_Intro_to_AI": "Google Cloud Digital Leader",
    "CIS-4331_Azure_Cloud": "Microsoft Azure Fundamentals (AZ-900)",
    "CIS-4332_Cyber_Analyst": "CompTIA CySA+",
    "CIS-4333_Penetration_Testing": "CompTIA PenTest+"
}

for course_dir, cert in new_courses.items():
    c_path = os.path.join(base_dir, course_dir)
    
    for i in range(1, 16): # Modules 1 to 15
        mod_dir = os.path.join(c_path, f"Module_{i:02d}")
        
        # 1. Video Script
        v_dir = os.path.join(mod_dir, "01_Video_Scripts")
        v_content = f"""### Video Script: {cert} Domain {i} Concepts

**Estimated Duration:** 7 minutes
**Visual:** Instructor on camera transitioning to a whiteboard diagram.
**[Alt-text: A flowchart diagram showing the core IT concepts related to {cert} Domain {i}, with arrows indicating the workflow.]**

**Audio:** "Welcome to Module {i}. In this module, we are diving into the core objectives for {cert}. It is critical that you understand these foundational concepts before we jump into the lab environment. Remember, the exam will test not just your ability to define these terms, but your ability to troubleshoot them."
"""
        with open(os.path.join(v_dir, f"Video_Script_Module_{i:02d}.md"), "w") as f:
            f.write(v_content)

        # 2. Reading Guide
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

        # 3. Lab Activity
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

        # 4. Quiz
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

    # Handle Module 16 (Final Exam)
    mod_16_dir = os.path.join(c_path, "Module_16")
    
    r16_dir = os.path.join(mod_16_dir, "02_Reading_Guides")
    with open(os.path.join(r16_dir, "Reading_Guide_Module_16.md"), "w") as f:
        f.write(f"### Reading Guide: Final Prep\nReview all high-yield notes for the {cert} exam.")

    a16_dir = os.path.join(mod_16_dir, "03_Activities")
    with open(os.path.join(a16_dir, "Final_Exam_Submission.md"), "w") as f:
        f.write(f"### Final Exam\n**Objective:** Take the official {cert} exam at ComputerMinds and upload your score report.")

print("Content generation for all 16 modules across 5 new courses complete.")
