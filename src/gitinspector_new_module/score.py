from commit import Commit
from issue import Issue
from comment import Comment

tnum = input("insert the team number : ")
ci = Commit()
ci.go(tnum)

i = Issue()
i.go(tnum)

ce = Comment()
ce.go(tnum)

bunmo = ci.totalnum + i.totalnum + ce.totalnum

for k in i.a.keys():
    commitnum = ci.a[k]
    issuenum = i.a[k]
    commentnum = ce.a[k]
    bunja = commitnum + issuenum + commentnum
    result = bunja / bunmo * 100
    print(k," 's score : ", result)
