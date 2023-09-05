import boto3
from boto3 import client
import json
import polars as pl

BUCKET = 'my-kafka-project'
# Provide the prefix for the folder containing your JSON files
Client = client('s3',
                aws_access_key_id='{}',
                aws_secret_access_key='{}'
                )

# List objects in the S3 bucket
response = Client.list_objects(Bucket=BUCKET)
objects = response.get('Contents', [])

# Initialize an empty list to store Polars DataFrames
dfs = []

# Iterate through the objects and read JSON files
for obj in objects:
    key = obj['Key']
    if key.endswith('.json'):
        result = Client.get_object(Bucket=BUCKET, Key=key)
        text = result["Body"].read().decode()
        json_data = json.loads(text)
        df = pl.DataFrame([json_data])
        dfs.append(df)

# Concatenate the list of DataFrames into a single Polars DataFrame
final_df = pl.concat(dfs)

# Convert the Polars DataFrame to a CSV file
local_csv_path = './df.csv'
csv_data = final_df.write_csv(local_csv_path)
