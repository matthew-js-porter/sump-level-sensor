import unittest

from gpiozero import Device
from gpiozero.pins.mock import MockFactory

from sump.floatsensor import FloatSensor

from sump.sump import SumpMonitor
from unittest.mock import MagicMock


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Device.pin_factory = MockFactory()

    def test_monitor_when_water_level_is_low(self):
        float_sensor = MyTestCase.__low_water_level_float_sensor()

        sump_monitor = SumpMonitor(float_sensor)
        sump_monitor.monitor()

        self.assertEqual('LOW', sump_monitor.water_level)
        float_sensor.is_water_level_high.assert_called()

    def test_monitor_when_water_level_is_high(self):
        float_sensor = MyTestCase.__high_water_level_float_sensor()

        sump_monitor = SumpMonitor(float_sensor)
        sump_monitor.monitor()

        self.assertEqual('HIGH', sump_monitor.water_level)
        float_sensor.is_water_level_high.assert_called()

    @staticmethod
    def __low_water_level_float_sensor():
        float_sensor = FloatSensor(16)
        float_sensor.is_water_level_high = MagicMock(return_value=False)
        return float_sensor

    @staticmethod
    def __high_water_level_float_sensor():
        float_sensor = FloatSensor(16)
        float_sensor.is_water_level_high = MagicMock(return_value=True)
        return float_sensor

if __name__ == '__main__':
    unittest.main()
