from .score_commit import Commit
from .score_issue import MyIssue
from .score_comments import Comment
import os

class ScoreMonth(object):
    def __init__(self, repos, previous_directory):
        repos_string = ", ".join([repo.name for repo in repos])
        repos_string = repos_string.split("_")
        repos_string = repos_string[1]

        os.chdir(previous_directory)

        f = open("gitinspector\\output\\scoreMonth.csv",'w')
        data = "State"
        f.write(data)

        ci = Commit()
        ci.go(repos_string)

        iss = MyIssue()
        iss.go(repos_string)

        ce = Comment()
        ce.go(repos_string)

        months_score = {}

        for i in ci.months_all.keys():
            bunmo = 0
            if i in ci.months_all.keys():
                bunmo += ci.months_all[i]

            if i in ce.months_all.keys():
                bunmo += ce.months_all[i]

            if i in iss.months_all.keys():
                bunmo += iss.months_all[i]

            for j in ci.months.keys(): #가장 넓은 범위의 이름
                bunja = 0
                if j in ci.months.keys():
                    if i in ci.months[j].keys():
                        bunja += ci.months[j][i]
                if j in ce.months.keys(): # comment에 이름이 있다면
                    if i in ce.months[j].keys(): # comment에 날짜도 있다면
                        bunja += ce.months[j][i]

                if j in iss.months.keys(): # comment에 이름이 있다면
                    if i in iss.months[j].keys(): # comment에 날짜도 있다면
                        bunja += iss.months[j][i]

                result = bunja / bunmo * 100

                if i in months_score.keys():
                    months_score[i][j] = result
                else:
                    months_score[i] = {j:result}

        for i in months_score:
            del months_score[i]["gychoics"]

        for i in months_score['05']:
            data = "," + "{0}".format(i)
            f.write(data)
        data = "\n"
        f.write(data)

        for i in months_score:
            data = i
            f.write(data)
            for j in months_score[i]:
                data = ",{0:.2f}".format(months_score[i][j])
                f.write(data)
            else:
                data = "\n"
                f.write(data)
        data = "\n"
        f.write(data)

        f.close()
