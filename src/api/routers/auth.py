from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.api.depends import get_user_service
from src.services.users_service.JWTauth import authenticate_user, HashService

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/token")
async def token_user(user_service: get_user_service,
                     response: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(response.username, response.password, user_service)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    access_token = HashService().create_access_token({"username": user.username})
    return {"access_token": access_token,
            "token_type": "bearer",
            "user_id": user.id,
            "username": user.username,
            }
