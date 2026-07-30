# pytest fixtures provide test data and setup/teardown

# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def sample_task():
    return {"title": "Test Task", "description": "A test"}

@pytest.fixture
def auth_headers():
    # Get a real token or fake one for testing
    return {"Authorization": "Bearer test-token"}
# tests/test_api.py
def test_create_task(client, sample_task, auth_headers):
    response = client.post("/tasks", json=sample_task, headers=auth_headers)
    assert response.status_code == 201
    
    
    
    
    
    
# Database Fixtures with Cleanup

@pytest.fixture
def test_db():
    """Create a test database, yield it, then clean up."""
    # Setup
    db = create_test_database()

    yield db  # Test runs here

    # Teardown
    db.drop_all_tables()
    db.close()

def test_with_database(test_db):
    # test_db is a fresh database
    test_db.add(Task(title="Test"))
    assert test_db.query(Task).count() == 1