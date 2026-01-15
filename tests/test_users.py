from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/users",
        json={"name": "Meghna", "email": "meghna@test.com", "age": 21}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Meghna"


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_user():
    response = client.put(
        "/users/1",
        json={"name": "Updated Name", "email": "updated@test.com", "age": 22}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Name"


def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
