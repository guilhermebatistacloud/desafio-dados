
# 🚀 Desafio Final - Engenharia de Dados

Projeto desenvolvido como parte do Desafio Final do Bootcamp de Engenharia de Dados, com foco em construção de pipelines ETL utilizando Apache Kafka, Apache Spark, PostgreSQL e Amazon S3.

---

## 📚 Tecnologias e Ferramentas

- Docker & Docker Compose
- Apache Kafka + Kafka Connect
- Apache Spark (SQL API)
- PostgreSQL
- Amazon S3 (Data Lake)
- Kafka UI (interface de monitoramento)
- Apache Airflow (opcional)

---

## 🏗️ Arquitetura do Pipeline

```
JSON (raw)
   ↓
Spark (Bronze - Parquet/Delta)
   ↓
Spark (Silver - Dados Limpos)
   ↓
Spark (Gold - Métricas Agregadas)
   ↓
PostgreSQL → Kafka Connect → Kafka Topics
   ↓
Kafka Connect (Sink) → Amazon S3
```

---

## 🧩 Estrutura de Pastas

```
desafio-dados/
├── postgres/                          # Volume do banco de dados
├── connect/
│   └── custom-kafka-connectors-image/ # Dockerfile da imagem com conectores
├── spark/                             # Scripts e notebooks Spark
├── scripts/                           # Utilitários auxiliares
├── s3/                                # (Opcional) Emulação de S3
├── airflow/                           # (Opcional) DAGs e configs do Airflow
├── .env_kafka_connect                 # Credenciais AWS (NÃO versionar)
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

## ⚙️ Configuração Inicial

### 🔐 Variáveis de ambiente AWS

Crie um arquivo `.env_kafka_connect` na raiz do projeto com o seguinte conteúdo:

```env
AWS_ACCESS_KEY_ID=SEU_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=SUA_SECRET_KEY
```

> **Importante:** não compartilhe esse arquivo. Ele está ignorado pelo `.gitignore`.

---

### 🐳 Subir os containers

```bash
docker-compose build
docker-compose up -d
```

---

## 📦 Pipelines ETL

- **Bronze**: Leitura bruta de JSON → Parquet/Delta
- **Silver**: Limpeza, remoção de duplicatas, normalização
- **Gold**: Agregações e cálculos analíticos
- **Kafka Connect**: PostgreSQL → Kafka Topics
- **Sink Connector**: Kafka → Amazon S3

---

## ✅ Entregáveis

- 📸 Tabelas carregadas no PostgreSQL
- 🧾 Códigos Spark SQL para cada camada
- 🔧 Configuração dos conectores Kafka
- 📦 Dados no S3, organizados e particionados

---

## 🧠 Autor

Guilherme Batista das Dores  
Desenvolvedor | Analista de Sistemas | Tech Lead

---

## 📜 Licença

Este projeto é apenas para fins educacionais no Bootcamp de Engenharia de Dados.
