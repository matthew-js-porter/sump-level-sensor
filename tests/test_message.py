import unittest

from unittest.mock import MagicMock
from sump.message import MessageQueue


class TestMessageQueue(unittest.TestCase):

    def setUp(self):
        self.topic_arn = 'arn:aws:sns:topic'
        self.topic_name = 'topic'
        self.message = 'message'

    def test_publish(self):
        client = self.__mock_client()
        message_queue = MessageQueue(client, self.topic_name)

        message_queue.publish(self.message)

        client.create_topic.assert_called_with(Name=self.topic_name)
        client.publish.assert_called_with(TopicArn=self.topic_arn, Message=self.message)

    def __mock_client(self):
        client = MagicMock()
        client.create_topic = MagicMock(return_value={'TopicArn': self.topic_arn})
        client.publish = MagicMock()
        return client


if __name__ == '__main__':
    unittest.main()
