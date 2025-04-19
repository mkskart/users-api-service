import pytest
import json
from app import create_app, db
from app.models import User

@pytest.fixture
def client():
    # spin up a Flask app configured for testing with in‑memory SQLite
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    })
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_create_user(client):
    payload = {"name": "Alice", "email": "alice@example.com"}
    resp = client.post(
        "/users",
        data=json.dumps(payload),
        content_type="application/json"
    )
    assert resp.status_code == 201
    data = resp.get_json()
    assert "id" in data
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"

def test_get_user_not_found(client):
    resp = client.get("/users/999")
    assert resp.status_code == 404
    data = resp.get_json()
    assert data["message"] == "User not found"
