### 2. Video Script 4.2: Introduction to systemctl
**Estimated Duration:** 5 minutes
**Visual:** Side-by-side comparison. Left: Windows Services.msc. Right: Linux terminal with `systemctl status sshd`.
**[Alt-text: Left side shows the graphical Windows Services console. Right side shows the terminal output of 'systemctl status sshd', highlighting the green 'active (running)' text.]**
**Audio:** "Processes that run in the background without user interaction are called 'Services' in Windows, and 'Daemons' in Linux. To manage these, modern Linux uses the `systemd` init system. The primary command you will use is `systemctl`. If a web developer says the Apache web server is down, you run `systemctl status apache2`. If it says 'inactive', you run `systemctl start apache2`. To ensure it starts automatically every time the server reboots, you run `systemctl enable apache2`."

---
