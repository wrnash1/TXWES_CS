# Video Script: Module 16 — Linux+ XK0-005 Exam Preparation (Part 2 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Introduction

Welcome back to Module 16, Part 2.

In Part 1, we reviewed the exam structure and covered Domains 1 and 2. Now we tackle Domain 3 (Scripting, Containers, and Automation) and Domain 4 (Troubleshooting), followed by exam strategy and 20 practice questions. This is your final preparation session before the exam.

---

### Section 4: Domain 3 — Scripting, Containers, and Automation Review

Domain 3 covers 19% of the exam. The XK0-005 version added containers and automation topics not tested in XK0-004.

**3.1 Bash Scripting Essentials**

Variables and quoting:

```bash
NAME="World"
echo "Hello, $NAME"       # Double quotes: variable expanded
echo 'Hello, $NAME'       # Single quotes: literal, no expansion
echo "Path is: $(pwd)"    # Command substitution
```

Conditional syntax:

```bash
if [ -f /etc/passwd ]; then
    echo "File exists"
elif [ -d /etc ]; then
    echo "Directory exists"
else
    echo "Neither"
fi
```

Test operators — know these:

| Operator | Meaning |
|----------|---------|
| `-f file` | File exists and is regular file |
| `-d dir` | Directory exists |
| `-e path` | Path exists (any type) |
| `-r file` | File is readable |
| `-w file` | File is writable |
| `-z string` | String is empty |
| `-n string` | String is not empty |
| `str1 = str2` | Strings are equal |
| `n1 -eq n2` | Numbers are equal |
| `n1 -gt n2` | n1 is greater than n2 |
| `n1 -lt n2` | n1 is less than n2 |

Loops:

```bash
# For loop with list:
for user in alice bob charlie; do
    echo "Creating user: $user"
    useradd "$user"
done

# For loop with range:
for i in {1..10}; do
    echo "Item $i"
done

# While loop:
count=0
while [ $count -lt 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

Functions:

```bash
greet() {
    local name="$1"
    echo "Hello, $name"
}
greet "Alice"
```

Exit codes: `0` = success, non-zero = failure. `$?` holds the last exit code.

```bash
ls /nonexistent
echo $?    # Returns 2 (file not found)
```

**3.2 Regular Expressions and Text Processing**

```bash
grep "pattern" file
grep -i "pattern" file       # Case insensitive
grep -v "pattern" file       # Invert match
grep -r "pattern" /dir/      # Recursive
grep -E "pattern|pattern2"   # Extended regex

awk '{print $1, $3}' file    # Print fields 1 and 3
awk -F: '{print $1}' /etc/passwd    # Colon delimiter, print username field
sed 's/old/new/g' file       # Replace all occurrences
sed -i 's/old/new/g' file    # In-place replacement
sed '/pattern/d' file        # Delete matching lines
cut -d: -f1 /etc/passwd      # Cut with colon delimiter, field 1
sort -n file                  # Numeric sort
sort -u file                  # Unique sort
uniq -c file                  # Count duplicates
wc -l file                   # Count lines
```

**3.3 Containers — Docker Basics**

Key container concepts:

- **Image** — read-only template for creating containers
- **Container** — running instance of an image
- **Dockerfile** — recipe for building an image
- **Registry** — repository for images (Docker Hub, private registries)

Essential Docker commands:

```bash
docker pull nginx               # Download image
docker images                   # List local images
docker run -d -p 80:80 nginx    # Run container in background
docker run -it ubuntu bash      # Interactive container
docker ps                       # List running containers
docker ps -a                    # List all containers
docker stop container_id
docker rm container_id
docker exec -it container_id bash    # Shell into running container
docker logs container_id
docker build -t myapp:1.0 .     # Build from Dockerfile
docker push myapp:1.0            # Push to registry
```

**Basic Dockerfile:**

```dockerfile
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y nginx
COPY index.html /var/www/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

**Container vs. Virtual Machine:**

- Containers share the host kernel; VMs have their own
- Containers are faster to start and use fewer resources
- VMs provide stronger isolation
- The exam tests both conceptually

**3.4 Ansible**

Ansible key concepts reviewed:

- Agentless: uses SSH, no agent needed on managed hosts
- Idempotent: running the same playbook twice produces the same result
- Inventory: `/etc/ansible/hosts` or custom file
- Playbook: YAML file with plays → tasks
- Module: `package`, `service`, `copy`, `file`, `user`, `command`, `shell`
- `become: yes` — privilege escalation via sudo
- `--check` — dry run mode
- `ansible -m ping all` — connectivity test

---

### Section 5: Domain 4 — Troubleshooting Review

Domain 4 is the second largest domain at 28%. CompTIA emphasizes systematic troubleshooting methodology.

**4.1 Troubleshooting Methodology**

The CompTIA A+/Linux+ troubleshooting process:

1. Identify the problem
2. Establish a theory of probable cause
3. Test the theory
4. Establish a plan of action
5. Implement the solution
6. Verify full functionality
7. Document findings and resolution

**4.2 Boot Process Troubleshooting**

UEFI/BIOS → Boot loader (GRUB2) → Kernel → initramfs → systemd → target

GRUB2 recovery:

- At boot, press `e` to edit GRUB entry
- Add `rd.break` to kernel line — drops to initramfs shell before root is mounted
- Add `single` or `1` — boots to single-user mode
- `systemd.unit=rescue.target` — boots to rescue mode

Resetting root password (RHEL/Rocky):

1. Edit GRUB entry — add `rd.break` after `rhgb quiet`
2. At `switch_root` prompt:
   ```bash
   mount -o remount,rw /sysroot
   chroot /sysroot
   passwd root
   touch /.autorelabel
   exit; exit
   ```

**4.3 Network Troubleshooting**

OSI layer approach:

- Layer 1/2: `ip link show` — interface up? `ethtool eth0` — link detected?
- Layer 3: `ip addr show`, `ip route show`, `ping <gateway>`
- Layer 4: `ss -tlnp`, `nmap -p port host`
- Layer 7: `curl`, `dig`, service logs

Common causes:

- No route to host → routing table issue
- Connection refused → service not listening or firewall
- Connection timeout → firewall silently dropping
- DNS failure → `/etc/resolv.conf`, `/etc/nsswitch.conf`

**4.4 Storage Troubleshooting**

```bash
dmesg | grep -i "error\|fail\|disk"   # Kernel disk errors
lsblk                                  # Block device tree
fdisk -l                               # Partition table
df -h                                  # Filesystem usage
df -i                                  # Inode usage
du -sh /*                              # Top-level disk usage
smartctl -a /dev/sda                   # SMART disk health
```

Full disk vs. full inodes: `df -h` vs. `df -i` distinguish these.

**4.5 Service Troubleshooting**

```bash
systemctl status servicename          # Status and recent logs
journalctl -u servicename -n 50       # Last 50 log lines
journalctl -u servicename -p err      # Errors only
journalctl -b -1 -u servicename       # Last boot
systemctl list-dependencies service   # Dependency tree
```

**4.6 Permission and Access Troubleshooting**

When a user cannot access a file:

1. Check file permissions: `ls -la /path/to/file`
2. Check user's groups: `id username`
3. Check ACLs: `getfacl /path/to/file`
4. Check SELinux context: `ls -Z /path/to/file`
5. Check SELinux denials: `ausearch -m avc -ts recent`

**4.7 Memory and CPU Troubleshooting**

```bash
free -h                  # Memory usage
vmstat 1 5               # Virtual memory statistics (5 samples, 1-sec interval)
top                      # Real-time CPU and memory
sar -u 1 5               # CPU stats from sysstat
sar -r 1 5               # Memory stats from sysstat
uptime                   # Load averages
lscpu                    # CPU information
```

Load average interpretation: 3 numbers (1-min, 5-min, 15-min averages). On a single-core system, load of 1.0 = 100% utilized. On a 4-core system, load of 4.0 = 100% utilized.

---

### Section 6: Exam Strategy

**Time Management**

90 questions in 90 minutes = 1 minute per question average. In practice:

- Multiple-choice: 30–45 seconds each
- Multiple-response: 60–90 seconds each
- Performance-based: 10–15 minutes each

Mark difficult questions and return. Don't stall on one question and miss 10 easier ones.

**Elimination Strategy**

On multiple-choice questions:

1. Eliminate obviously wrong answers first (usually 1–2)
2. From remaining options, identify keywords that match exam objectives
3. When two options look similar, look for the one with correct syntax or the more specific answer
4. Deprecated tools (ifconfig, route, netstat) are usually wrong answers on XK0-005

**Command Syntax Gotchas**

High-frequency syntax traps on the exam:

- `scp -P 2222` (uppercase P) vs `ssh -p 2222` (lowercase p)
- `useradd -G` (replace groups) vs `usermod -aG` (append to groups)
- `lvextend -L +10G` (add 10G) vs `lvextend -L 10G` (set to 10G total)
- `chage -d 0` (force password change) vs `chage -M 0` (expire immediately)
- `setenforce 0` (permissive, NOT disable) vs `SELINUX=disabled` in config
- `--permanent` in firewall-cmd requires `--reload` to take effect
- `systemctl enable` is NOT the same as `systemctl start`

**When You Don't Know**

If you are completely unsure:

- Look for the most technically precise answer
- Prefer answers that use modern tools (`ip` over `ifconfig`, `ss` over `netstat`, `systemctl` over `service`)
- Prefer answers that follow the principle of least privilege
- If two answers both seem correct, the one that is more complete or includes a safety check is usually right

**Day-Before Checklist**

- Review all flash cards (key commands and flags)
- Review the domain breakdown — know the weight of each domain
- Get 8 hours of sleep
- Eat before the exam — your brain needs fuel
- Arrive 15 minutes early (testing center) or test your equipment early (online)

---

### Summary — Module 16 and Course Wrap-Up

Module 16 provided a complete exam preparation framework:

- Exam structure: 90 questions, 90 minutes, 4 domains, 720 passing score
- Domain 1 (32%): system management — filesystem, users, permissions, packages, processes, storage, systemd
- Domain 2 (21%): security — SELinux, SSH, firewall, auditd, passwords
- Domain 3 (19%): scripting, containers, Ansible
- Domain 4 (28%): troubleshooting — boot, networking, storage, services, permissions
- Exam strategy: time management, elimination, syntax gotchas, confidence

**Course Achievement**

Over 16 modules, you've built a complete Linux administration skill set:

- Shell navigation, text processing, and scripting
- User and group management
- File system management and permissions
- Package management
- Networking with ip and nmcli
- systemd service management and journalctl
- LVM and storage
- SSH hardening and remote administration
- SELinux and security hardening

This knowledge covers the Linux+ XK0-005 exam and — more importantly — the real-world skills needed in every Linux administration role. Everything in this course is used in production every day by Linux administrators worldwide.

Good luck on your exam. You've earned it. Go get certified.
