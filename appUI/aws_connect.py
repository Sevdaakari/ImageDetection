import os
import boto3
from dotenv import load_dotenv, dotenv_values
import time

load_dotenv()
config = dotenv_values("./appUI/.env.secret")

# Access to S3 bucket
s3 = boto3.resource(
    service_name='s3',
    region_name=config['REGION_NAME'],
    aws_access_key_id=config['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=config['AWS_SECRET_ACCESS_KEY']
)


def upload_images_to_aws(images_dir, bucket_name):  
    # Get a list of files in the directory
    image_files = os.listdir(images_dir)

    # Upload each image file to the S3 bucket
    for filename in image_files:
        # Skip directories and non-image files
        if os.path.isdir(filename) or not filename.endswith(('.jpg', '.jpeg', '.png')):
            continue

        # Set the destination key (object key) in the S3 bucket
        key = f"images/{filename}"  # Adjust the key as needed

        # Upload the file to the S3 bucket
        s3.Bucket(bucket_name).upload_file(Filename=os.path.join(images_dir, filename), Key=key)
        
        # Delete the local image file after successful upload
        os.remove(os.path.join(images_dir, filename))

        print(f"Image '{filename}' uploaded to S3 bucket '{bucket_name}' and deleted from local folder")


def main():
    images_dir = "C:/Users/YSultanov/Sevda/studyPython/ML/imgDetApp/media/images"  # Local folder containing images
    bucket_name = "image-app-test-sevda"  # Name of the S3 bucket

    while True:
        # Check if there are images in the local folder
        if os.listdir(images_dir):
            upload_images_to_aws(images_dir, bucket_name)
        else:
            print('No images to be uploaded to aws')
        
        time.sleep(20) 


if __name__ == "__main__":
    main()