# main.py
from fastapi import FastAPI, Depends

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/tasks")
def list_tasks(db = Depends(get_db)):
    return db.query(Task).all()






# Override the dependency in tests:

# tests/test_api.py
from fastapi.testclient import TestClient
from main import app, get_db

# Fake database for testing
def get_fake_db():
    return FakeDatabase(tasks=[
        {"id": 1, "title": "Fake Task 1"},
        {"id": 2, "title": "Fake Task 2"},
    ])
# Override the real dependency
app.dependency_overrides[get_db] = get_fake_db
client = TestClient(app)
def test_list_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) == 2