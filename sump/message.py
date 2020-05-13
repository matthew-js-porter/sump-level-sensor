"""This Module contains message queue classes for publishing messages"""


class MessageQueue:
    """An abstraction for publishing messages to aws SNS"""
    def __init__(self, client, topic_arn: str):
        self.topic_arn = topic_arn
        self.client = client

    def publish(self, message: str):
        """Publishes a message to the message queue
        Args:
            message: The message to be published to the queue.
        """
        self.client.publish(
            TopicArn=self.topic_arn,
            Message=message
        )
