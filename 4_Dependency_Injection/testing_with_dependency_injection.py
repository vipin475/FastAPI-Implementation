from fastapi.testclient import TestClient

# Fake database for testing
def get_fake_db():
    return FakeDatabase()

# Override the real dependency with fake
app.dependency_overrides[get_db] = get_fake_db

client = TestClient(app)

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200