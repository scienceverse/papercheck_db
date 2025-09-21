"""Core configuration settings for the papercheck_db application."""

from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False
    )

    # Database settings
    database_url: str = Field(default='localhost', description="PostgreSQL database URL")
    postgres_user: str = Field(
        default='admin', description="PostgreSQL username"
    )
    postgres_password: str = Field(
        default='admin', description="PostgreSQL password"
    )
    postgres_db: str = Field(
        default='papercheck_dev', description="PostgreSQL database name"
    )
    postgres_host: str = Field(default="localhost", description="PostgreSQL host")
    postgres_port: int = Field(default=5432, description="PostgreSQL port")

    # Environment
    environment: str = Field(default="development", description="Environment name")

    @property
    def is_development(self) -> bool:
        """Check if running in development mode."""
        return self.environment.lower() in ("development", "dev", "local")

    @property
    def is_production(self) -> bool:
        """Check if running in production mode."""
        return self.environment.lower() in ("production", "prod")


# Global settings instance
settings = Settings()
