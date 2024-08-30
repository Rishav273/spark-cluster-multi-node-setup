FROM openjdk:11-jre-slim

ENV SPARK_VERSION=3.3.2
ENV HADOOP_VERSION=3
ENV GCS_CONNECTOR_VERSION=2.2.5

RUN apt-get update && \
    apt-get install -y wget python3 python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python

RUN wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    tar -xvzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /spark && \
    rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

# Download and install GCS connector
RUN wget https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-${GCS_CONNECTOR_VERSION}.jar && \
    mv gcs-connector-hadoop3-${GCS_CONNECTOR_VERSION}.jar /spark/jars/

ENV SPARK_HOME=/spark
ENV PATH=$PATH:$SPARK_HOME/bin

WORKDIR /spark

# Install PySpark
RUN pip3 install pyspark==${SPARK_VERSION}