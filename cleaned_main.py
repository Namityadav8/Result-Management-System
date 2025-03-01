import pandas as pd
import random
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count
from kafka import KafkaProducer, KafkaConsumer
import json
from pymongo import MongoClient
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
spark = SparkSession.builder.appName("ResultManagementSystem").getOrCreate()
students = [{'StudentID': i, 'Name': f'Student_{i}'} for i in range(1, 10001)]
students_df = pd.DataFrame(students)
subjects = ['Electronics', 'Programming', 'Database', 'Data Science', 'Mathematics', 'DSA']
for subject in subjects:
    students_df[subject] = [random.randint(30, 100) for _ in range(10000)]
students_spark_df = spark.createDataFrame(students_df)
statistics_df = students_spark_df.select([avg(col(sub)).alias(f'{sub}_Average') for sub in subjects])
statistics_df.show()
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
data = statistics_df.toPandas().to_dict(orient='records')
producer.send('student_statistics', value=data)
producer.close()
consumer = KafkaConsumer('student_statistics', bootstrap_servers='localhost:9092', value_deserializer=lambda x: json.loads(x.decode('utf-8')))
for message in consumer:
    print("Received Data:", message.value)
    break
client = MongoClient('mongodb://localhost:27017/')
db = client['ResultManagement']
feedback_collection = db['Feedback']
feedback = {'StudentID': 1, 'Feedback': 'Satisfied'}
feedback_collection.insert_one(feedback)
feedback_data = ['Good', 'Bad', 'Excellent', 'Average', 'Poor']
labels = [1, 0, 1, 1, 0]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(feedback_data)
clf = MultinomialNB()
clf.fit(X, labels)
new_feedback = ['Excellent Service']
X_new = vectorizer.transform(new_feedback)
prediction = clf.predict(X_new)
print("Feedback Sentiment:", "Positive" if prediction[0] == 1 else "Negative")
