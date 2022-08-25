from .models import User
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']