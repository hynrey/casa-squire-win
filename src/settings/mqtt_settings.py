from pydantic import Field
from pydantic_settings import BaseSettings


class MQTTSettings(BaseSettings):
    host: str = Field(default="localhost", validation_alias="MQTT_HOST")
    port: int = Field(default=1883, validation_alias="MQTT_PORT")
    username: str = Field(default=None, validation_alias="MQTT_USERNAME")
    password: str = Field(default=None, validation_alias="MQTT_PASSWORD")
    listen_topic: str = Field(default="commands", validation_alias="MQTT_TOPIC")
    response_topic: str = Field(default="responses", validation_alias="MQTT_RESPONSE_TOPIC")
    reconnect: bool = Field(default=True, validation_alias="MQTT_RECONNECT")
    reconnect_interval: int = Field(default=10, validation_alias="MQTT_RECONNECT_INTERVAL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"
