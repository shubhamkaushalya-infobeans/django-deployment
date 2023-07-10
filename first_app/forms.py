from typing import Any, Dict
from django import forms
from django.core import validators

# For custom validations using validators

def check_name_having_text(value):
    if 'shubham' not in value:
        raise validators.ValidationError('First name should contains word shubham')


class ContanctForm(forms.Form):
    STATUS_CHOICES = (
        (1,("Male")),
        (2,("FeMale")),
        (3,("Other")),
    )
    # name    = forms.CharField(required=True, validators=[validators.MaxLengthValidator(10)])
    #custom validation likes
    name    = forms.CharField(required=True, validators=[check_name_having_text])
    email   = forms.EmailField(label='Enter your email')
    reemail = forms.EmailField(label='Enter your email again')
    gender  = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect,initial="1")
    message = forms.CharField(widget=forms.Textarea)

    # Another method of validation
    def clean(self):
        all_details = super().clean()
        email = all_details['email']
        reemail = all_details['reemail']

        if email !=  reemail:
            raise forms.ValidationError('Both tha entered emails are not matching')