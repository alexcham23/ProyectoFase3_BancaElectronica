from django.contrib import admin
from django.urls import path
from Admin import views

urlpatterns=[
    path('',views.admon, name='ahora'),
    path('Create-Client-People/', views.persona ,name='Persona'),
    path('Create-Client-Company/',views.empresa,name='Company'),
    path('Cuenta-Monetaria/',views.monetaria,name='Cmonetaria'),
    path('Cuenta-Ahorro/',views.ahorro,name='Cahorro'),
    path('Cuenta-Plazo-Fijo/',views.PlazoFijo,name='Cplazo'),
]