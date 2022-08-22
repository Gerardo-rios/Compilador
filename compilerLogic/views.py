import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .controller.src import analizadorLexico 
def index(request):
    """"
    Cargar los analizadores en chevere
    Cuando uno sea elegido, se pasa a la vista de abajo para hacer el análisis
    TAMBIEN PONER LA OPCION DE ANALISIS COMPLETO EN DONDE SE HARÁN LOS 3 ANALISIS 
    """
    context = {
        'data': "Acá se debe cargar los 3 analizadores"
    }
    return render(request, 'analyzers/index.html', context)

def lex_analyzer(request):
    """
    En este metodo se deben cargar los archivos para que sean analizados
    Osea como en dropdown box para elegir el numero de archivo podrías er
    en total son 6. 
    DE IGUAL FORMA PARA LOS OTROS ANALIZADORES 
    """
    return render(request, 'analyzers/lexiconAnalyzer.html')

def results(request):
    """
    ACÁ LLAMAS AL METODO DEL ANALIZADOR CORRESPONDIENTE, 
    PASANDOLE EL NUMERO DE ARCHIVO EN ESTE CASO
    Y EN ESTA VISTA SE CARGARÍAN LOS RESULTADOS
    """
    fileIndex = request.GET.get('FileIndex', 3)
    data = analizadorLexico.doAnalysis(fileIndex)
    return render(request, 'analyzers/result.html', {'data': data})

def test(request):
    """
    ACÁ LLAMAS AL METODO DEL ANALIZADOR CORRESPONDIENTE, 
    PASANDOLE EL NUMERO DE ARCHIVO EN ESTE CASO
    Y EN ESTA VISTA SE CARGARÍAN LOS RESULTADOS
    """

    return render(request, 'home/index.html')


def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin.html':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template
        if load_template == 'analizador-lexico.html':
            fileIndex = request.GET.get('FileIndex', 3)
            data = analizadorLexico.doAnalysis(fileIndex)
            context['data'] = data
                
        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

