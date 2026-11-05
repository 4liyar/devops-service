
# DevOps Service Application

## Project Description

This project is a simple web service developed using Python Flask as part of a DevOps project.

The application provides a service information page, a health check endpoint, and application version information.

## Features

- Service information page (`/`)
- Health check endpoint (`/health`)
- Application version endpoint (`/version`)
- HTTP 200 response when the application is healthy
- HTTP 404 response for invalid URLs

## Technologies Used

- Ubuntu Linux
- Python 3
- Flask
- Git and GitHub
- Docker (planned)
- CI/CD pipeline (planned)

## Installation

Clone the repository and open the project directory.

Create a Python virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask application:

```bash
python app.py
```

The application runs on port 5000.

## Endpoints

| Endpoint | Description |
|---|---|
| `/` | Displays service information and application version |
| `/health` | Returns application health status |
| `/version` | Returns the current application version |

## Application Version

Current version: `v1.0.0`

The application version can be configured using the `APP_VERSION` environment variable.

## Testing

Automated tests will be added using pytest.

## Project Structure

The repository will contain application source code, tests, a Dockerfile, dependencies, CI/CD configuration, and documentation.

## Author

Individual DevOps Project
