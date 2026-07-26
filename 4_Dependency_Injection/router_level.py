from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/admin",
    dependencies=[Depends(require_admin)] # applies to all the routes in this router
)

@router.get("/users")
def list_users(): # require_admin runs automatically
    ...
    
    
@router.delete("/users/{user_id}")
def delete_user(user_id: int):  # require_admin runs automatically
    ...