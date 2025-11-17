from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountSignupForm(forms.ModelForm):
    
    password = forms.CharField(label = 'Senha', widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
