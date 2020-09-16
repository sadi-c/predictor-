import boto3

bucket = 'bucket-example'
s3 = boto3.resource('s3')


def createBucket():
    try:
        s3.create_bucket(Bucket=bucket,
                         ACL='public-read-write',
                         CreateBucketConfiguration={'LocationConstraint': 'us-east-1'}
                         )
        return print("Bucket created Successfully!")

    except Exception:
        return print("Bucket already exists!")


createBucket()
# bucket-example'
