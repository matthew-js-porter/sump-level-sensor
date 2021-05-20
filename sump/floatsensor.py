"""This module contains the FloatSensor class that uses GPIO to read water levels. """
from gpiozero import InputDevice


class FloatSensor(InputDevice):
    """An InputDevice that reads water levels using a float sensor."""
    def __init__(self, pins):
        super().__init__(pins, pull_up=False)

    def is_water_level_high(self) -> bool:
        """Returns true is the water level is higher than the float sensor."""
        return self.is_active

    @property
    def is_active(self):
        return not super().is_active
