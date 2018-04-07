import boto3

def lambda_handler(event, context):
    return {
        "isBase64Encoded": "true",
        "statusCode": 200,
        "headers": {},
        "body": {"message":"helloworld"}
    }
