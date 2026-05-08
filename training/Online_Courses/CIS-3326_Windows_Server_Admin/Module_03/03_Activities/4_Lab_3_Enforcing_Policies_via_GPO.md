### 4. Lab 3: Enforcing Policies via GPO
**Objective:** Create a GPO that restricts user capabilities and apply it to a specific OU.
**Instructions:**
1. Log into your Windows Server Domain Controller VM.
2. Open **Group Policy Management** from the Tools menu.
3. Expand your domain, right-click the "Marketing" OU you created in Lab 2, and select "Create a GPO in this domain, and Link it here...".
4. Name the GPO `Marketing_Restrictions`.
5. Right-click the new GPO and select **Edit**.
6. Navigate to **User Configuration -> Policies -> Administrative Templates -> Control Panel**.
7. Double-click "Prohibit access to Control Panel and PC settings", select **Enabled**, and click OK.
8. Run the command `gpupdate /force` in a command prompt.
**Deliverable:** Take a screenshot of the Group Policy Management Console showing the `Marketing_Restrictions` GPO successfully linked to the Marketing OU.

---
