#-*- coding: utf-8 -*-
import json
import requests

class Issue:
    totalnum = 0
    day = {}
    months = {}
    weeks = {}
    day_all = {}
    months_all = {}
    weeks_all = {}
    def go(self,tnum):
        team = "2018-cap1-" + str(tnum)
        url = "https://api.github.com/repos/kookmin-sw/" + team + "/issues?per_page=100&page=1&state=all"
        while True:
            response = requests.get(url)
            issues = response.json()
            link = response.headers.get('link', None)

            Issue.totalnum += len(issues)

            for i in range(len(issues)):
                date = issues[i]['created_at'].split('T')[0]
                name = issues[i]['user']['login']
                month = date.split('-')[1]

                if name in Issue.day:
                    if date in Issue.day[name]:
                        Issue.day[name][date] = Issue.day[name][date] + 1
                    else:
                        Issue.day[name][date] = 1
                else:
                    Issue.day[name] = {date:1}

                if name in Issue.months:
                    if month in Issue.months[name]:
                        Issue.months[name][month] = Issue.months[name][month] + 1
                    else:
                        Issue.months[name][month] = 1
                else:
                    Issue.months[name] = {month:1}

                if date in Issue.day_all:
                    Issue.day_all[date] = Issue.day_all[date] + 1
                else:
                    Issue.day_all[date] = 1

                if month in Issue.months_all:
                    Issue.months_all[month] = Issue.months_all[month] + 1
                else:
                    Issue.months_all[month] = 1
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
