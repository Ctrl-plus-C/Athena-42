from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^userprofile/', views.userprofile, name='userprofile'),
    url(r'^postquestion/', views.postquestion, name='postquestion'),
    url(r'^notif/', views.notif, name='notif'),
    url(r'^answerquestion/', views.answerquestion, name='answerquestion'),
    url(r'^listedquestion', views.listedquestion, name='yourlistedquestions'),
    url(r'^api/question/$', views.QuestionsAPI.as_view(), name='QuestionsAPI'),    
    url(r'^api/answers/$', views.AnswerAPI.as_view(), name='AnswerAPI'),
    url(r'^api/answers/(?P<question_id>[-\w]+)/$', views.AnswerAPI.as_view(), name='AnswerAPI'),
    url(r'^api/skills/$', views.SkillAPI.as_view(), name='SkillAPI'),
    url(r'^api/skills/(?P<user>[-\w]+)/$', views.SkillAPI.as_view(), name='SkillAPI'),
    url(r'^api/tags/$', views.TagsAPI.as_view(), name='TagsAPI'),
    url(r'^api/tags/(?P<question>[-\w]+)/$', views.TagsAPI.as_view(), name='TagsAPI'),
    url(r'^api/bider/$',views.BiderAPI.as_view(),name='BiderAPI'),
    url(r'^api/bider/(?P<question_id>[-\w]+)/$',views.BiderAPI.as_view(),name='BiderAPI'),
    url(r'^api/userdetails/$',views.get_userdata,name='get_userdata'),
]