# End-to-end tests hit the real API with a real database. They're slow but realistic.


# tests/e2e/test_tasks_api.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestTasksAPI:

    def test_full_crud_flow(self):
        # Create
        create_response = client.post(
            "/tasks",
            json={"title": "E2E Test", "description": "Testing"}
        )
        assert create_response.status_code == 201
        task = create_response.json()
        task_id = task["id"]

        # Read
        get_response = client.get(f"/tasks/{task_id}")
        assert get_response.status_code == 200
        assert get_response.json()["title"] == "E2E Test"

        # Update
        update_response = client.patch(
            f"/tasks/{task_id}",
            json={"completed": True}
        )
        assert update_response.status_code == 200
        assert update_response.json()["completed"] == True

        # Delete
        delete_response = client.delete(f"/tasks/{task_id}")
        assert delete_response.status_code == 204

        # Verify deleted
        get_deleted = client.get(f"/tasks/{task_id}")
        assert get_deleted.status_code == 404