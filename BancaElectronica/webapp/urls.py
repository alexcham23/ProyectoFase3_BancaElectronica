from django.conf.urls import include
from django.contrib import admin
from django.urls import  path
from webapp import views
urlpatterns=[
    path('',views.login),
    path('bancaPrincipal/',views.BancaPrincipal,name='Principal'),
    path('EstadoCuenta/',views.EstadoCuenta,name='EstadoCuenta'),
    path('PlanillaProveedor/',views.PlanillaProveedor,name='PlanillaProveedor'),
    path('Transferencia-a-Tercero/',views.Tercero,name='tercero'),
    path('Transferencia-Locales/',views.Locales,name='propios'),
    path('CuentasActivas/',views.CuentaActiva,name='CuentaActiva'),
    path('CuentaSuspendida/',views.CuentaSuspendida,name='CuentaSuspendida'),
    path('servicios/',views.Servicio,name='servicio'),
    path('Pre-Autorizacion-Cheques',views.PreCheques,name='precheques'),
    path('Prestamo/',views.Prestamo,name='Prestamo'),
    #path('Admin/',include('Admin.urls')),
]