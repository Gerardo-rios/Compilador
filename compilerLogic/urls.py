from django.urls import path

from . import views

urlpatterns = [
    # ex: /compiler -> main page
    path('', views.index, name='index'),
    # ex: /compiler/lex-analyzer
    path('lex-analyzer/', views.lex_analyzer, name='lex_analyzer'),
    # ex: /compiler/lex-analyzer/results
    path('lex-analyzer/results/', views.results, name='results'),
]
