from django import forms
from django.core.validators import RegexValidator

class WordForm(forms.Form):
    word = forms.CharField(max_length=20, required=True, validators=[RegexValidator('^[A-Za-z]+$', message='A word can not contain digits or spaces')])
