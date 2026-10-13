# Texas Wesleyan University — Computer Science & IT Department
## Instructor LMS Setup & Grading Manual (Canvas LMS): CIS-3325 OS Admin Linux (CompTIA Linux+ XK0-005)

This guide provides step-by-step instructions for configuring the Canvas LMS course shell, setting up the weighted gradebook, publishing assignments, and applying rubrics to monitor and grade student performance.

---

## 1. Canvas Gradebook Setup (Weighted Categories)

Texas Wesleyan University computer science online courses use a weighted grading system. You must configure Canvas to calculate course grades using these exact weights:

| Assignment Group | Gradebook Weight | Description |
|---|---|---|
| **Practice Quizzes** | **20%** | Weekly concepts quizzes (Modules 01–15) aligned to CompTIA Linux+ XK0-005 exam domains |
| **Weekly Discussions** | **20%** | Graded discussion forums (Modules 01–15) |
| **Hands-on Labs** | **30%** | Weekly practical lab reports & screenshots (Modules 01–15) executed in a Linux VM or WSL2 environment |
| **Final Certification Exam** | **30%** | CompTIA Linux+ (XK0-005) proctored exam or equivalent (Module 16) |

### Steps to Configure Weights in Canvas:
1. In your Canvas course navigation menu, click **Assignments**.
2. Click the **+ Group** button in the top right to create the four groups listed above.
3. Once all groups are created, click the **Settings (three vertical dots)** icon next to the "+ Assignment" button.
4. Select **Assignment Groups Weight**.
5. Check the box for **Weight final grade based on assignment groups**.
6. Input the respective weights (20%, 20%, 30%, 30%) for each group and click **Save**.

---

## 2. Canvas Course Shell Structure & Content Deployment

When importing materials from this curriculum package into Canvas, organize them using the **Modules** tool.

### Recommended Canvas Module Layout:
Create 16 modules in the Canvas Modules page. For each module, add the following items:
*   **Module XX: [Topic Name]**
    1.  *Page:* **Video Lectures & Scripts** (Copy the text of `01_Video_Script_Module_XX.md`)
    2.  *Page:* **ZTC Reading Guide** (Copy the text of `02_Reading_Guide_Module_XX.md`)
    3.  *Assignment:* **Hands-on Lab Activity** (Link to `03_Lab_Module_XX.md`)
    4.  *Quiz:* **Module Practice Quiz** (Input questions from `04_Quiz_Module_XX.md`)
    5.  *Discussion:* **Graded Discussion Forum** (Copy the prompt from `05_Discussion_Module_XX.md`)

### Module Topic Reference for Canvas Module Titles:
| Module | Canvas Module Title |
|---|---|
| Module 01 | Module 01: Linux Installation & VM Setup |
| Module 02 | Module 02: Filesystem Navigation & File Management |
| Module 03 | Module 03: Text Processing (grep, awk, sed) |
| Module 04 | Module 04: Vim & Text Editors |
| Module 05 | Module 05: Process Management |
| Module 06 | Module 06: Storage & Filesystems |
| Module 07 | Module 07: User & Group Administration |
| Module 08 | Module 08: File Permissions & ACLs |
| Module 09 | Module 09: Shell Scripting (Bash) |
| Module 10 | Module 10: Package Management (apt/dnf) |
| Module 11 | Module 11: Networking (ip, nmcli, SSH) |
| Module 12 | Module 12: Systemd & Services |
| Module 13 | Module 13: LVM & RAID Storage |
| Module 14 | Module 14: SSH Hardening & Ansible |
| Module 15 | Module 15: SELinux/AppArmor & Security |
| Module 16 | Module 16: Final Exam Prep & CompTIA Linux+ Certification |

---

## 3. Assignment Setup Settings

To ensure proper gradebook monitoring, configure the submission settings in Canvas as follows:

### A. Weekly Graded Discussions (Modules 01–15)
*   **Points:** 10
*   **Submission Type:** Graded Discussion
*   **Settings:**
    *   Check **Allow threaded replies**.
    *   Check **Users must post before seeing replies** (prevents copy-cat posting).
*   **Gradebook Category:** *Weekly Discussions*

### B. Weekly Hands-on Labs (Modules 01–15)
*   **Points:** 100
*   **Submission Type:** Online -> **File Uploads**
*   **Allowed File Extensions:** `pdf`, `docx`, `png`, `jpg` (restricting formats ensures easily readable screenshots/reports in SpeedGrader).
*   **Description note:** Students should submit screenshots of their Linux terminal showing command execution results, along with a brief written reflection. Screenshots should display the full terminal window including the command prompt, the command entered, and the resulting output.
*   **Gradebook Category:** *Hands-on Labs*

### C. Weekly Practice Quizzes (Modules 01–15)
*   **Points:** Set dynamically based on the number of questions.
*   **Quiz Type:** Graded Quiz
*   **Settings:**
    *   Check **Shuffle Answers**.
    *   Check **Allow Multiple Attempts** (Highest Score is kept, encouraging active recall study).
    *   Set **Time Limit** to 30 minutes per quiz.
*   **Gradebook Category:** *Practice Quizzes*

### D. Final Certification Exam (Module 16)
*   **Points:** 100
*   **Submission Type:** Online -> **File Uploads** (`pdf`, `png`, `jpg`)
*   **Description:** Students must upload a scanned copy or screenshot of their official CompTIA score report showing their name, exam name (CompTIA Linux+ XK0-005), score, and test date. The CompTIA passing score is 720 out of 900.
*   **Gradebook Category:** *Final Certification Exam*

---

## 4. Grading Manual & Rubrics

Use these departmental rubrics to grade student submissions in SpeedGrader:

### Discussion Board Grading Rubric (10 Points Total)

| Criteria | Proficient (Full Marks) | Developing (Half Marks) | Novice (Low/No Marks) |
|---|---|---|---|
| **Initial Post Content** *(6 Pts)* | **5–6 Points**<br>Addresses all prompt questions. High technical accuracy, complete explanations, and uses correct Linux command-line terminology. Meets word count (150–200 words). | **3–4 Points**<br>Addresses some prompt questions. Explanations lack technical depth or accuracy. Lacks formatting or falls below word count. | **0–2 Points**<br>Initial post is incomplete, off-topic, or missing. |
| **Peer Responses** *(4 Pts)* | **4 Points**<br>Responds to at least two classmates with constructive feedback (at least 50 words each). Contributes meaningfully to the conversation with technical additions or corrections. | **2 Points**<br>Responds to only one peer, or peer replies are superficial (e.g., "Great post, I agree!"). | **0 Points**<br>No peer responses submitted. |

### Hands-on Lab Grading Rubric (100 Points Total)

| Criteria | Points | Description |
|---|---|---|
| **Task Completion** | **50 Points** | Student completed all step-by-step commands and configurations outlined in the lab instructions. Commands are syntactically correct and the outputs confirm successful execution. |
| **Deliverable Screenshots** | **30 Points** | Clear, legible terminal screenshots are uploaded. Screenshots explicitly show the command prompt, command entered, and resulting output. File permissions, process lists, or configuration values match expected results. |
| **Troubleshooting & Reflections** | **20 Points** | Student wrote a brief summary of what they did, documenting any errors encountered and how they were resolved. Demonstrates understanding of *why* the commands work, not just *that* they worked. |

### Final Exam Grade Calculation Rules

Instructors must grade the Final Certification Exam assignment in Module 16 using the following departmental rules:
*   **If the Student Passes the CompTIA Linux+ Exam (Score >= 720/900):** Input **100% (A)** in the gradebook. Passing the exam automatically satisfies the final exam requirement.
*   **If the Student Does Not Pass the Certification:** The final exam grade is prorated based on their numeric score relative to the passing threshold. Use the following formula:
    *   **CompTIA Linux+ (XK0-005):** Passing score = 720 on a 100–900 scale.
        $$\text{Final Exam Grade} = \left( \frac{\text{Student Score}}{720} \right) \times 100$$
        *(If the result exceeds 100%, cap at 100%. Scores below 100 points on the CompTIA scale are treated as 0%.)*

---

## 5. Monitoring Progress & Enforcing Course Policies

As an asynchronous instructor, you must actively monitor student progress in the Canvas Gradebook and enforce the following policies:

### Attendance Tracking
*   Every Monday morning, review the previous week's logs in the Canvas Gradebook.
*   If a student did not submit at least one item (discussion post, quiz, or lab) during the week, mark them **Absent** in your departmental attendance database.
*   If a student is absent for two consecutive weeks, send a warning email and submit an **Academic Early Alert** to the Registrar.

### Late Work Policy (Automatic Grade Book Enforcement)
*   You can automate late grading in Canvas by going to **Grades** -> **Settings (Gear icon)** -> **Late Submission Policy**.
*   Select **Apply deduction for late submissions**.
*   Set **Late submission deduction percentage** to **10%** and **Deduction interval** to **Day**.
*   Set **Lowest possible grade** to **0%**.
*   Select **Apply grade for missing submissions** and set it to **0%**.

### Academic Integrity & AI Auditing Tips
*   **Cross-Check Discussions:** If a student's discussion post uses overly formal academic vocabulary that differs significantly from their other writing, paste a segment into an AI detection tool or search for key phrasing.
*   **Inspect Screenshots:** Verify that lab screenshots contain indicators of authentic student work — matching username in the terminal prompt, matching directory structures or hostname, and timestamps consistent with the submission date. Screenshots must show a real Linux terminal, not a mockup or copied image.
*   **Require Citations:** Ensure that any commands or configurations troubleshoot-resolved using generative AI are properly cited by the student in their lab writeup (e.g., "I used ChatGPT to understand the syntax of `iptables -A INPUT -p tcp --dport 22 -j ACCEPT`").
*   **Verify Unique Environments:** Students working in VMs should have distinct hostnames. If two students submit screenshots with identical hostnames, IP addresses, or filesystem contents, investigate for potential collaboration or shared work.
