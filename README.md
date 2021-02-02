# Data Pipeline Sample
- Sample Data Pipeline code using Kafka, Spark and Airflow tried on Mac(local setup)
## Pre-requisite
### Kafka setup
- Install Kafka (used Kafka 2.6.0 for this sample)
- Start Zookeeper and kafka server
- Create a topic named "patient-data"
  - *kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic patient-data*
### Spark setup
- Install Spark (used 3.0.1 for this sample)
### AWS S3 setup
- AWS account and S3 bucket
- Access Key and Secret key for the AWS account
### Airflow setup
- Install Airflow

## Sample 1: Airflow to trigger Spark Job which fetches data from Kafka topic
- Ingest data to kafka topic
  - *kafka-console-producer --broker-list localhost:9092 --topic patient-data*
  - >This is a test kafka message
- Change Spark job and test
  - Change Spark master settings in fetch_data.py based on Spark installation.
  - Start spark: *./start-all.sh*
  - Run spark job(fetch_data.py) manually
    - *spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 fetch_data.py*
    - Should display count of message in Kafka topic
- Use Apache Airflow to automate scheduling the Spark job
  - Update spark_dag.py based on file location
  - Place spark_dag.py in "dags" folder under Airflow home directory
  - Start Airflow
    - *airflow initdb*
    - *airflow webserver*
  - Start Airflow scheduler
    - *airflow scheduler*
  - Go to Airflow UI and trigger "spark_job_dag"
## Sample 2: Airflow to trigger Spark Job which fetches data from Kafka topic and saves that in AWS S3
- Ingest data to kafka topic
  - *kafka-console-producer --broker-list localhost:9092 --topic patient-data*
  - >10 20 30 40
- Change Spark job and test
  - Change data_pipeline.py to include correct ACCESS_KEY, SECRET_KEY, S3_BUCKET
  - Start spark: *./start-all.sh*
  - Run spark job(data_pipeline.py) manually
    - */usr/local/Cellar/apache-spark/3.0.1/libexec/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1,com.amazonaws:aws-java-sdk:1.11.633,org.apache.hadoop:hadoop-aws:3.2.0 /Users/philips/Documents/Study_code/Spark/spark-samples/spark_kafka_s3.py*
    - command may change based on folder structure, also aws-java-sdk & hadoop-aws versions may be different
    - If successful, it will save parquet data in S3 bucket 
- Use Apache Airflow to automate scheduling the Spark job
  - Update save_data_S3.py based on file location
  - Place save_data_S3.py in "dags" folder under Airflow home directory
  - Start Airflow
    - *airflow initdb*
    - *airflow webserver*
  - Start Airflow scheduler
    - *airflow scheduler*
  - Go to Airflow UI and trigger "S3_data_save_dag"
## References:
  - https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html
