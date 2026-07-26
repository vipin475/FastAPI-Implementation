from fastapi import Depends
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# yield enables cleanup — code after yield runs after the endpoint
        

@app.get("/users")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    return db_user