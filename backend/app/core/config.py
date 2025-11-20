try:
    from pydantic_settings import BaseSettings
except ImportError:
    from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "mysql+pymysql://root@localhost/shopping-svelte"
    
    # App
    APP_TITLE: str = "Shopping Cart API"
    APP_VERSION: str = "0.1.0"
    
    # Upload
    UPLOAD_DIR: str = "static/uploads"
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10MB
    
    # Admin
    ADMIN_USERNAME: str = "admin"
    ADMIN_PASSWORD: str = "admin"
    ADMIN_EMAIL: str = "admin@example.com"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

