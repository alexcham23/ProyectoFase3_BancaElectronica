from django import forms
from django.db.models import fields
from .models import *
tipo=(('Mensual','Mensual'),('Quincenal','Quincenal'))
class Login(forms.Form):
    Usuario= forms.CharField(required=True,max_length=50, help_text='Igrese su Usuario')
    Password=forms.CharField(widget=forms.PasswordInput(),help_text="Ingrese su contraseña") 
    class meta:
        fields=("Usuario", "Password")
class terceros(forms.Form):
    cuenta = forms.DecimalField(label="Cuenta de Tercero",widget=forms.TextInput(attrs={'placeholder': 'Ingre el numero de Cuenta',"type":"number"}),required=True,max_digits=10, decimal_places=0)

class PagoEmpresarial(forms.Form):
    global tipo
    Cuenta = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese el numero de Cuenta'}), label="Cuenta del Proveedor")
    Nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese el Nombre Proveedor'}), label="Nombre del Proveedor")
    Sueldo = forms.DecimalField(required=True,max_digits=7, decimal_places=2, widget=forms.TextInput(attrs={'placeholder': 'Ingrese el Sueldo Apagar',"type":"number"}), label="Monto Apagar")
    Tiempo =forms.ChoiceField(required=True,choices=tipo,label="Forma de Pago")
    class Meta:
        fields=("Cuenta","Nombre","Sueldo","Tiempo")    