#-*- coding: utf-8 -*-
import json
import requests

class Comment:
    totalnum = 0
    a = {}
    def go(self,tnum):
        team = tnum
        url = "https://api.github.com/repos/kookmin-sw/" + team + "/issues/comments?per_page=100&page=1"
        while True:
            response = requests.get(url)
            comments = response.json()
            link = response.headers.get('link', None)

#총 issue 갯수
            Comment.totalnum += len(comments)

#유져 별 comment 갯수
            for i in range(len(comments)):
                name = comments[i]['user']['login']

                if name in Comment.a:
                    Comment.a[name] = Comment.a[name] + 1
                else:
                    Comment.a[name] = 1
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
    c = Comment()
    c.go(tnum)
    print("total comment number : ", c.totalnum)
    print("per user comment number : ", c.a)
