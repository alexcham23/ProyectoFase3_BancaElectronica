from django import forms
from django.db.models import fields
from .models import *
tipo=(('Mensual','Mensual'),('Quincenal','Quincenal'))
tiempo=(('12','12'),('24','24'),('36','36'),('48','48'))
class Login(forms.Form):
    Usuario= forms.CharField(required=True,max_length=50, help_text='Igrese su Usuario')
    Password=forms.CharField(widget=forms.PasswordInput(),help_text="Ingrese su contraseña") 
    class meta:
        fields=("Usuario", "Password")
class terceros(forms.Form):
    cuenta = forms.DecimalField(label="Cuenta de Tercero",widget=forms.TextInput(attrs={'placeholder': 'Ingre el numero de Cuenta',"type":"number"}),required=True,max_digits=10, decimal_places=0)

class PagoEmpresarial(forms.Form):
    global tipo
    Cuenta = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese el numero de Cuenta'}), label="No. Cuenta")
    Nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese el Nombre '}), label="Nombre ")
    MontoPago = forms.DecimalField(required=True,max_digits=7, decimal_places=2, widget=forms.TextInput(attrs={'placeholder': 'Ingrese el Sueldo Apagar',"type":"number"}), label="Monto Apagar")
    TiempoPago =forms.ChoiceField(required=True,choices=tipo,label="Forma de Pago")
    class Meta:
        fields=("Cuenta","Nombre","MontoPago","TiempoPago")    
        
class Archivo(forms.Form):
    archivo=forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese el link del archivo '}), label="Dirreccion Archivo CSV ")
    class Meta:
        fields=("archivo")

class Pagoplani(forms.Form):
    Password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña",help_text="Ingrese su contraseña") 
    class Meta:
        fields=("Password")
class cortizador(forms.Form):
    global tiempo
    monto = forms.DecimalField(min_value=1000,initial=1000 ,label= "¿Qué Monto Necesitas?   ")
    TiempoPago =forms.ChoiceField(choices=tiempo,label="¿En cuántos meses deseas pagarlo?   ")
    class Meta:
        fields=("monto","TiempoPago")

class solicitudPrestamo (forms.Form):
    Monto = forms.DecimalField(min_value=1000,initial=1000 ,required=True,max_digits=7, decimal_places=2, widget=forms.TextInput(attrs={'placeholder': '',"type":"number"}), label="Cantidad que esta solicitando")
    TiempoPago =forms.ChoiceField(choices=tiempo,label="¿En cuántos meses deseas pagarlo?   ")
    descripcion = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': ' '}), label="Para que seria el prestamo ")
    class Meta:
        fields=('Monto','TiempoPago','descripcion')