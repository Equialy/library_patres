from dotenv import load_dotenv
import os

load_dotenv()

from dataclasses import dataclass, field


@dataclass(frozen=True)
class PostgresConfig:
    """
    Настройки базы данных Postgres
    """
    host: str = field(default=str(os.getenv("PG_HOST")))
    port: int = field(default=str(os.getenv("PG_PORT")))
    user: str = field(default=str(os.getenv("PG_USER")))
    password: str = field(default=str(os.getenv("PG_PASSWORD")))
    database: str = field(default=str(os.getenv("PG_DB_NAME")))
    echo: bool = field(default=True)

    @property
    def postgres_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass(frozen=True)
class JWT:
    """
    Настройки JWT токена.
    """

    secret_key: str = field(default=str(os.getenv('SECRET_KEY')))
    algorithm: str = field(default=str(os.getenv('ALGORITHM')))
    token_lifetime: int = field(default=...)
    schema_crypt_context: str = field(default=str(os.getenv('CRYPT_SCHEMA')))


config_postgres = PostgresConfig()
config_jwt = JWT()