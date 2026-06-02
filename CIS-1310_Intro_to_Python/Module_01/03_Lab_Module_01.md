# Lab Activity: Module 01 — Python Basics & Local Environment

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Estimated Time:** 90–120 minutes (includes VirtualBox setup)

---

## Overview

This lab sets up the virtual machine environment you will use for every lab in this course. You will install VirtualBox, create an Ubuntu Linux VM, verify your Python 3 installation, explore the REPL, and write and run your first Python scripts. Every subsequent CIS-1310 lab assumes this environment is fully set up — do not skip any steps.

---

## Prerequisites

- A computer running Windows 10/11, macOS 12+, or Linux
- At least 8 GB of total RAM (2–4 GB will be allocated to the VM)
- At least 25 GB of free disk space
- Broadband internet connection (you will download approximately 2 GB of files)

---

## Part 1 — Install VirtualBox

VirtualBox is free, open-source virtualization software from Oracle. It runs a complete second operating system — the "guest" — inside a window on your real computer — the "host." The guest is fully isolated. Anything you install or break inside the VM has no effect on your real machine.

### Step 1.1 — Download VirtualBox

1. Open your browser and go to [virtualbox.org](https://www.virtualbox.org/).
2. Click **Downloads**.
3. Under "VirtualBox platform packages," download the installer for your host OS:
   - **Windows:** Click "Windows hosts"
   - **macOS (Intel):** Click "macOS / Intel hosts"
   - **macOS (Apple Silicon M1/M2/M3):** Click "macOS / ARM hosts"
   - **Linux:** Select your distribution
4. Save the installer to your Downloads folder.

### Step 1.2 — Install VirtualBox

**Windows:**

1. Run the downloaded `.exe` installer.
2. Accept all defaults — click **Next** through each screen.
3. When prompted about network interfaces, click **Yes** (VirtualBox needs to create a virtual network adapter).
4. Click **Install** and wait for completion. Click **Finish**.

**macOS:**

1. Open the downloaded `.dmg`, double-click `VirtualBox.pkg`.
2. Click **Continue** through each screen, then **Install**.
3. If macOS asks to allow a system extension, go to **System Settings → Privacy & Security → Allow** (Oracle entry).

**Expected result:** VirtualBox Manager opens showing "Welcome to VirtualBox!" with no VMs listed.

> **SCREENSHOT 1 REQUIRED:** Take a screenshot of VirtualBox Manager open. Save as `lab01_screenshot_01_virtualbox.png`.

---

## Part 2 — Download Ubuntu 22.04 LTS

Ubuntu is one of the most popular Linux distributions in the world. Ubuntu 22.04 LTS (Long-Term Support) is the standard for development servers, data science environments, and cloud infrastructure. Working in Ubuntu prepares you for the real-world environments you will encounter as an IT professional.

### Step 2.1 — Download the ISO

1. Go to [ubuntu.com/download/desktop](https://ubuntu.com/download/desktop).
2. Click **Download 22.04.X LTS** — the LTS version, not the latest short-term release.
3. Save the `.iso` file to Downloads. It is approximately **1.4 GB**.

> You can continue building the VM in Part 3 while the download runs in the background.

---

## Part 3 — Create the Ubuntu Virtual Machine

### Step 3.1 — Create a New VM

1. In VirtualBox Manager, click **New** (the blue star icon).
2. Enter the following settings:

   | Setting | Value |
   |---|---|
   | Name | `Ubuntu-CIS1310` |
   | Type | Linux |
   | Version | Ubuntu (64-bit) |

3. Click **Next**.

### Step 3.2 — Configure Memory

1. Set **Base Memory** to `2048 MB` minimum — set `4096 MB` if your computer has 16 GB of RAM or more.
   > Never allocate more than half your host computer's total RAM to a VM.
2. Set **Processors** to `2`. Click **Next**.

### Step 3.3 — Create a Virtual Hard Disk

1. Select **Create a Virtual Hard Disk Now**.
2. Set disk size to **`25 GB`**.
3. Leave type as **VDI** and storage as **Dynamically allocated**.
   > Dynamically allocated means the file on your real computer only grows as Ubuntu uses space.
4. Click **Next** → **Finish**.

**Expected result:** `Ubuntu-CIS1310` appears in VirtualBox Manager with status "Powered Off."

---

## Part 4 — Install Ubuntu

### Step 4.1 — Attach the ISO and Boot

1. Wait for the Ubuntu `.iso` download to finish.
2. In VirtualBox, select `Ubuntu-CIS1310` → click **Settings** → **Storage**.
3. Click the **Empty** disc icon under "Controller: IDE."
4. In the right panel, click the disc icon next to "Optical Drive" → **Choose a Disk File…**
5. Select the Ubuntu `.iso` from Downloads. Click **OK**.
6. Click the green **Start** button to launch the VM.

### Step 4.2 — Run the Ubuntu Installer

1. When the installer loads, select **English** → **Install Ubuntu**.
2. Choose your keyboard layout → **Continue**.
3. Select **Normal installation** → **Continue**.
4. On "Installation type," select **Erase disk and install Ubuntu**.

   > **Important:** This only erases the *virtual* disk VirtualBox created — not your real computer's drive.

5. Click **Install Now** → **Continue** to confirm.
6. Select timezone (e.g., **Chicago** for CST) → **Continue**.
7. Fill in the user account form:

   | Field | Value |
   |---|---|
   | Your name | Your real name |
   | Computer's name | `cis1310-vm` |
   | Username | `student` (all lowercase) |
   | Password | Choose a strong password — you will type it often |

8. Click **Continue**. Wait 5–15 minutes for installation.
9. Click **Restart Now** when prompted. Press **Enter** when asked to remove the installation medium.

### Step 4.3 — First Login

1. The Ubuntu login screen appears. Click your username and enter your password.
2. Click through the first-time setup wizard (skip all optional steps).

> **SCREENSHOT 2 REQUIRED:** Take a screenshot of the Ubuntu desktop running inside VirtualBox. Save as `lab01_screenshot_02_ubuntu_desktop.png`.

---

## Part 5 — Verify Python 3 and Install pip

Open a Terminal in Ubuntu: press **Ctrl+Alt+T**, or click the grid icon → search "Terminal" → click it.

### Step 5.1 — Check Python 3 Version

```bash
python3 --version
```

Expected output:

```text
Python 3.10.12
```

> Your exact minor version number may differ. You need Python 3.10 or higher.

> **SCREENSHOT 3 REQUIRED:** Screenshot of `python3 --version` output. Save as `lab01_screenshot_03_python_version.png`.

If you see `python3: command not found`, run:

```bash
sudo apt update
sudo apt install python3 -y
```

### Step 5.2 — Update Package Lists and Install pip

```bash
sudo apt update
sudo apt install python3-pip -y
```

Verify pip is installed:

```bash
pip3 --version
```

Expected output (version numbers may vary):

```text
pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)
```

### Step 5.3 — Create Your Course Working Directory

```bash
mkdir ~/cis1310
cd ~/cis1310
pwd
```

Expected output of `pwd`:

```text
/home/student/cis1310
```

> Every CIS-1310 lab saves files to `~/cis1310`. Always run `cd ~/cis1310` at the start of each lab session.

---

## Part 6 — Explore the Python REPL

### Step 6.1 — Launch the REPL

```bash
python3
```

You will see:

```text
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### Step 6.2 — Test Arithmetic in the REPL

Type each expression and press Enter after each one. Observe the output.

```python
>>> 2 + 2
```

Expected: `4`

```python
>>> 10 / 3
```

Expected: `3.3333333333333335` — this is regular division, result is a `float`

```python
>>> 10 // 3
```

Expected: `3` — **floor division**: divides and rounds down to nearest whole number

```python
>>> 10 % 3
```

Expected: `1` — **modulo**: returns the remainder after division

```python
>>> 2 ** 8
```

Expected: `256` — **exponentiation**: 2 to the power of 8

### Step 6.3 — Check Data Types

```python
>>> type(42)
```

Expected: `<class 'int'>`

```python
>>> type(3.14)
```

Expected: `<class 'float'>`

```python
>>> type('hello')
```

Expected: `<class 'str'>`

```python
>>> type(True)
```

Expected: `<class 'bool'>`

### Step 6.4 — Test String Concatenation

```python
>>> 'Texas' + ' Wesleyan'
```

Expected: `'Texas Wesleyan'`

```python
>>> 'CIS' + '-' + '1310'
```

Expected: `'CIS-1310'`

### Step 6.5 — Observe REPL Auto-Print vs. print()

```python
>>> 'Hello, World!'
```

Expected: `'Hello, World!'` — note the quotes (REPL shows the *representation* of the value)

```python
>>> print('Hello, World!')
```

Expected: `Hello, World!` — no quotes (print() outputs the *value* itself)

This difference matters. The REPL automatically shows the repr of an object. `print()` shows the human-readable string. In a script file, only `print()` produces output.

### Step 6.6 — Exit the REPL

```python
>>> exit()
```

Or press **Ctrl+D**. You return to the regular bash prompt.

> **SCREENSHOT 4 REQUIRED:** Take a screenshot of your REPL session showing at least 6 different expressions evaluated. Save as `lab01_screenshot_04_repl_session.png`.

---

## Part 7 — Write and Run Python Scripts

### Step 7.1 — Navigate to Your Course Directory

```bash
cd ~/cis1310
```

### Step 7.2 — Create hello.py

```bash
nano hello.py
```

The `nano` text editor opens. Type the following exactly — pay attention to spacing:

```python
# hello.py
# Module 01 Lab — CIS-1310 Introduction to Python
# Author: [Your Name]

print('Hello, Texas Wesleyan!')
print('Welcome to CIS-1310 — Introduction to Python')

# Store values in variables and print them
course = 'CIS-1310'
instructor = 'Professor Nash'

print('Course:', course)
print('Instructor:', instructor)
```

Save and exit nano:

- Press **Ctrl+O** (write Out)
- Press **Enter** to confirm filename
- Press **Ctrl+X** to exit

### Step 7.3 — Run hello.py

```bash
python3 hello.py
```

Expected output:

```text
Hello, Texas Wesleyan!
Welcome to CIS-1310 — Introduction to Python
Course: CIS-1310
Instructor: Professor Nash
```

> **SCREENSHOT 5 REQUIRED:** Screenshot of the `python3 hello.py` command and its output. Save as `lab01_screenshot_05_hello_script.png`.

### Step 7.4 — Create indentation_demo.py

```bash
nano indentation_demo.py
```

Type the following:

```python
# indentation_demo.py
# Demonstrates Python indentation rules — Module 01 Lab

# Example 1: if/else block
temperature = 85

if temperature > 80:
    print('It is hot outside.')      # 4 spaces — INSIDE the if block
    print('Stay hydrated!')          # 4 spaces — still INSIDE
else:
    print('The weather is fine.')    # 4 spaces — INSIDE the else block

print('Temperature check complete.') # 0 spaces — OUTSIDE both blocks

# Example 2: nested indentation — loop inside loop
print('')
print('Nested loop example:')

for i in range(1, 4):              # level 1 — 0 spaces (for is top-level)
    print('i =', i)                # level 2 — 4 spaces (inside for)
    if i == 2:                     # level 2 — 4 spaces (inside for)
        print('  Found two!')      # level 3 — 8 spaces (inside for AND if)
```

Save (Ctrl+O, Enter, Ctrl+X) and run:

```bash
python3 indentation_demo.py
```

Expected output:

```text
It is hot outside.
Stay hydrated!
Temperature check complete.

Nested loop example:
i = 1
i = 2
  Found two!
i = 3
```

Trace through the output to make sure it matches your understanding of the indentation blocks.

> **SCREENSHOT 6 REQUIRED:** Screenshot of `indentation_demo.py` running with correct output. Save as `lab01_screenshot_06_indentation_demo.png`.

### Step 7.5 — Trigger an IndentationError on Purpose

Understanding errors by generating them intentionally is one of the best learning techniques. Create this intentionally broken file:

```bash
nano broken_indent.py
```

Type this — note the inconsistent indentation on line 4:

```python
# broken_indent.py — INTENTIONALLY BROKEN — do not fix until instructed
if 5 > 3:
    print('Four spaces here')
  print('Only two spaces here — this will fail')
```

Save and run:

```bash
python3 broken_indent.py
```

Expected error output:

```text
  File "broken_indent.py", line 4
    print('Only two spaces here — this will fail')
                                                  ^
IndentationError: unindent does not match any outer indentation level
```

Read the error message carefully:

- Python reports the **file name** and **line number** of the problem
- It shows you the **exact line** that caused the failure
- The error type is `IndentationError` — a parse-time error (before any code runs)

Now fix it: open `broken_indent.py` again and change the 2-space indent to 4 spaces. Run it again — it should execute without errors.

> **SCREENSHOT 7 REQUIRED:** Screenshot of the `IndentationError` output from the broken file. Save as `lab01_screenshot_07_indentation_error.png`.

---

## Part 8 — Explore the \_\_pycache\_\_ Directory

After running your scripts, Python created bytecode files automatically.

```bash
ls -la ~/cis1310/
```

You should see your `.py` files and a `__pycache__` directory.

```bash
ls -la ~/cis1310/__pycache__/
```

You will see `.pyc` files with names like `hello.cpython-310.pyc`. These are the compiled bytecode files that Python generated internally. You never create or manage these — Python handles them automatically.

The filename format `scriptname.cpython-310.pyc` tells you:

- `scriptname` — the original `.py` file name
- `cpython` — the implementation (CPython)
- `310` — Python version 3.10
- `.pyc` — compiled Python bytecode

> **SCREENSHOT 8 REQUIRED:** Screenshot showing the `__pycache__` directory listing. Save as `lab01_screenshot_08_pycache.png`.

---

## Deliverables

Zip all 8 screenshots into a single file and upload to the Canvas Module 01 Lab Assignment.

| # | File Name | What It Shows |
|---|---|---|
| 1 | `lab01_screenshot_01_virtualbox.png` | VirtualBox Manager open |
| 2 | `lab01_screenshot_02_ubuntu_desktop.png` | Ubuntu desktop running in VirtualBox |
| 3 | `lab01_screenshot_03_python_version.png` | `python3 --version` output |
| 4 | `lab01_screenshot_04_repl_session.png` | REPL with at least 6 expressions |
| 5 | `lab01_screenshot_05_hello_script.png` | `hello.py` running with correct output |
| 6 | `lab01_screenshot_06_indentation_demo.png` | `indentation_demo.py` correct output |
| 7 | `lab01_screenshot_07_indentation_error.png` | Intentional `IndentationError` output |
| 8 | `lab01_screenshot_08_pycache.png` | `__pycache__` directory listing |

---

## Troubleshooting Guide

**VirtualBox says "VT-x/AMD-V hardware acceleration is not available."**
Reboot your computer, enter BIOS/UEFI (usually F2, F10, Delete, or Esc at startup), find **Virtualization Technology** or **AMD-V**, enable it, save, and reboot.

**Ubuntu installer screen is black or freezes.**
In VirtualBox VM settings → **Display** → increase Video Memory to **128 MB** and enable **3D Acceleration**.

**`python3 --version` shows Python 3.8 or older.**
Run `sudo apt update && sudo apt upgrade -y`. Then `sudo apt install python3.11 -y` if needed.

**`python3: command not found`**
Run `sudo apt update && sudo apt install python3 -y`.

**`pip3: command not found`**
Run `sudo apt install python3-pip -y`.

**`nano: command not found`**
Run `sudo apt install nano -y`.

**Can't copy-paste into the VM.**
In VirtualBox: **Devices → Shared Clipboard → Bidirectional**. This enables clipboard sharing between host and guest.

**The VM window is too small to work in.**
In VirtualBox: **View → Virtual Screen 1 → Scale to 150%** or **View → Auto-resize Guest Display**.
