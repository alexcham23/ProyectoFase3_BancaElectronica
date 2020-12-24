from django import forms
from django.db.models import fields
from .models import *

class Login(forms.Form):
    Usuario= forms.CharField(required=True,max_length=50, help_text='Igrese su Usuario')
    Password=forms.CharField(widget=forms.PasswordInput(),help_text="Ingrese su contraseña") 
    class meta:
        fields=("Usuario", "Contraseña")
        