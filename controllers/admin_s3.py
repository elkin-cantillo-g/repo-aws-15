import boto3
from keys import ACCESS_KEY, SECRET_KEY

def connection_s3():
    session_aws = boto3.Session(ACCESS_KEY, SECRET_KEY)
    session_s3 = session_aws.resource('s3')
    print(session_aws)

connection_s3()
    
