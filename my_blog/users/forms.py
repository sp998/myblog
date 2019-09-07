from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm as ucform
from .models import Profile

class userRegister(ucform):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class userUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class updateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']

