"""Entry point module. Will monitor the water levels for the sump and publish information to the message queue. """
import boto3
from gpiozero import Device
from gpiozero.pins.mock import MockFactory

from sump.floatsensor import FloatSensor
from sump.message import MessageQueue


def main():
    """The main method for the module that will read water levels and publish state to the message queue."""

    client = boto3.client('sns')
    topic_arn = 'arn:aws:sns:us-east-1:545853618712:sump-water'

    message_queue = MessageQueue(client, topic_arn)

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
        print("water level is %s." % self.water_level)


class MessageSendingSumpMonitor(SumpMonitor):
    """A SumpMonitor the water_level to a message queue."""
    def __init__(self, float_sensor: FloatSensor, message_queue: MessageQueue):
        super(MessageSendingSumpMonitor, self).__init__(float_sensor)
        self.message_queue = message_queue

    def monitor(self):
        previous_water_level = self.water_level
        super(MessageSendingSumpMonitor, self).monitor()
        if previous_water_level != self.water_level:
            self.message_queue.publish(self.water_level)


if __name__ == '__main__':
    main()
