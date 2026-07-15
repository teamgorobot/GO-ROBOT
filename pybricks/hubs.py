class PrimeHub:
    def __init__(self, *args, **kwargs):
        self.light = _LightController()
        self.display = _DisplayController()
        self.buttons = _ButtonsController()
        self.system = _SystemController()
        self.battery = _BatteryController()


class _LightController:
    def on(self, *args, **kwargs):
        return None

    def blink(self, *args, **kwargs):
        return None


class _DisplayController:
    def pixel(self, *args, **kwargs):
        return None

    def icon(self, *args, **kwargs):
        return None


class _ButtonsController:
    def pressed(self):
        return []


class _SystemController:
    def set_stop_button(self, *args, **kwargs):
        return None


class _BatteryController:
    def voltage(self):
        return 12.0
