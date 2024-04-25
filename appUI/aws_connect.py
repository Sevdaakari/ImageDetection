import boto3
from dotenv import load_dotenv, dotenv_values


load_dotenv()
config = dotenv_values(".env.secret")

# Access to S3 bucket
s3 = boto3.resource(
    service_name='s3',
    region_name=config['REGION_NAME'],
    aws_access_key_id=config['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=config['AWS_SECRET_ACCESS_KEY']
)


# Upload files to S3 bucket
images = open("./images")
for image in images:
    s3.Bucket('image-app-test-sevda').upload_file(Filename=image, Key='{image}.jpg')
