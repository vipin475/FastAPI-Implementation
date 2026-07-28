from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# creating a user
hashed = hash_password("mysecretpassword")
# store hashed in databsae, NEVER store the plain password

# verifying login
if verify_password(user_input, stored_hash):
    # password correct
    ...
else:
    # password wrong
    ...
    
    
    
    
    
# Why bcrypt?

# Intentionally slow (prevents brute force)
# Includes salt (same password → different hashes)
# Widely audited and trusted