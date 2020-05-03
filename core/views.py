
from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
"""
uma maneira de direcionar a rota para http://127.0.0.1:8000/agenda/
tem que importar o redirect from django.shortcuts import redirect
def index(request):
    return redirect('/agenda/')
"""
def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request,"Usuário ou Senha Inválido")
    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    """
    se quiser filtrar por usuario, mas precisa autenticar o usuario...
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    """
    usuario = request.user
    evento = Evento.objects.filter (usuario=usuario)
    #evento = Evento.objects.all()

    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
