from django import forms
from first_app.models import User
#Form Using Modal
class Signup(forms.ModelForm):
    class Meta():
        model =  User
        fields = '__all__'
