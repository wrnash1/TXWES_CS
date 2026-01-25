# TXWES_CS Student VM Guide

Welcome to the Computer Science Workstation VM! This image is configured for:
- CIS-3321 Network Administration
- CIS-3325 Operating System Administration
- CIS-3326 Windows Server Administration
- CIS-4327 Database Fundamentals
- CIS-4328 Information Systems Security

## Getting Started

1.  **Launch**: Open the VM image from your USB using VirtualBox or VMware Player.
2.  **Login**:
    - **User**: `student`
    - **Password**: `student`

## Lab Locations
All your labs and supporting materials are located in `/home/student/Training`.

## Submitting Your Work
After completing a lab, run the submission script:
```bash
/home/student/Training/txwes-submit.sh
```
Follow the prompts to ensure Professor Nash receives your progress.

## Tools Installed
- **Automation**: Git, Python3, Vim
- **Network**: Nmap, Curl, Tracepath
- **Admin**: PowerShell Core (`pwsh`), SQLite/Postgres clients
- **Security**: OpenSSL, GPG, Firewalld
