from django.shortcuts import render
from django.http import HttpResponse
import os
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
	os.system('python3 /home/ubuntu/gitinspector/gitinspector.py -F html > /home/ubuntu/2018-cap1-6/src/webapp/gitwatcher/templates/gitwatcher/statistics1.html')
	return render(request, 'gitwatcher/statistics1.html')


def gitwatch2(request, address):
	words = address.split('/')
	length = len(words)
	address = words[length-1]
	os.chdir('/home/ubuntu')
	os.system('aws s3 cp s3://ec2s3example/' + address + '.zip ./')
	os.system('unzip ' + address +'.zip -d ./' + address)
	os.chdir('/home/ubuntu/' + address)
	os.system('python3 /home/ubuntu/gitinspector/gitinspector.py -F html > /home/ubuntu/2018-cap1-6/src/webapp/gitwatcher/templates/gitwatcher/statistics2.html')
	return render(request, 'gitwatcher/statistics2.html')