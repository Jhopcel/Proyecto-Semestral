from django.forms import ModelForm, fields, Form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(Form):
    username = forms.CharField(widget=forms.TextInput(), label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    class Meta:
        fields = ['username', 'password']

class RegistrarUsuarioForm(UserCreationForm):
    rut = forms.CharField(max_length=80, required=True, label="Rut")
    direccion = forms.CharField(max_length=80, required=True, label="Dirección")
    telefono = forms.CharField(max_length=100, required=True, label="Teléfono")
    comuna = forms.CharField(max_length=100, required=True, label="Comuna")
    region = forms.CharField(max_length=100, required=True, label="Región")
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'rut', 'direccion', 'telefono', 'comuna', 'region']

class PerfilUsuarioForm(Form):
    first_name = forms.CharField(max_length=150, required=True, label="Nombres")
    last_name = forms.CharField(max_length=150, required=True, label="Apellidos")
    rut = forms.CharField(max_length=80, required=False, label="Rut")
    direccion = forms.CharField(max_length=80, required=False, label="Dirección")
    telefono = forms.CharField(max_length=100, required=True, label="Teléfono")
    comuna = forms.CharField(max_length=100, required=True, label="Comuna")
    region = forms.CharField(max_length=100, required=True, label="Región")

    class Meta:
        fields = '__all__'

