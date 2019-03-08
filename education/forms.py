from django import forms
from .models import User
from registration.forms import RegistrationForm

class CustomUserForm(RegistrationForm):
    class Meta:
        model = User
        exclude = ['last_login', 'is_superuser', 'groups', 'user_permissions', 'is_staff', 'is_active', 'date_joined_0', 'date_joined_1', 'date_joined', 'password', 'is_moderator', 'reputation', 'assigned_mentor']