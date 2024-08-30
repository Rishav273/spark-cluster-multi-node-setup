from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("SimpleSparkApp") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

# Set log level to ERROR
spark.sparkContext.setLogLevel("ERROR")

# Create a simple DataFrame
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35), ("Mandy", 29)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Show the DataFrame
print("DataFrame contents:")
df.show()

# Perform a simple transformation
avg_age = df.agg({"Age": "avg"}).collect()[0][0]
print(f"Average age: {avg_age}")

# Stop the Spark session
spark.stop()
