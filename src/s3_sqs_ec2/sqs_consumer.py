import threading
import time
import utils
import json
import subprocess

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
		print("SQSConsumer Thread running!")
		maxRetry = 10000 # MAXIMUM 10000 tries
		numMsgs = 0
		maxMsgs = self.getNumberOfMessages()
		count = 0
		print("No. of Messages to consume:", maxMsgs)
		while numMsgs < maxMsgs or count < maxRetry:
			time.sleep(SLEEP)
			numMsgs += self.consumeMessages()
			count += 1
			print("Iteration No.:", count, numMsgs)
		print("SQSConsumer Thread Stopped")
		
	def getQueue(self, sqsQueueName=QUEUE_NAME):
  #Get the SQS queue using the SQS resource object and QUEUE_NAME
		queue = None
		try:
			queue = self.sqs.get_queue_by_name(QueueName=sqsQueueName)
		except Exception as err:
			print("Error Message {0}".format(err))
		return queue

	def getNumberOfMessages(self):
		numMessages = 0
		try:
			queue = self.getQueue()
			if queue:				
			  # Receive messages from the SQS queue by using the receive_messages API method.
				# Enable long polling and set maximum number of messages to 10.
				attribs = queue.attributes
				numMessages = int(attribs.get(QUEUE_ATTR_NAME))
		except Exception as err:
			print("Error Message {0}".format(err))
		return numMessages

	def consumeMessages(self, sqsQueueName=QUEUE_NAME):
		numMsgs = 0
		try:
			queue = self.getQueue()
			if queue:
				mesgs =  queue.receive_messages(													
										AttributeNames=['All'], MaxNumberOfMessages=10, WaitTimeSeconds=20)
				if not len(mesgs):
					print("There are no messages in Queue to display")
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
                                        print(fileName)
                                        print(size)
                                        print(bucketName)


					# !!!! The example of excution of bashscript!!!!
                                        #filePath = "/mnt/s3mount/" + fileName
                                        #subprocess.call(["./soma_aws.sh", filePath, "/mnt/s3output"])

        	# Delete Message from the SQS queue
					self.deleteMessage(queue, mesg)
					time.sleep(1)
				numMsgs = len(mesgs)
		except Exception as err:
			print("Error Message {0}".format(err))
		return numMsgs

	def deleteMessage(self, queue, mesg):
		try:
			#Delete Message from the SQS queue
			mesg.delete() 									
			print("Message deleted from Queue")
			return True
		except Exception as err:
			print("Error Message {0}".format(err))
		return False
	
def main():
	try:
		thread1 = SQSConsumer(1, "Thread-1", 1)
		thread1.start()
	except Exception as err:
		print("Error Message {0}".format(err))
	thread1.join()
	return thread1

if __name__ == '__main__':
	main()

