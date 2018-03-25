from django.shortcuts import render

def index(request):
    if request.method == "POST":
        url = request.POST['url'] # 이걸 gitinspector 모듈로 보내야 함.
        return render(request,"gitwatcher/result.html",{"url": url})
    else:
        return render(request,"gitwatcher/index.html")


