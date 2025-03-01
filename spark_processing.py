from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min

spark = SparkSession.builder.appName("StudentAnalysis").getOrCreate()
df = spark.read.json("students.json")

for subject in ["Electronics", "Programming", "Database", "Data Science", "Mathematics", "DSA"]:
    print(f"Statistics for {subject}:")
    df.select(avg(f"Marks.{subject}").alias("Average"), max(f"Marks.{subject}").alias("Max"), min(f"Marks.{subject}").alias("Min")).show()