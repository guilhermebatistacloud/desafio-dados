FROM confluentinc/cp-kafka-connect:7.5.0

# Cria diretório padrão de plugins (caso não exista)
RUN mkdir -p /usr/share/confluent-hub-components

# Instala o conector JDBC (PostgreSQL)
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.7.4

# Instala o conector S3 Sink com workaround de permissões
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-s3:latest

# Instala driver PostgreSQL JDBC
RUN mkdir -p /usr/share/java/kafka-connect-jdbc && \
    curl -o /usr/share/java/kafka-connect-jdbc/postgresql-42.7.3.jar https://jdbc.postgresql.org/download/postgresql-42.7.3.jar