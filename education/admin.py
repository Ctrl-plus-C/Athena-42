from django.contrib import admin
from .models import User, Skill, Question, Answer, Tag, Bider
# Register your models here.
admin.site.register(User)
admin.site.register(Skill)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(Bider)