FROM confluentinc/cp-kafka-connect:7.5.0

# Instalar o conector JDBC (PostgreSQL)
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.7.4

# Instalar o conector S3 Sink
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-s3:10.7.4

# Instalar driver JDBC PostgreSQL
RUN curl -o /usr/share/java/kafka-connect-jdbc/postgresql-42.7.3.jar https://jdbc.postgresql.org/download/postgresql-42.7.3.jar
