<<<<<<< HEAD
from pydantic import BaseSettings,SettingConfigDict

class Settings(BaseSettings):
    model_config = SettingConfigDict(
        env_file = ".env",
        extra ="ignore"
    )
    DB_CONNECTION:str


## Create the object of Settings class 
=======

from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
    DB_CONNECTION:str

>>>>>>> 1700e50e328902a6b873dea850819e5f04e75f2a
settings = Settings()
