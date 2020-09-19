import pandas as pd
import boto3
import uploadFile
import createBucket

client = boto3.client("s3")
path = f"s3://{createBucket.bucket}/{uploadFile.filename}"
bucketname = "lmtd-team-beta"

def fetcher():
    try:

        with open('APPL.csv', 'wb') as f:
            s3.download_fileobj(bucketname, "APPL.csv", f)


        

    except Exception:
        return print("Error! Unable to fetch the file!")


# print("\nFetching file from AWS Bucket:")
# fetcher()
