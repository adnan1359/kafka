from confluent_kafka import Consumer
import json

# Define the consumer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}

# Initialize the consumer and call it 'c'
c = Consumer(conf)

# Tell the consumer which topic to listen to
c.subscribe(['my-topic'])

event_count = {}

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print(msg.error())
        continue

    data = json.loads(msg.value().decode())

    event_type = data["event"]
    event_count[event_type] = event_count.get(event_type, 0) + 1

    print("Running Count:", event_count)
