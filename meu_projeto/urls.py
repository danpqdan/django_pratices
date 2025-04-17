from django.contrib import admin
from django.shortcuts import redirect 
from django.urls import path, include  
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saudacao/', include('saudacao.urls')),  
    path('login/', include('login.urls')),
    path('menu/', include('menu.urls')),
    path('clientes/', include('clientes.urls')),
    path('produtos/', include('produtos.urls')),
    path('vendas/', include('vendas.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('', lambda request: redirect('/login/')), 
]


