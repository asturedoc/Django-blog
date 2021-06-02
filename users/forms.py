from users.models import Profile
from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(
            label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(
            label='Confirm Password(again)', widget=forms.PasswordInput())

    class Meta(UserCreationForm.Meta):
        model=User
        fields=['username', 'email', 'password1','password2']
        help_texts = {
            'username': None,
            
        }

class UserUpdateForm(forms.ModelForm):
      email = forms.EmailField()
      class Meta:
          model=User
          fields=['username', 'email']
          help_texts = {
            'username': None,
            
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']
