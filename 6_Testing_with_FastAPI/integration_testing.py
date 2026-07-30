# tests/integration/test_web_service.py

import os
os.environ["USE_FAKE_DB"] = "true"  # Use fake data layer

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_get_task():
    # Create
    response = client.post("/tasks", json={"title": "Test Task"})
    assert response.status_code == 201
    task_id = response.json()["id"]

    # Get
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
    
    
    
# The fake data layer replaces the real database, but everything else is real.