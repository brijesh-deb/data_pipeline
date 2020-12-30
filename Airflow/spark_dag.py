from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

dag = DAG('spark_job_dag', description='DAG to trigger pySpark job',
          schedule_interval='0 12 * * *',
          start_date=datetime(2020, 3, 20), catchup=False)

start_task = DummyOperator(task_id='start_task', dag=dag)

commands = """
    cd /Users/philips/Documents/Study_code/Spark/spark-samples;
    /usr/local/Cellar/apache-spark/3.0.1/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 fetch_data.py;
    """

fetch_data = BashOperator(
    task_id='spark-task',
    bash_command=commands,
    dag=dag)

start_task >> fetch_data
