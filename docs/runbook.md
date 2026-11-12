# Deployment Runbook & Checklist (Version v1.0.0 and v1.1.0)

## 1. Prerequisites
- [x] Ensure Docker Desktop is installed and running on the target system/host.
- [x] Verify that the code has passed all CI checks and the latest changes are pulled from the `main` branch.
- [x] Ensure sufficient privileges/permissions to execute Docker commands on the host machine.

## 2. Artifact Identification
- **Service Name:** devops-service
- **Release Version:** v1.0.0/v1.1.0
- **Git Commit SHA:** (e.g., retrieve via `git rev-parse HEAD`)
- **Docker Image Tag:** `devops-service:v1.0.0/1.1.0`

## 3. Deployment Steps
1. Build the Docker image tagged with the specific release version:
   ```bash
   docker build -t devops-service:v1.0.0 .
   docker build -t devops-service:v1.1.0 .

2. remove old Container
   docker rm -f service-v1
   docker rm -f service-v1-1

3. run first v1.0.0
docker run -d -p 5000:5000 --name service-v1 -e APP_VERSION=v1.0.0 devops-service:v1.0.0
   Check 
   curl.exe http://localhost:5000/health
   

4. run second v1.1.0
docker run -d -p 5001:5000 --name service-v1-1 -e APP_VERSION=v1.1.0 devops-service:v1.1.0
   Check
   curl.exe http://localhost:5001/health

