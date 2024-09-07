from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, when, date_format
from pyspark.sql.types import LongType, IntegerType
# from IPython.display import HTML
import pandas as pd
pd.set_option("display.max_columns", None)


def main():
    
    spark = SparkSession.builder \
    .appName("PySparkTransforms") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

    sc = spark.sparkContext
    sc.setLogLevel("ERROR")

    df = spark.read \
        .option("mode", "PERMISSIVE") \
        .option("header", "true") \
        .csv("../files/Online_10052024.csv")

    df = df.repartition(8)

    df.write \
        .option("header", "true") \
        .mode("overwrite") \
        .csv("../files/output.csv")

    print("Done.")

if __name__ == "__main__":
    main()

