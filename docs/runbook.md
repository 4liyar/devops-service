# Deployment Runbook & Checklist (Version v1.0.0 and v1.1.0)

## 1. Prerequisites
- [x] Ensure Docker Desktop is installed and running on the target system/host.
- [x] Verify that the code has passed all CI checks and the latest changes are pulled from the main branch.
- [x] Ensure sufficient privileges/permissions to execute Docker commands on the host machine.

## 2. Artifact Identification
- *Service Name:* devops-service
- *Release Versions:* v1.0.0 (Commit: a060527) and v1.1.0 (Commit: 34d3ffa)
- *Docker Image Tags:* devops-service:v1.0.0 and devops-service:v1.1.0
- *CI Artifact Retention:* Retained automatically by GitHub Actions upon successful CI completion.


## 3. Deployment Steps
1. Build the Docker image tagged with the specific release version:
   ```bash
   docker build -t devops-service:v1.0.0 .
   docker build -t devops-service:v1.1.0 .

2. remove old Container:
   ```bash
   docker rm -f service-v1
   docker rm -f service-v1-1

3. run first v1.0.0:
   ```bash
   docker run -d -p 5000:5000 --name service-v1 -e APP_VERSION=v1.0.0 devops-service:v1.0.0

4. Check 
   ```bash
   curl.exe http://localhost:5000/health


5. run second v1.1.0:
   ```bash
   docker run -d -p 5001:5000 --name service-v1-1 -e APP_VERSION=v1.1.0 devops-service:v1.1.0


6. Check
   ```bash
   curl.exe http://localhost:5001/health


## 4. Rollback Steps
If v1.1.0 fails health checks or encounters an error after deployment:
1. Stop and remove the faulty v1.1.0 container:
   ```bash
   docker rm -f service-v1-1
2. Restore and verify the previous known working release (v1.0.0):
   ```bash
   docker run -d -p 5000:5000 --name service-v1 -e APP_VERSION=v1.0.0 devops
   service:v1.0.0
   curl.exe http://localhost:5000/health
