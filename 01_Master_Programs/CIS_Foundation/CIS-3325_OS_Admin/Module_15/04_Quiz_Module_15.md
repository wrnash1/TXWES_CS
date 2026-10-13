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

---

*Questions 6–20 — 5 pts each*

---

**Question 6**

An administrator runs `docker ps` on a server and sees no output. They then run `docker ps -a` and see five containers all in the `Exited` state. What is the correct interpretation?

A) There are no containers on the system — `Exited` entries are ghost records that will clear automatically.
B) All five containers have stopped but their filesystems and configuration still exist on disk. They can be restarted with `docker start` or permanently removed with `docker rm`.
C) The Docker daemon has crashed. Run `systemctl restart docker` to recover the containers.
D) The containers are paused. Run `docker unpause` on each to resume them.

*   **Correct Answer:** B) All five containers have stopped but their filesystems and configuration still exist on disk. They can be restarted with `docker start` or permanently removed with `docker rm`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `Exited` containers are real, persistent objects stored on disk in `/var/lib/docker/containers/`. They occupy disk space and retain their writable layer. They are not ghost records and are not automatically removed unless the container was created with `--rm`.
    *   *Why C is incorrect:* If the Docker daemon had crashed, `docker ps -a` itself would fail with a connection error to the Docker socket. The ability to run `docker ps -a` and see output confirms the daemon is running normally.
    *   *Why D is incorrect:* Paused containers are shown with status `Paused` in `docker ps` output, not `Exited`. A paused container still has its process frozen in memory. An exited container's main process has terminated — it is a fundamentally different state.

---

**Question 7**

An administrator wants a container's data to persist after the container is removed. They plan to store a PostgreSQL database inside the container. Which storage approach is most appropriate for production use?

A) Write the data to `/tmp` inside the container because `/tmp` is always preserved across container restarts.
B) Use a Docker named volume mounted at `/var/lib/postgresql/data` inside the container.
C) Use a bind mount pointing to a directory inside the container image's layer.
D) Commit the running container to a new image with `docker commit` after each write to preserve data.

*   **Correct Answer:** B) Use a Docker named volume mounted at `/var/lib/postgresql/data` inside the container.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `/tmp` inside a container is part of the container's writable layer and is destroyed when the container is removed. It also does not persist across container recreations. Storing a database in `/tmp` would result in data loss on any container removal.
    *   *Why C is incorrect:* Container image layers are read-only. A bind mount must point to a path on the host filesystem, not inside the image layer. Bind mounts are a valid alternative to named volumes for development, but the source path must be a real directory on the host.
    *   *Why D is incorrect:* `docker commit` creates a new image snapshot of the container's current filesystem state. Using commits for database persistence is impractical because it requires a manual commit after every write, creates enormous image layer growth, and is not atomic — a crash between writes loses all data since the last commit.

---

**Question 8**

A Dockerfile contains the following instructions in this order: `FROM ubuntu:22.04`, `RUN apt-get update`, `COPY app.py /app/`, `RUN pip install flask`. A developer changes only `app.py` and rebuilds. Which layers does Docker rebuild from cache and which does it re-execute?

A) All four layers are rebuilt from scratch on every `docker build` run.
B) `FROM` and both `RUN` layers are served from cache. Only the `COPY app.py` layer and the subsequent `RUN pip install flask` layer are re-executed.
C) Only the `COPY app.py` layer is re-executed. The `RUN pip install flask` layer is served from cache because pip was already installed.
D) Docker cannot use cache for any layer that follows a `COPY` instruction.

*   **Correct Answer:** B) `FROM` and both `RUN` layers are served from cache. Only the `COPY app.py` layer and the subsequent `RUN pip install flask` layer are re-executed.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Docker's layer cache is one of its most valuable build features. Layers are cached based on their instruction and context. Unchanged layers before the first modification are served from cache, significantly speeding up rebuilds.
    *   *Why C is incorrect:* Docker's build cache is invalidated at the first layer that changes and for all subsequent layers. Because `COPY app.py` is invalidated (the file changed), the layer after it — `RUN pip install flask` — must also be re-executed even if the pip command itself is unchanged. Cache invalidation cascades forward through all dependent layers.
    *   *Why D is incorrect:* `COPY` instructions use cache normally. If the source files have not changed since the last build, Docker serves the `COPY` layer from cache. Cache invalidation occurs only when the content being copied has actually changed.

---

**Question 9**

An administrator runs `docker run -d --name db -e POSTGRES_PASSWORD=secret -v pgdata:/var/lib/postgresql/data postgres:15`. What does the `-e POSTGRES_PASSWORD=secret` flag do?

A) It encrypts all data written to the `pgdata` volume using the key `secret`.
B) It sets an environment variable `POSTGRES_PASSWORD` with the value `secret` inside the container, which the PostgreSQL image uses to set the database superuser password at initialization.
C) It creates a Docker secret named `secret` and mounts it at `/run/secrets/POSTGRES_PASSWORD` inside the container.
D) It restricts access to the container so only users with the password `secret` can run `docker exec` against it.

*   **Correct Answer:** B) It sets an environment variable `POSTGRES_PASSWORD` with the value `secret` inside the container, which the PostgreSQL image uses to set the database superuser password at initialization.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Docker does not perform volume encryption via the `-e` flag. Volume encryption requires host-level disk encryption (dm-crypt/LUKS) or filesystem-level encryption. The `-e` flag only sets environment variables visible to processes inside the container.
    *   *Why C is incorrect:* Docker Secrets are a Swarm-mode feature that stores sensitive data in the Swarm manager and mounts it as a file under `/run/secrets/`. They require `docker service` or `docker stack` and are not activated by the `-e` flag in a plain `docker run` command.
    *   *Why D is incorrect:* Docker has no mechanism to password-protect access to `docker exec`. Access to the Docker daemon (and therefore all container operations) is controlled by membership in the `docker` group or root privilege — not by per-container passwords.

---

**Question 10**

An administrator needs to pass a secret API key to a container at runtime without baking it into the image. Which approach follows security best practices?

A) Add the key as a `ENV API_KEY=value` line in the Dockerfile.
B) Pass the key as a runtime environment variable: `docker run -e API_KEY=$MY_KEY myapp`.
C) Copy the key into the image with `COPY secrets/api_key.txt /app/`.
D) Hard-code the key in the application source code before running `docker build`.

*   **Correct Answer:** B) Pass the key as a runtime environment variable: `docker run -e API_KEY=$MY_KEY myapp`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Secrets embedded in a Dockerfile via `ENV` are baked into every image layer and are visible to anyone who runs `docker history` or `docker inspect` on the image. They are also committed to version control if the Dockerfile is stored in a repository.
    *   *Why C is incorrect:* Files copied into an image with `COPY` become part of the image layers and are visible to any user who pulls and inspects the image. Even if the file is deleted in a later `RUN` layer, it remains accessible in the earlier layer's filesystem snapshot.
    *   *Why D is incorrect:* Hard-coding secrets in source code is the most severe anti-pattern. The key is embedded in version control history, visible in the image, and cannot be rotated without a code change and full rebuild.

---

**Question 11**

Which command shows real-time CPU, memory, network I/O, and block I/O statistics for all running containers, updated every second?

A) `docker inspect --live`
B) `docker logs -f`
C) `docker stats`
D) `docker top`

*   **Correct Answer:** C) `docker stats`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `docker inspect --live` is not a valid command. `docker inspect` outputs a static JSON snapshot of container metadata at the moment it is run. It does not provide live updating resource metrics.
    *   *Why B is incorrect:* `docker logs -f` follows the stdout/stderr output of a container's main process in real time. It does not display CPU, memory, or I/O utilization metrics.
    *   *Why D is incorrect:* `docker top CONTAINER` shows the processes currently running inside a specific container — similar to the Unix `ps` command scoped to the container. It lists process names, PIDs, and users but does not show resource consumption rates or update continuously.

---

**Question 12**

An administrator writes this Dockerfile:

```
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

Why is `COPY requirements.txt .` placed before `COPY . .` rather than copying everything in a single `COPY . .` instruction?

A) Docker requires all `COPY` instructions to be listed before any `RUN` instructions.
B) Separating the requirements copy from the full source copy maximizes layer cache reuse — the expensive `pip install` layer is only re-executed when `requirements.txt` changes, not on every source code change.
C) `COPY . .` would overwrite `requirements.txt` if it appeared first, causing the pip install to fail.
D) Python applications require `requirements.txt` to be owned by root, which is only guaranteed when it is copied in a separate instruction.

*   **Correct Answer:** B) Separating the requirements copy from the full source copy maximizes layer cache reuse — the expensive `pip install` layer is only re-executed when `requirements.txt` changes, not on every source code change.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* There is no requirement in Dockerfile syntax that `COPY` instructions precede `RUN` instructions. Instructions can be ordered in any sequence. The ordering here is a deliberate optimization strategy, not a syntax requirement.
    *   *Why C is incorrect:* `COPY . .` copies all files from the build context into the working directory. `requirements.txt` would be copied again as part of this instruction, but it would simply overwrite the existing file with an identical copy — this causes no failure. The motivation for the split is cache efficiency, not overwrite prevention.
    *   *Why D is incorrect:* File ownership inside the container defaults to root for all `COPY` instructions unless `--chown` is specified. There is no ownership difference between files copied in separate versus combined `COPY` instructions.

---

**Question 13**

An administrator needs to remove all stopped containers, all unused networks, all dangling images, and all unused images (not just dangling ones) in a single operation. Which command accomplishes this?

A) `docker system prune`
B) `docker system prune -a`
C) `docker image prune && docker container prune`
D) `docker rm $(docker ps -aq) && docker rmi $(docker images -q)`

*   **Correct Answer:** B) `docker system prune -a`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `docker system prune` without `-a` removes stopped containers, unused networks, and only dangling (untagged) images. It does not remove images that are tagged but not currently used by any container. Adding `-a` extends removal to all unused images regardless of whether they are tagged.
    *   *Why C is incorrect:* `docker image prune` removes only dangling images by default (same as `docker system prune` without `-a`). `docker container prune` removes stopped containers. This combination does not remove unused networks or unused tagged images. It is also two separate commands, not a single operation.
    *   *Why D is incorrect:* This approach uses shell command substitution to construct removal commands. `docker images -q` lists all image IDs including those used by running containers — attempting to remove them will fail with an error. It also does not remove unused networks and is not the recommended operational approach.

---

**Question 14**

A developer runs `docker exec -it webserver bash` and gets the error: `OCI runtime exec failed: exec: "bash": executable file not found in $PATH`. What is the most likely explanation?

A) The container is stopped. Run `docker start webserver` first.
B) The container's image is based on a minimal distribution (such as Alpine Linux) that does not include bash. Try `docker exec -it webserver sh` instead.
C) The `docker exec` command requires the `--user root` flag to run a shell.
D) The container's filesystem is read-only and shells cannot be executed in read-only containers.

*   **Correct Answer:** B) The container's image is based on a minimal distribution (such as Alpine Linux) that does not include bash. Try `docker exec -it webserver sh` instead.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* If the container were stopped, `docker exec` would fail with a different error — "container is not running" — not an "executable file not found" error. The "executable file not found" message confirms the container is running but the specified binary does not exist in the image.
    *   *Why C is incorrect:* `docker exec` does not require `--user root` to run a shell. By default it runs as the user defined in the image's `USER` instruction. The error message specifically says bash was not found, which is an image content issue, not a privilege issue.
    *   *Why D is incorrect:* A read-only container filesystem would prevent writes but would not prevent executing pre-existing binaries. Read-only mode (`--read-only`) allows execution of existing programs — it only prevents creating or modifying files. The error is about a missing binary, not filesystem access restrictions.

---

**Question 15**

An administrator runs `docker network ls` and sees three networks: `bridge`, `host`, and `none`. A developer reports that two containers on the default `bridge` network cannot reach each other by container name — they must use IP addresses. What explains this limitation and what is the fix?

A) The default `bridge` network uses IPv6 only. Switch both containers to IPv4 with `--ip` flags.
B) Containers on the default `bridge` network do not have automatic DNS name resolution. Create a custom bridge network with `docker network create`, connect both containers to it, and they can resolve each other by container name.
C) Container name resolution requires the Docker daemon to be restarted with `--dns` flags pointing to an internal resolver.
D) The `bridge` network only supports one container at a time. Use the `host` network to allow multiple containers to share the network stack.

*   **Correct Answer:** B) Containers on the default `bridge` network do not have automatic DNS name resolution. Create a custom bridge network with `docker network create`, connect both containers to it, and they can resolve each other by container name.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The default bridge network supports both IPv4 and IPv6. The limitation is DNS name resolution between containers, not an IP version issue. Containers can ping each other by IP on the default bridge without any flag changes.
    *   *Why C is incorrect:* Docker's embedded DNS server is enabled automatically on custom bridge networks — no daemon restart or `--dns` flag is needed. The default bridge network simply predates Docker's built-in DNS feature and does not include it for backward compatibility reasons.
    *   *Why D is incorrect:* The `bridge` network supports multiple containers simultaneously — this is its primary purpose. The `host` network removes container network isolation entirely, giving the container direct access to the host's network interfaces. Using `host` mode to solve a name resolution problem is an extreme and insecure approach.

---

**Question 16**

An administrator wants to limit a container to use no more than 512 MB of RAM and 1 CPU core. Which `docker run` flags enforce these resource limits?

A) `-m 512M --cpus 1`
B) `--memory-limit=512M --cpu-count=1`
C) `--ram 512 --cores 1`
D) `-m 512 -c 1`

*   **Correct Answer:** A) `-m 512M --cpus 1`
*   **Distractor Analysis:**
    *   *Why B is incorrect:* `--memory-limit` and `--cpu-count` are not valid Docker flags. Docker uses `-m` or `--memory` for memory limits and `--cpus` for CPU limits. Fabricated flag names are common distractors on certification exams.
    *   *Why C is incorrect:* `--ram` and `--cores` are not Docker flags. Docker's resource constraint flags use the names `--memory` (or `-m`) and `--cpus`. Always verify exact flag names against `docker run --help`.
    *   *Why D is incorrect:* `-m 512` without a unit suffix sets the memory limit to 512 bytes, not 512 megabytes. Docker requires an explicit unit suffix: `b` (bytes), `k` (kilobytes), `m` (megabytes), or `g` (gigabytes). The `-c` flag sets `--cpu-shares` (a relative weight for CPU scheduling), not an absolute CPU count. `--cpus 1` is the correct flag for an absolute CPU core limit.

---

**Question 17**

What is the functional difference between the `CMD` and `ENTRYPOINT` Dockerfile instructions?

A) `CMD` runs during the image build phase. `ENTRYPOINT` runs when the container starts.
B) `ENTRYPOINT` defines the fixed executable that always runs when the container starts. `CMD` provides default arguments to the entrypoint that can be overridden by passing arguments to `docker run`. When no `ENTRYPOINT` is set, `CMD` is the full default command.
C) `CMD` can only run shell built-in commands. `ENTRYPOINT` is required for any external binary.
D) `ENTRYPOINT` is for Linux containers only. `CMD` works on both Linux and Windows containers.

*   **Correct Answer:** B) `ENTRYPOINT` defines the fixed executable that always runs when the container starts. `CMD` provides default arguments to the entrypoint that can be overridden by passing arguments to `docker run`. When no `ENTRYPOINT` is set, `CMD` is the full default command.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Both `CMD` and `ENTRYPOINT` define container runtime behavior — neither runs during the image build phase. Build-time commands use the `RUN` instruction. `CMD` and `ENTRYPOINT` only affect what happens when a container starts from the image.
    *   *Why C is incorrect:* There is no restriction on what commands `CMD` or `ENTRYPOINT` can execute. Both support shell form (`CMD command arg`) and exec form (`CMD ["command", "arg"]`) and can invoke any executable available in the image.
    *   *Why D is incorrect:* Both `CMD` and `ENTRYPOINT` work on both Linux and Windows containers. The choice between them is about behavior and override flexibility, not platform compatibility.

---

**Question 18**

An administrator runs `docker volume inspect pgdata` and sees the `Mountpoint` field shows `/var/lib/docker/volumes/pgdata/_data`. A developer asks what happens to the files in that directory if `docker volume rm pgdata` is run. What is the correct answer?

A) The files are moved to `/tmp/docker-volumes/pgdata/` as a safety backup before the volume record is removed.
B) The volume record and all data in `/var/lib/docker/volumes/pgdata/_data` are permanently deleted from the host filesystem. This operation is irreversible.
C) Only the Docker volume metadata is removed. The actual data in `_data` remains on disk and can be re-attached by creating a new volume with the same name.
D) `docker volume rm` fails if any data exists in the volume — the volume must be emptied first.

*   **Correct Answer:** B) The volume record and all data in `/var/lib/docker/volumes/pgdata/_data` are permanently deleted from the host filesystem. This operation is irreversible.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Docker performs no automatic backup when removing volumes. There is no safety net — `docker volume rm` is a destructive, immediate, and permanent operation. Administrators must back up critical data before removing volumes.
    *   *Why C is incorrect:* `docker volume rm` deletes both the metadata and the underlying data directory. Creating a new volume with the same name creates an empty volume — it does not recover the deleted data. The data is gone from the host filesystem after `rm`.
    *   *Why D is incorrect:* `docker volume rm` removes the volume regardless of whether it contains data. The only guard is that Docker refuses to remove a volume that is currently mounted by a running or stopped container — it returns an error in that case. An unused volume with data is removed without warning.

---

**Question 19**

An administrator needs to transfer a Docker image to an air-gapped server with no internet access and no shared registry. Which command sequence correctly exports the image on the source server and imports it on the destination?

A) `docker export myapp:1.0 > myapp.tar` on source; `docker import myapp.tar` on destination.
B) `docker save -o myapp.tar myapp:1.0` on source; `docker load -i myapp.tar` on destination.
C) `docker commit myapp myapp:1.0` on source; `docker pull myapp:1.0` on destination.
D) `docker cp myapp:1.0 /tmp/myapp.tar` on source; `docker cp /tmp/myapp.tar destination:/` on destination.

*   **Correct Answer:** B) `docker save -o myapp.tar myapp:1.0` on source; `docker load -i myapp.tar` on destination.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `docker export` exports the filesystem of a running or stopped container (not an image) as a flat tar archive. It strips all image metadata including layers, history, and tags. `docker import` creates a single-layer image from this flat archive, losing all build history and layer optimizations. This approach is for container filesystem snapshots, not for transferring complete images.
    *   *Why C is incorrect:* `docker commit` creates a new image from a running container's current state on the source server. `docker pull` downloads from a registry — it cannot pull from a local file and would fail with a network error on the air-gapped destination server.
    *   *Why D is incorrect:* `docker cp` copies files between a running container and the host filesystem. `myapp:1.0` is an image tag, not a container name — this command would fail. `docker cp` has no network transfer capability and cannot move files between separate host machines.

---

**Question 20**

An administrator runs `docker build -t myapp:latest .` and notices the build takes 4 minutes each time even when only a single source file changes. The Dockerfile structure is: `FROM node:18`, `COPY . /app`, `RUN npm install`, `CMD ["node", "app.js"]`. What refactoring would most reduce rebuild time?

A) Replace `FROM node:18` with `FROM scratch` to eliminate the base image overhead.
B) Move `COPY . /app` to after `CMD` so source files are copied last.
C) Split the copy into two steps: first `COPY package.json /app/`, then `RUN npm install`, then `COPY . /app/` — so the expensive `npm install` layer is only invalidated when `package.json` changes, not on every source file change.
D) Add `--no-cache` to the build command so Docker skips cache checks and builds faster.

*   **Correct Answer:** C) Split the copy into two steps: first `COPY package.json /app/`, then `RUN npm install`, then `COPY . /app/` — so the expensive `npm install` layer is only invalidated when `package.json` changes, not on every source file change.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `FROM scratch` is for building minimal images that contain only a statically compiled binary. A Node.js application requires the Node.js runtime — replacing the base image with `scratch` would cause the container to fail at startup because `node` would not exist. This does not address the caching issue.
    *   *Why B is incorrect:* `CMD` is the container startup command and is typically the last instruction. Moving `COPY` after `CMD` has no effect on layer ordering during the build — Docker executes Dockerfile instructions top-to-bottom. `CMD` does not execute during build; it only sets the default command for container startup.
    *   *Why D is incorrect:* `--no-cache` disables the layer cache entirely, forcing Docker to rebuild every layer from scratch on every run. This would make rebuilds slower, not faster. The correct optimization is to structure the Dockerfile to maximize cache hits for expensive layers.
