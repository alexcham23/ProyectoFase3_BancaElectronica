import MySQLdb
from django import forms
from django.contrib import messages
from django.http.response import HttpResponseRedirect
#from django.forms.forms import Form
from .forms import *
from django.shortcuts import redirect, render
db = MySQLdb.connect(host='localhost', user= 'Admin', password='Option65.la', db='BancaElectronica',port=7575, connect_timeout=30)
# Create your views here.
def BancaPrincipal(request):
    return render(request,'Cuenta.html')
    
def EstadoCuenta(request):
    return render(request,'Estado.html')

def PlanillaProveedor(request):
    return render(request,'Planpro.html')

def Tercero(request):
    return render(request,'Terceros.html')

def Locales(request):
    return render(request,'Propias.html')
    
def CuentaActiva(request):
    return render(request,'suspender.html')

def CuentaSuspendida(request):
    return render(request,'Activar.html')

def Servicio(request):
    return render(request,'Servicios.html')

def PreCheques(request):
    return render(request,'ChequesPre.html')

def Prestamo(request):
    return render(request,'Prestamo.html')
    
def login(request):
    global db
    acount=""
    form=Login()
    var={
        "form":form,
    }
    if request.method == "POST":
        form= Login(data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            username=datos.get("Usuario")
            password=datos.get("Password")
            print(str(password),username)
            c=db.cursor()
            select='SELECT * FROM usuario WHERE Usuario=%s and Pasword=%s'
            c.execute(select,(username,password))
            acount=c.fetchone()
            print(acount)
            c.close()
            form=Login()
            if acount:
                #(2, 'alexcham23g', 'Option65.la', 'Individual', 0)
                if acount[3]=="Administrador":
                    #messages.info(request,'bienvenido Administrador')
                    return redirect('ahora')
                elif acount[3]=="Individual" and acount[4]<3:
                    c=db.cursor()
                    select='UPDATE usuario SET IngresosFallidos=%s WHERE IdUsuario=%s'   
                    c.execute(select,('0',str(acount[0])))
                    db.commit()
                    c.close()   
                    #messages.info(request,'Bienvenido Individual')
                    return redirect('Principal')
                elif acount[3]=="Empresarial" and acount[4]<3:
                    c=db.cursor()
                    select='UPDATE usuario SET IngresosFallidos=%s WHERE IdUsuario=%s'   
                    c.execute(select,('0',str(acount[0])))
                    db.commit()
                    c.close()                       
                    return redirect('Principal')
                else:
                    messages.error(request,'Su Cuenta esta bloqueado Cominiquese con el Banco el Ahorro mas Cercano')
            else:
                username1=datos.get("Usuario")
                print(username)
                c=db.cursor()
                select='SELECT * FROM usuario WHERE Usuario=\''+username1+'\''
                c.execute(select)
                acount=c.fetchone() 
                x=acount[0]
                c.close()
                print(acount[4])
                if acount:
                    if  int(acount[4]) <= 2 and acount[3]=="Individual" or acount[3]=="Empresarial":
                        cantidad=acount[4]+1 
                        c=db.cursor()
                        select='UPDATE usuario SET IngresosFallidos=%s WHERE IdUsuario=%s'   
                        c.execute(select,(str(cantidad),str(x))) 
                        db.commit()
                        c.close()      
                        messages.error(request,'contraseña invalida')
                    elif acount[3]=="Individual" or acount[3]=="Empresarial" and int(acount[4]) == 3:
                        messages.error(request,'Su Cuenta esta bloqueado Cominiquese con el Banco el Ahorro mas Cercano')
                    else:
                        messages.error(request,'Usuario o Contraseña invalida')
                else:
                    messages.error(request,'Usuario o Contraseña invalida')
    return render(request,'index.html',var)