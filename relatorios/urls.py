from django.urls import path
from .views import relatorio_vendas

urlpatterns = [
    path("relatorio/", relatorio_vendas, name="relatorio_vendas"),
]
