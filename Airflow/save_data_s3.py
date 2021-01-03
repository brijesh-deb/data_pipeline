from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

dag = DAG('S3_data_save_dag', description='DAG to save data in S3',
          schedule_interval='0 12 * * *',
          start_date=datetime(2020, 3, 20), catchup=False)

start_task = DummyOperator(task_id='start_task', dag=dag)

commands = "/usr/local/Cellar/apache-spark/3.0.1/libexec/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1,com.amazonaws:aws-java-sdk:1.11.633,org.apache.hadoop:hadoop-aws:3.2.0 /Users/philips/Documents/Study_code/Spark/spark-samples/data_pipeline.py"

save_data = BashOperator(
    task_id='spark-save-task',
    bash_command=commands,
    dag=dag)

start_task >> save_data
