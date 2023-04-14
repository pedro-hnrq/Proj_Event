from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from .models import Evento, Certificado
from django.http import Http404, FileResponse
import csv
from secrets import token_urlsafe
import os
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

@login_required(login_url='/auth/login/')
def novo_evento(request):
    if request.method == "GET":
        return render(request, 'novo_evento.html')
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
        
        messages.add_message(request, constants.SUCCESS, 'Evento cadastrado com sucesso')
        return redirect(reverse('novo_evento'))

@login_required(login_url='/auth/login/')   
def gerenciar_evento(request):    
    if request.method == "GET":
        eventos = Evento.objects.filter(criador=request.user)
        
        nome_1 = request.GET.get('nome')        
        if nome_1:
            eventos = eventos.filter(nome__contains=nome_1)
        
        return render(request, 'gerenciar_evento.html', {'eventos': eventos})

@login_required(login_url='/auth/login/')
def inscrever_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == "GET":
        return render(request, 'inscrever_evento.html', {'evento': evento})
    elif request.method == "POST":
        # Validar se o usuário já é um participante
        evento.participantes.add(request.user)
        evento.save()

        messages.add_message(request, constants.SUCCESS, 'Inscrição com sucesso.')
        return redirect(reverse('inscrever_evento', kwargs={'id': id}))
    
@login_required(login_url='/auth/login/')
def participantes_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if not evento.criador == request.user:
        raise Http404('Esse evento não é seu')
    if request.method == "GET":
        participantes = evento.participantes.all()[::3]
        return render(request, 'participantes_evento.html', {'evento': evento, 'participantes': participantes})

@login_required(login_url='/auth/login/')
def gerar_csv(request, id):
    evento = get_object_or_404(Evento, id=id)
    if not evento.criador == request.user:
        raise Http404('Esse evento não é seu')
    
    participantes = evento.participantes.all()
    
    if not participantes.exists():
        messages.add_message(request, constants.ERROR, 'Não há participantes inscritos no evento.')
        return redirect('participantes_evento', id=id)
    
    token = f'{token_urlsafe(6)}.csv'
    path = os.path.join(settings.MEDIA_ROOT, 'csv', token)

    with open(path, 'w') as arq:
        writer = csv.writer(arq, delimiter=",")
        for participante in participantes:
            x = (participante.username, participante.email)
            writer.writerow(x)
            
    response = FileResponse(open(path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{token}"'
    return response

    # return redirect(f'/media/{token}')
    
@login_required(login_url='/auth/login/')   
def certificados_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if not evento.criador == request.user:
        raise Http404('Esse evento não é seu')
    if request.method == "GET":
        qtd_certificados = evento.participantes.all().count() - Certificado.objects.filter(evento=evento).count()
        return render(request, 'certificados_evento.html', {'evento': evento, 'qtd_certificados': qtd_certificados, 'evento': evento})


   
@login_required(login_url='/auth/login/')
def gerar_certificado(request, id):
    evento = get_object_or_404(Evento, id=id)
    if not evento.criador == request.user:
        raise Http404('Esse evento não é seu')
    
    # Referencia ao caminho
    path_template = os.path.join(settings.BASE_DIR, 'templates/static/evento/img/template_certificado.png')
    path_fonte = os.path.join(settings.BASE_DIR, 'templates/static/evento/fontes/arimo.ttf')
    
    certificados_gerados = 0
    
    for participante in evento.participantes.all():
        # TODO: validar se o certificado foi gerado
        img = Image.open(path_template) # Abrir a imagem
        draw = ImageDraw.Draw(img) # Escrever na imagem
        
        fonte_nome = ImageFont.truetype(path_fonte, 80)# fonte e tamnho na imagem
        fonte_info = ImageFont.truetype(path_fonte, 30)
        
        draw.text((249, 630), f"{participante.username}", font=fonte_nome, fill=(0,0,0))
        draw.text((750, 772), f"{evento.nome}", font=fonte_info, fill=(0,0,0))
        draw.text((809, 843 ), f"{evento.carga_horaria} horas", font=fonte_info, fill=(0,0,0))
        
        output = BytesIO()
        img.save(output, format="PNG", quality=100)
        output.seek(0)
        
        img_final = InMemoryUploadedFile(output,
                                         'ImageField',
                                         f'{token_urlsafe(8)}.png',
                                         'imagem.jpeg',
                                         sys.getsizeof(output),
                                         None)
      
        certificado_gerado = Certificado(
            certificado=img_final,
            participante=participante,
            evento=evento,
        )
        certificado_gerado.save()
        
        if certificados_gerados != evento.participantes.all().count():
            messages.add_message(request, constants.ERROR, 'Ocorreu um erro na geração de certificados')
        else:
            messages.add_message(request, constants.SUCCESS, 'Certificados gerados')
        
    return redirect(reverse('certificados_evento', kwargs={'id': evento.id}))


def procurar_certificado(request, id):
    evento = get_object_or_404(Evento, id=id)
    if not evento.criador == request.user:
        raise Http404('Esse evento não é seu')
    
    email = request.POST.get('email')
    
    # filter().filter = and
    certificado = Certificado.objects.filter(evento=evento).filter(participante__email=email).first()
    
    if not certificado:
        messages.add_message(request, constants.WARNING, 'Certificado não encontrado')
        return redirect(reverse('certificados_evento', kwargs={'id': evento.id}))
    
    return redirect(certificado.certificado.url)