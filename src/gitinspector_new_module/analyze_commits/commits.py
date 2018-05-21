#-*- coding: utf-8 -*-
import json
import requests

tnum = input("insert the team number : ")
team = "2018-cap1-" + str(tnum)
totalnum = 0
a = {}
url = "https://api.github.com/repos/kookmin-sw/" + team + "/commits?per_page=100&page=1"
while True:
    response = requests.get(url)
    commits = response.json()
    link = response.headers.get('link', None)

#총 갯수
    totalnum += len(commits)

#유져 별 갯수
    for i in range(len(commits)):
        name = commits[i]['commit']['author']['name']

        if name in a:
            a[name] = a[name] + 1
        else:
            a[name] = 1
    
    if link is not None:
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
    else:
        break

print("total commit number : ", totalnum)
print("per user commit number : ", a)
