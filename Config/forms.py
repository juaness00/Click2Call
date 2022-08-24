from .models import User
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        field = ['username','password']

form = UserForm()
