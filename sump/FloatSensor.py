from gpiozero import InputDevice


class FloatSensor(InputDevice):
    def __init__(self, pins):
        super(FloatSensor, self).__init__(pins, pull_up=False)

    def is_tripped(self) -> bool:
        return self.is_active

    def is_active(self):
        return not super.is_active