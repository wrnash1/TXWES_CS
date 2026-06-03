# Reading Guide: Module 15 - Containerization: Docker Basics on Linux

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Exam Domain:** Domain 4.0 - Automation and Scripting

---

### Glossary

**Container** - A running instance of a Docker image. Uses Linux namespaces and cgroups for isolation. Shares the host kernel. Starts in milliseconds. Has a writable layer on top of the read-only image.

**Image** - A read-only template used to create containers. Built from a Dockerfile. Stored in layers. Multiple containers can run from the same image simultaneously.

**Namespace** - A Linux kernel feature that provides isolated views of system resources (PIDs, network interfaces, mounts, users, hostnames) for each container.

**cgroup (control group)** - A Linux kernel feature that limits and accounts for the CPU, memory, disk I/O, and network resources available to a set of processes.

**Dockerfile** - A text file containing instructions for building a Docker image. Each instruction creates a new image layer.

**Docker Hub** - The default public registry for Docker images. Images are pulled from Docker Hub when no registry is specified.

**Volume** - Docker-managed persistent storage stored in `/var/lib/docker/volumes/`. Survives container removal. Preferred over bind mounts for production data.

**Bind mount** - Maps a specific host directory into a container. Changes on either side are immediately visible on the other. Common in development workflows.

**Port mapping** - Publishing a container port on the host using `-p HOST_PORT:CONTAINER_PORT`. Makes the containerized service accessible from outside the container.

**Build context** - The directory passed to `docker build`. Files referenced in `COPY` instructions must exist in the build context.

---

### Container vs VM Comparison

| Feature | Container | Virtual Machine |
|---------|-----------|----------------|
| Kernel | Shares host kernel | Full guest OS kernel |
| Isolation mechanism | Namespaces + cgroups | Hypervisor hardware boundary |
| Startup time | Milliseconds | Seconds to minutes |
| Image size | Megabytes | Gigabytes |
| Security isolation | Weaker (shared kernel) | Stronger (full OS boundary) |
| Portability | High | Hypervisor-dependent |

---

### Docker Installation (Ubuntu)

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

After `usermod`, log out and back in for the docker group to take effect.

---

### Essential Docker CLI Commands

| Command | Purpose |
|---------|---------|
| `docker images` | List local images |
| `docker pull IMAGE` | Download image from registry |
| `docker run IMAGE` | Create and start a container |
| `docker run -d IMAGE` | Run detached (background) |
| `docker run -it IMAGE CMD` | Run interactive with TTY |
| `docker run -p H:C IMAGE` | Map host port H to container port C |
| `docker run --name NAME IMAGE` | Assign a container name |
| `docker run -v VOL:PATH IMAGE` | Mount volume at PATH |
| `docker run -e KEY=VAL IMAGE` | Set environment variable |
| `docker run --rm IMAGE` | Auto-remove container when it stops |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers (including stopped) |
| `docker stop NAME` | Stop a running container (SIGTERM) |
| `docker start NAME` | Start a stopped container |
| `docker restart NAME` | Stop + start |
| `docker rm NAME` | Remove a stopped container |
| `docker rm -f NAME` | Force remove (stop + delete) |
| `docker rmi IMAGE` | Remove an image |
| `docker logs NAME` | Show container stdout/stderr |
| `docker logs -f NAME` | Follow log output |
| `docker exec -it NAME bash` | Open interactive shell in container |
| `docker exec NAME CMD` | Run command in running container |
| `docker inspect NAME` | Show detailed container/image JSON |
| `docker stats` | Live resource usage for all containers |

---

### Docker Volume Commands

| Command | Purpose |
|---------|---------|
| `docker volume create NAME` | Create a named volume |
| `docker volume ls` | List volumes |
| `docker volume inspect NAME` | Show volume details |
| `docker volume rm NAME` | Remove a volume |
| `docker volume prune` | Remove all unused volumes |

Volume mount syntax: `-v NAME:CONTAINER_PATH`

Bind mount syntax: `-v /host/path:/container/path`

---

### Docker Network Commands

| Command | Purpose |
|---------|---------|
| `docker network ls` | List networks |
| `docker network create NAME` | Create a custom bridge network |
| `docker network inspect NAME` | Show network details |
| `docker network connect NET CONTAINER` | Connect container to network |
| `docker network rm NAME` | Remove a network |

Containers on a custom bridge network can resolve each other by container name. Containers on the default `bridge` network cannot resolve by name — IP only.

---

### Dockerfile Instruction Reference

| Instruction | Purpose |
|-------------|---------|
| `FROM IMAGE` | Set base image (must be first instruction) |
| `RUN CMD` | Execute command during build; creates a layer |
| `COPY SRC DEST` | Copy files from build context into image |
| `ADD SRC DEST` | Like COPY; also handles URLs and tar extraction |
| `ENV KEY=VALUE` | Set environment variable |
| `EXPOSE PORT` | Document port (does not publish to host) |
| `CMD ["CMD","ARG"]` | Default command; overridable with `docker run CMD` |
| `ENTRYPOINT ["CMD"]` | Fixed entry command; CMD provides arguments |
| `WORKDIR PATH` | Set working directory for subsequent instructions |
| `USER NAME` | Set user for subsequent instructions |
| `LABEL key=value` | Add metadata to the image |

---

### Docker Build and Push Workflow

```bash
docker build -t myapp:1.0 .
docker tag myapp:1.0 user/myapp:1.0
docker login
docker push user/myapp:1.0
docker pull user/myapp:1.0
```

---

### Image Management Commands

| Command | Purpose |
|---------|---------|
| `docker image prune` | Remove dangling (untagged) images |
| `docker image prune -a` | Remove all unused images |
| `docker save -o FILE.tar IMAGE` | Export image to tar file |
| `docker load -i FILE.tar` | Import image from tar file |
| `docker system df` | Show disk usage |
| `docker system prune` | Remove stopped containers, unused networks, dangling images |
| `docker system prune -a` | Also remove all unused images |

---

### Exam Tips

1. Containers share the host kernel via namespaces and cgroups. VMs have a full guest OS on a hypervisor. This is the most fundamental distinction and is directly tested.

2. `docker ps` shows only running containers. `docker ps -a` shows all. `docker stop` does not delete. `docker rm` is required to delete. Confusing stop with delete is a common exam trap.

3. `-p HOST:CONTAINER` maps ports. `-v NAME:PATH` mounts volumes. `-e KEY=VALUE` sets environment variables. `-d` runs detached. `-it` runs interactive with TTY. Know all five flags.

4. `docker logs NAME` reads stdout/stderr from the container's main process. `docker exec -it NAME bash` opens a shell inside a running container. These are different operations.

5. Volumes in `/var/lib/docker/volumes/` survive container removal. Bind mounts map host directories directly. Use volumes for databases in production; bind mounts for development source code.

6. Dockerfile: `FROM` is always first. `RUN` creates a new layer. `COPY` copies from the build context on the host. `EXPOSE` only documents a port — it does not publish it. `CMD` is the default command.

7. The build context is the directory passed to `docker build`. `COPY` can only reference files within the build context. Files outside it cause "not found in build context" errors.

8. `docker system prune` removes stopped containers, unused networks, and dangling images. Adding `-a` also removes all unused images. Use `docker system df` to see what is consuming disk space before pruning.

---

### Study Checklist

Before the quiz and lab, confirm you can do all of the following without looking them up:

* Explain how containers differ from VMs in terms of kernel sharing and isolation mechanism
* Run a container in detached mode with port mapping and a named volume
* View running containers and all containers including stopped ones
* Stop, start, and remove a container
* Open an interactive shell inside a running container with docker exec
* View container log output and follow it in real time
* Write a minimal Dockerfile with FROM, RUN, COPY, EXPOSE, and CMD
* Build an image from a Dockerfile
* Explain the difference between a Docker volume and a bind mount
* Remove stopped containers and unused images with docker system prune
