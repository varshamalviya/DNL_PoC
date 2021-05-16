import json
import boto3
from io import BytesIO

def lambda_handler(event, context):
       #return 'say Hi'
        s3 = boto3.client('s3')
        if event:
            #print(event)
            file_obj = event['Records'][0]
            #print(file_obj)
            bucketname = str(file_obj['s3']['bucket']['name'])
            #print(bucketname)
            filename = str(file_obj['s3']['object']['key'])
            #print(filename)
            filestring = filename.split('.')
            obj = s3.get_object(Bucket=bucketname,Key = filename)
            file_content = obj['Body'].read()
            
            print(type(file_content))
            var = file_content.decode("utf-8")
            print(type(var))
            var = var.replace('Amazon','Amazon©')
            var = var.replace('Google','Google©')
            var = var.replace('Oracle','Oracle©')
            var = var.replace('Mircosoft','Mircosoft©')
            var = var.replace('Deloitte','Deloitte©')
            print(var)
            s3.put_object(Bucket = 'replacedstring' , Key = filename , Body =var)
            #print(var)
    # TODO implement

