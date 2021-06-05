from django.shortcuts import render
from mainApp.forms import Formulario
# Create your views here.
def index(request):
    return render(request, 'mainApp/index.html')


def formulario(request):
    form = Formulario()
    return render(request, 'mainApp/formulario.html', {'form': form})


