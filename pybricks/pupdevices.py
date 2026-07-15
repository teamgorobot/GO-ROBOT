class Light:
    pass


class Motor:
    def __init__(self, *args, **kwargs):
        self.control = type("Control", (), {"limits": lambda self, *a, **k: None})()


class ColorSensor:
    def __init__(self, *args, **kwargs):
        pass

    def color(self, *args, **kwargs):
        from .parameters import Color
        return Color.NONE


class UltrasonicSensor:
    pass


class ForceSensor:
    pass
