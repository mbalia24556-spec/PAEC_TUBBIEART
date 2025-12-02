
# Create your views here.
from django.shortcuts import render

def inicio(request):
    return render(request, 'web/inicio.html')

def objetivo(request):
    return render(request, 'web/objetivo.html')

def avance1(request):
    return render(request, 'web/avance1.html')

def avance2(request):
    return render(request, 'web/avance2.html')

def avance3(request):
    return render(request, 'web/avance3.html')

def resultados(request):
    return render(request, 'web/resultados.html')

def complicaciones(request):
    return render(request, 'web/complicaciones.html')

def equipo(request):
    return render(request, 'web/equipo.html')
