from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, when, date_format, lit
from pyspark.sql.types import LongType, IntegerType
# from IPython.display import HTML
import pandas as pd
pd.set_option("display.max_columns", None)


def main():
    
    spark = SparkSession.builder \
    .appName("PySparkTransforms") \
    .master("spark://spark-master:7077") \
    .config("spark.executor.memory", "1800m") \
    .config("spark.driver.memory", "1g") \
    .config("spark.executor.cores", "3") \
    .config("spark.executor.instances", "3") \
    .config("spark.default.parallelism", "9") \
    .config("spark.sql.shuffle.partitions", "9") \
    .getOrCreate()

    sc = spark.sparkContext
    sc.setLogLevel("ERROR")

    print("Reading data...")
    df = spark.read \
        .option("mode", "PERMISSIVE") \
        .option("header", "true") \
        .csv("../files/Online_10052024.csv")

    df = df.repartition(9)


    # df = df.withColumn("Business Date", to_timestamp(col("Business Date")))

    # df = df.withColumn("order_type", lit("sale"))

    df.write \
        .option("header", "true") \
        .mode("overwrite") \
        .csv("../files/output.csv")

    print("Done.")

    print("Press any key to exit...")
    input()

if __name__ == "__main__":
    main()

