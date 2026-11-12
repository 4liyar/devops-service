import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200



def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.is_json
    assert response.json["status"] == "healthy"
    assert response.json["service"] == "devops-service"
    assert response.json["version"] == "v1.1.0"
    assert isinstance(response.json["uptime_seconds"], int)
    assert response.json["uptime_seconds"] >= 0


def test_version_endpoint(client):
    response = client.get("/version")
    assert response.status_code == 200


def test_invalid_route(client):
    response = client.get("/invalid-route")
    assert response.status_code == 404
