from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    # class Meta: Nested namespace for configuration and keep the configuration in one place
    class Meta:
        # form.save It will save in User model
        model = User
        # want this field in form and which order I want
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']