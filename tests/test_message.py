import unittest
from unittest.mock import Mock

from sump.message import MessageQueue


class TestMessageQueue(unittest.TestCase):
    def test_publish(self):
        client = Mock()
        message_queue = MessageQueue(client, 'topic')
        message_queue.publish("message")
        assert client.publish.called


if __name__ == '__main__':
    unittest.main()
