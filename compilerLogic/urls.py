from django.urls import path

from . import views
from django.urls import path, re_path

urlpatterns = [
    # ex: /compiler -> main page
    path('', views.index, name='index'),
    re_path(r'^.*\.*', views.pages, name='pages'),
    #path('test', views.test, name='test'),
    ## ex: /compiler/lex-analyzer
    #path('lex-analyzer/', views.lex_analyzer, name='lex_analyzer'),
    ## ex: /compiler/lex-analyzer/results
    #path('lex-analyzer/results/', views.results, name='results'),
]
