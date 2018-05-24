from commit import Commit
from issue import Issue
from comment import Comment

tnum = input("insert the team number : ")
ci = Commit()
ci.go(tnum)

iss = Issue()
iss.go(tnum)

ce = Comment()
ce.go(tnum)

days_score = {}
for i in ci.day_all.keys(): # 가장 넓은 범위의 날짜
    # 분모 계산(전체 커밋 + 이슈 + 코멘트)
    bunmo = 0
    if i in ci.day_all.keys():
        bunmo += ci.day_all[i]
    
    if i in ce.day_all.keys():
        bunmo += ce.day_all[i]
    
    if i in iss.day_all.keys():
        bunmo += iss.day_all[i]


    for j in ci.day.keys(): #가장 넓은 범위의 이름
        bunja = 0
        if j in ci.day.keys():
            if i in ci.day[j].keys():
                bunja += ci.day[j][i]
        if j in ce.day.keys(): # comment에 이름이 있다면
            if i in ce.day[j].keys(): # comment에 날짜도 있다면
                bunja += ce.day[j][i]

        if j in iss.day.keys(): # comment에 이름이 있다면
            if i in iss.day[j].keys(): # comment에 날짜도 있다면
                bunja += iss.day[j][i]
       
        result = bunja / bunmo * 100
        
        if i in days_score.keys():
            days_score[i][j] = result
        else:
            days_score[i] = {j:result}


print(days_score)
