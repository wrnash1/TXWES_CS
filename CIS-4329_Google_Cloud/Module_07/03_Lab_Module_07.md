# Lab: Module 07 — Cloud Run and Serverless Computing

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Lab Overview

In this lab you will deploy a Cloud Run service, write and deploy a Cloud
Function, connect them with an Eventarc trigger, and configure traffic splitting
in Cloud Run for a canary deployment.

**Estimated Time:** 80 minutes

**Prerequisites:**

- Active GCP project with billing enabled
- Cloud Run API, Cloud Functions API, and Eventarc API enabled
- Cloud Build API enabled (for container builds)
- Cloud Shell access

**Learning Objectives:**

By the end of this lab you will be able to:

1. Build and deploy a containerized application to Cloud Run
2. Configure Cloud Run autoscaling and traffic splitting
3. Deploy a Cloud Function (Gen 2) with an HTTP trigger
4. Create an Eventarc trigger connecting Cloud Storage to Cloud Run
5. Use Cloud Tasks to enqueue and process work items

---

## Part 1 — Deploy a Cloud Run Service (20 minutes)

### Step 1.1 — Set Environment and Enable APIs

```bash
export PROJECT_ID=$(gcloud config get-value project)
export REGION=us-central1

gcloud services enable \
  run.googleapis.com \
  cloudfunctions.googleapis.com \
  eventarc.googleapis.com \
  cloudbuild.googleapis.com \
  cloudtasks.googleapis.com
```

### Step 1.2 — Create a Simple Container Application

```bash
# Create application directory
mkdir lab07-app && cd lab07-app

# Create the application file
cat > main.py << 'EOF'
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
        "message": "Hello from Cloud Run!",
        "version": os.environ.get("VERSION", "v1"),
        "hostname": os.environ.get("K_SERVICE", "local")
    })

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
EOF

# Create requirements file
cat > requirements.txt << 'EOF'
Flask==3.0.0
gunicorn==21.2.0
EOF

# Create Dockerfile
cat > Dockerfile << 'EOF'
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 main:app
EOF
```

### Step 1.3 — Build and Push the Container

```bash
# Submit build to Cloud Build
gcloud builds submit \
  --tag=gcr.io/$PROJECT_ID/lab07-app:v1

# Verify the image was created
gcloud container images list --repository=gcr.io/$PROJECT_ID
```

### Step 1.4 — Deploy to Cloud Run

```bash
gcloud run deploy lab07-service \
  --image=gcr.io/$PROJECT_ID/lab07-app:v1 \
  --region=$REGION \
  --platform=managed \
  --allow-unauthenticated \
  --set-env-vars=VERSION=v1 \
  --min-instances=0 \
  --max-instances=5 \
  --concurrency=80 \
  --memory=256Mi \
  --cpu=1

# Get the service URL
SERVICE_URL=$(gcloud run services describe lab07-service \
  --region=$REGION \
  --format='value(status.url)')
echo "Service URL: $SERVICE_URL"

# Test the service
curl $SERVICE_URL
```

### Step 1.5 — Deploy V2 and Configure Traffic Splitting

```bash
# Build v2 of the application (update VERSION env var)
gcloud run deploy lab07-service \
  --image=gcr.io/$PROJECT_ID/lab07-app:v1 \
  --region=$REGION \
  --set-env-vars=VERSION=v2 \
  --no-traffic \
  --tag=v2

# List revisions
gcloud run revisions list \
  --service=lab07-service \
  --region=$REGION

# Split traffic: 90% to v1, 10% to v2 (canary)
V2_REVISION=$(gcloud run revisions list \
  --service=lab07-service \
  --region=$REGION \
  --format='value(metadata.name)' \
  --filter="status.conditions[0].status=True" | head -1)

gcloud run services update-traffic lab07-service \
  --region=$REGION \
  --to-revisions=LATEST=10,v1-tag=90

# Test multiple times to see both versions
for i in {1..10}; do curl -s $SERVICE_URL | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['version'])"; done
```

---

## Part 2 — Cloud Function (Gen 2) with HTTP Trigger (15 minutes)

### Step 2.1 — Create the Function

```bash
mkdir ../lab07-function && cd ../lab07-function

cat > main.py << 'EOF'
import functions_framework
import json
from datetime import datetime

@functions_framework.http
def process_event(request):
    """HTTP Cloud Function."""
    request_json = request.get_json(silent=True)
    request_args = request.args

    event_data = request_json or dict(request_args)
    event_data["processed_at"] = datetime.utcnow().isoformat()

    print(f"Processing event: {json.dumps(event_data)}")

    return json.dumps({
        "status": "processed",
        "data": event_data
    }), 200, {"Content-Type": "application/json"}
EOF

cat > requirements.txt << 'EOF'
functions-framework==3.*
EOF
```

### Step 2.2 — Deploy the Function

```bash
gcloud functions deploy lab07-process-fn \
  --gen2 \
  --runtime=python311 \
  --region=$REGION \
  --source=. \
  --entry-point=process_event \
  --trigger-http \
  --allow-unauthenticated \
  --memory=256MiB \
  --timeout=60s

# Get function URL and test
FN_URL=$(gcloud functions describe lab07-process-fn \
  --gen2 --region=$REGION --format='value(serviceConfig.uri)')
echo "Function URL: $FN_URL"

curl -X POST $FN_URL \
  -H "Content-Type: application/json" \
  -d '{"order_id": "12345", "product": "widget"}'
```

---

## Part 3 — Eventarc Trigger (20 minutes)

### Step 3.1 — Create a Cloud Storage Bucket and Service Account

```bash
cd ..

# Create the trigger bucket
export TRIGGER_BUCKET="lab07-events-${PROJECT_ID}"
gcloud storage buckets create gs://$TRIGGER_BUCKET \
  --location=$REGION

# Create a service account for Eventarc
gcloud iam service-accounts create eventarc-sa \
  --display-name="Eventarc Service Account"

export EVENTARC_SA="eventarc-sa@${PROJECT_ID}.iam.gserviceaccount.com"

# Grant Cloud Run invoker to the SA
gcloud run services add-iam-policy-binding lab07-service \
  --region=$REGION \
  --member="serviceAccount:$EVENTARC_SA" \
  --role=roles/run.invoker

# Grant Eventarc event receiver
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$EVENTARC_SA" \
  --role=roles/eventarc.eventReceiver
```

### Step 3.2 — Create the Eventarc Trigger

```bash
# Grant Cloud Storage permission to publish Eventarc events
STORAGE_SA=$(gcloud storage service-agent --project=$PROJECT_ID)
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$STORAGE_SA" \
  --role=roles/pubsub.publisher

# Create the trigger
gcloud eventarc triggers create lab07-storage-trigger \
  --location=$REGION \
  --destination-run-service=lab07-service \
  --destination-run-region=$REGION \
  --event-filters="type=google.cloud.storage.object.v1.finalized" \
  --event-filters="bucket=$TRIGGER_BUCKET" \
  --service-account=$EVENTARC_SA

# Verify trigger creation
gcloud eventarc triggers list --location=$REGION
```

### Step 3.3 — Test the Trigger

```bash
# Upload a file to trigger the event
echo "Lab 07 test file" > test-event.txt
gcloud storage cp test-event.txt gs://$TRIGGER_BUCKET/

# View Cloud Run logs to see the event received (wait 10-20 seconds)
gcloud run services logs read lab07-service \
  --region=$REGION \
  --limit=20
```

---

## Part 4 — Cloud Tasks (15 minutes)

### Step 4.1 — Create a Task Queue

```bash
gcloud tasks queues create lab07-queue \
  --location=$REGION \
  --max-concurrent-dispatches=5 \
  --max-attempts=3

gcloud tasks queues describe lab07-queue --location=$REGION
```

### Step 4.2 — Create a Service Account for Task Authentication

```bash
gcloud iam service-accounts create tasks-sa \
  --display-name="Cloud Tasks Service Account"

export TASKS_SA="tasks-sa@${PROJECT_ID}.iam.gserviceaccount.com"

gcloud run services add-iam-policy-binding lab07-service \
  --region=$REGION \
  --member="serviceAccount:$TASKS_SA" \
  --role=roles/run.invoker
```

### Step 4.3 — Enqueue a Task

```bash
# Enqueue a task to the Cloud Run service
gcloud tasks create-http-task \
  --queue=lab07-queue \
  --location=$REGION \
  --url="${SERVICE_URL}/" \
  --method=GET \
  --oidc-service-account-email=$TASKS_SA \
  --header="X-Task-ID:lab07-task-001"

# List pending tasks
gcloud tasks list --queue=lab07-queue --location=$REGION
```

---

## Lab Deliverables

Submit a lab report containing:

1. Screenshot of `gcloud run services describe lab07-service` showing the
   service URL and revision information.
2. Output of the traffic splitting test loop showing both v1 and v2 responses.
3. Output of the Cloud Function invocation with the processed JSON response.
4. Output of `gcloud eventarc triggers list` showing the storage trigger.
5. Cloud Run log output showing the Eventarc event received after file upload.
6. Output of `gcloud tasks queues describe lab07-queue`.
7. Answers to the lab questions.

**Lab Questions:**

1. What is a Cloud Run revision, and why is the ability to split traffic between
   revisions useful for production deployments?
2. What is the key difference between Cloud Functions Gen 1 and Gen 2 in terms
   of infrastructure and concurrency?
3. When would you use Eventarc instead of a Pub/Sub subscription with a push
   delivery to Cloud Run?
4. A Cloud Run service needs to read from a private Cloud SQL instance. It has
   no external IP and cannot route through the public internet. What GCP
   feature enables this?
5. Your team needs to send 10,000 tasks to a processing service over 24 hours,
   with no more than 10 tasks per second. Which service would you use and why?

---

## Cleanup

```bash
# Delete Cloud Run service
gcloud run services delete lab07-service --region=$REGION --quiet

# Delete Cloud Function
gcloud functions delete lab07-process-fn \
  --gen2 --region=$REGION --quiet

# Delete Eventarc trigger
gcloud eventarc triggers delete lab07-storage-trigger \
  --location=$REGION --quiet

# Delete Cloud Tasks queue
gcloud tasks queues delete lab07-queue --location=$REGION --quiet

# Delete bucket
gcloud storage rm -r gs://$TRIGGER_BUCKET --quiet

# Delete service accounts
gcloud iam service-accounts delete $EVENTARC_SA --quiet
gcloud iam service-accounts delete $TASKS_SA --quiet

# Delete container image
gcloud container images delete gcr.io/$PROJECT_ID/lab07-app:v1 --quiet
```

---

## Part 9 — Challenge Exercise

### Challenge 1: Cloud Run Minimum Instances and Cold Start Comparison

Measure the latency difference between a Cloud Run service with zero minimum
instances versus one with `min-instances=1`.

1. Deploy a second revision of `lab07-service` with `--min-instances=0` and
   wait for it to scale to zero (stop sending traffic for 5 minutes):

```bash
gcloud run services update lab07-service \
  --region=$REGION \
  --min-instances=0 \
  --tag=cold
```

1. Record the response time for the first request after scale-to-zero (cold
   start):

```bash
COLD_URL=$(gcloud run services describe lab07-service \
  --region=$REGION --format='value(status.url)')
time curl -s $COLD_URL > /dev/null
```

1. Update the service to keep at least 1 warm instance and compare:

```bash
gcloud run services update lab07-service \
  --region=$REGION \
  --min-instances=1
sleep 10
time curl -s $COLD_URL > /dev/null
```

1. Record both latency measurements and the cost implication of each
   configuration in your lab report.

### Challenge 2: Cloud Tasks Rate-Limited Queue

Create a Cloud Tasks queue that dispatches tasks at a controlled rate and
observe how rate limiting protects the target Cloud Run service.

1. Create a queue limited to 2 dispatches per second with a 3-retry backoff:

```bash
gcloud tasks queues create lab07-rate-queue \
  --location=$REGION \
  --max-dispatches-per-second=2 \
  --max-concurrent-dispatches=5 \
  --max-attempts=3 \
  --min-backoff=5s \
  --max-backoff=60s
```

1. Enqueue 10 tasks targeting the Cloud Run service URL:

```bash
SERVICE_URL=$(gcloud run services describe lab07-service \
  --region=$REGION --format='value(status.url)')
for i in $(seq 1 10); do
  gcloud tasks create-http-task \
    --queue=lab07-rate-queue \
    --location=$REGION \
    --url="$SERVICE_URL" \
    --body-content="{\"task_id\": $i}"
done
```

1. Monitor the queue and confirm tasks dispatch at no more than 2 per second:

```bash
gcloud tasks queues describe lab07-rate-queue --location=$REGION
```

### Reflection Questions

1. You measured a latency difference between cold-start and warm-instance Cloud
   Run requests. Given this tradeoff, describe a real-world scenario where
   paying for `min-instances=1` is justified, and a scenario where
   `min-instances=0` with cold starts is acceptable.
2. The Cloud Tasks queue you created dispatches at 2 requests per second even
   when 10 tasks are enqueued at once. How does this rate limiting protect the
   downstream Cloud Run service, and what would happen without it if 10,000
   tasks were enqueued simultaneously?

---

End of Lab — Module 07

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash
