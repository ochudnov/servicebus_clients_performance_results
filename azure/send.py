# producer sent  120 messages in 29.680049180984497 secs ;
# rate=4.043119985019498 msgs/sec

import json
import os
import time

from azure.servicebus import ServiceBusService

import perftest


with open(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                       '../config.json')
                          ), 'r') as read_file:
    config = json.load(read_file)

topic_name = config['topic_name']
service_namespace = config['service_namespace']
key_name = config['key_name']
key_value = config['key_value']

bus_service = ServiceBusService(
    service_namespace=service_namespace,
    shared_access_key_name=key_name,
    shared_access_key_value=key_value)

bus_service.create_topic(topic_name)

producer = perftest.PerfProducer(bus_service)
producer.start()

for i in range(1, 30):
    time.sleep(1)
    print("producer sent ", producer.rate.print_rate())

producer.stop()
