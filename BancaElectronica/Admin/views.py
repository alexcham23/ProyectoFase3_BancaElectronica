from django.contrib.messages.api import error
from django.shortcuts import render
from django.contrib import messages
from .forms import *
from datetime import date, datetime
import MySQLdb
from  django.db.models import Q
# Create your views here.
db = MySQLdb.connect(host='localhost', user= 'Admin', password='Option65.la', db='BancaElectronica',port=7575, connect_timeout=30)
def admon (request):
    return render(request,'admon.html')

def empresa(request):
    global db
    form= Empresa()
    variables = {
        "form":form,
    }
    if request.method=="POST":
        form=Empresa(data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            c=db.cursor()
            consulta='INSERT INTO usuario VALUES(null,\''+datos.get("Usuario")+'\',\''+datos.get("Password")+'\',\'Empresa\',\'0\')'
            c.execute(consulta)
            db.commit()
            flecha=c.lastrowid
            c.close()
            c=db.cursor()
            consulta='INSERT INTO empresa VALUES('+str(datos.get("nit"))+',\''+datos.get("Tipo_Empresa")+'\',\''+datos.get("nombre_empresa")+'\',\''+datos.get("nombre_comercial")+'\','
            consulta1='\''+datos.get("representante_legal")+'\',\''+datos.get("dirrecion")+'\','+str(datos.get("telefono_empresa"))+','+str(datos.get("telefono_representante"))+',\''+datos.get("email")+'\','+str(flecha)+')'
            consulta=consulta+consulta1
            c.execute(consulta)
            db.commit()
            c.close()
            messages.success(request, 'Cliente registrado con Exito')
            #nombre="Usuario Registrado"
            form=Empresa()
            #variables={"form":form,"mensaje":nombre}
    else:
        nombre="Usuario Ya registrado"
        variables={"form":form,}
    return render(request,'CreateCompany.html',variables)

def persona(self):
    global db
    form=Persona()
    variable={
        "form":form,
    }
    if self.method=="POST":
        form=Persona(data=self.POST)
        if form.is_valid():
            datos=form.cleaned_data
            c=db.cursor()
            consulta='INSERT INTO usuario VALUES(null,\''+datos.get("Usuario")+'\',\''+datos.get("Password")+'\',\'Individual\',\'0\')'
            c.execute(consulta)
            db.commit()
            flecha=c.lastrowid
            c.close()
            c=db.cursor()
            consulta='INSERT INTO persona VALUES('+str(datos.get("nit"))+','+str(datos.get("cui"))+',\''+datos.get("nombre")+'\',\''+datos.get("apellido")+'\','
            fecha= str(datos.get("Fecha_de_Nacimiento")).replace("-","")
            
            if str(datos.get("Telefono_Opcional"))=="None":
                print(fecha)
                
                consulta1=''+fecha+','+str(datos.get("Telefono_Principal"))+',null,\''+datos.get("dirrecion")+'\',\''+datos.get("email")+'\','+str(flecha)+')'
            else:
                consulta1=''+fecha+','+str(datos.get("Telefono_Principal"))+','+str(datos.get("Telefono_Opcional"))+',\''+datos.get("dirrecion")+'\',\''+datos.get("email")+'\','+str(flecha)+')'
            consulta=consulta+consulta1
            print(consulta)
            c.execute(consulta)
            db.commit()
            c.close()
            messages.success(self, 'Cliente registrado con Exito')
            #nombre="Usuario Registrado"
            form=Persona()
            #variables={"form":form,"mensaje":nombre}
        else:    
            messages.error(self, 'error en el sistema')
    else:
        #nombre="Usuario Ya registrado"
        variable={"form":form,}
    return render(self,'CreatePeopleClient.html',variable)

def monetaria(request):
    global db
    form= CuentaMonetaria()
    var={
        "form": form,
    }
    if request.method=="POST":
        form=CuentaMonetaria(data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            c=db.cursor()
            consulta='SELECT c.NitPersona,c.Usuario,x.TipoUsuario FROM persona c INNER JOIN usuario x on c.Usuario=x.IdUsuario WHERE c.NitPersona=\''+str(datos.get("nit"))+'\';'
            print(consulta)
            c.execute(consulta)
            record=c.fetchone()
            c.close()
            print(record)
            if record:
                
                c=db.cursor()
                consult='INSERT INTO cuenta VALUES(null,\'Monetaria\',\''+datos.get("Moneda")+'\',\''+str(datos.get("Monto"))+'\',null,'+str(date.today()).replace("-","")+',\'Activo\',15,0,null,'+str(datos.get("nit"))+','+str(record[1])+');'
                c.execute(consult)
                db.commit()
                c.close()
                form=CuentaMonetaria()
                messages.success(request,'Cuenta Monetaria Creada')
            else:
                c=db.cursor()
                consultas='SELECT c.NitEmpresa,c.Usuario,x.TipoUsuario FROM empresa c INNER JOIN usuario x ON c.Usuario=x.IdUsuario WHERE c.NitEmpresa=\''+str(datos.get("nit"))+'\';'
                c.execute(consultas)
                record=c.fetchone()
                c.close()
                print(record)
                if record:
                    c=db.cursor()
                    print(record[1])
                    consult='INSERT INTO cuenta VALUES(null,\'Monetaria\',\''+datos.get("Moneda")+'\','+str(datos.get("Monto"))+',null,'+str(date.today()).replace("-","")+',\'Activo\',0,0,'+str(datos.get("nit"))+',null,'+str(record[1])+');'
                    print(date.today())
                    c.execute(consult)
                    print(consult)
                    db.commit()
                    c.close()
                    print("aqui")
                    form=CuentaMonetaria()
                    messages.success(request,'Cuenta Monetaria Creada')
                else:
                    print("rayos callo esto")
                    messages.error(request,'No se encontro')
    else:
        var={"form":form,}
    return render(request,'Monetaria.html',var)

def ahorro(request):
    global db
    form=Cuenta_Ahorro()
    var={
        "form": form
    }
    if request.method=="POST":
        form=Cuenta_Ahorro(data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            c=db.cursor()
            consulta='SELECT c.NitPersona,c.Usuario,x.TipoUsuario FROM persona c INNER JOIN usuario x on c.Usuario=x.IdUsuario WHERE c.NitPersona=\''+str(datos.get("nit"))+'\';'
            print(consulta)
            c.execute(consulta)
            record=c.fetchone()
            c.close()
            print(record)
            if record:
                c=db.cursor()
                consult='INSERT INTO cuenta VALUES(null,\'Ahorro\',\''+datos.get("Moneda")+'\',\''+str(datos.get("Monto"))+'\',null,'+str(date.today()).replace("-","")+',\'Activo\',0,'+str(datos.get("Interes")/100)+',null,'+str(datos.get("nit"))+','+str(record[1])+');'
                c.execute(consult)
                db.commit()
                c.close()
                form=Cuenta_Ahorro()
                messages.success(request,'Cuenta de Ahorro Creada')
            else:
                c=db.cursor()
                consultas='SELECT c.NitEmpresa,c.Usuario,x.TipoUsuario FROM empresa c INNER JOIN usuario x ON c.Usuario=x.IdUsuario WHERE c.NitEmpresa=\''+str(datos.get("nit"))+'\';'
                c.execute(consultas)
                record=c.fetchone()
                c.close()
                print(record)
                if record:
                    c=db.cursor()
                    print(record[1])
                    consult='INSERT INTO cuenta VALUES(null,\'Ahorro\',\''+datos.get("Moneda")+'\','+str(datos.get("Monto"))+',null,'+str(date.today()).replace("-","")+',\'Activo\',0,'+str(datos.get("Interes")/100)+','+str(datos.get("nit"))+',null,'+str(record[1])+');'
                    print(date.today())
                    c.execute(consult)
                    print(consult)
                    db.commit()
                    c.close()
                    print("aqui")
                    form=Cuenta_Ahorro()
                    messages.success(request,'Cuenta de Ahorro Creada')
                else:
                    print("rayos callo esto")
                    messages.error(request,'No se encontro')
    else:
        var={"form":form,}
    return render(request,'Ahorro.html',var)

def PlazoFijo(request):
    form=Plazo_Fijo()
    vars={
        "form": form
    }
    if request.method=="POST":
        form=Plazo_Fijo(data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            c=db.cursor()
            consulta='SELECT c.NitPersona,c.Usuario,x.TipoUsuario FROM persona c INNER JOIN usuario x on c.Usuario=x.IdUsuario WHERE c.NitPersona=\''+str(datos.get("nit"))+'\';'
            print(consulta)
            c.execute(consulta)
            record=c.fetchone()
            c.close()
            print(record)
            if record:
                c=db.cursor()
                consult='INSERT INTO cuenta VALUES(null,\'Ahorro\',\''+datos.get("Moneda")+'\',\''+str(datos.get("Monto"))+'\',\''+datos.get("Plazo_A_Pagar")+'\','+str(date.today()).replace("-","")+',\'Activo\',0,'+str(datos.get("Interes")/100)+',null,'+str(datos.get("nit"))+','+str(record[1])+');'
                c.execute(consult)
                db.commit()
                c.close()
                form=Plazo_Fijo()
                messages.success(request,'Cuenta de Plazo Fijo Creada')
            else:
                c=db.cursor()
                consultas='SELECT c.NitEmpresa,c.Usuario,x.TipoUsuario FROM empresa c INNER JOIN usuario x ON c.Usuario=x.IdUsuario WHERE c.NitEmpresa=\''+str(datos.get("nit"))+'\';'
                c.execute(consultas)
                record=c.fetchone()
                c.close()
                print(record)
                if record:
                    c=db.cursor()
                    print(record[1])
                    consult='INSERT INTO cuenta VALUES(null,\'Ahorro\',\''+datos.get("Moneda")+'\','+str(datos.get("Monto"))+',\''+datos.get("Plazo_A_Pagar")+'\','+str(date.today()).replace("-","")+',\'Activo\',0,'+str(datos.get("Interes")/100)+','+str(datos.get("nit"))+',null,'+str(record[1])+');'
                    print(date.today())
                    c.execute(consult)
                    print(consult)
                    db.commit()
                    c.close()
                    print("aqui")
                    form=Plazo_Fijo()
                    messages.success(request,'Cuenta de Plazo Fijo Creada')
                else:
                    print("rayos callo esto")
                    messages.error(request,'No se encontro')
    else:
        var={"form":form,}
    return render(request,'Plazofijo.html',vars)

def CreditCard(request):
    global db
    form=Creditcard()
    var={"form":form}
    if request.method=="POST":
        form=Creditcard(data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            c=db.cursor()
            consulta='SELECT * from cuenta c, persona b where b.NitPersona=c.ClientePersona and c.NoCuenta=\''+str(datos.get("cuenta"))+'\';'
            #print(consulta)
            c.execute(consulta)
            record=c.fetchone()
            consulta= 'SELECT count(*) FROM creditcard where CuentaAsociada=\''+str(datos.get("cuenta"))+'\';'
            c.execute(consulta)
            contador=c.fetchone()
            print(contador)
            c.close()
            fecha=str(datos.get("vencimiento")).split("/")
            if int(fecha[0])<=12 and int(fecha[1])>20 and int(fecha[1])<100:
                if record:
                    if contador[0]==0:
                        print("entro")
                        if datos.get("Marca")=="PREFEPUNTOS" and datos.get("Limite") >= 5000 and datos.get("Limite")<=7000:
                            c=db.cursor()
                            consulta='INSERT INTO creditcard VALUES (\''+str(datos.get("tarjeta"))+'\',\'PREFEPUNTOS\',\'Q\',\''+str(datos.get("Limite"))+'\''
                            consulta+=','+fecha[0]+','+fecha[0]+',\''+str(datos.get("cvv"))+'\',\'0\',\'0\',\'Individual\',\''+str(datos.get("cuenta"))+'\');'
                            print(consulta)
                            c.execute(consulta) 
                            db.commit()
                            c.close()   
                            messages.info(request,'Se ha asociado la tarjeta al client')
                        
                        elif datos.get("Marca")=="CASHBACK" and datos.get("Limite") >= 5000 and datos.get("Limite")<=7000:
                            c=db.cursor()
                            consulta='INSERT INTO creditcard VALUES (\''+str(datos.get("tarjeta"))+'\',\'CASHBACK\',\'Q\',\''+str(datos.get("Limite"))+'\''
                            consulta+=','+fecha[0]+','+fecha[1]+',\''+str(datos.get("cvv"))+'\',\'0\',\'0\',\'Individual\',\''+str(datos.get("cuenta"))+'\');'
                            c.execute(consulta) 
                            db.commit()
                            c.close() 
                            messages.info(request,'Se ha asociado la tarjeta al client')
                        else:
                            messages.error(request, 'limite entre 5000 - 7000')
                    elif contador[0]==1:
                        if datos.get("Marca")=="PREFEPUNTOS" and datos.get("Limite") >= 4500 and datos.get("Limite")<=5500:
                            c=db.cursor()
                            consulta='INSERT INTO creditcard VALUES (\''+str(datos.get("tarjeta"))+'\',\'PREFEPUNTOS\',\'Q\',\''+str(datos.get("Limite"))+'\''
                            consulta+=','+fecha[0]+','+fecha[0]+',\''+str(datos.get("cvv"))+'\',\'0\',\'0\',\'Individual\',\''+str(datos.get("cuenta"))+'\');'
                            print(consulta)
                            c.execute(consulta) 
                            db.commit()
                            c.close()   
                            messages.info(request,'Se ha asociado la tarjeta al client')
                        
                        elif datos.get("Marca")=="CASHBACK" and datos.get("Limite") >= 4500 and datos.get("Limite")<=5500:
                            c=db.cursor()
                            consulta='INSERT INTO creditcard VALUES (\''+str(datos.get("tarjeta"))+'\',\'CASHBACK\',\'Q\',\''+str(datos.get("Limite"))+'\''
                            consulta+=','+fecha[0]+','+fecha[1]+',\''+str(datos.get("cvv"))+'\',\'0\',\'0\',\'Individual\',\''+str(datos.get("cuenta"))+'\');'
                            c.execute(consulta) 
                            db.commit()
                            c.close() 
                            messages.info(request,'Se ha asociado la tarjeta al client')
                        else:
                            messages.error(request, 'limite entre 4500 - 5500')                    
                    elif contador[0]==3:
                        if datos.get("Marca")=="PREFEPUNTOS" and datos.get("Limite") >= 3500 and datos.get("Limite")<=4000:
                            c=db.cursor()
                            consulta='INSERT INTO creditcard VALUES (\''+str(datos.get("tarjeta"))+'\',\'PREFEPUNTOS\',\'Q\',\''+str(datos.get("Limite"))+'\''
                            consulta+=','+fecha[0]+','+fecha[0]+',\''+str(datos.get("cvv"))+'\',\'0\',\'0\',\'Individual\',\''+str(datos.get("cuenta"))+'\');'
                            print(consulta)
                            c.execute(consulta) 
                            db.commit()
                            c.close()   
                            messages.info(request,'Se ha asociado la tarjeta al client')
                        
                        elif datos.get("Marca")=="CASHBACK" and datos.get("Limite") >= 3500 and datos.get("Limite")<=4000:
                            c=db.cursor()
                            consulta='INSERT INTO creditcard VALUES (\''+str(datos.get("tarjeta"))+'\',\'CASHBACK\',\'Q\',\''+str(datos.get("Limite"))+'\''
                            consulta+=','+fecha[0]+','+fecha[1]+',\''+str(datos.get("cvv"))+'\',\'0\',\'0\',\'Individual\',\''+str(datos.get("cuenta"))+'\');'
                            c.execute(consulta) 
                            db.commit()
                            c.close() 
                            messages.info(request,'Se ha asociado la tarjeta al client')
                        else:
                            messages.error(request, 'limite entre 3500 - 4000')
                    else:
                        messages.error(request,'Ha llegado al limite de tarjetas por cliente')
                
                else: 
                    c=db.cursor()
                    consulta='SELECT * from cuenta c, empresa b where b.NitEmpresa=c.ClienteEmpresa and c.NoCuenta=\''+str(datos.get("cuenta"))+'\';'
                    #print(consulta)
                    c.execute(consulta)
                    record=c.fetchone()  
                    c.close()
                    if  record:
                        if contador[0]==0:
                            print("entro2")
                            if datos.get("Marca")=="PREFEPUNTOS" and datos.get("Limite") >= 10000 and datos.get("Limite")<=15000:
                                c=db.cursor()
                                consulta='INSERT INTO creditcard VALUES (\''+str(datos.get("tarjeta"))+'\',\'PREFEPUNTOS\',\'Q\',\''+str(datos.get("Limite"))+'\''
                                consulta+=','+fecha[0]+','+fecha[0]+',\''+str(datos.get("cvv"))+'\',\'0\',\'0\',\'Empresa\',\''+str(datos.get("cuenta"))+'\');'
                                print(consulta)
                                c.execute(consulta) 
                                db.commit()
                                c.close()   
                                messages.info(request,'Se ha asociado la tarjeta al client')
                        
                            elif datos.get("Marca")=="CASHBACK" and datos.get("Limite") >= 10000 and datos.get("Limite")<=15000:
                                c=db.cursor()
                                consulta='INSERT INTO creditcard VALUES (\''+str(datos.get("tarjeta"))+'\',\'CASHBACK\',\'Q\',\''+str(datos.get("Limite"))+'\''
                                consulta+=','+fecha[0]+','+fecha[1]+',\''+str(datos.get("cvv"))+'\',\'0\',\'0\',\'Empresa\',\''+str(datos.get("cuenta"))+'\');'
                                c.execute(consulta) 
                                db.commit()
                                c.close() 
                                messages.info(request,'Se ha asociado la tarjeta al client')
                            else:
                                messages.error(request, 'limite Primera tarjeta entre 10000 - 15000')
                        elif contador[0]==1:
                            #print("entro2")
                            if datos.get("Marca")=="PREFEPUNTOS" and datos.get("Limite") >= 12000 and datos.get("Limite")<=17000:
                                c=db.cursor()
                                consulta='INSERT INTO creditcard VALUES (\''+str(datos.get("tarjeta"))+'\',\'PREFEPUNTOS\',\'Q\',\''+str(datos.get("Limite"))+'\''
                                consulta+=','+fecha[0]+','+fecha[0]+',\''+str(datos.get("cvv"))+'\',\'0\',\'0\',\'Empresa\',\''+str(datos.get("cuenta"))+'\');'
                                print(consulta)
                                c.execute(consulta) 
                                db.commit()
                                c.close()   
                                messages.info(request,'Se ha asociado la tarjeta al client')
                        
                            elif datos.get("Marca")=="CASHBACK" and datos.get("Limite") >= 12000 and datos.get("Limite")<=17000:
                                c=db.cursor()
                                consulta='INSERT INTO creditcard VALUES (\''+str(datos.get("tarjeta"))+'\',\'CASHBACK\',\'Q\',\''+str(datos.get("Limite"))+'\''
                                consulta+=','+fecha[0]+','+fecha[1]+',\''+str(datos.get("cvv"))+'\',\'0\',\'0\',\'Empresa\',\''+str(datos.get("cuenta"))+'\');'
                                c.execute(consulta) 
                                db.commit()
                                c.close() 
                                messages.info(request,'Se ha asociado la tarjeta al client')
                            else:
                                messages.error(request, 'limite Segunda tarjeta entre 12000 - 17000')     
                        elif contador[0]==3:
                            #print("entro2")
                            if datos.get("Marca")=="PREFEPUNTOS" and datos.get("Limite") >= 12000 and datos.get("Limite")<=17000:
                                c=db.cursor()
                                consulta='INSERT INTO creditcard VALUES (\''+str(datos.get("tarjeta"))+'\',\'PREFEPUNTOS\',\'Q\',\''+str(datos.get("Limite"))+'\''
                                consulta+=','+fecha[0]+','+fecha[0]+',\''+str(datos.get("cvv"))+'\',\'0\',\'0\',\'Empresa\',\''+str(datos.get("cuenta"))+'\');'
                                print(consulta)
                                c.execute(consulta) 
                                db.commit()
                                c.close()   
                                messages.info(request,'Se ha asociado la tarjeta al client')
                        
                            elif datos.get("Marca")=="CASHBACK" and datos.get("Limite") >= 15000 and datos.get("Limite")<=19000:
                                c=db.cursor()
                                consulta='INSERT INTO creditcard VALUES (\''+str(datos.get("tarjeta"))+'\',\'CASHBACK\',\'Q\',\''+str(datos.get("Limite"))+'\''
                                consulta+=','+fecha[0]+','+fecha[1]+',\''+str(datos.get("cvv"))+'\',\'0\',\'0\',\'Empresa\',\''+str(datos.get("cuenta"))+'\');'
                                c.execute(consulta) 
                                db.commit()
                                c.close() 
                                messages.info(request,'Se ha asociado la tarjeta al client')
                            else:
                                messages.error(request, 'limite Tercera tarjeta entre 15000 - 19000')     
                        else:
                            messages.error(request,'Ha llegado al limite de tarjetas por cliente')    
                    else:
                        messages.error(request,'El numero de cuenta o existe')                                                     
            else:
                messages.error("Error en la fecha de vencimiento")    
                
            
    return render(request,'CreditCard.html',var)
