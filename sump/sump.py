"""Entry point module. Will monitor the water levels for the sump and publish information to the message queue. """
import boto3
from sump.floatsensor import FloatSensor

from sump.message import MessageQueue


def main():
    """The main method for the module that will read water levels and publish state to the message queue."""
    client = boto3.client('sns')
    topic_arn = 'arn:aws:sns:us-east-1:545853618712:sump-water'

    message_queue = MessageQueue(client, topic_arn)
    message_queue.publish("Hello!")

    while True:
        pass


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
        super(MessageSendingSumpMonitor, self).__init__(float_sensor)
        self.message_queue = message_queue

    def monitor(self):
        super(MessageSendingSumpMonitor, self).monitor()
        self.message_queue.publish(self.water_level)


if __name__ == '__main__':
    main()
