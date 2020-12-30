# Data Pipeline Sample
- Sample Data Pipeline code using Kafka, Spark and Airflow tried on Mac local setup
## Kafka for data ingestion
- Install Kafka on Mac, used Kafka 2.6.0 for running this sample
- Start Zookeeper and kafka server
- Create a topic named "patient-data"
  - *kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic patient-data*
- Initialize Producer console and send message
  - *kafka-console-producer --broker-list localhost:9092 --topic patient-data*
  - >This is a test kafka message
## Spark for data processing
## Airflow
