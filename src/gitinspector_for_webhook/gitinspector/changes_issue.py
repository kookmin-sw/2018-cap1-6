#-*- coding: utf-8 -*-
import json
import requests

class Issue:
    totalnum = 0
    a = {}
    def go(self,tnum):

        team = tnum
        url = "https://api.github.com/repos/kookmin-sw/" + team + "/issues?state=all&per_page=100&page=1"
        while True:
            response = requests.get(url)
            issues = response.json()
            link = response.headers.get('link', None)

        #총 갯수
            Issue.totalnum += len(issues)

        #유져 별 갯수
            for i in range(len(issues)):
                name = issues[i]['user']['login']

                if name in Issue.a:
                    Issue.a[name] = Issue.a[name] + 1
                else:
                    Issue.a[name] = 1

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

if __name__ == "__main__":
    tnum = input("insert the team number : ")
    c = Issue()
    c.go(tnum)
    print("total issue number : ", c.totalnum)
    print("per user issue number : ", c.a)
