from . import views
from django.conf.urls import url

#서버에 요청이 들어오면 어떻게 처리할지
urlpatterns = [
	url(r'^$', views.index),
	url(r'^clonegit$',views.clonegit),
	url(r'^clonegit/(?P<address>[\/\w_\.-]+)/result$', views.gitwatch1),
	url(r'^storedData$',views.storedData),
	url(r'^storedData/(?P<address>[\/\w_\.-]+)$',views.result)
	#url(r'^(?P<address>[\/\w_\.-]+)/option2/submit$', views.gitwatch2)
]
