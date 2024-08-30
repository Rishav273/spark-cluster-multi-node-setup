from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("SimpleSparkApp") \
    .getOrCreate()

# Create a simple DataFrame
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Show the DataFrame
print("DataFrame contents:")
df.show()

# Perform a simple transformation
avg_age = df.agg({"Age": "avg"}).collect()[0][0]
print(f"Average age: {avg_age}")

# Stop the Spark session
spark.stop()
