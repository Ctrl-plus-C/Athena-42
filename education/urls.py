from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^api/question/(?P<title>[-\w]+)/$', views.QuestionsAPI.as_view(), name='QuestionsAPI'),
    url(r'^api/answers/(?P<question_id>[-\w]+)/$', views.AnswerAPI.as_view(), name='AnswerAPI'),
    url(r'^api/skills/(?P<user>[-\w]+)/$', views.SkillAPI.as_view(), name='SkillAPI'),
    url(r'^api/tags/(?P<question>[-\w]+)/$', views.TagsAPI.as_view(), name='TagsAPI'),
]