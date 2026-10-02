from pydantic import BaseSettings,SettingConfigDict

class Settings(BaseSettings):
    model_config = SettingConfigDict(
        env_file = ".env",
        extra ="ignore"
    )
    DB_CONNECTION:str


## Create the object of Settings class 
settings = Settings()
