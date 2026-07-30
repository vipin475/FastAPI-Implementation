from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    
    
    
    
    
    
    
    
    
# pytest                    # Run all tests
# pytest test_api.py        # Run specific file
# pytest -v                 # Verbose output
# pytest -x                 # Stop on first failure
# pytest --tb=short         # Shorter tracebacks