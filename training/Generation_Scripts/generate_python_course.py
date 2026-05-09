import os

base_dir = "/home/wrnash1/Developer/TXWES_CS/training/Online_Courses"
course_dir = "CIS-1310_Intro_to_Python"
cert = "PCAP (Certified Associate in Python Programming)"
desc = "Introduction to Python Programming, covering data types, control flow, functions, modules, and Object-Oriented Programming (OOP)."
oer = "Python Institute Free Training (edube.org)"

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
2. A computer capable of running Google Colab in a web browser or a local Python IDLE installation.

## Grading Policy
*   Coding Quizzes: 30%
*   Hands-on Programming Labs: 40%
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
*   **Primary Source:** [{oer}](https://edube.org/)
*   **Secondary Source:** [Official Python 3 Documentation](https://docs.python.org/3/tutorial/index.html)

> **Instructor Note:** The Python Institute provides free, interactive web-based training. Use the links above to practice your code in real-time.
"""
with open(os.path.join(c_path, "ZTC_OER_Reading_Materials.md"), "w") as f:
    f.write(ztc_content)

# 4. Course Map
map_content = f"""# Online Course Map: {course_dir}
**Target Certification:** {cert}

## 16-Week Breakdown
*   **Modules 1-4:** Basics, Variables, Data Types, and Operators
*   **Modules 5-8:** Control Flow (If/Else, While/For Loops)
*   **Modules 9-12:** Data Collections (Lists, Tuples, Dictionaries) and Functions
*   **Modules 13-15:** Modules, Exceptions, and Object-Oriented Programming (OOP)
*   **Module 16:** Final {cert} Certification Exam
"""
with open(os.path.join(info_dir, "Online_Course_Map.md"), "w") as f:
    f.write(map_content)

# 5. Content Generation Modules 1-15
for i in range(1, 16):
    mod_dir = os.path.join(c_path, f"Module_{i:02d}")
    
    # Video
    v_dir = os.path.join(mod_dir, "01_Video_Scripts")
    v_content = f"""### Video Script: Python PCAP Domain {i}

**Estimated Duration:** 7 minutes
**Visual:** Screencast of an IDE (like VS Code or Google Colab) showing Python syntax being written in real-time.
**[Alt-text: A dark-themed code editor showing syntax-highlighted Python code with comments explaining the logic.]**

**Audio:** "Welcome to Module {i}. Today we are going to write some actual Python code focusing on Domain {i} of the {cert} exam. Programming requires practice, so follow along with me on your screen and type out the code exactly as I do."
"""
    with open(os.path.join(v_dir, f"Video_Script_Module_{i:02d}.md"), "w") as f:
        f.write(v_content)

    # Reading
    r_dir = os.path.join(mod_dir, "02_Reading_Guides")
    r_content = f"""### Reading Guide: Python Module {i}

**Zero Textbook Cost (ZTC) Resource Link:**
Refer to your `ZTC_OER_Reading_Materials.md` for direct links to the official Python 3 documentation.

**High-Yield Summaries:**
*   **Core Concept:** This module focuses on understanding how Python processes the logic for Domain {i}.
*   **Exam Tip:** The PCAP exam loves to test your ability to spot syntax errors, specifically missing colons or incorrect indentation.
"""
    with open(os.path.join(r_dir, f"Reading_Guide_Module_{i:02d}.md"), "w") as f:
        f.write(r_content)

    # Lab
    a_dir = os.path.join(mod_dir, "03_Activities")
    a_content = f"""### Lab {i}: Applied Python Programming

**Objective:** Write a Python script applying the concepts from Module {i}.
**Format:** Google Colab or Local IDE.

**Instructions:**
1. Open a new Python environment.
2. Write a script that solves the specific challenge presented in this week's lecture (e.g., iterating through a list, handling a ValueError exception).
3. Ensure your code is thoroughly commented and adheres to PEP 8 style guidelines.
4. Run your script to verify the output is correct.

**Deliverable:**
Upload a `.py` file containing your source code to the Blackboard drop-box.
"""
    with open(os.path.join(a_dir, f"Lab_Module_{i:02d}.md"), "w") as f:
        f.write(a_content)

    # Quiz
    q_dir = os.path.join(mod_dir, "Assessments")
    q_content = f"""### Quiz {i}: Python Syntax Question Bank

**Question 1:**
What will be the output of the code snippet provided in the lecture regarding Domain {i}?
A) A syntax error.
B) The expected value.
C) A TypeError exception.
D) None of the above.

*   **Correct Answer:** B
*   **Distractor Analysis:** 
    *   *Why A is incorrect:* The code is properly indented and has correct syntax.
    *   *Why C is incorrect:* Python handles the dynamic typing correctly in this specific example.
"""
    with open(os.path.join(q_dir, f"Quiz_Module_{i:02d}.md"), "w") as f:
        f.write(q_content)

# 6. Module 16 (Final)
mod_16_dir = os.path.join(c_path, "Module_16")

r16_dir = os.path.join(mod_16_dir, "02_Reading_Guides")
with open(os.path.join(r16_dir, "Reading_Guide_Module_16.md"), "w") as f:
    f.write(f"### Reading Guide: Final Prep\nReview all Python syntax and OOP concepts for the {cert} exam.")

a16_dir = os.path.join(mod_16_dir, "03_Activities")
with open(os.path.join(a16_dir, "Final_Exam_Submission.md"), "w") as f:
    f.write(f"### Final Exam\n**Objective:** Take the official {cert} exam at ComputerMinds and upload your score report to the drop-box.")

print("Python course generation complete.")
