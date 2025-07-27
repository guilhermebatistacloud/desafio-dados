#!/bin/bash

echo "🔌 Registrando JDBC Source Connector..."
curl -X POST http://localhost:8083/connectors \
  -H "Content-Type: application/json" \
  -d @connect/connectors/jdbc_source_gold_metricas.json

echo -e "\n📤 Registrando S3 Sink Connector..."
curl -X POST http://localhost:8083/connectors \
  -H "Content-Type: application/json" \
  -d @connect/connectors/s3_sink_gold_metricas.json
