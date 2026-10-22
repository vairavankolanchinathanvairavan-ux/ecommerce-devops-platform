from app.main import app


def test_home_endpoint():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "running"


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_products_endpoint():
    client = app.test_client()
    response = client.get("/api/products")

    assert response.status_code == 200
    assert len(response.json) == 3
    assert response.json[0]["name"] == "Laptop"
