import boto3
from MessageQueue import MessageQueue

client = boto3.client('sns')
topicARN = 'arn:aws:sns:us-east-1:545853618712:sump-water-level'

messageQueue = MessageQueue(client, topicARN)
messageQueue.publish("Hello World!")
