import unittest

from gpiozero import Device
from gpiozero.pins.mock import MockFactory
from sump.message import MessageQueue

from sump.floatsensor import FloatSensor

from sump.sump import SumpMonitor, MessageSendingSumpMonitor
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

    def test_send_message_if_water_level_changed(self):
        float_sensor = MyTestCase.__low_water_level_float_sensor()

        sns_client = MagicMock()
        message_queue = MessageQueue(sns_client, 'topic')
        message_queue.publish = MagicMock()

        sump_monitor = MessageSendingSumpMonitor(float_sensor, message_queue)
        sump_monitor.monitor()

        message_queue.publish.assert_called_with('LOW')
        self.assertEqual('LOW', sump_monitor.water_level)

    def test_only_send_message_on_new_status(self):
        float_sensor = MyTestCase.__low_water_level_float_sensor()

        sns_client = MagicMock()
        message_queue = MessageQueue(sns_client, 'topic')
        message_queue.publish = MagicMock()

        sump_monitor = MessageSendingSumpMonitor(float_sensor, message_queue)
        sump_monitor.water_level = 'LOW'
        sump_monitor.monitor()

        message_queue.publish.assert_not_called()
        self.assertEqual('LOW', sump_monitor.water_level)

    def test_error_when_monitoring(self):
        float_sensor = MyTestCase.__error_float_sensor()

        sns_client = MagicMock()
        message_queue = MessageQueue(sns_client, 'topic')
        message_queue.publish = MagicMock()

        sump_monitor = MessageSendingSumpMonitor(float_sensor, message_queue)
        sump_monitor.water_level = 'LOW'
        self.assertRaises(IOError, sump_monitor.monitor)


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

    @staticmethod
    def __error_float_sensor():
        float_sensor = FloatSensor(16)
        float_sensor.is_water_level_high = MagicMock(side_effect=IOError("ERROR!"))
        return float_sensor


if __name__ == '__main__':
    unittest.main()
