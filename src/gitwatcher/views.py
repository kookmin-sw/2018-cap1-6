from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.

def index(request):
	return render(request,'gitwatcher/index.html')


def gitwatch(request, address):
	address = 'https://github.com/' + address
	os.chdir('/home/ubuntu')
	os.system('git clone ' + address + '.git')
	words = address.split('/')
	length = len(words)
	os.chdir('/home/ubuntu/' + words[length-1])
	os.system('python3 /home/ubuntu/gitinspector/gitinspector.py -F html > /home/ubuntu/2018-cap1-6/src/webapp/gitwatcher/templates/gitwatcher/statistics.html')
	return render(request, 'gitwatcher/statistics.html')