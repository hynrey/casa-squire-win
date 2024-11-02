import logging
import socket

import servicemanager
import win32event
import win32service
import win32serviceutil

from src.utils.mqtt_client import mqtt_client

log = logging.getLogger(__name__)


class CasaSquireService(win32serviceutil.ServiceFramework):
    _svc_name_ = "CasaSquire Service"
    _svc_display_name_ = "CasaSquire"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self.stop_requested = False

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)
        self.stop_requested = True

    def SvcDoRun(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, ""),
        )
        self.main()

    def main(self):
        mqtt_client.run()
