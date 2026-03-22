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