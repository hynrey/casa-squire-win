import asyncio
import json
import logging

from aiomqtt.client import Client

from src.handlers import command_handler
from src.settings import mqtt_settings

log = logging.getLogger(__name__)


class MQTTClient:

    client = None

    def __init__(self):
        self.host = mqtt_settings.host
        self.port = mqtt_settings.port
        self.username = mqtt_settings.username
        self.password = mqtt_settings.password

        self.listen_topic = mqtt_settings.listen_topic
        self.response_topic = mqtt_settings.response_topic

        self.reconnect = mqtt_settings.reconnect
        self.reconnect_interval = mqtt_settings.reconnect_interval

    def run(self):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(self.listen())

    async def listen(self):
        if self.client is None:
            await self.connect()
        while True:
            try:
                async with self.client:
                    await self.client.subscribe(self.listen_topic + "/#")
                    async for message in self.client.messages:
                        _, device_id = message.topic.value.split("/")
                        payload = json.loads(message.payload.decode("utf-8"))
                        log.info(f"Got message: '{payload}'")

                        action = payload.get("action")
                        data = payload.get("data", {})

                        try:
                            result = await command_handler.handle_command(action, data)
                            await self.publish({"id": device_id, "success": result})
                        except Exception as error:
                            log.error(f'Error "{error}"')
                            await self.publish(
                                {"id": device_id, "success": False, "error": str(error)}
                            )

            except Exception as error:
                log.warning(f'Error "{error}". Reconnecting in {self.reconnect_interval} seconds.')
                await asyncio.sleep(self.reconnect_interval)

    async def connect(self):
        self.client = Client(
            hostname=self.host, port=self.port, username=self.username, password=self.password
        )

    async def publish(self, data):
        await self.client.publish(self.response_topic, json.dumps(data))


mqtt_client = MQTTClient()
