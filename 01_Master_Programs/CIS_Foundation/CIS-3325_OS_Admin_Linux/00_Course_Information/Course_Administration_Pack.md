# CIS-3325 OS Admin Linux — Course Administration Pack
## CompTIA Linux+ (XK0-005) | Texas Wesleyan University | Fall 2026

This document contains the administrative backbone for CIS-3325 OS Administration (Linux Track). Copy these items into the appropriate areas of Canvas: the Welcome Announcement into the **Announcements** section, the Video Script into the **Module 00: Course Welcome** page, and the Online Syllabus Summary into the **Syllabus** tab of the Canvas course shell.

---

## 1. Welcome Announcement

**Canvas Announcement Subject:** Welcome to CIS-3325: OS Administration (Linux Track) — CompTIA Linux+ (XK0-005)!

**Message:**

Welcome to CIS-3325 OS Administration — Linux Track! I am Professor Nash. This semester, we are going deep into the operating system that powers the internet.

Linux runs over 90% of the world's cloud servers, every major supercomputer, and the majority of production infrastructure at companies like Google, Amazon, Meta, and Verizon. If you want to work in cloud computing, cybersecurity, DevOps, or enterprise IT — Linux is not optional. It is foundational.

This course is fully aligned with the **CompTIA Linux+ (XK0-005)** certification, one of the most respected vendor-neutral Linux credentials in the industry. By Module 16, you will sit for the official certification exam.

Here is what you need to know to start:

1. **This is a 100% online, asynchronous course.** There are no scheduled live sessions. You set your own weekly schedule, but all assignments are due Sunday at 11:59 PM CST each week.
2. **This course is Zero Textbook Cost (ZTC).** You will not purchase anything. All reading materials, video scripts, and study guides are inside Canvas or linked to free OER resources.
3. **You need a Linux environment.** Before Module 01 is due, install VirtualBox and Ubuntu Server 24.04 LTS on your machine. The instructions are in the STUDENT_GUIDE.md file in the Course Information folder and in Module 01. WSL2 is an acceptable alternative for most modules.
4. **Assignments open Monday and are due Sunday.** This gives you a full week per module. Do not fall behind — Linux skills are cumulative.

Start by reviewing the **Syllabus** in the Course Information section and then proceed to **Module 01: Linux Installation & VM Setup**. See you in the terminal.

— Professor Nash

---

## 2. Instructor Welcome Video Script

**Title:** Welcome to CIS-3325 OS Administration (Linux Track)
**Canvas Location:** Module 00 — Course Welcome / Course Information page
**Estimated Duration:** 3 minutes
**Visual:** Instructor on camera, optionally with a terminal window visible in the background.

---

**[0:00 – 0:30] — Hook**

"Welcome to Operating System Administration, Linux Track. I'm Professor Nash. Before we get into the course overview, I want you to open a terminal — any terminal — and type this command: `uptime`. On Windows, open WSL and type it. On Mac, open Terminal and type it. That one command tells you how long your system has been running, how many users are logged in, and the load average over the last 1, 5, and 15 minutes. You just read system health data. That is what Linux administrators do, and that is what this course is about."

**[0:30 – 1:15] — Why Linux Matters**

"Linux is not a niche skill. It runs the servers behind every website you visit, every cloud application you use, and every container your code runs in. When you deploy an application to AWS or Google Cloud, it is running on Linux. When Verizon manages network infrastructure, it is running on Linux. If you want to work in cloud, DevOps, cybersecurity, or enterprise networking — learning Linux is not optional. It is the price of admission.

This course is fully aligned with the CompTIA Linux+ certification, exam code XK0-005. That certification validates that you can administer real Linux systems. By the end of this course, you will sit for that exam."

**[1:15 – 2:00] — How the Course Works**

"This is a fully asynchronous online course. Every week you have one module, and every module follows the same structure: a video script page to read, a reading guide pointing you to free OER resources, a hands-on lab you complete in your own Linux VM, a practice quiz, and a graded discussion board. All assignments are due Sunday at 11:59 PM CST.

There is no textbook to buy. Everything is free. The primary textbook is *The Linux Command Line* by William Shotts — it is freely available online and it is excellent. The primary video resource is the LearnLinuxTV Linux Essentials playlist on YouTube — also free. Check the ZTC Reading Materials file in the Course Information folder for all links."

**[2:00 – 2:45] — The Lab Environment**

"Before Module 01 is due, you need a Linux environment. I recommend installing VirtualBox on your laptop and creating an Ubuntu Server 24.04 LTS virtual machine. The instructions are in the Student Guide and in Module 01. If you are on Windows 10 or 11, Windows Subsystem for Linux — WSL2 — also works for most modules.

The labs in this course require root access. That is another reason we use a VM — you can break things and rebuild them safely. Breaking things is actually part of the curriculum. Deliberately misconfigure permissions, delete the wrong file, and fix it. That is how Linux skills get built."

**[2:45 – 3:00] — Closing**

"Review the syllabus, get your Linux VM running, and meet me in Module 01. The terminal is waiting. Let's get started."

---

## 3. Updated Online Syllabus Summary

**Canvas Location:** Paste into the Canvas **Syllabus** tab description area (above the assignment calendar).

---

**Course:** CIS-3325 — OS Administration (Linux Track)
**Subtitle:** CompTIA Linux+ (XK0-005) Aligned
**Instructor:** Professor Nash | nash@txwes.edu
**Format:** 100% Online Asynchronous | Canvas LMS | Fall 2026
**Credit Hours:** 3

---

**Course Description:**
This course provides hands-on training in Linux system administration, aligned with the CompTIA Linux+ (XK0-005) certification exam blueprint. Topics include Linux installation and VM setup, filesystem navigation, text processing, Vim, process management, storage, user administration, file permissions and ACLs, Bash scripting, package management, networking, systemd, LVM and RAID, SSH hardening, Ansible automation, and SELinux/AppArmor security. The course culminates in the official CompTIA Linux+ certification exam.

---

**Course Learning Outcomes:**
By the end of this course, students will be able to:
1. Configure and administer core Linux system components aligned with CompTIA Linux+ (XK0-005) domains.
2. Execute and verify production-level terminal commands including service management, storage provisioning, and network configuration.
3. Analyze Linux system failures and security vulnerabilities and implement mitigation strategies.
4. Demonstrate competency aligned with the CompTIA Linux+ (XK0-005) certification exam blueprint.

---

**Required Materials — Zero Textbook Cost (ZTC):**
No textbook purchase required. All materials are free.
*   *The Linux Command Line* by William Shotts — [linuxcommand.org/tlcl.php](https://linuxcommand.org/tlcl.php)
*   Linux Essentials Course by LearnLinuxTV — [YouTube Playlist](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78)
*   CompTIA Linux+ XK0-005 Exam Objectives (free PDF) — [comptia.org/certifications/linux](https://www.comptia.org/certifications/linux)

**Hardware/Software:**
Computer capable of running a Linux VM (VirtualBox — free) or WSL2 (Windows 10/11 built-in). Minimum 8 GB RAM recommended for VM work. High-speed internet required.

---

**Grading Breakdown:**

| Component | Weight |
|---|---|
| Weekly Practice Quizzes (Modules 01–15) | 20% |
| Weekly Discussion Boards (Modules 01–15) | 20% |
| Hands-on Lab Assignments (Modules 01–15) | 30% |
| Final Certification Exam — CompTIA Linux+ XK0-005 (Module 16) | 30% |

**Grading Scale:** A=90–100 | B=80–89 | C=70–79 | D=60–69 | F=<60

---

**Module Schedule:**

| Module | Topic |
|:---|:---|
| Module 01 | Linux Installation & VM Setup |
| Module 02 | Filesystem Navigation & File Management |
| Module 03 | Text Processing (grep, awk, sed) |
| Module 04 | Vim & Text Editors |
| Module 05 | Process Management |
| Module 06 | Storage & Filesystems |
| Module 07 | User & Group Administration |
| Module 08 | File Permissions & ACLs |
| Module 09 | Shell Scripting (Bash) |
| Module 10 | Package Management (apt/dnf) |
| Module 11 | Networking (ip, nmcli, SSH) |
| Module 12 | Systemd & Services |
| Module 13 | LVM & RAID Storage |
| Module 14 | SSH Hardening & Ansible |
| Module 15 | SELinux/AppArmor & Security |
| Module 16 | Final Exam Prep & CompTIA Linux+ (XK0-005) Certification |

---

**Key Policies:**
*   **Late Work:** Accepted up to 72 hours past deadline with 10% per-day deduction. No credit after 72 hours without documented extenuating circumstances.
*   **Attendance:** Submit at least one assignment per week to be counted present. Two consecutive weeks without submission triggers an Academic Early Alert.
*   **Academic Integrity:** AI tools permitted for brainstorming and debugging. All final submissions must represent your own cognitive work. Directly submitted AI output without attribution is academic dishonesty.
*   **Final Exam:** CompTIA Linux+ (XK0-005) proctored exam (720/900 to pass). Submit official score report to Canvas Module 16. Passing = 100% final exam grade. Not passing = prorated score: (your score / 720) x 100.
*   **Syllabus Changes:** Instructor reserves the right to modify this syllabus at any time. All changes communicated via Canvas Announcements.
