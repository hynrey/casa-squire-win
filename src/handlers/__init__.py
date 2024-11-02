import logging

from src.handlers.shutdown import ShutdownCommand

log = logging.getLogger(__name__)


class CommandHandler:

    _commands = {
        "shutdown": ShutdownCommand(),
    }

    async def handle_command(self, action, data):
        command = self._commands.get(action)
        if command:
            return await command.execute(data)
        else:
            log.error(f"No handler found for action: {action}")


command_handler = CommandHandler()
