from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^api/question/(?P<title>[-\w]+)/$', views.QuestionsAPI.as_view(), name='QuestionsAPI'),
]