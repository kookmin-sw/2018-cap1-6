#-*- coding: utf-8 -*-
import sys
import json
import urllib

reload(sys)
sys.setdefaultencoding('utf-8')

api_token = 'f2e322a062f91b81101f8ee29a7a02979292f23f'
header = {'Authorization': 'token %s' % api_token}
team = "2018-cap1-16"
url = "https://api.github.com/repos/kookmin-sw/" + team + "/issues/comments?per_page=100"

req = urllib.request.Request(url,headers=header)
comments = json.load(urllib.requests.urlopen(req))

print("team name is : ",team)
#총 issue 갯수
totalnum = len(comments)
print("total comment number : ", totalnum)

#유져 별 comment 갯수
a = {}
for i in range(len(comments)):
    name = comments[i]['user']['login']

    if name in a:
        a[name] = a[name] + 1
    else:
        a[name] = 1

print("per user comment number : ", a)

