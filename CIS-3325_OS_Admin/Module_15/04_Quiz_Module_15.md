# Quiz: Module 15 - Containerization – Docker Basics on Linux
## Course: CIS-3325_OS_Admin (CompTIA Linux+ XK0-005)

---

**Question 1**
A developer asks how Docker containers differ from virtual machines. Which statement is most accurate?
A) Containers include a full guest operating system and boot via a hypervisor, making them more portable than VMs.
B) Containers share the host Linux kernel and use namespaces and cgroups for isolation, while VMs run separate guest OS instances on a hypervisor.
C) Containers provide stronger security isolation than VMs because they run in encrypted memory regions.
D) Containers require more RAM than VMs because each container loads a complete OS image at runtime.
*   **Correct Answer:** B) Containers share the host Linux kernel and use namespaces and cgroups for isolation, while VMs run separate guest OS instances on a hypervisor.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This description applies to VMs, not containers. Containers do not include a guest OS or use a hypervisor. It is precisely the absence of a full OS that makes containers lightweight and fast to start.
    *   *Why C is incorrect:* VMs actually provide stronger hardware-level isolation than containers because VMs include a full OS boundary and hypervisor separation. Containers share the host kernel, which means a kernel vulnerability could potentially affect all containers on the host.
    *   *Why D is incorrect:* The opposite is true — containers consume far less RAM than VMs because they do not load a complete OS. A container runs only the application process and its dependencies within the host's existing kernel.

---

---

**Question 2**
An administrator runs `docker run -d -p 8080:80 nginx` on a Linux server. What does the `-p 8080:80` flag accomplish?
A) It limits the container's CPU usage to 80% with a burst cap of 8080 MHz.
B) It maps TCP port 8080 on the host to port 80 inside the container, making the containerized nginx accessible on the host's port 8080.
C) It creates a volume that mounts the host directory `/8080` to the container path `/80`.
D) It sets the container's hostname to `8080` and assigns it to network `80`.
*   **Correct Answer:** B) It maps TCP port 8080 on the host to port 80 inside the container, making the containerized nginx accessible on the host's port 8080.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* CPU resource limits are set with `--cpus` or `--cpu-shares` flags, not with `-p`. The `-p` flag is exclusively for port mapping between host and container.
    *   *Why C is incorrect:* Volume mounts use the `-v` flag with the syntax `-v /host/path:/container/path`. The `-p` flag has no relationship to filesystem mounts.
    *   *Why D is incorrect:* Container hostname is set with `--hostname` and network assignment uses `--network`. The `-p` flag performs port publishing only and does not affect the container's network identity.

---

---

**Question 3**
An administrator needs to view the stdout log output from a running Docker container named `webserver`. Which command is correct?
A) docker inspect webserver
B) docker logs webserver
C) docker exec webserver cat /var/log/nginx/access.log
D) journalctl -u docker -n 50
*   **Correct Answer:** B) docker logs webserver
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `docker inspect webserver` outputs detailed JSON metadata about the container — configuration, network settings, mounts, and environment variables. It does not show application stdout/stderr log output.
    *   *Why C is incorrect:* `docker exec webserver cat /var/log/nginx/access.log` reads a specific log file inside the container's filesystem. This works only if nginx writes to a file rather than stdout. Docker's standard logging mechanism captures stdout/stderr, which `docker logs` reads directly.
    *   *Why D is incorrect:* `journalctl -u docker` shows systemd journal entries for the Docker daemon service itself — startup messages, pull events, and daemon errors. It does not show the application output from individual containers.

---

**Question 4**
After stopping a container with `docker stop webserver`, an administrator runs `docker ps` and does not see the container listed. They conclude the container has been deleted. Is this assessment correct?
A) Yes — `docker stop` stops and removes the container in a single operation.
B) No — `docker ps` only shows running containers. The stopped container still exists and can be seen with `docker ps -a`. It must be removed separately with `docker rm webserver`.
C) Yes — stopped containers are automatically garbage-collected by the Docker daemon after 60 seconds.
D) No — the container is paused, not stopped. Run `docker unpause webserver` to resume it.
*   **Correct Answer:** B) No — `docker ps` only shows running containers. The stopped container still exists and can be seen with `docker ps -a`. It must be removed separately with `docker rm webserver`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `docker stop` only sends SIGTERM (then SIGKILL if needed) to halt the container's main process — it does not delete the container. The container transitions to a stopped state and remains on disk until explicitly removed with `docker rm`.
    *   *Why C is incorrect:* Docker does not automatically garbage-collect stopped containers. They persist indefinitely until removed with `docker rm` or until the daemon is run with `--rm` flag per-container at creation time (`docker run --rm`).
    *   *Why D is incorrect:* `docker pause` suspends all processes in a container using cgroups freezer — it is a separate operation from `docker stop`. A stopped container has its process terminated; a paused container has its processes frozen but still exists in memory. `docker stop` does not pause — it terminates.

---

**Question 5**
A Dockerfile contains the line `COPY index.html /usr/share/nginx/html/`. During `docker build`, this step fails with "COPY failed: file not found in build context." What is the most likely cause?
A) The `/usr/share/nginx/html/` directory does not exist inside the container and must be created with a `RUN mkdir` instruction first.
B) The `index.html` file does not exist in the build context directory (the directory passed to `docker build`) on the host machine.
C) The `COPY` instruction requires the `--chown` flag to specify the file owner inside the container.
D) Docker does not allow copying HTML files — only binary executables and configuration files can be copied with the `COPY` instruction.
*   **Correct Answer:** B) The `index.html` file does not exist in the build context directory (the directory passed to `docker build`) on the host machine.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Docker's `COPY` instruction creates intermediate directories as needed when writing to the container filesystem. If the destination path's parent directories do not exist, Docker creates them — a separate `RUN mkdir` is not required for this error.
    *   *Why C is incorrect:* `--chown` is an optional flag that sets file ownership inside the container. Its absence does not cause a build failure — files default to root ownership. The error message "file not found in build context" specifically points to a missing source file on the host.
    *   *Why D is incorrect:* `COPY` has no restriction on file types. Any file — HTML, binaries, scripts, configuration files, images — can be copied into a container image using the `COPY` instruction.
