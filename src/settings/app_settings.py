from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    debug: bool = Field(default=False, validation_alias="DEBUG")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"
