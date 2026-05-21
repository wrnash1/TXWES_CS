# Texas Wesleyan University — Computer Science & IT Department
## Instructor LMS Setup & Grading Manual (Canvas LMS): CIS-3326 Windows Server Admin

This guide provides step-by-step instructions for configuring the Canvas LMS course shell, setting up the weighted gradebook, publishing assignments, and applying rubrics to monitor and grade student performance.

---

## 1. Canvas Gradebook Setup (Weighted Categories)

Texas Wesleyan University computer science online courses use a weighted grading system. You must configure Canvas to calculate course grades using these exact weights:

| Assignment Group | Gradebook Weight | Description |
|---|---|---|
| **Practice Quizzes** | **20%** | Weekly concepts quizzes (Modules 01–15) |
| **Weekly Discussions** | **20%** | Graded discussion forums (Modules 01–15) |
| **Hands-on Labs** | **30%** | Weekly practical lab reports & screenshots (Modules 01–15) |
| **Final Certification Exam** | **30%** | Proctored vendor exam or equivalent (Module 16) |

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
    1.  *Page:* **Video Lectures & Scripts** (Copy the text of `01_Video_Script_XX.md`)
    2.  *Page:* **ZTC Reading Guide** (Copy the text of `02_Reading_Guide_XX.md`)
    3.  *Assignment:* **Hands-on Lab Activity** (Link to `03_Lab_XX.md`)
    4.  *Quiz:* **Module Practice Quiz** (Input questions from `04_Quiz_XX.md`)
    5.  *Discussion:* **Graded Discussion Forum** (Copy the prompt from `05_Discussion_XX.md`)
    6.  *Page (Module 08 only):* **Midterm Review & Study Guide** (Copy the text of `Midterm_Review_Module_08.md`)

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
*   **Gradebook Category:** *Hands-on Labs*

### C. Weekly Practice Quizzes (Modules 01–15)
*   **Points:** Set dynamically based on the number of questions.
*   **Quiz Type:** Graded Quiz
*   **Settings:**
    *   Check **Shuffle Answers**.
    *   Check **Allow Multiple Attempts** (Highest Score is kept, encouraging active recall study).
*   **Gradebook Category:** *Practice Quizzes*

### D. Final Certification Exam (Module 16)
*   **Points:** 100
*   **Submission Type:** Online -> **File Uploads** (`pdf`, `png`, `jpg`)
*   **Description:** Students must upload a scanned copy or screenshot of their official proctored score report or certificate credential.
*   **Gradebook Category:** *Final Certification Exam*

---

## 4. Grading Manual & Rubrics

Use these departmental rubrics to grade student submissions in SpeedGrader:

### Discussion Board Grading Rubric (10 Points Total)

| Criteria | Proficient (Full Marks) | Developing (Half Marks) | Novice (Low/No Marks) |
|---|---|---|---|
| **Initial Post Content** *(6 Pts)* | **5–6 Points**<br>Addresses all prompt questions. High technical accuracy, complete explanations, and uses correct course terminology. Meets word count (150–200 words). | **3–4 Points**<br>Addresses some prompt questions. Explanations lack technical depth or accuracy. Lacks formatting or falls below word count. | **0–2 Points**<br>Initial post is incomplete, off-topic, or missing. |
| **Peer Responses** *(4 Pts)* | **4 Points**<br>Responds to at least two classmates with constructive feedback (at least 50 words each). Contributes to the conversation. | **2 Points**<br>Responds to only one peer, or peer replies are superficial (e.g., "Great post, I agree!"). | **0 Points**<br>No peer responses submitted. |

### Hands-on Lab Grading Rubric (100 Points Total)

| Criteria | Points | Description |
|---|---|---|
| **Task Completion** | **50 Points** | Student completed all step-by-step commands and configurations outlined in the lab instructions. Code/configurations are correct. |
| **Deliverable Screenshots** | **30 Points** | Clear, legible screenshots are uploaded. The screenshots explicitly show successful command executions, terminal logs, or configuration verifications. |
| **Troubleshooting & Reflections** | **20 Points** | Student wrote a brief summary of what they did, documenting any errors they encountered and how they resolved them. |

### Final Exam Grade Calculation Rules

Instructors must grade the Final Certification Exam assignment in Module 16 using the following departmental rules:
*   **If the Student Passes the Certification:** Input **100% (A)** in the gradebook. Passing the exam automatically satisfies the final exam requirement.
*   **If the Student Does Not Pass the Certification:** The final exam grade is prorated based on their numeric score relative to the passing threshold. Use the following formulas based on the certification vendor:
    *   **General Certifications / Other Vendors (Cisco, AWS, Python PCAP, JS JSE, LPI Linux, Scrum, Salesforce, etc.):**
        Prorate based on the numeric score relative to the passing threshold:
        $$\text{Final Exam Grade} = \left( \frac{\text{Student Score}}{\text{Passing Score}} \right) \times 100$$
        *(If the result exceeds 100%, cap at 100%. Passing the exam automatically satisfies the final exam with 100%.)*

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
*   **Inspect Screenshots:** Verify that lab screenshots contain indicators of student work (e.g., matching command line prompts, matching directory structures, or timestamps) to ensure screenshots are not copied from other students.
*   **Require Citations:** Ensure that any code or commands troubleshoot-resolved using generative AI are properly cited by the student in their lab writeup.
