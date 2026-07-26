from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    api_key: str
    debug: bool = False

@lru_cache  # Cache settings, don't reload every request
def get_settings():
    return Settings()


@app.get("/info")
def get_info(settings: Settings = Depends(get_settings)):
    return {"debug": settings.debug}