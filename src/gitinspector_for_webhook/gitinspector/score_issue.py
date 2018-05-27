#-*- coding: utf-8 -*-
import json
import requests

class MyIssue:
    totalnum = 0
    day = {}
    months = {}
    weeks = {}
    day_all = {}
    months_all = {}
    weeks_all = {}
    def go(self,tnum):
        team = tnum
        url = "https://api.github.com/repos/kookmin-sw/" + team + "/issues?per_page=100&page=1&state=all"
        while True:
            response = requests.get(url)
            issues = response.json()
            link = response.headers.get('link', None)

            MyIssue.totalnum += len(issues)

            for i in range(len(issues)):
                date = issues[i]['created_at'].split('T')[0]
                name = issues[i]['user']['login']
                month = date.split('-')[1]

                if name in MyIssue.day:
                    if date in MyIssue.day[name]:
                        MyIssue.day[name][date] = MyIssue.day[name][date] + 1
                    else:
                        MyIssue.day[name][date] = 1
                else:
                    MyIssue.day[name] = {date:1}

                if name in MyIssue.months:
                    if month in MyIssue.months[name]:
                        MyIssue.months[name][month] = MyIssue.months[name][month] + 1
                    else:
                        MyIssue.months[name][month] = 1
                else:
                    MyIssue.months[name] = {month:1}

                if date in MyIssue.day_all:
                    MyIssue.day_all[date] = MyIssue.day_all[date] + 1
                else:
                    MyIssue.day_all[date] = 1

                if month in MyIssue.months_all:
                    MyIssue.months_all[month] = MyIssue.months_all[month] + 1
                else:
                    MyIssue.months_all[month] = 1
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
    print("per date,name issue number : ", c.day)
    print("per month issue number : ", c.months)
    print("per date issue number : ",c.day_all)
    print("per month issue number : ",c.months_all)
