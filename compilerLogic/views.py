from django.shortcuts import render
from django.http import HttpResponse, Http404
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
    fileIndex = request.GET.get('FileIndex', 1)
    data = analizadorLexico.doAnalysis(fileIndex)
    return render(request, 'analyzers/result.html', {'data': data})


