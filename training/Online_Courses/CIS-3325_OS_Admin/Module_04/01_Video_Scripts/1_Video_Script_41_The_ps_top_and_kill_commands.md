### 1. Video Script 4.1: The 'ps', 'top', and 'kill' commands
**Estimated Duration:** 6 minutes
**Visual:** Instructor on camera.
**Audio:** "Welcome to Module 4. Every application running on an operating system is called a 'Process'. When a server gets slow, your first job as an administrator is to find out which process is hogging the CPU or RAM, and terminate it if necessary."
**Visual:** Screencast of a Linux terminal running the 'top' command.
**[Alt-text: A terminal showing the dynamic output of the 'top' command. The columns PID, USER, %CPU, and %MEM are highlighted.]**
**Audio:** "In Windows, you use the Task Manager. In Linux, you use the command line. The `ps` command gives you a static snapshot of running processes. But the `top` command gives you a dynamic, real-time view. Look at this output: the PID is the Process ID. Every process has a unique number. If I see a rogue script consuming 99% of my CPU, I note its PID, exit `top`, and use the `kill` command to terminate it forcefully. `kill -9` followed by the PID is the ultimate 'end task' button."

---
