# Deployment Notes

- **Service Name:** devops-service
- **Port:** 5000
- **Health Check Endpoint:** http://localhost:5000/health
- **Expected Status:** `{"status":"healthy"}`
- **Deployment Note:** Ensure the container is running and all automated CI checks pass before merging changes to main.
