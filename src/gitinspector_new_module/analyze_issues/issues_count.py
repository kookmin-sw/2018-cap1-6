#-*- coding: utf-8 -*-
import sys
import json
import urllib2

reload(sys)
sys.setdefaultencoding('utf-8')

for i in range(1,30):
    team = "2018-cap1-" + str(i)
    url = "https://api.github.com/repos/kookmin-sw/" + team + "/issues?state=all"
    try:
        issues = json.load(urllib2.urlopen(url))
    except:
        continue;

    if len(issues) == 0:
        continue
    print("team name is : ",team)
    #총 issue 갯수
    totalnum = issues[0]['number']
    print("total issue number : ", totalnum)

    #유져 별 issue 갯수
    a = {}
    for i in range(len(issues)):
        name = issues[i]['user']['login']

        if name in a:
            a[name] = a[name] + 1
        else:
            a[name] = 1

    print("per user issue number : ", a)

