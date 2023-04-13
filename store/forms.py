from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from . import models


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = models.User
        fields = ("username", "email", "first_name", "last_name")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = models.User
        fields = ("username", "email", "first_name", "last_name")


