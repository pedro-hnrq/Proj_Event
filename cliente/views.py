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
    if request.method == "GET":
        evento = get_object_or_404(Evento, id=id)
        return render(request, 'editar_evento.html', {'evento': evento})    
  
    elif request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        data_inicio = request.POST.get('data_inicio')
        data_termino = request.POST.get('data_termino')
        carga_horaria = request.POST.get('carga_horaria')

        cor_principal = request.POST.get('cor_principal')
        cor_secundaria = request.POST.get('cor_secundaria')
        cor_fundo = request.POST.get('cor_fundo')
        
        logo = request.FILES.get('logo')
        
        if logo:
            if logo.size > 100_000_000:
                messages.add_message(request, constants.WARNING,
                                     'A logo do evento deve ter menos de 10MB')
                return redirect(f'/home/editar_evento/{id}')
        
        evento = Evento(
            criador=request.user,
            nome=nome,
            descricao=descricao,
            data_inicio=data_inicio,
            data_termino=data_termino,
            carga_horaria=carga_horaria,
            cor_principal=cor_principal,
            cor_secundaria=cor_secundaria,
            cor_fundo=cor_fundo,
            logo=logo,
        )
        
        evento.save()
        messages.add_message(request, constants.SUCCESS, f'Evento {evento.nome} editado com sucesso')
        return redirect(reverse('gerenciar'))