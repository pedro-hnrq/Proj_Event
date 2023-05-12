from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from eventos.models import Certificado
from django.contrib.auth.decorators import login_required
from eventos.models import Evento
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.messages import constants

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
    
def excluir_evento(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    messages.add_message(request, constants.SUCCESS, f'Evento: {evento.nome}, excluído com sucesso')
    return redirect(reverse('gerenciar'))

@login_required(login_url='/auth/login/')
def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    
    if request.method == "GET":
        
        return render(request, 'editar_evento.html', {'evento': evento})    
  
    elif request.method == "POST":
        evento.nome = request.POST.get('nome')
        evento.descricao = request.POST.get('descricao')
        evento.data_inicio = request.POST.get('data_inicio')
        evento.data_termino = request.POST.get('data_termino')
        evento.carga_horaria = request.POST.get('carga_horaria')

        evento.cor_principal = request.POST.get('cor_principal')
        evento.cor_secundaria = request.POST.get('cor_secundaria')
        evento.cor_fundo = request.POST.get('cor_fundo')
        
        logo = request.FILES.get('logo')
        
        if logo:
            if logo.size > 100_000_000:
                messages.add_message(request, constants.WARNING,
                                     'A logo do evento deve ter menos de 10MB')
                return redirect(f'/home/editar_evento/{id}')
        
            evento.logo = logo
        
        evento.save()
        messages.add_message(request, constants.INFO, f'Evento {evento.nome} editado com sucesso')
        return redirect(reverse('gerenciar'))