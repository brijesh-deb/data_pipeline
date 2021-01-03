from pyspark.sql import SparkSession

if __name__ == "__main__":
    ACCESS_KEY="XXXXXXXXX"
    SECRET_KEY="XXXXXXXXX"

    spark = SparkSession \
        .builder \
        .appName("Job_Kafka_to_S3") \
        .master("local") \
        .config('spark.hadoop.fs.s3a.access.key',ACCESS_KEY) \
        .config('spark.hadoop.fs.s3a.secret.key',SECRET_KEY) \
        .config('spark.hadoop.fs.s3a.impl','org.apache.hadoop.fs.s3a.S3AFileSystem') \
        .config('spark.hadoop.fs.s3a.multipart.size', '104857600') \
        .getOrCreate()

    KAFKA_TOPIC_NAME_CONS = "patient-data"
    KAFKA_BOOTSTRAP_SERVERS_CONS = 'localhost:9092'

    # Construct a DataFrame that reads from patient-data topic
    print("33333 - before kafka load")
    batch_df = spark \
        .read \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS_CONS) \
        .option("subscribe", KAFKA_TOPIC_NAME_CONS) \
        .load()

    batch_df.show()

    S3_BUCKET="XXXXXXXXX"
    S3_URL="s3a://"+S3_BUCKET+"/patient.parquet"
    batch_df.write.parquet(S3_URL,mode='overwrite')
