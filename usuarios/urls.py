from django.urls import path
from . import views

urlpatterns = [
    path("cadastrar/", views.cadastrar_usuario, name="cadastrar_usuario"),
    path("login/", views.login_usuario, name="login_usuario"),
    path("logout/", views.logout_usuario, name="logout_usuario"),
    path("listar/", views.listar_usuarios, name="listar_usuarios"),
    path("editar/<int:user_id>/", views.editar_usuario, name="editar_usuario"),
    path("excluir/<int:user_id>/", views.excluir_usuario, name="excluir_usuario"),
]
