from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SparkTest") \
    .master("spark://localhost:7077") \
    .getOrCreate()

df = spark.createDataFrame([(1, "Hello"), (2, "World")], ["id", "text"])
df.show()

spark.stop()