# start shell
docker exec -it spark-cluster-spark-master-1 /bin/sh


# submit spark job
docker exec -it spark-cluster-spark-master-1 /spark/bin/spark-submit /scripts/simple_spark_job.py