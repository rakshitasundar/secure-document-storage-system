import json
import boto3

s3 = boto3.client('s3')

BUCKET_NAME = 'secure-document-storage-rakshita'

def lambda_handler(event, context):
    try:
        # List documents in the S3 bucket
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)

        files = []

        if 'Contents' in response:
            for obj in response['Contents']:
                files.append({
                    'FileName': obj['Key'],
                    'Size': obj['Size']
                })

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Secure Document Storage System is working!',
                'bucket': BUCKET_NAME,
                'documents': files
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }