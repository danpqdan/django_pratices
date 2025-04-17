from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required 

@login_required
def saudacao_bom_dia(request):
    saudacao = "Bom dia!"

    # Passa a saudação para o template
    return render(request, 'saudacao.html', {'saudacao': saudacao})
