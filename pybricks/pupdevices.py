class Light:
    pass


class Motor:
    def __init__(self, *args, **kwargs):
        class Control:
            def limits(self, *a, **k):
                return None

        self.control = Control()


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
