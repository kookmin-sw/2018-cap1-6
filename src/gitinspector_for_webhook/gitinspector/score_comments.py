#-*- coding: utf-8 -*-
import json
import requests

class Comment:
    totalnum = 0
    day = {}
    months = {}
    weeks = {}

    day_all = {}
    months_all = {}
    weeks_all = {}

    def go(self,tnum):
        team = tnum
        url = "https://api.github.com/repos/kookmin-sw/" + team + "/issues/comments?per_page=100&page=1"
        while True:
            response = requests.get(url)
            comments = response.json()
            link = response.headers.get('link', None)

            Comment.totalnum += len(comments)

            for i in range(len(comments)):
                date = comments[i]['created_at'].split('T')[0]
                name = comments[i]['user']['login']
                month = date.split('-')[1]

                if name in Comment.day:
                    if date in Comment.day[name]:
                        Comment.day[name][date] = Comment.day[name][date] + 1
                    else:
                        Comment.day[name][date] = 1
                else:
                    Comment.day[name] = {date:1}

                if name in Comment.months:
                    if month in Comment.months[name]:
                        Comment.months[name][month] = Comment.months[name][month] + 1
                    else:
                        Comment.months[name][month] = 1
                else:
                    Comment.months[name] = {month:1}

                if date in Comment.day_all:
                    Comment.day_all[date] = Comment.day_all[date] + 1
                else:
                    Comment.day_all[date] = 1

                if month in Comment.months_all:
                    Comment.months_all[month] = Comment.months_all[month] + 1
                else:
                    Comment.months_all[month] = 1

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
    print("per date,name comment number : ", c.day)
    print("per month,name comment number : ", c.months)
    print("per date comment number : ",c.day_all)
    print("per month comment number : ",c.months_all)
