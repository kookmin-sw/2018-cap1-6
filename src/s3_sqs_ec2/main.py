from analyzer import run
import threading
import time
import utils
import json
import subprocess
import botocore
import boto3
import sys

QUEUE_NAME = "s3Queue"
QUEUE_ATTR_NAME = "ApproximateNumberOfMessages"
SLEEP = 10


def Connect2sqs():
	#Connect to SQS service
	return utils.connect2Service('sqs')


#The SQSConsumer class retrieves messages from an SQS queue.
class SQSConsumer (threading.Thread):
    	sqs = Connect2sqs()

	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

	def run(self):
		#print(self.name+ " Thread running!")
		numMsgs = 0
		maxMsgs = self.getNumberOfMessages()
		count = 0
		#print(self.name+"\'s Messages to consume:"+ maxMsgs)
		while True:
			time.sleep(SLEEP)
			numMsgs += self.consumeMessages()
			count += 1
			#print(str(self.name) + " Iteration No.:" + str(count))
		
	def getQueue(self, sqsQueueName=QUEUE_NAME):
  #Get the SQS queue using the SQS resource object and QUEUE_NAME
		queue = None
		try:
			queue = self.sqs.get_queue_by_name(QueueName=sqsQueueName)
		except Exception as err:
			print(str(err))
		return queue

	def getNumberOfMessages(self):
		numMessages = 0
		try:
			queue = self.getQueue()
			if queue:				
			  # Receive messages from the SQS queue by using the receive_messages API method.
				# Enable long polling and set maximum number of messages to 10.2
				attribs = queue.attributes
				numMessages = int(attribs.get(QUEUE_ATTR_NAME))
		except Exception as err:
			print(str(err))
		return numMessages

        def getFile(self,fileName,bucketName):
                s3 = boto3.client('s3')
                arr = fileName.split('/')
                fname = arr[-1]
                path = '/home/ec2-user/files/' + fname
                try:
                    s3.download_file(bucketName,fileName,path)
                    print(fileName+" download completed.")
                except botocore.exceptions.ClientError as e:
                    if e.response['Error']['Code'] == "404":
                        print("The object does not exist.")
                    else:
                        raise

	def consumeMessages(self, sqsQueueName=QUEUE_NAME):
		numMsgs = 0
		try:
			queue = self.getQueue()
			if queue:
				mesgs =  queue.receive_messages(AttributeNames=['All'], MaxNumberOfMessages=10, WaitTimeSeconds=20)
				if not len(mesgs):
					return numMsgs
				for mesg in mesgs:		
					# Retrieve the Attributes of a message.
					attributes = mesg.attributes		
					senderId = attributes.get('SenderId')
					sentTimestamp = attributes.get('SentTimestamp')
					
					# !!!!!!!!Retrieve the body of a message.!!!!!!!!!!!!!!
					bd = mesg.body
                                        event = eval(bd)
                                        jsonmsg = json.loads(event['Message'])
                                        fileName = jsonmsg["Records"][0]["s3"]["object"]["key"]
                                        size = jsonmsg["Records"][0]["s3"]["object"]["size"]
                                        bucketName = jsonmsg["Records"][0]["s3"]["bucket"]["name"]
                                        name = fileName.split('/')[-1].split('.')[0]
                                        print("------------------------------------------------------------")
                                        print(self.name + " get message!")
                                        print("filename " + str(fileName) + " at bucketname " + str(bucketName) + " working start!")
                                        
					self.deleteMessage(queue, mesg)
					time.sleep(1)
                                        self.getFile(fileName,bucketName)
                                        run(name)
                                        print("--------------------analyze finished!--------------")


				numMsgs = len(mesgs)
		except Exception as err:
			print(str(err))
		return numMsgs

	def deleteMessage(self, queue, mesg):
		try:
			mesg.delete() 									
			print("this Message deleted from Queue")
			return True
		except Exception as err:
			print(str(err))
		return False
	
def main():
        #orig_stdout = sys.stdout
        #f = open('log.txt', 'w')
        #sys.stdout = f

	try:
		thread1 = SQSConsumer(1, "moonsang", 1)
		thread2 = SQSConsumer(2, "hohyun", 1)
		thread3 = SQSConsumer(3, "gunha", 1)
		thread4 = SQSConsumer(4, "woondae", 1)
		thread1.start()
		thread2.start()
		thread3.start()
		thread4.start()
                print("4 thread started!")
	except Exception as err:
		print(str(err))
	thread1.join()
	thread2.join()
	thread3.join()
	thread4.join()

        #sys.stdout = orig_stdout
        #f.close()
if __name__ == '__main__':
	main()

