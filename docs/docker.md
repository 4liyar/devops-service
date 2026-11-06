

# Docker Deployment Documentation

## 1. Application Information

Application Name: DevOps Service

Application Version: v1.0.0

Framework: Python Flask

Container Image: devops-service:v1.0.0

## 2. Build the Docker Image

Run the following command from the project directory:

```bash
sudo docker build -t devops-service:v1.0.0 .
```

This command builds the application image using the Dockerfile.

## 3. Start the Docker Container

```bash
sudo docker run -d \
  --name devops-service-container \
  -p 127.0.0.1:8080:5000 \
  devops-service:v1.0.0
```

The container starts the Flask application using `python app.py`.

## 4. Port Mapping

Host Address: 127.0.0.1

Host Port: 8080

Container Port: 5000

The application is accessible only from the Ubuntu machine through:

http://127.0.0.1:8080

## 5. Application Configuration

The application uses the APP_VERSION environment variable.

Default application version: v1.0.0

To override the version when starting a new container, use:

```bash
sudo docker run -d \
  --name devops-service-custom \
  -p 127.0.0.1:8081:5000 \
  -e APP_VERSION=v1.0.1 \
  devops-service:v1.0.0
```

## 6. Check Container Status

```bash
sudo docker ps
```

## 7. View Application Logs

```bash
sudo docker logs devops-service-container
```

To follow logs continuously:

```bash
sudo docker logs -f devops-service-container
```

Press Ctrl+C to stop following logs.


## 8. Health Check

The application provides a `/health` endpoint to check
whether the Flask web service is responding successfully.

### Test the Health Endpoint

Run:

```bash
curl -i http://127.0.0.1:8080/health
```

Expected HTTP status:

```text
HTTP/1.1 200 OK
```

Expected JSON response:

```json
{
  "service": "DevOps Service",
  "status": "healthy",
  "version": "v1.0.0"
}
```

### Response Fields

| Field | Description |
|---|---|
| service | Identifies the application |
| status | Indicates the application health |
| version | Displays the application version |

### Health Check Purpose

The health endpoint helps verify that the application
is running and responding to HTTP requests.

The endpoint returns HTTP 200 when the application
is healthy.

This basic health check does not verify external
services such as databases.


## 9. Non-Root Security

The container runs as the appuser account rather than root.

Verify using:

```bash
sudo docker exec devops-service-container id
```

The user ID must not be 0.

## 10. Stop and Restart

Stop:

```bash
sudo docker stop devops-service-container
```

Restart:

```bash
sudo docker start devops-service-container
```

## 11. Network Security

The published service port is bound to 127.0.0.1.

This prevents direct access through the host's external network interfaces and limits access to the local Ubuntu environment.

