import sys

import servicemanager
import win32serviceutil

from src.service import CasaSquireService
from src.settings import app_settings
from src.utils.logs import configure_logging
from src.utils.mqtt_client import mqtt_client

if __name__ == "__main__":
    configure_logging()
    if not app_settings.debug:
        if len(sys.argv) == 1:
            servicemanager.Initialize()
            servicemanager.PrepareToHostSingle(CasaSquireService)
            servicemanager.StartServiceCtrlDispatcher()
        else:
            win32serviceutil.HandleCommandLine(CasaSquireService)
    else:
        mqtt_client.run()
