from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder \
    .appName("GCSReadWrite") \
    .master("spark://spark-master:7077") \
    .config("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
    .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", "/secrets/spatial-encoder-433413-r0-e8a0dfd3124d.json") \
    .getOrCreate()

# Set log level to ERROR
spark.sparkContext.setLogLevel("ERROR")

# Read CSV file from GCS bucket
bucket_name = "rishavm-gcs-airflow-project"
input_file_path = "raw/alboom_historical_offline_UAE_sale_chunk_1.csv"
gcs_input_path = f"gs://{bucket_name}/{input_file_path}"

df = spark.read.csv(gcs_input_path, header=True, inferSchema=True)

# Show the first few rows of the DataFrame
print("DataFrame contents:")
df.show(10)

# Perform any additional operations on the DataFrame here
row_count = df.count()
print(f"Total number of rows: {row_count}")
