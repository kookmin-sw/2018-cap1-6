#-*- coding: utf-8 -*-
import json
import requests

class Commit:
    totalnum = 0
    a = {}
    def go(self,tnum):

        team = "2018-cap1-" + str(tnum)
        url = "https://api.github.com/repos/kookmin-sw/" + team + "/commits?per_page=100&page=1"
        while True:
            response = requests.get(url)
            commits = response.json()
            link = response.headers.get('link', None)
        #총 갯수
            Commit.totalnum += len(commits)

        #유져 별 갯수
            for i in range(len(commits)):
                if commits[i]['author'] is None:
                    continue
                name = commits[i]["author"]['login']
                if name in Commit.a:
                    Commit.a[name] = Commit.a[name] + 1
                else:
                    Commit.a[name] = 1
    
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
    c = Commit()
    c.go(tnum)
    print("total commit number : ", c.totalnum)
    print("per user commit number : ", c.a)
