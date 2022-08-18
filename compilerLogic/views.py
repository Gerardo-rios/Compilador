from django.shortcuts import render
from django.http import HttpResponse, Http404
from .controller.src import analizadorLexico 
def index(request):
    context = {
        'data': "Acá se debe cargar los 3 analizadores"
    }
    return render(request, 'analyzers/index.html', context)

def lex_analyzer(request):
    return render(request, 'analyzers/lexiconAnalyzer.html')

def results(request):
    data = analizadorLexico.sendData()
    return render(request, 'analyzers/result.html', {'data': data})


