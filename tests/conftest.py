import pytest
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class AdminAuth(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra="ignore")
    name: str
    password: str


class EnvSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra="ignore")
    base_url: str


@pytest.fixture
def env_settings():  # -> EnvSettings:
    return EnvSettings(_env_file='.env')


@pytest.fixture
def admin_auth():  # -> AdminAuth:
    return AdminAuth(_env_file='.env')

# admin_auth = AdminAuth(username="admin", password="password123")
