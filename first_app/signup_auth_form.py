from django import forms
from django.contrib.auth.models import User
from first_app.models import UserProfileMoreInformationForm

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileMoreInformationFormView(forms.ModelForm):
    class Meta():
        model = UserProfileMoreInformationForm
        fields = ('web_url','profile_pic')
