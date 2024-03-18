from PIL import Image
import boto3
from io import BytesIO

# Creatin an instance for the bucket used
s3 = boto3.client('s3')
bucket_name = 'normalsizeimages'

# Changing the extensions for the png files.


def png_to_jpg():
    response = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' in response:
        for obj in response['Contents']:
            key = obj['Key']
            if key.endswith('.png'):
                response = s3.get_object(Bucket=bucket_name, Key=key)
                image_data = response['Body'].read()

                img = Image.open(BytesIO(image_data))
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                output = BytesIO()
                img.save(output, format='JPEG')

                new_key = key[:-4] + '.jpeg'
                s3.put_object(Bucket=bucket_name, Key=new_key,
                              Body=output.getvalue())
                s3.delete_object(Bucket=bucket_name, Key=key)


# Changing the names for the files.
def changing_names():
    response = s3.list_objects_v2(Bucket=bucket_name)
    a = 1

    if 'Contents' in response:
        for obj in response['Contents']:
            key = obj['Key']
            new_key = 'image-{}.jpeg'.format(a)
            s3.copy_object(Bucket=bucket_name, Key=new_key,
                           CopySource={'Bucket': bucket_name, 'Key': key})
            s3.delete_object(Bucket=bucket_name, Key=key)
            a += 1


# Changin the size of the file to a thumbnail size.
def re_size():
    bucket_name_2 = 'thumbnailsize'

    response = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' in response:
        for obj in response['Contents']:
            key = obj['Key']
            if key.endswith('.jpeg'):
                response = s3.get_object(Bucket=bucket_name, Key=key)
                image_data = response['Body'].read()

                img = Image.open(BytesIO(image_data))
                resized_img = img.resize((1280, 720))
                output = BytesIO()
                resized_img.save(output, format='JPEG')
                output.seek(0)
                s3.put_object(Bucket=bucket_name_2, Key=key, Body=output)

# Executing the files of the lambda.


def lambda_handler(event, context):
    png_to_jpg()
    changing_names()
    re_size()
