from typing import Reversible
from django.conf.urls import include
from django.contrib import admin
from django.urls import reverse
from django.urls import path
from Admin import views

urlpatterns=[
    path('',views.admon, name='ahora'),
    path('Create-Client-People/', views.persona ,name='Persona'),
    path('Create-Client-Company/',views.empresa,name='Company'),
    path('Cuenta-Monetaria/',views.monetaria,name='Cmonetaria'),
    path('Cuenta-Ahorro/',views.ahorro,name='Cahorro'),
    path('Cuenta-Plazo-Fijo/',views.PlazoFijo,name='Cplazo'),
    path('Credit-Card/',views.CreditCard, name='credits'),
    path('Autorizacion-Prestamos/',views.PrestamoAutori,name='autoripresta'),
    path('Rechazo-Prestamo/',views.prestamorechazo,name='Presrecha'),
    path('validar-Prestamo/',views.autoripresta,name='Autoripres'),
]