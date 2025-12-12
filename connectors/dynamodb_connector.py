import boto3
import os

class DynamoDBConnector:

    _instance = None
    _dynamodb_client = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DynamoDBConnector, cls).__new__(cls)
            if os.environ.get("ENV", "AWS") == "LOCAL":
                cls._dynamodb_client = boto3.resource(
                    "dynamodb",
                    region_name='sa-east-1',  # Region name is required, but value can be arbitrary for local
                    endpoint_url='http://localhost:8000',
                    aws_access_key_id='nkb1cp',
                    aws_secret_access_key='fdxxag'
                )
            else:
                cls._instance._dynamodb_client = boto3.resource('dynamodb')

        return cls._instance


    def get_table(self, table_name):
        return self._dynamodb_client.Table(table_name)