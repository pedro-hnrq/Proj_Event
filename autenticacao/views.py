from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants
from .utils import password_is_valid, email_html
import os
from django.conf import settings
from .models import Ativacao
from hashlib import sha256
from django.contrib.auth.views import PasswordResetConfirmView


def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Vai tirar todos os espaços strip()
        if len(username.strip()) == 0 or len(email.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'E-mail ou Senha não podem ficar vazior')
            return redirect('/auth/cadastro/')
        
        if not password_is_valid(request, senha, confirmar_senha):
            return redirect(reverse('cadastro'))
        
        # Verificar se as Senhas são Iguais
        # if not (senha == confirmar_senha):
        #     messages.add_message(request, constants.ERROR, 'Senhas inválidas')  
        #     return redirect(reverse('cadastro'))
        
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe')  
            return redirect(reverse('cadastro'))   
        
        v_email = User.objects.filter(email=email)
        
        if v_email.exists():
            messages.add_message(request, constants.ERROR, 'Email já existe')
            return redirect(reverse('cadastro'))  
        
        try:
            user = User.objects.create_user(username=username, 
                                            email=email, 
                                            password=senha, 
                                            is_active=False)
            user.save()
            
            token = sha256(f"{username}{email}".encode()).hexdigest()
            ativacao = Ativacao(token=token, user=user)
            ativacao.save()
            
            path_template = os.path.join(settings.BASE_DIR, 'autenticacao/templates/emails/cadastro_confirmado.html')
            email_html(path_template, 'Confirme seu cadastro no Type Event', [email,], username=username, link_ativacao=f"127.0.0.1:8000/auth/ativar_conta/{token}")
            messages.add_message(request, constants.INFO, 'Verifique sua caixa de E-mail.')  
            return redirect(reverse('login'))
        except:
            messages.add_message(request, constants.ERROR, 'Erro Interno no sistema')
            return redirect(reverse('cadastro'))
        
def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')

    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=username, 
                                 password=senha)

        if not user:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect(reverse('login'))
        
        auth.login(request, user)
        return redirect('/eventos/novo_evento/')
    
def sair(request):
    auth.logout(request)
    return redirect('/auth/login')

def ativar_conta(request, token):
    token = get_object_or_404(Ativacao, token=token)
    if token.ativo:
        messages.add_message(request, constants.WARNING, 'Essa token já foi usado')
        return redirect('/auth/login')
    user = User.objects.get(username=token.user.username)
    user.is_active = True
    user.save()
    token.ativo = True
    token.save()    
    messages.add_message(request, constants.SUCCESS, f'Conta ativa com sucesso {user}!')
    return redirect('/auth/login')

