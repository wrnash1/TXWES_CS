# Texas Wesleyan University (TXWES) Computer Science Department
## Student Study Guide: CIS-3325 OS Admin Linux (CompTIA Linux+ XK0-005)

Welcome to the Texas Wesleyan Computer Science department! This comprehensive orientation and study guide is designed to help you set up your Linux lab environment, learn how to document and submit your lab assignments, and study effectively using our Zero Textbook Cost (ZTC) Open Educational Resources (OER) curriculum model.

---

## 1. Lab Environment Setup

All hands-on labs in this course are designed to be run directly in a Linux environment on your own computer. This provides flexibility and mirrors real-world Linux system administration practices.

### Option A: Virtual Machine (Recommended)
Running a Linux virtual machine (VM) gives you a full, isolated Linux environment with root access — exactly what you need for system administration labs.

1. **Install VirtualBox (Free):**
   * Download Oracle VirtualBox from [virtualbox.org](https://www.virtualbox.org/).
   * Install it on your Windows, macOS, or Linux host machine.

2. **Download a Linux ISO:**
   * **Ubuntu Server 24.04 LTS** (recommended): [ubuntu.com/download/server](https://ubuntu.com/download/server) — Free download.
   * **Fedora Server 40** (for dnf/SELinux labs): [fedoraproject.org](https://fedoraproject.org/server/) — Free download.

3. **Create a New VM in VirtualBox:**
   * Allocate at least **2 GB RAM** and **20 GB disk**.
   * Mount the ISO as a virtual optical drive and complete the Linux install process.
   * Create a non-root user account during setup and note your username and password.

4. **Install Guest Additions (Optional but Recommended):**
   * Enables shared clipboard and better screen resolution.
   * In VirtualBox menu: **Devices** -> **Insert Guest Additions CD image**.

### Option B: Windows Subsystem for Linux (WSL2)
If you are on Windows 10/11 and prefer not to use a VM, WSL2 is a fast alternative for most command-line labs.

1. Open **PowerShell as Administrator** and run:
   ```
   wsl --install
   ```
2. Restart your computer and complete the Ubuntu setup (create a username and password).
3. Launch WSL from the Start menu or by typing `wsl` in any terminal.

**Note:** WSL2 is suitable for most modules but has limitations for storage (LVM/RAID), systemd, SELinux, and networking labs. If you encounter issues with those specific modules, use a full VM.

### Required Tools (Pre-installed on Most Linux Distros)
The following command-line tools are used throughout the course. Verify they are installed on your system:

| Tool | Purpose | Install Command (Ubuntu/Debian) |
|:---|:---|:---|
| `vim` | Text editor | `sudo apt install vim` |
| `git` | Version control | `sudo apt install git` |
| `net-tools` | Legacy networking (`ifconfig`) | `sudo apt install net-tools` |
| `openssh-server` | SSH server for SSH labs | `sudo apt install openssh-server` |
| `ansible` | Automation (Module 14) | `sudo apt install ansible` |
| `apparmor-utils` | AppArmor tools (Module 15) | `sudo apt install apparmor-utils` |

---

## 2. Lab Submission Workflow

Every course module (Modules 01 to 15) contains a practical lab activity. When you complete a lab, you will document your progress and upload the deliverables directly to the Canvas LMS.

### How to Submit
1. **Execute the Lab:** Work through all steps in the `03_Lab_Module_XX.md` instructions inside your Linux VM or WSL2 environment.
2. **Capture Screenshots:** Take screenshots of your terminal showing the key commands and their outputs. Each screenshot should display:
   * Your command prompt (including username and hostname)
   * The full command you ran
   * The complete output or result
3. **Write a Reflection:** In a document (PDF or DOCX), write 2-3 sentences per major task describing what you did and any issues you resolved.
4. **Upload to Canvas:** Navigate to your Canvas LMS course shell, locate the corresponding Module assignment under **Hands-on Labs**, and upload your screenshots and reflection document.

### Acceptable File Formats
*   **Screenshots:** `.png` or `.jpg`
*   **Written reports:** `.pdf` or `.docx`
*   Combine all items into a single PDF when possible for cleaner submission.

---

## 3. The Zero Textbook Cost (ZTC) & OER Strategy

To save you money and ensure your training remains aligned with the latest Linux administration standards, we use a **Zero Textbook Cost** model. All required course materials are provided free through open-educational resources and within the Canvas course shell.

### Your Three Primary Free Resources
1. **[The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php)** — The definitive free Linux textbook. Readable online or downloadable as a PDF. Referenced in every module's reading guide.
2. **[Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78)** — Professional video lectures aligned to Linux administration fundamentals.
3. **[CompTIA Linux+ Certification Page](https://www.comptia.org/certifications/linux)** — Download the official XK0-005 exam objectives PDF (free). This is your master blueprint for what the certification tests.

---

## 4. Active Learning Study Strategies (Linux+ Command-Line Focus)

Linux administration is a **hands-on skill**. Reading about commands without typing them is ineffective. Apply these strategies:

*   **Type Every Command Manually:** Do not copy-paste from the reading guides. Typing commands builds muscle memory and forces you to understand the syntax. When you make a typo, read the error message carefully — it almost always tells you exactly what went wrong.
*   **Use `man` Pages as Your First Reference:** Before searching online, run `man <command>` (e.g., `man chmod`, `man grep`, `man systemctl`). Reading the manual page for a command you just used cements understanding of its flags and behavior.
*   **Break Things on Purpose:** After completing a lab correctly, try intentionally misconfiguring something (wrong permissions, wrong service name) to see what error messages look like. Understanding failure modes is essential for Linux administration and the XK0-005 performance-based questions.
*   **Build a Personal Cheat Sheet:** After each module, write down the 5-10 most important commands and their flags in your own words. Review this sheet before each quiz. By Module 16, you'll have a comprehensive personal study guide.
*   **Practice Active Recall on Quizzes:** When reviewing quiz questions, analyze the *distractor explanations* — understand exactly why each wrong answer is wrong. The CompTIA Linux+ exam uses similar distractor patterns.
*   **Replicate the Lab from Memory:** After completing a lab the first time with the guide open, close the guide and try to replicate the key tasks from memory. If you can do it without looking, you own the knowledge.

---

## 5. 27-Course Curriculum & Certification Directory

Below is the study roadmap for the Computer Science and IT curriculum. This course is part of the systems administration track.

| Course Code & Name | Target Certification | Key Study Strategy | Primary Free OER Resource |
| :--- | :--- | :--- | :--- |
| **CIS-3325_OS_Admin_Linux: OS Administration (Linux)** | CompTIA Linux+ (XK0-005) | Type every command manually. Use `man` pages first. Build a personal command cheat sheet each module. | [The Linux Command Line — Shotts](https://linuxcommand.org/tlcl.php) |

---

## 6. Final Exam Certification Policy (Module 16)

The culmination of this course (Module 16) is the official **CompTIA Linux+ (XK0-005)** certification exam. Rather than a traditional written final exam, you will complete the official vendor-proctored certification exam.

### Exam Details
*   **Exam Name:** CompTIA Linux+ (XK0-005)
*   **Exam Format:** 90 questions (multiple choice + performance-based) over 90 minutes
*   **Passing Score:** **720 out of 900**
*   **Testing Vendor:** CompTIA / PearsonVUE
*   **Exam Cost:** Covered by student as part of certification preparation. Check with the TXWES financial aid office regarding potential voucher assistance programs.

### How to Schedule
1. Create a free account at [comptia.org](https://www.comptia.org/).
2. Purchase an exam voucher or use a CertMaster bundle code if provided by the department.
3. Schedule your exam at an authorized PearsonVUE testing center or select the **online proctored** option from home.

### Submitting Your Score Report to Canvas
1. After completing your exam, CompTIA will display your score report immediately.
2. Download or screenshot your **official score report** showing: your full name, exam name (CompTIA Linux+ XK0-005), your numeric score, the passing score (720), and the exam date.
3. Upload the score report to the **Module 16 Final Certification Exam** assignment in Canvas.

### Grade Calculation
*   **Score >= 720 (Pass):** You receive **100%** for the Final Exam component of your grade. Congratulations — you are CompTIA Linux+ certified!
*   **Score < 720 (Did Not Pass):** Your Final Exam grade is prorated: `(Your Score / 720) x 100`. For example, a score of 650 earns `(650/720) x 100 = 90.3%` for the final exam component.
