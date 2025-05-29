from kafka import KafkaConsumer
import json, time, os

consumer = KafkaConsumer('sensor-topic',
                         bootstrap_servers='kafka:9092',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

batch = []
start_time = time.time()
window_sec = 60

if not os.path.exists("batches"): os.makedirs("batches")

i = 0
for msg in consumer:
    batch.append(msg.value)
    if time.time() - start_time > window_sec:
        with open(f"batches/batch_{i}.json", 'w') as f:
            json.dump(batch, f)
        print(f"Saved batch_{i}.json")
        batch = []
        start_time = time.time()
        i += 1
