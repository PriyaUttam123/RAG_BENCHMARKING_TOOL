from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    gemini_api_key: str = ""
    cohere_api_key: str = ""
    supabase_url: str = ""
    supabase_key: str = ""

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()