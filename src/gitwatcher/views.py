from django.shortcuts import render
from django.http import HttpResponse
import os
from django.template import Context, loader
#import boto3
#import botocore
# Create your views here.

def index(request):
	return render(request,'gitwatcher/index.html')

def clonegit(request):
	return render(request,'gitwatcher/clonegit.html')

def gitwatch1(request, address):
	address = 'https://github.com/' + address
	os.chdir('/home/ec2-user')
	os.system('git clone ' + address + '.git')
	words = address.split('/')
	length = len(words)
	os.chdir('/home/ec2-user/' + words[length-1])
	os.system('python3 /home/ec2-user/gitinspector/gitinspector.py -F html > /home/ec2-user/ttests/gitwatcher/templates/gitwatcher/statistics1.html --grading')
	os.chdir('/home/ec2-user')
	os.system('rm -rf ' + words[length-1])

	return render(request, 'gitwatcher/statistics1.html')

def storedData(request):
	path = '/home/ec2-user/files/html'
	files = os.listdir(path)
	k = lambda x: int(x[10] if x[11] is "_" else int(x[10:12]))
	#files.sort(key=k)
	context = {}
	context['mydict'] = {}
	os.chdir(path)

	for i in range(0,len(files)):
		os.system('cp ' + files[i] + ' /home/ec2-user/ttests/gitwatcher/templates/gitwatcher/')  #django의 template으로 복사하기
		temp = files[i].split('_')
		if temp[1] in context['mydict']:
			if temp[3].find('.') != -1: #html이 붙어 있는 것을 떼어주기 위한 작업
				remove_html = temp[3].split('.')
				branch = remove_html[0]
			else:
				branch = temp[3]
			for j in range(4,len(temp)):
				if j == len(temp)-1:  # 마지막 branch명에 html이 붙어 있는 것을 떼어주기 위한 방법
					remove_html = temp[j].split('.')
					branch += '_'
					branch += remove_html[0]
				else:
					branch += '_'
					branch += temp[j]
			context['mydict'][temp[1]].append(branch)
		else:
			if temp[3].find('.') != -1:
				remove_html = temp[3].split('.')
				branch = remove_html[0]
			else:
				branch = temp[3]
			context['mydict'][temp[1]] = []
			for j in range(4,len(temp)):
				if j == len(temp)-1:
					remove_html = temp[j].split('.')
					branch += '_'
					branch += remove_html[0]
				else:
					branch += '_'
					branch += temp[j]
			context['mydict'][temp[1]].append(branch)

	return render(request,'gitwatcher/storedData.html',context)

def result(request, address):
	addr = 'gitwatcher/' + address + '.html'
	return render(request, addr)

'''
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
'''
