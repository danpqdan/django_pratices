from django.urls import path
from . import views 

urlpatterns = [
path('bom-dia/', views.saudacao_bom_dia, name='saudacao_bom_dia'),
]