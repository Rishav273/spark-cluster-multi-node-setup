FROM openjdk:11-jre-slim

ENV SPARK_VERSION=3.3.2
ENV HADOOP_VERSION=3

RUN apt-get update && apt-get install -y wget

RUN wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    tar -xvzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /spark && \
    rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

ENV SPARK_HOME=/spark
ENV PATH=$PATH:$SPARK_HOME/bin

WORKDIR /spark