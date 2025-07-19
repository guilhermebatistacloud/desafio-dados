from pyspark.sql import SparkSession

# 1. Cria sessão Spark
spark = SparkSession.builder \
    .appName("Pipeline Bronze - Ingestão Bruta") \
    .getOrCreate()

# 2. Caminhos de entrada e saída
input_path = "input/dados-brutos.json"
output_path = "data/bronze/dados.parquet"

# 3. Lê o JSON bruto
df = spark.read.option("multiline", "true").json(input_path)

# 4. Mostra schema e preview (debug)
print("Esquema inferido:")
df.printSchema()

print("Exemplo de dados:")
df.show(5, truncate=False)

# 5. Grava em Parquet na camada Bronze
df.write.mode("overwrite").parquet(output_path)

print(f"✔️ Dados brutos salvos em: {output_path}")

table = "bronze_data"

df.write \
  .mode("overwrite") \
  .format("jdbc") \
  .option("url", "jdbc:postgresql://postgres:5432/desafio") \
  .option("dbtable", table) \
  .option("user", "postgres") \
  .option("password", "Jp1987") \
  .option("driver", "org.postgresql.Driver") \
  .save()

print(f"✔️ Dados brutos salvos no banco : tabela -> {table}")

# 6. Finaliza sessão
spark.stop()