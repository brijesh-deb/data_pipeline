from pyspark.sql import SparkSession

if __name__ == "__main__":
    print("PySpark for batch queries on Kafka")

    spark = SparkSession \
        .builder \
        .appName("Kafka batch query") \
        .master("spark://MACC02ZH00BNQMC:7077") \
        .getOrCreate()

    KAFKA_TOPIC_NAME_CONS = "patient-data"
    KAFKA_BOOTSTRAP_SERVERS_CONS = 'localhost:9092'

    # Construct a DataFrame that reads from testtopic
    batch_df = spark \
        .read \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS_CONS) \
        .option("subscribe", KAFKA_TOPIC_NAME_CONS) \
        .load()

    print("Printing Schema of transaction_detail_df: ")
    batch_df.printSchema()
    print(" ***** Dataframe row count:")
    print(str(batch_df.count()))