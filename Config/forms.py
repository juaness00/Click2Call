from .models import User, Client
from django.forms import ModelForm
from django import forms
class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password']

class ClientForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),required=False)
    contactInfo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Contact Info'}),required=False)
    paymentNumber = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Payment Number'}),required=False)
    class Meta:
        model = Client
        fields = ['password','contactInfo', 'paymentNumber','plan_id']

class RegisterForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username (No Special Symbols)'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    UserType = forms.IntegerField(widget=forms.HiddenInput(), initial='2') 
    class Meta:
        model = Client
        fields = ['username', 'password', 'contactInfo']
        labels = {'contactInfo':'Email'}
        widgets = {
            'contactInfo':forms.TextInput(attrs={'placeholder': 'example@email.com'})
        }

class MovieForm(forms.Form):
    favoriteMovie = forms.ChoiceField()