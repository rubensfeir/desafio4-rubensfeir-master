from django.shortcuts import render
from mainApp.forms import Formulario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from mainApp.models import Usuario
from mainApp.forms import Formulario, IniciarSesion
# Create your views here.
def index(request):
    return render(request, 'mainApp/index.html')


def formulario(request):
    form = Formulario()
    return render(request, 'mainApp/formulario.html', {'form': form})


def resultados(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    username= request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username=username, password=password)

    usuario = Usuario(user=user, fname=fname, lname=lname)
    usuario.save()

def loginView(request):
    form = IniciarSesion()
    return render(request, 'mainApp/login.html', {'form': form})

def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    usuario = authenticate(username=username, password= password)
    login(request,usuario)
    return render(request, 'mainApp/index.html')

def logoutView(request):
    logout(request)
    return render(request, 'mainApp/index.html')


    context = { }
    context['fname'] = fname
    context['lname'] = lname
    context['username'] = username
    context['password'] = password
    return render(request, 'mainApp/resultados.html', context)