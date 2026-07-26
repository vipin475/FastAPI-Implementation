from fastapi import Depends, HTTPException, Header

def get_current_user(authorization: str = Header()):
    token = authorization.replace("Bearer ", "")
    user = decode_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user

@app.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/my-posts")
def get_my_posts(current_user: User = Depends(get_current_user)):
    return get_posts_for_user(current_user.id)