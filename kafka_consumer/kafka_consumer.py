from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('student_statistics', bootstrap_servers='localhost:9092', value_deserializer=lambda v: json.loads(v.decode('utf-8')))

for msg in consumer:
    print("Received Statistics:", msg.value)