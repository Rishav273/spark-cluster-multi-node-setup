# start shell
docker exec -it spark-cluster-spark-master-1 /bin/sh


# submit spark job
docker exec -it spark-cluster-spark-master-1 /spark/bin/spark-submit /scripts/simple_spark_job.py

# submit spark job
docker exec -it spark-cluster-spark-master-1 /spark/bin/spark-submit /scripts/pyspark_transforms.py

# submit spark job to read from gcp
docker exec -it spark-cluster-spark-master-1 /spark/bin/spark-submit /scripts/read_from_gcp.py

# start jupyter notebook
docker exec -it spark-cluster-jupyter-1 jupyter notebook list

# spark master
http://localhost:8080

# jupyter workspace
http://localhost:8888/tree