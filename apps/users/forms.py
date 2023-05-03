from django import forms
from apps.users.models import Account
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Enter password",
        widget=forms.PasswordInput(attrs={
            'class':'form-control', 
            'type':'password',
            'placeholder':'Enter password'
        }),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={
            'class':'form-control', 
            'type':'password',
            'placeholder':'Confirm password'
        }),
    )

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2')
        widgets = {
            'first_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'First Name',
                'autofocus': ''
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Last Name'
            }),
            'phone':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Phone (with country code)'
            }),
            'email':forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email address',
                'autofocus': 'off'
            }),
        }