from typing import Reversible
from django.conf.urls import include
from django.contrib import admin
from django.urls import reverse
from django.urls import  path
from webapp import views
urlpatterns=[
    path('',views.login,name='lobit'),
    path('bancaPrincipal/',views.BancaPrincipal,name='Principal'),
    path('EstadoCuenta/',views.EstadoCuenta,name='EstadoCuenta'),
    path('Planilla/',views.Planilla,name='planilla'),
    path('Proveedor/',views.Proveedor,name='proveedor'),
    path('Transferencia-a-Tercero/',views.Tercero,name='tercero'),
    path('Transferencia-Locales/',views.Locales,name='propios'),
    path('CuentasActivas/',views.CuentaActiva,name='CuentaActiva'),
    path('CuentaSuspendida/',views.CuentaSuspendida,name='CuentaSuspendida'),
    path('servicios/',views.Servicio,name='servicio'),
    path('Pre-Autorizacion-Cheques',views.PreCheques,name='precheques'),
    path('Prestamo/',views.prestamo,name='Prestamo'),
    path('Registro-Proveedores/',views.ProvRegister,name='registerprov'),
    path('Editar-Proveedor/<int:id>/',views.editproveedor,name='EditarProv'),
    path('Delet-Proveedor/<int:id>/',views.deletprovedor,name='DeletProv'),
    path('Registro-Empleado/',views.PlanRegister,name='PlanillaReg'),
    path('Editar-Empleado/<int:id>/',views.EditPlanilla,name='editPLa'),
    path('Eliminar-Empleado/<int:id>/',views.DeletPlanilla,name='Deletplan'),
    path('LecturaCsv/',views.csvImport,name='csv'),
    path('Autorizar-Pago-Empresarial/<int:id>/',views.PagoPlan,name='pagoplan'),
    path('Cotizar-Prestamo/',views.cotizar,name='cotiza'),
    #path('Admin/',include('Admin.urls')),
]