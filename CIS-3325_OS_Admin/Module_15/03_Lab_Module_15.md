# Lab Activity: Module 15 - Containerization: Docker Basics on Linux

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Time:** 75 minutes
**Points:** 100

---

### Objectives

By the end of this lab you will be able to:

* Install Docker and verify the installation
* Run containers in interactive and detached modes
* Manage the container lifecycle (stop, start, remove)
* Use volumes for persistent storage
* View container logs and execute commands inside running containers
* Write a Dockerfile and build a custom image
* Use docker system prune to clean up unused resources

---

### Prerequisites

* Ubuntu 22.04 LTS virtual machine with sudo access
* Internet access for pulling images from Docker Hub

---

### Part 1 — Docker Installation and Setup (10 points)

#### Step 1.1 — Install Docker

```bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl enable --now docker
docker --version
```

#### Step 1.2 — Add your user to the docker group

```bash
sudo usermod -aG docker $USER
```

Log out and back in, then verify you can run docker without sudo:

```bash
docker info | head -10
```

If you see output without a permission error, the group membership is active.

#### Step 1.3 — Run the hello-world test

```bash
docker run hello-world
```

This pulls the `hello-world` image and runs a container that prints a success message. Confirm you see "Hello from Docker!"

---

### Part 2 — Container Basics (20 points)

#### Step 2.1 — Run an interactive container

```bash
docker run -it ubuntu bash
```

You are now inside a container. Run these commands:

```bash
cat /etc/os-release
hostname
ps aux
exit
```

Note that the container has its own hostname and process table. When you `exit`, the container stops.

#### Step 2.2 — Run a detached container

```bash
docker run -d -p 8080:80 --name webserver nginx
```

#### Step 2.3 — Verify it is running

```bash
docker ps
curl http://localhost:8080/
```

You should see the nginx welcome page HTML output.

#### Step 2.4 — View container logs

```bash
docker logs webserver
docker logs --tail 5 webserver
```

Each `curl` request generated a log entry. Try accessing the server a few more times and then run `docker logs webserver` to see the requests accumulate.

#### Step 2.5 — Execute a command inside the running container

```bash
docker exec webserver cat /etc/nginx/nginx.conf
docker exec -it webserver bash
```

Inside the container, run `nginx -v` to check the version, then `exit`.

---

### Part 3 — Container Lifecycle (15 points)

#### Step 3.1 — Stop the container and verify

```bash
docker stop webserver
docker ps
docker ps -a
```

Confirm that `docker ps` shows no running containers but `docker ps -a` still shows `webserver` in a stopped state.

#### Step 3.2 — Start the container again

```bash
docker start webserver
docker ps
curl http://localhost:8080/
```

The container resumes. Its configuration and state are preserved.

#### Step 3.3 — Remove the container

```bash
docker stop webserver
docker rm webserver
docker ps -a
```

Confirm the container no longer appears in `docker ps -a`.

#### Step 3.4 — Use --rm for automatic cleanup

```bash
docker run --rm -d -p 8080:80 --name tempweb nginx
curl http://localhost:8080/
docker stop tempweb
docker ps -a
```

With `--rm`, stopping the container also removes it. Confirm it is gone from `docker ps -a`.

---

### Part 4 — Volumes for Persistent Data (15 points)

#### Step 4.1 — Create a named volume

```bash
docker volume create labdata
docker volume ls
docker volume inspect labdata
```

Note the `Mountpoint` field — this is where Docker stores the volume on the host.

#### Step 4.2 — Run a container with the volume

```bash
docker run -d --name vol-demo \
  -v labdata:/data \
  ubuntu sleep 3600
```

#### Step 4.3 — Write data to the volume

```bash
docker exec vol-demo bash -c 'echo "persistent data $(date)" > /data/test.txt'
docker exec vol-demo cat /data/test.txt
```

#### Step 4.4 — Destroy the container and verify data persists

```bash
docker rm -f vol-demo
docker volume inspect labdata
```

The volume still exists. Verify the data survived:

```bash
docker run --rm -v labdata:/data ubuntu cat /data/test.txt
```

The file is still there — the data outlived the container.

#### Step 4.5 — Clean up the volume

```bash
docker volume rm labdata
```

---

### Part 5 — Dockerfile and Custom Image (25 points)

#### Step 5.1 — Create a project directory

```bash
mkdir -p ~/lab15-image/html
cd ~/lab15-image
```

#### Step 5.2 — Create a custom HTML page

```bash
cat > html/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head><title>Lab 15 - Docker Build</title></head>
<body>
<h1>Lab 15 Custom Image</h1>
<p>Built with Docker on: BUILDDATE</p>
</body>
</html>
EOF
```

#### Step 5.3 — Write the Dockerfile

```bash
cat > Dockerfile << 'EOF'
FROM nginx:alpine

LABEL maintainer="lab15-student"

RUN sed -i "s/BUILDDATE/$(date +%Y-%m-%d)/" /dev/null || true

COPY html/ /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
EOF
```

#### Step 5.4 — Build the image

```bash
docker build -t lab15-web:1.0 .
docker images | grep lab15
```

Confirm the image appears with the tag `lab15-web:1.0`.

#### Step 5.5 — Run the custom image

```bash
docker run -d -p 8081:80 --name lab15-container lab15-web:1.0
curl http://localhost:8081/
```

You should see your custom HTML page. Confirm the heading "Lab 15 Custom Image" appears.

#### Step 5.6 — Inspect the image layers

```bash
docker history lab15-web:1.0
```

Note each layer corresponds to a Dockerfile instruction. The `COPY` instruction created a small layer. The `FROM nginx:alpine` provides the base layers.

#### Step 5.7 — Clean up

```bash
docker stop lab15-container
docker rm lab15-container
```

---

### Part 6 — System Cleanup (15 points)

#### Step 6.1 — Check disk usage

```bash
docker system df
```

Shows how much disk space is used by images, containers, and volumes.

#### Step 6.2 — Create some garbage to clean up

```bash
docker run --name junk1 ubuntu echo "unused container 1"
docker run --name junk2 ubuntu echo "unused container 2"
docker images | grep ubuntu
```

#### Step 6.3 — Run docker system prune

```bash
docker system prune
```

Answer `y` when prompted. This removes:

* All stopped containers
* All unused networks
* All dangling (untagged) images

Verify:

```bash
docker ps -a
docker images
docker system df
```

#### Step 6.4 — Remove the lab image

```bash
docker rmi lab15-web:1.0
docker images
```

---

### Analysis Questions

Answer these questions in writing after completing the lab. Submit with your lab screenshots.

1. Explain what happens to data written inside a container when the container is removed, and explain how a named volume solves this problem. What is the host path where Docker stores named volume data?

2. What is the difference between `docker stop` and `docker rm`? What does `docker ps -a` show that `docker ps` does not? What flag on `docker run` causes a container to be automatically removed when it stops?

3. In the Dockerfile you wrote, explain the purpose of each instruction: `FROM`, `COPY`, `EXPOSE`, and `CMD`. Why is `EXPOSE` insufficient to make the container's port accessible from the host?

4. You run `docker build -t myapp:1.0 .` and receive an error: "COPY failed: file not found in build context: stat config.json: file does not exist." What does this mean and how do you fix it?

5. What does `docker system prune` remove? What does adding `-a` change? Why is it important to run `docker system df` before pruning on a production server?

---

### Submission Requirements

* Screenshots of each Part completion (terminal output visible)
* Written answers to all 5 analysis questions
* Include the output of `docker history lab15-web:1.0` showing the image layers

---

### Grading Rubric

| Component | Points |
|-----------|--------|
| Part 1: Docker installed and hello-world verified | 10 |
| Part 2: Container run, logs viewed, exec used | 20 |
| Part 3: Lifecycle (stop/start/rm/--rm) demonstrated | 15 |
| Part 4: Volume created, data written, survived container removal | 15 |
| Part 5: Dockerfile written, image built and run | 25 |
| Part 6: System prune executed and verified | 15 |
| **Total** | **100** |
