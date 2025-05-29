from kafka import KafkaProducer
import time, csv, json, os

producer = KafkaProducer(bootstrap_servers='kafka:9092',
                         value_serializer=lambda m: json.dumps(m).encode('utf-8'))

data_dir = './data'
for file in os.listdir(data_dir):
    with open(os.path.join(data_dir, file)) as f:
        reader = csv.DictReader(f)
        for row in reader:
            producer.send('sensor-topic', value=row)
            print("Sent:", row)
            time.sleep(0.5)  # simulasi delay streaming
