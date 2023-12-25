from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    telefono = forms.CharField(max_length=15, required=True, help_text='Número de teléfono')
    CUI = forms.CharField(max_length=15, required=True, help_text='Número de DPI')
    
    class Meta:
        model = User
        fields = ['first_name','last_name','CUI','telefono','username','email','password1','password2']