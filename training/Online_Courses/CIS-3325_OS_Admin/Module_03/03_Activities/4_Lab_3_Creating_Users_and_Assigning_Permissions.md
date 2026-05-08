### 4. Lab 3: Creating Users and Assigning Permissions
**Objective:** Manage local users and utilize chmod/chown to secure files.
**Instructions:**
1. Log into your Ubuntu Server VM.
2. Create a new user named 'student1': `sudo useradd -m student1`
3. Create a new group named 'developers': `sudo groupadd developers`
4. Add 'student1' to the 'developers' group: `sudo usermod -aG developers student1`
5. Create a file in the `/opt` directory: `sudo touch /opt/project.sh`
6. Change the owner of the file to 'student1' and the group to 'developers': `sudo chown student1:developers /opt/project.sh`
7. Change the permissions so the owner has full rights, the group can read and execute, and others have no access: `sudo chmod 750 /opt/project.sh`
**Deliverable:** Take a screenshot of the output of `ls -l /opt/project.sh` showing the correct owner, group, and `rwxr-x---` permissions.

---
