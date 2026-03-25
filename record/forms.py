from django import forms
from .models import Record 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class RecordForm(forms.ModelForm):
    class Meta:
         model = Record
         fields = ['name', 'city', 'phone'] 


