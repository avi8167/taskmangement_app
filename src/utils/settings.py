
from pydantic import BaseSettings,SettingConfigDict

class Settings(BaseSettings):
    model_config = SettingConfigDict(
        env_file = ".env",
        extra ="ignore"
    )
    DB_CONNECTION:str


## Create the object of Settings class 

from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
    DB_CONNECTION:str
settings = Settings()
