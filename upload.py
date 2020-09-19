import boto3
#import createBucket

#s3 = boto3.resource('s3')
aws_session = boto3.Session()
s3_client = aws_session.client('s3')

bucket_name= "lmtd-team-beta"
#mybucket = s3.Bucket('lmtd-team-beta')
#filename = 'AAPL.csv'


def uploader(filename):
    print(type(filename))
    try:
        s3_client.upload_file(filename, bucket_name, filename)

        
    except Exception as e:
        #print(f"{filename} already exists ")
        print(e)
    else:
        print("File uploaded.")





#uploader("APPL.csv")
#check()