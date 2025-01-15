from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
from src.settings.base import config_jwt


class HashService:
    pwd_context = CryptContext(schemes=[config_jwt.schema_crypt_context], deprecated="auto")

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=30)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, config_jwt.secret_key, config_jwt.algorithm)
        return encoded_jwt


async def authenticate_user(username: str, hashed_password: str,
                            user_service):
    user = await user_service.user_if_exist(username=username)
    if not user and HashService().verify_password(hashed_password, user.hashed_password):
        return None
    return user
