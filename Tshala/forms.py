from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Video, Add


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class Video_form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ("caption", "video")

class Adding_form(forms.ModelForm):
    class Meta:
        model = Add
        fields = ("country", "city", "busstype", "companyname", "regnumber", "nameofd", "nameofs")