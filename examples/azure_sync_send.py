import json
import os

from azure.servicebus import ServiceBusService, Message

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                       '../config.json')
                          ), 'r') as read_file:
    config = json.load(read_file)

topic_name = config['topic_name']
service_namespace = config['service_namespace']
key_name = config['key_name']
key_value = config['key_value']

sbs = ServiceBusService(
    service_namespace=service_namespace,
    shared_access_key_name=key_name,
    shared_access_key_value=key_value)

sbs.create_topic(topic_name)

msg = Message("Azure test message")
sbs.send_topic_message(topic_name, msg)
print("Message sent")
