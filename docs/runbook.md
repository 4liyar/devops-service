# Deployment Runbook & Checklist (Version v1.0.0)

## 1. Prerequisites
- [ ] Ensure Docker Desktop is installed and running on the target system/host.
- [ ] Verify that the code has passed all CI checks and the latest changes are pulled from the `main` branch.
- [ ] Ensure sufficient privileges/permissions to execute Docker commands on the host machine.

## 2. Artifact Identification
- **Service Name:** devops-service
- **Release Version:** v1.0.0
- **Git Commit SHA:** (e.g., retrieve via `git rev-parse HEAD`)
- **Docker Image Tag:** `devops-service:v1.0.0`

## 3. Deployment Steps
1. Build the Docker image tagged with the specific release version:
   ```bash
   docker build -t devops-service:v1.0.0 .بسدث
