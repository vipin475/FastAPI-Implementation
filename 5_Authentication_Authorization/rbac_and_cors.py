from enum import Enum
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from small_app.security import get_current_user

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://myapp.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*",]
)

class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"
    
class User(BaseModel):
    username: str
    role: Role = Role.USER
    


def require_role(required_role: Role):
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions"
            )
        return current_user
    return role_checker

# Usage
@app.delete("/users/{user_id}")
async def delete_user(user_id: int, admin: User = Depends(require_role(Role.ADMIN))):
    return {"deleted": user_id}