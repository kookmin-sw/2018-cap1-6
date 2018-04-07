import boto3, botocore
from botocore.exceptions import NoCredentialsError

NUM_MESSAGES = 10

def connect2Service(service):
	#Returning the connection
	try:
		return boto3.resource(service)
	except botocore.exceptions.BotoCoreError as e:                                         
		if isinstance(e, botocore.exceptions.NoCredentialsError):
			print("No AWS Credentials file found or credentials are invalid")
	return None
