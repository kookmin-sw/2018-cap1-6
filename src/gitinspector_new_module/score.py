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

print("commit : ",ci.totalnum)
print("commit per user",ci.a)
print("issue : ",i.totalnum)
print("issue per user",i.a)
print("comment : ",ce.totalnum)
print("comment per user",ce.a)
