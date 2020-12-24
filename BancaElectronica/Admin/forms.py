from django import forms
from django.db.models import fields
from .models import *

class Empresa(forms.Form):
    nit=forms.IntegerField(required=True, help_text='Campo Numerico')
    nombre_empresa=forms.CharField(required=True,max_length=50, help_text='Nombre de la empresa')
    nombre_comercial = forms.CharField(required=True, max_length=50, help_text='Nombre Comercial de la empresa')
    representante_legal = forms.CharField(required=True, max_length=75, help_text='Nombre Representante Legal')
    dirrecion = forms.CharField(required=True, max_length=250, help_text='Ingrese su dirrecion')
    telefono_empresa = forms.DecimalField(required=True,max_digits=8,decimal_places=0,help_text='Ingrese el numero telefonico')
    telefono_representante = forms.DecimalField(required=True,max_digits=8,decimal_places=0,help_text='Ingrese el numero telefonico')
    email = forms.EmailField(required=True,max_length=50,help_text='Ingrese su dirrecion de Correo')
    EmpresaTipo=(
        ('Sociedad Anonima','Sociedad Anonima'),
        ('Compania Limitada','Compania Limitada'),
        ('Empresa Individual','Empresa Individual'),
    )
    Tipo_Empresa= forms.ChoiceField(required=True,choices=EmpresaTipo)
    Usuario=forms.CharField(required=True,max_length=50,help_text='Requerido para Banca Electronica')
    Password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields=("nit","nombre_empresa","nombre_comercial","Tipo_Empresa","representante_legal","dirrecion","telefono_empresa","telefono_representante","email","Usuario","Password")
class DateInput(forms.DateInput):
    input_type='date'

class  Persona(forms.Form):
    nit = forms.DecimalField(required=True, help_text="Campo Numerico",max_digits=8, decimal_places=0)
    cui = forms.DecimalField(required=True, help_text="Campo Numerico",max_digits=13, decimal_places=0)
    nombre= forms.CharField(required=True,max_length=50, help_text='Nombre del Cliente')
    apellido= forms.CharField(required=True,max_length=50, help_text='Apellido del Cliente')
    Fecha_de_Nacimiento = forms.DateField(widget=DateInput,required=True,help_text='ingrese su fecha de nacimiento')
    Telefono_Principal= forms.DecimalField(required=True,max_digits=8,decimal_places=0,help_text='Ingrese el numero telefonico')
    Telefono_Opcional = forms.DecimalField(required=False,max_digits=8,decimal_places=0,help_text='Ingrese el numero telefonico(opcional)')
    dirrecion = forms.CharField(required=True, max_length=250, help_text='Ingrese su dirrecion')
    email = forms.EmailField(required=True,max_length=50,help_text='Ingrese su dirrecion de Correo')
    Usuario=forms.CharField(required=True,max_length=50,help_text='Requerido para Banca Electronica')
    Password=forms.CharField(widget=forms.PasswordInput(),help_text="Ingrese su contraseña")
    
    class meta:
        fields=("nit","cui","nombre","apellido","Fecha_de_Nacimiento","Telefono_Principal","Telefono_Opcional","dirrecion","email","Usuario","Password")
#class Persona(forms.Form):
class CuentaMonetaria(forms.Form):
    monedatipo=(
        ("Q","Quetzales"),
        ("$","Dolares")
    )
    Moneda = forms.ChoiceField(required=True,choices=monedatipo)
    Monto= forms.DecimalField(required=True, max_digits=10, decimal_places=2, help_text="Ingrese un Monto") 
    nit= forms.DecimalField(required=True, help_text="Campo Numerico",max_digits=8, decimal_places=0)
    
    class meta:
        fields=("Moneda","Monto","nit")

class Cuenta_Ahorro(forms.Form):
    monedatipo=(
        ("Q","Quetzales"),
        ("$","Dolares")
    )
    Moneda = forms.ChoiceField(required=True,choices=monedatipo)
    Interes=forms.DecimalField(required=True, max_digits=3, decimal_places=0, help_text="Ingrese un Monto") 
    Monto= forms.DecimalField(required=True, max_digits=10, decimal_places=2, help_text="Ingrese un Monto") 
    nit= forms.DecimalField(required=True, help_text="Campo Numerico",max_digits=8, decimal_places=0)
    class meta:
        fields=("Moneda","Interes","Monto","nit")

class Plazo_Fijo(forms.Form):
    monedatipo=(
        ("Q","Quetzales"),
        ("$","Dolares")
    )
    Moneda = forms.ChoiceField(required=True,choices=monedatipo)
    Interes=forms.DecimalField(required=True, max_digits=3, decimal_places=0, help_text="Ingrese un Monto") 
    Monto= forms.DecimalField(required=True, max_digits=10, decimal_places=2, help_text="Ingrese un Monto") 
    nit= forms.DecimalField(required=True, help_text="Campo Numerico",max_digits=8, decimal_places=0)
    Plazotipo=(
        ("3","3 Meses"),
        ("6","6 Meses"),
        ("12","12 Meses"),
        ("24","24 Meses"),
        ("36","36 Meses")
    )
    Plazo_A_Pagar= forms.ChoiceField(required=True,choices=Plazotipo)
    class meta:
        fields=("Moneda","Interes","Monto","Plazo_A_Pagar","nit")