import json
from kafka import KafkaConsumer
from s3fs import S3FileSystem
import boto3

# Initialize the S3 client using boto3
s3 = boto3.client('s3', aws_access_key_id='{}}',
                  aws_secret_access_key='{}}')

# Kafka Consumer
consumer = KafkaConsumer(
    'kafka_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest'
)

# S3 bucket and object key
bucket_name = 'my-kafka-project'
s3_prefix = 'ordertable'  # Optional: Prefix for S3 object keys

for count, message in enumerate(consumer):
    try:
        # Load the Kafka message as JSON
        data = json.loads(message.value)

        # Convert the data to JSON format
        data_json = json.dumps(data)

        # Upload the JSON data to S3 with a unique object key
        object_key = f"{s3_prefix}_{count}.json"
        s3.put_object(Bucket=bucket_name, Key=object_key, Body=data_json)

        print(f'Data uploaded to S3: s3://{bucket_name}/{object_key}')
    except Exception as e:
        print("Error:", str(e))
