from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    """Configuración global."""
    
    database_url: str = "postgresql://trading_user:trading_pass@localhost:5432/trading_educativo_db"
    secret_key: str = "change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    anthropic_api_key: str = ""
    newsapi_key: str = ""
    alphavantage_key: str = ""
    
    sendgrid_api_key: str = ""
    sendgrid_from_email: str = "noreply@trading-educativo.local"
    
    ntfy_topic: str = "trading-educativo-mvp"
    discord_webhook_url: str = ""
    
    debug: bool = True
    cors_origins: List[str] = ["http://localhost:3000", "http://localhost:5173"]
    
    timezone: str = "Europe/Madrid"
    analysis_hour: int = 21
    analysis_minute: int = 0
    
    default_portfolio_value: float = 10000.0
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
