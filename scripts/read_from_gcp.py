from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from config.configurations import BUCKET_NAME, INPUT_FILE_PATH, SERVICE_ACCOUNT_FILE_PATH

# Initialize Spark session
spark = SparkSession.builder \
    .appName("GCSReadWrite") \
    .master("spark://spark-master:7077") \
    .config("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
    .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", SERVICE_ACCOUNT_FILE_PATH) \
    .getOrCreate()

# Set log level to ERROR
spark.sparkContext.setLogLevel("ERROR")

# Read CSV file from GCS bucket
gcs_input_path = f"gs://{BUCKET_NAME}/{INPUT_FILE_PATH}"

df = spark.read.csv(gcs_input_path, header=True, inferSchema=True)

# Show the first few rows of the DataFrame
print("DataFrame contents:")
df.show(10)

# Perform any additional operations on the DataFrame here
row_count = df.count()
print(f"Total number of rows: {row_count}")

print("Schema: \n", df.printSchema())

print("Done.")
