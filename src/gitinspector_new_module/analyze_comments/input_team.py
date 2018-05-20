#-*- coding: utf-8 -*-
import json
import requests

tnum = input("insert the team number : ")
team = "2018-cap1-" + str(tnum)
url = "https://api.github.com/repos/kookmin-sw/" + team + "/issues/comments?per_page=100"
response = requests.get(url)
comments = response.json()
link = response.headers.get('link',None)

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
print(type(link))
if link is not None:
    print(link)

links = link.split(',')
for link in links:
    # If there is a 'next' link return the URL between the angle brackets, or None
    if 'rel="next"' in link:
        print(link[link.find("<")+1:link.find(">")])
