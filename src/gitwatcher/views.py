from django.shortcuts import render
from django.http import HttpResponse
import os
import zipfile
from gitinspector import gitinspector as git
import boto3
import botocore
# Create your views here.

def index(request):
	return render(request,'gitwatcher/index.html')


def gitwatch1(request, address):
	address = 'https://github.com/' + address
	os.chdir('/home/ubuntu')
	os.system('git clone ' + address + '.git')
	words = address.split('/')
	length = len(words)
	os.chdir('/home/ubuntu/' + words[length-1])
	git.main()
	#os.system('python3 /home/ubuntu/gitinspector/gitinspector.py -F html > /home/ubuntu/ttests/gitwatcher/templates/gitwatcher/statistics1.html')
	return render(request, 'gitwatcher/statistics2.html')


def gitwatch2(request, address):
	words = address.split('/')
	length = len(words)
	address = words[length-1]

	BUCKET_NAME = 'gittos3fixed-outputbucket-ix0jgogj97ai'
	KEY = 'kookmin-sw/2018-cap1-11/branch/master/kookmin-sw_2018-cap1-11_branch_master.zip'
	s3 = boto3.resource('s3')
	try:
    	s3.Bucket(BUCKET_NAME).download_file(KEY, '\\home\\ubuntu\\다운로드성공.zip')
	except botocore.exceptions.Clienterror as e:
	    if e.response['Error']['Code'] == '404':
	        print("The object does not exist.")
	    else:
	        raise

	os.chdir('/home/ubuntu')
	os.system('unzip 다운로드성공.zip -d ./다운로드성공')
	os.chdir('/home/ubuntu/다운로드성공')
	git.main()
	#os.system('python3 /home/ubuntu/gitinspector/gitinspector.py -F html > /home/ubuntu/ttests/gitwatcher/templates/gitwatcher/statistics2.html')
	return render(request, 'gitwatcher/statistics2.html')
