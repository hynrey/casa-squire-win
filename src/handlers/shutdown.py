import logging
import os

from pydantic import BaseModel, Field, ValidationError

from src.handlers.base import CommandBase

log = logging.getLogger(__name__)


class ShutdownSchema(BaseModel):
    delay: int = Field(gt=0)


class ShutdownCommand(CommandBase):

    async def execute(self, data: dict):
        data = await self.validate_data(data)
        if data:
            log.info(f"Shutting down in {data.delay} seconds...")
            os.system(f"shutdown /s /t {data.delay}")
            return True
        return False

    async def validate_data(self, data: dict):
        try:
            return ShutdownSchema(**data)
        except ValidationError as error:
            raise error
