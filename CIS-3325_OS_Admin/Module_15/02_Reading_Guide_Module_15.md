# Reading Guide: Module 15 - Containerization – Docker Basics on Linux
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

### Introduction
Welcome to **Module 15 – Containerization: Docker Basics on Linux**! This week covers container fundamentals — how Docker differs from virtual machines, the Docker architecture (daemon, client, images, containers, registries), essential `docker` commands, and Dockerfile basics. Containerization is tested on CompTIA Linux+ XK0-005 under Domain 4.0 (Scripting, Containers, and Automation).

As you work through this material you will learn how to pull and run container images, manage the container lifecycle, inspect running containers, and understand the key differences between container isolation and full virtualization.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Container vs virtual machine**: A container is a lightweight, isolated process running on the host Linux kernel using namespaces (process, network, filesystem isolation) and cgroups (resource limits). Containers share the host kernel — they do not boot a separate OS. A virtual machine includes a full guest OS and requires a hypervisor, making VMs heavier but more strongly isolated. Containers start in milliseconds; VMs take seconds to minutes. The exam tests this distinction directly.
*   **Docker architecture**: Docker uses a client-server model. The **Docker daemon** (`dockerd`) runs as a background service managing containers and images. The **Docker client** (`docker` CLI) sends commands to the daemon. **Images** are read-only templates stored in layers; **containers** are running instances of images. The **Docker Hub** registry (`hub.docker.com`) is the default public repository for images. Private registries can be hosted on-premises.
*   **Core `docker` commands**: `docker pull nginx` downloads an image from Docker Hub. `docker run -d -p 80:80 nginx` starts a container in detached mode, mapping host port 80 to container port 80. `docker ps` lists running containers; `docker ps -a` lists all including stopped. `docker stop <id>` gracefully stops a container; `docker rm <id>` removes a stopped container. `docker images` lists locally cached images; `docker rmi <image>` removes an image.
*   **`docker exec` and `docker logs`**: `docker exec -it <container> /bin/bash` opens an interactive shell inside a running container (useful for troubleshooting). `docker logs <container>` displays stdout/stderr output from a container — the primary way to view application logs in a containerized environment. `docker inspect <container>` outputs detailed JSON metadata about a container including network settings, mounts, and environment variables.
*   **Dockerfile basics**: A `Dockerfile` is a text file of instructions that defines how to build a custom image. Key instructions: `FROM ubuntu:22.04` (base image), `RUN apt-get install -y nginx` (execute a command during build), `COPY index.html /var/www/html/` (copy files from host), `EXPOSE 80` (document the port the app listens on), `CMD ["nginx", "-g", "daemon off;"]` (default command when container starts). Build with `docker build -t myimage:1.0 .`.
*   **Docker volumes and networking**: By default, container filesystems are ephemeral — data is lost when the container is removed. **Volumes** (`docker run -v /host/path:/container/path`) provide persistent storage by mounting host directories or named volumes into containers. Docker creates a default bridge network; containers on the same bridge can communicate by name when using user-defined networks. `docker network ls` lists networks; `docker network inspect <name>` shows connected containers.

---

### 2. Certification Exam Tips
*   **Domain alignment:** Containerization maps to Linux+ Domain 4.0 (Scripting, Containers, and Automation). Expect 4–6 questions on container vs VM differences, core `docker` commands, image/container lifecycle, and basic Dockerfile syntax.
*   **Container vs VM isolation trap:** The exam frequently asks which statement is true about containers vs VMs. Key answer: containers share the host kernel; VMs do not. A container cannot run a different OS kernel than the host — a Linux host can run Linux containers but not Windows containers natively.
*   **`docker run` flag trap:** `-d` = detached (background), `-it` = interactive with TTY (for shell access), `-p host:container` = port mapping, `-v` = volume mount, `--name` = assign a name. The exam presents a `docker run` command and asks what a specific flag does.
*   **Image vs container distinction:** An image is immutable and stored on disk; a container is a running (or stopped) instance of an image. `docker ps` shows containers, not images. `docker images` shows images, not containers. Confusing these is a common exam trap.
*   **`docker stop` vs `docker rm`:** `docker stop` sends SIGTERM then SIGKILL to stop a running container — the container still exists in stopped state. `docker rm` deletes the stopped container. Both steps are required to fully clean up a container. `docker rm -f` forces removal of a running container.
*   **Study Resource:** [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) provides foundational Linux knowledge (processes, filesystems, networking) that underpins container concepts. [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78) includes video demonstrations of Docker installation, image management, container lifecycle commands, and Dockerfile builds in a live Linux environment.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Review the processes and virtualization chapters of the free OER textbook [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php) to reinforce the Linux process and filesystem concepts that containerization builds upon.
*   **Required Video:** Watch the Docker and containerization videos in the [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78), a free YouTube playlist that demonstrates Docker installation, image pulls, container management, and Dockerfile basics with live examples.

---

### Lab & Command Integration
In this week's hands-on lab you will install Docker, pull the `nginx` image with `docker pull nginx`, run it with `docker run -d -p 8080:80 nginx`, verify it is running with `docker ps`, inspect logs with `docker logs`, exec into the container with `docker exec -it`, and stop and remove it with `docker stop` and `docker rm`.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Review the relevant chapters in [The Linux Command Line by William Shotts](https://linuxcommand.org/tlcl.php).
- [ ] Watch the Docker videos in [Linux Essentials Course by LearnLinuxTV](https://www.youtube.com/playlist?list=PLT98CRl2KxEG0QLjR-8t7k3S4I15Z1A78).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
