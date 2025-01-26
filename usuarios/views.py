from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from django.contrib.auth import authenticate, login

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Usuario.objects.filter(username=username).first()
        if user:
            return render(request, 'cadastro.html', {'error': 'Já existe um usuário com esse username.'})

        user = Usuario.objects.create_user(username=username, email=email, password=password)
        user.save()

        return render(request, 'cadastro_sucesso.html')

def autenticar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(username=username, password=senha)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Nome de usuário ou senha inválidos.'})

def home(request):
    return render(request, 'home.html')