class MessageQueue:
    def __init__(self, client, topic_arn: str):
        self.topic_arn = topic_arn
        self.client = client

    def publish(self, message: str):
        self.client.publish(
            TopicArn=self.topic_arn,
            Message=message
        )
