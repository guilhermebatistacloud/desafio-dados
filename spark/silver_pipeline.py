from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, trim

# Inicializa Spark
spark = SparkSession.builder \
    .appName("Pipeline Silver - Limpeza") \
    .getOrCreate()

# Lê dados da Bronze
df_bronze = spark.read.parquet("file:///app/spark/data/bronze/dados.parquet")

# Limpeza: remove duplicatas
df_silver = df_bronze.dropDuplicates()

# Tratamento: remove nulos (ajuste conforme a regra de negócio)
df_silver = df_silver.na.drop()

# Padronização: nomes em minúsculas e sem espaços extras (se existir coluna 'nome')
if "nome" in df_silver.columns:
    df_silver = df_silver.withColumn("nome", lower(trim(col("nome"))))

# Mostra preview
df_silver.show(5)
df_silver.printSchema()

# Grava camada Silver
df_silver.write.mode("overwrite").parquet("file:///app/spark/data/silver/dados.parquet")

print("✔️ Dados limpos salvos na camada Silver!")

table = "silver_data"

df_silver.write \
  .mode("overwrite") \
  .format("jdbc") \
  .option("url", "jdbc:postgresql://postgres:5432/desafio") \
  .option("dbtable", table) \
  .option("user", "postgres") \
  .option("password", "Jp1987") \
  .option("driver", "org.postgresql.Driver") \
  .save()

print(f"✔️ Dados limpos salvos no banco : tabela -> {table}")

spark.stop()