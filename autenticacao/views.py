from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not (senha == confirmar_senha):
            messages.add_message(request, constants.ERROR, 'Senhas inválidas')  
            return redirect(reverse('cadastro'))
        
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe')  
            return redirect(reverse('cadastro'))   
        
        v_email = User.objects.filter(email=email)
        
        if v_email.exists()
            messages.add_message(request, constants.ERROR, 'Email já existe')
            return redirect(reverse('cadastro'))  
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        messages.add_message(request, constants.ERROR, 'Cadastro criado com Sucesso')  
        return redirect(reverse('login'))

