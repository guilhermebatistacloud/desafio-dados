#!/bin/bash

# Nome do container Spark
SPARK_CONTAINER="spark"

# Caminho dos JARs dentro do container
JAR_DIR="/app/jdbc"
JARS=$(docker exec "$SPARK_CONTAINER" bash -c "echo '$JAR_DIR'/*.jar | tr ' ' ','")
PACKAGES="org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0"

# Nome do pipeline a rodar (pode passar como argumento)
PIPELINE=${1:-gold_pipeline.py}

echo "🔧 Rodando $PIPELINE com os seguintes JARs:"
echo "$JARS"

# Executa dentro do container
docker exec -it "$SPARK_CONTAINER" spark-submit \
  --jars "$JARS" \
  --packages "$PACKAGES" \
  "/app/spark/$PIPELINE"