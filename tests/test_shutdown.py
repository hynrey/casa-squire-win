from unittest.mock import patch

import pytest
from pydantic import ValidationError

from src.handlers import command_handler


@pytest.mark.asyncio
@patch("os.system")
async def test_shutdown_command_success(mock_system):
    # Arrange
    action = "shutdown"
    data = {"delay": 10_000}
    # Act
    executed = await command_handler.handle_command(action, data)
    # Assert
    assert executed is True


@pytest.mark.asyncio
@patch("os.system")
async def test_shutdown_command_fail(mock_system):
    # Arrange
    action = "shutdown"
    data = {"delaxy": 10_000}
    # Act
    with pytest.raises(ValidationError):
        await command_handler.handle_command(action, data)
