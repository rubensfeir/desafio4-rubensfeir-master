from django.shortcuts import render
from mainApp.forms import Formulario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return render(request, 'mainApp/index.html')


def formulario(request):
    form = Formulario()
    return render(request, 'mainApp/formulario.html', {'form': form})


def resultados(request):
    fname = request.POST['fname']
    lname = request.POST['lname']

    context = {}
    context['fname'] = fname
    context['lname'] = lname


    return render(request, 'mainApp/resultados.html', context)