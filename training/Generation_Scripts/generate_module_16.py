import os
import glob

base_dir = "/home/wrnash1/Developer/TXWES_CS/training/Online_Courses"
courses = glob.glob(os.path.join(base_dir, "CIS-*"))

certs = {
    "CIS-3321_Network_Admin": "CompTIA Network+ (N10-008)",
    "CIS-3325_OS_Admin": "LPI Linux Essentials (010-160)",
    "CIS-3326_Windows_Server_Admin": "Microsoft Windows Server Administration",
    "CIS-4327_Database_Admin": "Google Cloud Professional Cloud Database Engineer",
    "CIS-4328_Information_Security": "CompTIA Security+ (SY0-701)",
    "CIS-4329_Google_Cloud": "Google Cloud Associate Cloud Engineer (ACE)"
}

for course in courses:
    course_name = os.path.basename(course)
    cert_name = certs.get(course_name, "Final Certification")
    
    act_dir = os.path.join(course, "Module_16", "03_Activities")
    os.makedirs(act_dir, exist_ok=True)
    
    content = f"""### Module 16 Activity: Final Certification Exam

**Objective:** 
Your final exam for this course is the official **{cert_name}** certification exam. You must schedule and take this exam at the ComputerMinds testing center.

**Instructions:**
1. Arrive at the ComputerMinds testing center at your scheduled time with two forms of valid ID.
2. Complete the {cert_name} exam.
3. Once finished, you will receive an official printout or digital copy of your score report.

**Deliverable:**
Upload a scanned copy, clear photograph, or official PDF of your final score report to this Blackboard drop-box. 

*Note: Your final grade will be calculated based on the prorated score of this exam as outlined in the Syllabus Grading Policy.*
"""
    with open(os.path.join(act_dir, "Final_Exam_Submission.md"), 'w') as f:
        f.write(content)

print("Generated Module 16 Final Exam Activities.")
