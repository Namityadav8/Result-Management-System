from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

data = {"Average": 75, "PassPercentage": 85}
producer.send("student_statistics", value=data)
print("Data sent to Kafka")