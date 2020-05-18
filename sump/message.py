"""This Module contains message queue classes for publishing messages"""


class MessageQueue:
    """An abstraction for publishing messages to aws SNS"""
    def __init__(self, client, topic: str):
        self.topic = topic
        self.client = client
        self.topic_arn = self.__fetch_topic_meta_data(topic)['TopicArn']

    def publish(self, message: str):
        """Publishes a message to the message queue
        Args:
            message: The message to be published to the queue.
        """
        self.client.publish(
            TopicArn=self.topic_arn,
            Message=message
        )

    def __fetch_topic_meta_data(self, topic_name):
        # create_topic will just return topic information if it already exists.
        return self.client.create_topic(Name=topic_name)
