import os
import MySQLdb
from django import forms
from django.contrib import messages
from django.db.models.query_utils import select_related_descend
from django.http.response import HttpResponseRedirect
import decimal
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
                        #print(dato[0])
                        c= db.cursor()
                        consulta='SELECT * FROM empresa where Usuario=%s'
                        #print(numero)
                        c.execute(consulta,str(numero))
                        Nit=c.fetchone()
                        #print(Nit)
                        consulta='SELECT * FROM cuenta WHERE NoCuenta=\''+dato[0]+'\''
                        c.execute(consulta)
                        info=c.fetchone()
                        consulta='SELECT * FROM pago_empresarial WHERE TipoPago=\'Planilla\' and CuentaReceptora=\''+dato[0]+'\''
                        c.execute(consulta)
                        info2=c.fetchone()
                        c.close()
                        if info:
                            if not info2:
                                c=db.cursor();
                                consulta='INSERT INTO pago_empresarial VALUES(null,\'Planilla\',\''+dato[1]+'\',\'Quincenal\','
                                consulta+='\''+dato[2]+'\',\''+dato[0]+'\',\''+str(Nit[0])+'\');'            
                                c.execute(consulta)
                                db.commit()
                                #return redirect('planilla')
                            else:
                                c=db.cursor()
                                consulta='UPDATE pago_empresarial SET Nombre=%s,MontoPago=%s WHERE  TipoPago=\'Planilla\' and CuentaReceptora=%s'   
                                c.execute(consulta,(dato[1],dato[2],dato[0]))
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
                                consulta='INSERT INTO pago_empresarial VALUES(null,\'Planilla\',\''+dato[1]+'\',\'Quincenal\','
                                consulta+='\''+dato[2]+'\',\''+dato[0]+'\',\''+str(Nit[0])+'\');'            
                                c.execute(consulta)
                                db.commit()
                                #return redirect('planilla')
                            else:
                                c=db.cursor()
                                consulta='UPDATE pago_empresarial SET Nombre=%s,MontoPago=%s WHERE  TipoPago=\'Planilla\' and CuentaReceptora=%s'   
                                c.execute(consulta,(dato[1],dato[2],dato[0]))
                                db.commit() 
                                c.close()    
                return redirect('planilla')                               
            else:
                messages.error(request,'El archivo no existe en la ruta indicada')
    return render(request,'csv.html',var)
def PagoPlan(request,id):
    global db,numero
    c=db.cursor()
    consulta='SELECT * FROM empresa where Usuario=%s'
    print(numero)
    c.execute(consulta,str(numero))
    Nit=c.fetchone()  
    c.close()
    #print(Nit[0])
    c= db.cursor(MySQLdb.cursors.DictCursor)
    consulta='SELECT LPAD(NoCuenta, 10, "0") as cuenta,TipoCuenta FROM cuenta where ClienteEmpresa=\''+str(Nit[0])+'\'' 
    c.execute(consulta)
    datos= c.fetchall()
    form=Pagoplani()
    var ={"form":form,"datos":datos}
    if request.method=="POST":
        print("entro")
        form=Pagoplani(data=request.POST)
        cuenta=request.POST['tabla']# recivo la informacion de select html
        if form.is_valid():
            datos=form.cleaned_data
            c=db.cursor()
            select='SELECT * FROM usuario where IdUsuario=%s'
            c.execute(select,str(numero))
            usuario=c.fetchone()
            c.close()
            if usuario[2] == datos.get("Password"):
                c=db.cursor()
                select='SELECT * FROM pago_empresarial where IdPagoEmpresarial=%s'
                c.execute(select,(str(id),))
                empresarial=c.fetchone()
                select='SELECT Monto FROM cuenta WHERE NoCuenta=\''+str(empresarial[5])+'\''
                c.execute(select)
                cuenta2=c.fetchone()
                select='SELECT Monto FROM cuenta WHERE NoCuenta=\''+str(cuenta)+'\''
                c.execute(select)
                estado=c.fetchone()                
                print(int(estado[0]))
                print(int(empresarial[4]))
                if int(estado[0])>=int(empresarial[4]):
                    montoactual=cuenta2[0]+empresarial[4]
                    fecha=str(date.today()).replace("-","")
                    select ='INSERT INTO transaccion VALUES(null,\' Pago salario\',\'Desposito\',\'Q\',\''+str(empresarial[4])+'\',\''+str(montoactual)+'\',\''+fecha+'\',\''+str(empresarial[5])+'\')'
                    c.execute(select)
                    db.commit()
                    flecha=c.lastrowid
                    select='INSERT INTO trnspago VALUES(\''+str(id)+'\',\''+str(flecha)+'\')'
                    c.execute(select)
                    db.commit()
                    select='UPDATE cuenta SET Monto=%s where NoCuenta=%s'
                    c.execute(select,(str(montoactual),str(empresarial[5])))
                    db.commit()
                    ##  Aqui empieza el retiro
                    montoactual=estado[0]-empresarial[4]
                    select ='INSERT INTO transaccion VALUES(null,\' Pago salario\',\'Retiro\',\'Q\',\''+str(empresarial[4])+'\',\''+str(montoactual)+'\',\''+fecha+'\',\''+str(cuenta)+'\')'
                    c.execute(select)
                    db.commit()
                    flecha=c.lastrowid
                    select='INSERT INTO trnspago VALUES(\''+str(id)+'\',\''+str(flecha)+'\')'
                    c.execute(select)
                    db.commit()
                    select='UPDATE cuenta SET Monto=%s where NoCuenta=%s'
                    c.execute(select,(str(montoactual),str(cuenta)))
                    db.commit()
                    c.close()               
                    messages.success(request,"SE HA REALIZADO LA TRANSACCION")
                elif cuenta2[0]==0:
                    messages.error(request, "CUENTA SIN FONDOS") 
                else:
                    messages.success(request,'TUS FONDOS SON INSFICIENTES PARA REALIZAR LA TRANSACCION')   
    return render(request,'PagoPlanilla.html',var)
#---------------------------------------------------------------

# Area de Prestamos---------------------------------------------------
def cotizar(request):
    lista=[]
    lista2={}
    form=cortizador()
    var={'form':form}
    if request.method=="POST" and 'cotiza' in request.POST:
        form=cortizador(data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            interes=float(intereses(datos.get("monto"),int(datos.get("TiempoPago"))))
            print(interes)
            cash=float(datos.get("monto"))
            print(cash)
            capital=float(datos.get("monto")/int(datos.get("TiempoPago")))
            for i in range(int(datos.get("TiempoPago"))):
                Pago_interes=cash*interes
                cuota=capital+Pago_interes
                otro={"capital":decimal.Decimal(capital),"pago":Pago_interes,"cuota":cuota,"cash":cash}
                lista.append(otro)
                cash-=capital
            for i in lista:
                lista2.update(i)
            print(lista2)
            form=cortizador()
            var={'form':form,'lista':lista}
    elif request.method=="POST" and 'solicita' in request.POST:
        print("nos va bien")
    return render(request,'cotizador.html',var)
#----------------------------------------------------------------------
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
def intereses(cash,tiempo):
    if cash>=1000 and cash<=5000:
        print("entro")
        if tiempo==12:
            print("hola")
            inter=0.05
            return inter
        elif tiempo==24:
            return 0.04
        elif tiempo==36:
            return 0.0335
        elif tiempo==48:
            return 0.025
    elif cash > 5000 and cash <=15000:
        if tiempo==12:
            return 0.0525
        elif tiempo==24:
            return 0.0415
        elif tiempo==36:
            return 0.035
        elif tiempo==48:
            return 0.026         
    elif cash > 15000 and cash <=30000:
        if tiempo==12:
            return 0.053
        elif tiempo==24:
            return 0.042
        elif tiempo==36:
            return 0.0355
        elif tiempo==48:
            return 0.0265
    elif cash > 30000 and cash <=60000:
        if tiempo==12:
            return 0.0535
        elif tiempo==24:
            return 0.0425
        elif tiempo==36:
            return 0.036
        elif tiempo==48:
            return 0.027
    elif cash > 60000:
        if tiempo==12:
            return 0.0545
        elif tiempo==24:
            return 0.0435
        elif tiempo==36:
            return 0.037
        elif tiempo==48:
            return 0.028
                  
           