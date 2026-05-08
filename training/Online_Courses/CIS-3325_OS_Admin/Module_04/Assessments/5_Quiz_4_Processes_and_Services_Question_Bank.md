### 5. Quiz 4: Processes and Services (Question Bank)
**Question 1**
An administrator runs a script that takes a long time to complete and wants to save the output to a log file instead of displaying it on the screen. However, they want to ensure that if the script fails, the error messages are *also* captured in the same log file. Which command achieves this?
A) ./script.sh > output.log
B) ./script.sh >> output.log
C) ./script.sh > output.log 2>&1
D) ./script.sh < output.log
*   **Correct Answer:** C) ./script.sh > output.log 2>&1
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `>` only redirects stdout (1). Errors (stderr, 2) will still print to the screen and be lost.
    *   *Why B is incorrect:* `>>` appends stdout, but still does not capture stderr.
    *   *Why D is incorrect:* `<` is used to feed the contents of a file into a script as input (stdin), not save output. `2>&1` redirects stderr (2) to wherever stdout (1) is currently pointing.

**Question 2**
You have just installed a new web server package (nginx) on your Linux machine. You started the service manually and verified it works. However, after rebooting the server, the website is down because the service did not start automatically. Which command must you run to ensure the service starts on every boot?
A) systemctl start nginx
B) systemctl enable nginx
C) systemctl reload nginx
D) systemctl status nginx
*   **Correct Answer:** B) systemctl enable nginx
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `start` only turns the service on for the current session; it does not configure it to start on the next boot.
    *   *Why C is incorrect:* `reload` tells a running service to re-read its configuration files without dropping connections; it does not configure boot behavior.
    *   *Why D is incorrect:* `status` simply reports whether the service is currently running or stopped.
