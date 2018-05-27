#-*- coding: utf-8 -*-
import json
import requests

class Commit:
    totalnum = 0
    day = {}
    months = {}
    weeks = {}

    day_all = {}
    months_all = {}
    weeks_all = {}
    def go(self,tnum):
        team = tnum
        url = "https://api.github.com/repos/kookmin-sw/" + team + "/commits?per_page=100&page=1"
        while True:
            response = requests.get(url)
            commits = response.json()
            link = response.headers.get('link', None)

            Commit.totalnum += len(commits)

            for i in range(len(commits)):
                if commits[i]['author'] is None:
                    continue

                date = commits[i]['commit']['author']['date'].split('T')[0]
                name = commits[i]['author']['login']
                month = date.split('-')[1]
                if name in Commit.day:
                    if date in Commit.day[name]:
                        Commit.day[name][date] = Commit.day[name][date] + 1
                    else:
                        Commit.day[name][date] = 1
                else:
                    Commit.day[name] = {date:1}

                if name in Commit.months:
                    if month in Commit.months[name]:
                        Commit.months[name][month] = Commit.months[name][month] + 1
                    else:
                        Commit.months[name][month] = 1
                else:
                    Commit.months[name] = {month:1}

                if date in Commit.day_all:
                    Commit.day_all[date] = Commit.day_all[date] + 1
                else:
                    Commit.day_all[date] = 1

                if month in Commit.months_all:
                    Commit.months_all[month] = Commit.months_all[month] + 1
                else:
                    Commit.months_all[month] = 1
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
    print("per date,name commit number : ", c.day)
    print("per month commit number : ", c.months)
    print("per date commit number : ",c.day_all)
    print("per month commit number : ",c.months_all)
