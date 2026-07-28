from passlib.context import CryptContext

from datetime import datetime, timedelta
from jose import jwt
from model import UserInDB

# Configuration
SECRET_KEY = "your-secret-key-keep-it-secret"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"])

def get_password_hash(plain_password: str) -> str:
    return pwd_context.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(datetime.timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_user(username: str) -> UserInDB | None:
    # In real app: query database
    # This is a fake user for demo
    if username == "alice":
        return UserInDB(
            username = "alice",
            hashed_password = get_password_hash("secret"), disabled=False,
        )
    return None

def authenticate_user(username: str, password: str) -> UserInDB | None:
    user = get_user(username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user