from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
            'class': 'pl-10 w-full py-3 px-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200'
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password',
            'class': 'pl-10 w-full py-3 px-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200'
        })
    )
    
    
class  SignupForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
            'class': 'pl-10 w-full py-3 px-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200'
        })
    )
    
    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your email address',
            'class': 'pl-10 w-full py-3 px-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200'
        })
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password',
            'class': 'pl-10 w-full py-3 px-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200'
        })
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat password',
            'class': 'pl-10 w-full py-3 px-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200'
        })
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')