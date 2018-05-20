#-*- coding: utf-8 -*-
import sys
import json
import urllib2

reload(sys)
sys.setdefaultencoding('utf-8')

tnum = input("insert the team number : ")
team = "2018-cap1-" + str(tnum)
url = "https://api.github.com/repos/kookmin-sw/" + team + "/issues/comments?per_page=100"
comments = json.load(urllib2.urlopen(url))

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

