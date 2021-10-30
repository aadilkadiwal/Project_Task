from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
 
# Add additional field first_name, last_name, email in UserCreationForm
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

# User can update username, first_name, last_name, email 
class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

# User can update image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']        