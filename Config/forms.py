from .models import User, Client
from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password']

class ClientForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    contactInfo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Contact Info'}))
    class Meta:
        model = Client
        fields = ['password','contactInfo']