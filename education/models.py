from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_moderator = models.BooleanField(default=True)
    available_mentor = models.BooleanField(default=True)
    available_mentee = models.BooleanField(default=True)
    assigned_mentor = models.ForeignKey("User",on_delete=models.CASCADE,blank=True, null=True)
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return str(self.username)

    def __unicode__(self):
        return str(self.username)

class Skill(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=1200, blank=False, null=False)

    def __str__(self):
        return str(self.username)

    def __unicode__(self):
        return str(self.username)

