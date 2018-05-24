from .commit import Commit
from .issue import Issue
from .comments import Comment

class Score(object):
    def __init__(self, repos):
        repos_string = ", ".join([repo.name for repo in repos])
        repos_string = repos_string.split("_")
        repos_string = repos_string[1]

        f = open("score.js",'w')
        data = "var chartData = [\n { key: \"Cumulative Return\", values:["
        f.write(data)

        ci = Commit()
        ci.go(repos_string)

        i = Issue()
        i.go(repos_string)

        ce = Comment()
        ce.go(repos_string)

        bunmo = ci.totalnum + i.totalnum + ce.totalnum

        summation = 0

        for k in i.a.keys():
            commitnum = ci.a[k]
            issuenum = i.a[k]
            commentnum = ce.a[k]
            bunja = commitnum + issuenum + commentnum
            result = bunja / bunmo * 100

            data = "{{ \"label\" : \"{0}\" , \"value\": {1:.2f}}} , ".format(k, result)
            f.write(data)

            summation += result

        mean = summation / len(i.a.keys())
        data = "{{ \"label\" : \"mean\" , \"value\": {0:.2f}}} , ".format(mean)
        f.write(data)
        f.close()
