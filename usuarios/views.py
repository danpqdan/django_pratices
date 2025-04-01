from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, UsuarioLoginForm, UsuarioUpdateForm


def cadastrar_usuario(request):
    """Cadastra um novo usuário utilizando e-mail como identificador."""
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Save will return the user object
            user = form.save()
            user.username = user.email  # Set username to email
            user.save()
            login(request, user)
            return redirect("listar_usuarios")
        else:
            # If form is invalid, we should not try to save it
            # Just render the form again with errors
            print(form.errors)  # Log errors for debugging
    else:
        form = UsuarioForm()

    return render(request, "cadastrar_usuario.html", {"form": form})


def login_usuario(request):
    """Realiza o login utilizando e-mail e senha."""
    if request.method == "POST":
        form = UsuarioLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("listar_usuarios")
    else:
        form = UsuarioLoginForm()
        return render(request, "login.html", {"form": form})


@login_required
def logout_usuario(request):
    """Faz logout do usuário e redireciona para a página de login."""
    logout(request)
    return redirect("login_usuario")


@login_required
def listar_usuarios(request):
    """Lista todos os usuários cadastrados."""
    usuarios = User.objects.all()
    return render(request, "listar_usuarios.html", {"usuarios": usuarios})


@login_required
def editar_usuario(request, user_id):
    """Permite editar o e-mail de um usuário."""
    usuario = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        form = UsuarioUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            user = form.save(commit=True)
            user.username = user.email  # Mantém o e-mail como username
            user.save()
            return redirect("listar_usuarios")
    else:
        form = UsuarioUpdateForm(instance=usuario)
        return render(request, "editar_usuario.html", {"form": form})


@login_required
def excluir_usuario(request, user_id):
    """Exclui um usuário."""
    usuario = get_object_or_404(User, id=user_id)
    usuario.delete()
    return redirect("listar_usuarios")
