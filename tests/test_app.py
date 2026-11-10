
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
    assert b"Team Service Information" in response.data
    assert b"v1.0.0" in response.data



def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert "service" in data
    assert "version" in data



def test_version_endpoint(client):
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json["version"] == "v1.0.0"


def test_invalid_route(client):
    response = client.get("/invalid")
    assert response.status_code == 404
