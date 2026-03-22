from confluent_kafka import Producer
import json
import time
from datetime import datetime
import random

p = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    if err:
        print(f"Delivery failed: {err}")
    else:
        print(f"Sent: {msg.value().decode()}")

events = ["click", "scroll", "purchase"]
pages = ["home", "pricing", "product"]

for i in range(5):
    event = {
    "user_id": i,
    "event": random.choice(events),
    "page": random.choice(pages),
    "timestamp": str(datetime.utcnow())
    }

    p.produce(
        'user-events',
        key=str(i),
        value=json.dumps(event),
        callback=delivery_report
    )

    p.flush()
    time.sleep(1)