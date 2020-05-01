from django.shortcuts import render
from core.models import Evento

# Create your views here.
"""
uma maneira de direcionar a rota para http://127.0.0.1:8000/agenda/
tem que importar o redirect from django.shortcuts import redirect
def index(request):
    return redirect('/agenda/')
"""
def lista_eventos(request):
    """
    se quiser filtrar por usuario, mas precisa autenticar o usuario...
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    """
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
