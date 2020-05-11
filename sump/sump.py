import boto3
from sump.FloatSensor import FloatSensor
from sump.MessageQueue import MessageQueue

def main():
    client = boto3.client('sns')
    topicARN = 'arn:aws:sns:us-east-1:545853618712:sump-water-level'

    messageQueue = MessageQueue(client, topicARN)
    messageQueue.publish("Hello World!")

    #float_sensor = FloatSensor('BOARD11')

    while True:
        pass

if __name__ == '__main__':
    main()