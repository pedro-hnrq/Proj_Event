from django.shortcuts import render
from eventos.models import Certificado
from django.contrib.auth.decorators import login_required
from eventos.models import Evento
from django.core.paginator import Paginator

@login_required(login_url='/auth/login/') 
def meus_certificados(request):
    certificados = Certificado.objects.filter(participante=request.user)
    return render(request, 'meus_certificados.html', {'certificados': certificados})

@login_required(login_url='/auth/login/')
def gerenciar(request):
    eventos_por_pagina = 5 # Define o número de eventos exibidos por página 
    if request.method == "GET":    
        eventos = Evento.objects.filter(criador=request.user)
        nome_1 = request.GET.get('nome')        
        if nome_1:
            eventos = eventos.filter(nome__contains=nome_1)
        
        paginator = Paginator(eventos, eventos_por_pagina) # Divide a lista de eventos em páginas
        pagina = request.GET.get('pagina')
        eventos_paginados = paginator.get_page(pagina) # Obtém os eventos correspondentes à página atual
        
        return render(request, 'gerenciar.html', {'eventos': eventos_paginados})