"""Entry point module. Will monitor the water levels for the sump and publish information to the message queue. """
import boto3
from sump.message import MessageQueue

def main():
    """The main method for the module that will read water levels and publish state to the message queue."""
    client = boto3.client('sns')
    topic_arn = 'arn:aws:sns:us-east-1:545853618712:sump-water-level'

    message_queue = MessageQueue(client, topic_arn)
    message_queue.publish("Hello!")

    while True:
        pass


if __name__ == '__main__':
    main()
