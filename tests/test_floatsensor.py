from time import sleep
from unittest import TestCase

from gpiozero import Device
from gpiozero.pins.mock import MockFactory

from sump.floatsensor import FloatSensor


class TestFloatSensor(TestCase):

    def test_water_level_is_low(self):
        float_pin = self.__mock_gpio_pin()
        float_sensor = FloatSensor(16)
        float_pin.drive_low()
        sleep(0.1)
        self.assertFalse(float_sensor.is_water_level_high())

    def test_water_level_is_high(self):
        float_pin = self.__mock_gpio_pin()
        float_sensor = FloatSensor(16)
        float_pin.drive_high()
        sleep(0.1)
        self.assertTrue(float_sensor.is_water_level_high())

    @staticmethod
    def __mock_gpio_pin():
        Device.pin_factory = MockFactory()
        float_pin = Device.pin_factory.pin(16)
        return float_pin
