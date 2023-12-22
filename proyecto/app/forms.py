from django import forms
from . models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'apellidos',
            'DPI',
            'Telefono',
            'nombre_usuario',
            'email',
            'contrasenia',
            'con_contrasenia',
            'roles',
        ]


class CreateUserForm(UserCreationForm):
    nombre = forms.CharField(max_length=30, required=True)
    apellidos = forms.CharField(max_length=30, required=True)
    DPI = forms.CharField(max_length=50, required=True)
    Telefono = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'nombre', 'apellidos', 'DPI', 'Telefono']