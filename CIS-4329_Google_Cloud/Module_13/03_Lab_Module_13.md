# Lab: Module 13 — CI/CD with Cloud Build and Artifact Registry

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Lab Overview

In this lab you will create an Artifact Registry Docker repository, write a
`cloudbuild.yaml` build pipeline, connect it to a Cloud Source Repository, and trigger
an automated build. You will verify the Docker image is pushed to Artifact Registry and
explore the build logs.

**Estimated time**: 60–75 minutes

**Cost estimate**: Under $1.00 USD if completed and cleaned up within the session

---

### Prerequisites

- A GCP project with billing enabled
- Cloud Shell or gcloud CLI authenticated
- APIs enabled:

```bash
gcloud services enable \
  cloudbuild.googleapis.com \
  artifactregistry.googleapis.com \
  sourcerepo.googleapis.com
```

---

### Part 1: Create Artifact Registry Repository

#### Task 1.1: Create a Docker Repository

```bash
gcloud config set project YOUR_PROJECT_ID

# Create a Docker repository in us-central1
gcloud artifacts repositories create lab13-repo \
  --repository-format=docker \
  --location=us-central1 \
  --description="Lab 13 Docker images"

# Verify creation
gcloud artifacts repositories list --location=us-central1

# Configure Docker authentication for Artifact Registry
gcloud auth configure-docker us-central1-docker.pkg.dev
```

---

### Part 2: Create a Sample Application

#### Task 2.1: Create Application Files

```bash
mkdir ~/lab13-app && cd ~/lab13-app

# Create a simple Python web app
cat > app.py << 'EOF'
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    version = os.environ.get('APP_VERSION', '1.0')
    return f'<h1>Lab 13 CI/CD App — Version {version}</h1>'

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
EOF

# Create requirements.txt
cat > requirements.txt << 'EOF'
flask==3.0.0
EOF

# Create Dockerfile
cat > Dockerfile << 'EOF'
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
ENV APP_VERSION=1.0
EXPOSE 8080
CMD ["python", "app.py"]
EOF
```

#### Task 2.2: Test the Docker Build Locally (Cloud Shell)

```bash
# Build the image locally in Cloud Shell
docker build -t lab13-app:local .

# Run locally to verify it works
docker run -d -p 8080:8080 --name lab13-test lab13-app:local

# Test the endpoint
curl http://localhost:8080/

# Stop the local container
docker stop lab13-test && docker rm lab13-test
```

---

### Part 3: Create the Cloud Build Configuration

#### Task 3.1: Write cloudbuild.yaml

```bash
cat > cloudbuild.yaml << 'EOF'
steps:
  # Step 1: Build the Docker image
  - name: 'gcr.io/cloud-builders/docker'
    id: 'build-image'
    args:
      - 'build'
      - '-t'
      - 'us-central1-docker.pkg.dev/$PROJECT_ID/lab13-repo/lab13-app:$COMMIT_SHA'
      - '-t'
      - 'us-central1-docker.pkg.dev/$PROJECT_ID/lab13-repo/lab13-app:latest'
      - '.'

  # Step 2: Push commit SHA tag
  - name: 'gcr.io/cloud-builders/docker'
    id: 'push-sha-tag'
    waitFor: ['build-image']
    args:
      - 'push'
      - 'us-central1-docker.pkg.dev/$PROJECT_ID/lab13-repo/lab13-app:$COMMIT_SHA'

  # Step 3: Push latest tag
  - name: 'gcr.io/cloud-builders/docker'
    id: 'push-latest-tag'
    waitFor: ['build-image']
    args:
      - 'push'
      - 'us-central1-docker.pkg.dev/$PROJECT_ID/lab13-repo/lab13-app:latest'

images:
  - 'us-central1-docker.pkg.dev/$PROJECT_ID/lab13-repo/lab13-app:$COMMIT_SHA'
  - 'us-central1-docker.pkg.dev/$PROJECT_ID/lab13-repo/lab13-app:latest'

timeout: '600s'

options:
  logging: CLOUD_LOGGING_ONLY
EOF
```

Note that steps 2 and 3 both have `waitFor: ['build-image']` so they run in parallel
after the build completes.

---

### Part 4: Grant Cloud Build Permissions

The Cloud Build service account needs write access to Artifact Registry:

```bash
# Get the project number
PROJECT_NUMBER=$(gcloud projects describe YOUR_PROJECT_ID \
  --format="value(projectNumber)")

# Grant Artifact Registry Writer to Cloud Build service account
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com" \
  --role="roles/artifactregistry.writer"
```

---

### Part 5: Run a Manual Build

#### Task 5.1: Trigger a Build from the Current Directory

```bash
cd ~/lab13-app

# Submit a build manually (no trigger needed for manual submission)
gcloud builds submit \
  --config=cloudbuild.yaml \
  --project=YOUR_PROJECT_ID \
  .
```

#### Task 5.2: Monitor the Build

```bash
# List recent builds
gcloud builds list --limit=5

# Get the latest build ID
BUILD_ID=$(gcloud builds list --limit=1 --format="value(id)")
echo "Build ID: $BUILD_ID"

# Stream build logs
gcloud builds log $BUILD_ID --stream
```

#### Task 5.3: Verify Image in Artifact Registry

```bash
# List images in the repository
gcloud artifacts docker images list \
  us-central1-docker.pkg.dev/YOUR_PROJECT_ID/lab13-repo \
  --format="table(image,tags,createTime)"
```

Confirm that the image appears with both a SHA tag and a `latest` tag.

---

### Part 6: Create a Cloud Source Repository Trigger (Optional)

If time permits, connect the build to a Cloud Source Repository:

```bash
# Create a Cloud Source Repository
gcloud source repos create lab13-source-repo

# Initialize git and push
cd ~/lab13-app
git init
git add .
git commit -m "Initial application commit"
git remote add google \
  https://source.developers.google.com/p/YOUR_PROJECT_ID/r/lab13-source-repo
git push google main

# Create a trigger that fires on push to main
gcloud builds triggers create cloud-source-repositories \
  --repo=lab13-source-repo \
  --branch-pattern="^main$" \
  --build-config=cloudbuild.yaml \
  --description="Build on push to main"

# List triggers
gcloud builds triggers list
```

---

### Part 7: Reflection Questions

1. Steps 2 and 3 in your `cloudbuild.yaml` used `waitFor: ['build-image']`. Draw a
   diagram showing the dependency order of all three steps and explain why this structure
   reduces build time.
2. You pushed two tags to Artifact Registry: `$COMMIT_SHA` and `latest`. What is the
   advantage of tagging with `$COMMIT_SHA` rather than only using `latest`?
3. What IAM role did you grant to the Cloud Build service account, and why is this
   permission required?
4. If the Cloud Build service account did not have the Artifact Registry Writer role,
   at which step would the build fail? What error would you expect to see in the logs?
5. In a production CI/CD pipeline, what additional step would you add between the build
   step and the push step to improve confidence before publishing the image?

---

### Part 8: Cleanup

```bash
# Delete images from Artifact Registry
gcloud artifacts docker images delete \
  us-central1-docker.pkg.dev/YOUR_PROJECT_ID/lab13-repo/lab13-app \
  --delete-tags --quiet

# Delete the repository
gcloud artifacts repositories delete lab13-repo \
  --location=us-central1 --quiet

# Remove IAM binding (optional cleanup)
PROJECT_NUMBER=$(gcloud projects describe YOUR_PROJECT_ID \
  --format="value(projectNumber)")
gcloud projects remove-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com" \
  --role="roles/artifactregistry.writer"
```

---

### Submission Checklist

- Artifact Registry Docker repository created
- Application files (app.py, Dockerfile, requirements.txt) created
- cloudbuild.yaml written with 3 steps including parallel push steps
- Cloud Build service account granted Artifact Registry Writer role
- Build submitted successfully with gcloud builds submit
- Build logs reviewed showing all steps completed
- Image verified in Artifact Registry with SHA and latest tags
- All 5 reflection questions answered
- Resources cleaned up

---

### Grading Rubric

| Task | Points |
|---|---|
| Artifact Registry repository created | 10 |
| Application files and Dockerfile created | 10 |
| cloudbuild.yaml with parallel steps | 20 |
| IAM permission granted correctly | 10 |
| Build submitted and completed successfully | 25 |
| Image verified in Artifact Registry | 10 |
| Reflection questions answered | 10 |
| Resources cleaned up | 5 |
| **Total** | **100** |
