from dotenv import load_dotenv
import os

load_dotenv()

from dataclasses import dataclass, field


@dataclass(frozen=True)
class PostgresConfig:
    """
    Настройки базы данных Postgres и тетовой базы
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

    test_host: str = field(default=str(os.getenv("TEST_PG_HOST")))
    test_port: int = field(default=str(os.getenv("TEST_PG_PORT")))
    test_user: str = field(default=str(os.getenv("TEST_PG_USER")))
    test_password: str = field(default=str(os.getenv("TEST_PG_PASSWORD")))
    test_database: str = field(default=str(os.getenv("TEST_PG_DB_NAME")))
    test_echo: bool = field(default=True)

    @property
    def test_db_postgres_url(self) -> str:
        return f"postgresql+asyncpg://{self.test_user}:{self.test_password}@{self.test_host}:{self.test_port}/{self.test_database}"


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
