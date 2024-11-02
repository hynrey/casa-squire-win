class CommandBase:
    def execute(self, device_id, data):
        raise NotImplementedError("Subclasses should implement this!")
