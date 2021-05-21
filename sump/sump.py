"""Entry point module. Will monitor the water levels for the sump and publish information to the message queue. """
import os
import logging
import logging.config
import configparser
import boto3
from gpiozero import Device
from gpiozero.pins.mock import MockFactory

from sump.floatsensor import FloatSensor
from sump.message import MessageQueue

config_file = os.path.join(os.path.dirname(__file__), 'logging.ini')
config = configparser.ConfigParser()
config.read(config_file)

logging.config.fileConfig(config_file)


def main():
    """The main method for the module that will read water levels and publish state to the message queue."""

    client = boto3.client('sns')
    topic = 'sump-water'

    message_queue = MessageQueue(client, topic)

    float_sensor = FloatSensor('BOARD11')
    sump_monitor = MessageSendingSumpMonitor(float_sensor, message_queue)
    while True:
        sump_monitor.monitor()


def mockmain():
    """The main method for the module that will use Mock Pin Factory.
    This is for testing on devices that do not have GPIO pins
    """
    Device.pin_factory = MockFactory()
    main()


class SumpMonitor:
    """Monitors the water level in the sump"""
    def __init__(self, float_sensor: FloatSensor):
        self.water_level = None
        self.float_sensor = float_sensor

    def monitor(self):
        """Monitors the level in the sump and sets the water_level"""
        if self.float_sensor.is_water_level_high():
            self.water_level = 'HIGH'
        else:
            self.water_level = 'LOW'


class MessageSendingSumpMonitor(SumpMonitor):
    """A SumpMonitor the water_level to a message queue."""
    def __init__(self, float_sensor: FloatSensor, message_queue: MessageQueue):
        super().__init__(float_sensor)
        self.message_queue = message_queue

    def monitor(self):
        try:
            self.__monitor_and_publish_message()
        except Exception:
            logging.exception("exception while monitoring sump")
            self.message_queue.publish('ERROR')
            raise

    def __monitor_and_publish_message(self):
        previous_water_level = self.water_level
        super().monitor()
        if previous_water_level != self.water_level:
            logging.info("Water level = %s", self.water_level)
            self.message_queue.publish(self.water_level)


if __name__ == '__main__':
    main()
