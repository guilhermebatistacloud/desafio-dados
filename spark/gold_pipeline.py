from pyspark.sql import SparkSession
from pyspark.sql.functions import count, avg, split

spark = SparkSession.builder.appName("Pipeline Gold").getOrCreate()

df_silver = spark.read.parquet("file:///app/spark/data/silver/dados.parquet")

# Extrai domínio do e-mail
df_gold = df_silver.withColumn("dominio", split("email", "@").getItem(1))

# Agrega por domínio
df_agg = df_gold.groupBy("dominio") \
    .agg(
        count("*").alias("total_usuarios"),
        avg("idade").alias("media_idade")
    )

df_agg.show()
df_agg.write.mode("overwrite").parquet("file:///app/spark/data/gold/metricas.parquet")

table = "gold_data"

df_agg.write \
  .mode("overwrite") \
  .format("jdbc") \
  .option("url", "jdbc:postgresql://postgres:5432/desafio") \
  .option("dbtable", table) \
  .option("user", "postgres") \
  .option("password", "Jp1987") \
  .option("driver", "org.postgresql.Driver") \
  .save()

print(f"✔️ Dados tratados salvos no banco : tabela -> {table}")

df_kafka = df_agg.select(to_json(struct("*")).alias("value"))

df_kafka.write \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "broker:9092") \
    .option("topic", "gold_data") \
    .save()

spark.stop()