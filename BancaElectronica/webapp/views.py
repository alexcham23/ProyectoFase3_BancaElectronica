import os
import MySQLdb
from django import forms
from django.contrib import messages
from django.db.models.query_utils import select_related_descend
from django.http.response import HttpResponseRedirect
#from django.forms.forms import Form
from .forms import *
from django.urls import reverse
from django.shortcuts import redirect, render
from datetime import date, datetime
import csv
db = MySQLdb.connect(host='localhost', user= 'Admin', password='Option65.la', db='BancaElectronica',port=7575, connect_timeout=30)
numero=0
# Create your views here.
def BancaPrincipal(request):
    return render(request,'Cuenta.html')
    
def EstadoCuenta(request):
    return render(request,'Estado.html')
#Area de pago planilla y proveedores--------------------------------------------------
def Planilla(request):
    global db,numero
    c=db.cursor()
    consulta='SELECT * FROM empresa where Usuario=%s'
    print(numero)
    c.execute(consulta,str(numero))
    Nit=c.fetchone()  
    c.close()
    #print(Nit[0])
    c= db.cursor(MySQLdb.cursors.DictCursor)
    consulta='SELECT IdPagoEmpresarial as id,LPAD(CuentaReceptora, 10, "0") as cuenta,Nombre,MontoPago,TiempoPago FROM pago_empresarial where TipoPago=\'Planilla\' and NitEmpresa=\''+str(Nit[0])+'\'' 
    c.execute(consulta)
    datos= c.fetchall()
    #"print(datos[0])
    var={'datos': datos}
    if request.method=="POST" and 'agregar' in request.POST:
        return redirect('PlanillaReg')
        #print("rachivossssssssssssssssssss")
    elif request.method=="POST" and 'archivo' in request.POST:
        return redirect('csv')
        #print("rachivo")
    return render(request,'Planilla.html',var)
def PlanRegister(request):
    global db,numero
    form=PagoEmpresarial()
    var={"form":form}
    if request.method=="POST":
        form=PagoEmpresarial(data=request.POST)
        if form.is_valid():   
            datos=form.cleaned_data
            c= db.cursor()
            consulta='SELECT * FROM empresa where Usuario=%s'
            print(numero)
            c.execute(consulta,str(numero))
            Nit=c.fetchone()
            print(Nit)
            consulta='SELECT * FROM cuenta WHERE NoCuenta=%s'
            c.execute(consulta,str(datos.get("Cuenta")))
            info=c.fetchone()
            consulta='SELECT * FROM pago_empresarial WHERE TipoPago=\'Planilla\' and CuentaReceptora=%s'
            c.execute(consulta,str(datos.get("Cuenta")))
            info2=c.fetchone()
            c.close()
            if info:
                if not info2:
                    c=db.cursor();
                    consulta='INSERT INTO pago_empresarial VALUES(null,\'Planilla\',\''+datos.get("Nombre")+'\',\''+datos.get("TiempoPago")+'\','
                    consulta+='\''+str(datos.get("MontoPago"))+'\',\''+str(datos.get("Cuenta"))+'\',\''+str(Nit[0])+'\');'            
                    c.execute(consulta)
                    db.commit()
                    return redirect('planilla')
                else:
                    messages.error(request,'La Cuenta ya existe')
            else:
                messages.error(request,'El numero de Cuenta no existe')
    return render(request,'RegistroEmpleado.html',var)
def EditPlanilla(request,id):
    c= db.cursor(MySQLdb.cursors.DictCursor)
    consulta='SELECT LPAD(CuentaReceptora, 10, "0") as Cuenta,Nombre,MontoPago,TiempoPago FROM pago_empresarial WHERE IdPagoEmpresarial=%s'
    print(id)
    c.execute(consulta,str(id))
    dato= c.fetchone()
    #print(dato)
    c.close()
    if request.method=="GET":
        form=PagoEmpresarial(initial=dato)
        #form.cleaned_data.
        print(form)
    else:
        form=PagoEmpresarial(data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            c=db.cursor()
            consulta='UPDATE pago_empresarial SET Nombre=%s, TiempoPago=%s, MontoPago=%s,CuentaReceptora=%s WHERE IdPagoEmpresarial=%s'   
            c.execute(consulta,(datos.get("Nombre"),datos.get("TiempoPago"),str(datos.get("MontoPago")),str(datos.get("Cuenta")),str(id)))
            db.commit() 
            c.close()           
            return redirect('planilla')                                                                            
    return render(request,'RegistroEmpleado.html',{"form":form})
def DeletPlanilla(request,id):
    c=db.cursor()
    select='DELETE FROM pago_empresarial WHERE IdPagoEmpresarial=%s'
    c.execute(select,str(id))
    db.commit()
    c.close()
    return redirect('planilla')
def Proveedor(request):
    global db,numero
    c=db.cursor()
    consulta='SELECT * FROM empresa where Usuario=%s'
    print(numero)
    c.execute(consulta,str(numero))
    Nit=c.fetchone()  
    c.close()
    #print(Nit[0])
    c= db.cursor(MySQLdb.cursors.DictCursor)
    consulta='SELECT IdPagoEmpresarial as id,LPAD(CuentaReceptora, 10, "0") as cuenta,Nombre,MontoPago,TiempoPago FROM pago_empresarial where TipoPago=\'Proveedor\' and NitEmpresa=\''+str(Nit[0])+'\'' 
    c.execute(consulta)
    datos= c.fetchall()
    #print(datos[0])
    var={'datos': datos}
    if request.method=="POST":
        return redirect('registerprov')
    return render(request,'Proveedor.html', var)
def ProvRegister(request):
    global db,numero
    form=PagoEmpresarial()
    var={"form":form}
    if request.method=="POST":
        form=PagoEmpresarial(data=request.POST)
        if form.is_valid():   
            datos=form.cleaned_data
            c= db.cursor()
            consulta='SELECT * FROM empresa where Usuario=%s'
            print(numero)
            c.execute(consulta,str(numero))
            Nit=c.fetchone()
            #print(Nit)
            consulta='SELECT * FROM cuenta WHERE NoCuenta=%s'
            c.execute(consulta,str(datos.get("Cuenta")))
            info=c.fetchone()
            print(info)
            consulta='SELECT * FROM pago_empresarial WHERE TipoPago=\'Proveedor\' and CuentaReceptora=%s'
            c.execute(consulta,str(datos.get("Cuenta")))
            info2=c.fetchone()
            print(info2)
            c.close()
            if info:
                if not info2:
                    c=db.cursor();
                    consulta='INSERT INTO pago_empresarial VALUES(null,\'Proveedor\',\''+datos.get("Nombre")+'\',\''+datos.get("TiempoPago")+'\','
                    consulta+='\''+str(datos.get("MontoPago"))+'\',\''+str(datos.get("Cuenta"))+'\',\''+str(Nit[0])+'\');'            
                    c.execute(consulta)
                    db.commit()
                    c.close()
                    return redirect('proveedor')
                else:
                    messages.error(request,'La Cuenta ya existe')
            else:
                messages.error(request,'El numero de Cuenta no existe')
                
    return render(request,'RegistroProveedores.html',var)
def editproveedor(request,id):
    c= db.cursor(MySQLdb.cursors.DictCursor)
    consulta='SELECT LPAD(CuentaReceptora, 10, "0") as Cuenta,Nombre,MontoPago,TiempoPago FROM pago_empresarial WHERE IdPagoEmpresarial=%s'
    print(id)
    c.execute(consulta,str(id))
    dato= c.fetchone()
    #print(dato)
    c.close()
    if request.method=="GET":
        form=PagoEmpresarial(initial=dato)
        #form.cleaned_data.
        print(form)
    else:
        form=PagoEmpresarial(data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            c=db.cursor()
            consulta='UPDATE pago_empresarial SET Nombre=%s, TiempoPago=%s, MontoPago=%s,CuentaReceptora=%s WHERE IdPagoEmpresarial=%s'   
            c.execute(consulta,(datos.get("Nombre"),datos.get("TiempoPago"),str(datos.get("MontoPago")),str(datos.get("Cuenta")),str(id)))
            db.commit() 
            c.close()           
            return redirect('proveedor')                                                                            
    return render(request,'RegistroProveedores.html',{"form":form})
def deletprovedor(request,id):
    c=db.cursor()
    select='DELETE FROM pago_empresarial WHERE IdPagoEmpresarial=%s'
    c.execute(select,str(id))
    db.commit()
    c.close()
    return redirect('proveedor')
def csvImport(request):
    global db,numero
    form=Archivo()
    var={"form":form}
    if request.method=="POST":
        form=Archivo(data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            if os.path.isfile(datos.get("archivo")):
                file=open(datos.get("archivo"),"r",encoding='utf-8')
                for r,leer in enumerate(file):
                    if r > 0:
                        #print(leer)
                        leer=leer.replace("\n","")
                        dato=leer.split(",")
                        print(dato[1])
                        c= db.cursor()
                        consulta='SELECT * FROM empresa where Usuario=%s'
                        print(numero)
                        c.execute(consulta,str(numero))
                        Nit=c.fetchone()
                        print(Nit)
                        consulta='SELECT * FROM cuenta WHERE NoCuenta=\''+dato[1]+'\''
                        c.execute(consulta)
                        info=c.fetchone()
                        consulta='SELECT * FROM pago_empresarial WHERE TipoPago=\'Planilla\' and CuentaReceptora=\''+dato[1]+'\''
                        c.execute(consulta)
                        info2=c.fetchone()
                        c.close()
                        if info:
                            if not info2:
                                c=db.cursor();
                                consulta='INSERT INTO pago_empresarial VALUES(null,\'Planilla\',\''+dato[0]+'\',\'Quincenal\','
                                consulta+='\''+dato[2]+'\',\''+dato[1]+'\',\''+str(Nit[0])+'\');'            
                                c.execute(consulta)
                                db.commit()
                                #return redirect('planilla')
                            else:
                                c=db.cursor()
                                consulta='UPDATE pago_empresarial SET Nombre=%s,MontoPago=%s WHERE  TipoPago=\'Planilla\' and CuentaReceptora=%s'   
                                c.execute(consulta,(dato[0],dato[2],dato[1]))
                                db.commit() 
                                c.close()   
                        else:
                            c=db.cursor()
                            consult='INSERT INTO cuenta VALUES(\''+dato[1]+'\',\'Monetaria\',\'Q\',\'250\',null,'+str(date.today()).replace("-","")+',\'Activo\',15,0,null,null,null);'
                            c.execute(consult)
                            db.commit()
                            c.close()
                            if not info2:
                                c=db.cursor();
                                consulta='INSERT INTO pago_empresarial VALUES(null,\'Planilla\',\''+dato[0]+'\',\'Quincenal\','
                                consulta+='\''+dato[2]+'\',\''+dato[1]+'\',\''+str(Nit[0])+'\');'            
                                c.execute(consulta)
                                db.commit()
                                #return redirect('planilla')
                            else:
                                c=db.cursor()
                                consulta='UPDATE pago_empresarial SET Nombre=%s,MontoPago=%s WHERE  TipoPago=\'Planilla\' and CuentaReceptora=%s'   
                                c.execute(consulta,(dato[0],dato[2],dato[1]))
                                db.commit() 
                                c.close()                           
            else:
                messages.error(request,'El archivo no existe en la ruta indicada')
    return render(request,'csv.html',var)
def PagoPlan(request):
    global db,numero
    c=db.cursor()
    consulta='SELECT * FROM empresa where Usuario=%s'
    print(numero)
    c.execute(consulta,str(numero))
    Nit=c.fetchone()  
    c.close()
    #print(Nit[0])
    c= db.cursor(MySQLdb.cursors.DictCursor)
    consulta='SELECT IdPagoEmpresarial as id,LPAD(CuentaReceptora, 10, "0") as cuenta,Nombre,MontoPago,TiempoPago FROM pago_empresarial where TipoPago=\'Planilla\' and NitEmpresa=\''+str(Nit[0])+'\'' 
    c.execute(consulta)
    datos= c.fetchall()
    return render(request,'PagoPlanilla.html')
#---------------------------------------------------------------
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
    global db,numero
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
            numero=acount[0]
            print(numero)
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
                elif acount[3]=="Empresa" and acount[4]<3:
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