#-*- coding: utf-8 -*-
import json
import requests

tnum = input("insert the team number : ")
team = "2018-cap1-" + str(tnum)
totalnum = 0
a = {}
url = "https://api.github.com/repos/kookmin-sw/" + team + "/issues/comments?per_page=100&page=1"
while True:
    response = requests.get(url)
    comments = response.json()
    link = response.headers.get('link', None)

#총 issue 갯수
    totalnum += len(comments)

#유져 별 comment 갯수
    for i in range(len(comments)):
        name = comments[i]['user']['login']

        if name in a:
            a[name] = a[name] + 1
        else:
            a[name] = 1
   
    links = link.split(',')

    flag = 0
    for link in links:
        if 'rel="next"' in link:
            url = link[link.find("<")+1:link.find(">")]
            break
        else:
            flag = 1
    
    if flag == 1:
        break

print("total comment number : ", totalnum)
print("per user comment number : ", a)
