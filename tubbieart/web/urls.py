from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('objetivo/', views.objetivo, name='objetivo'),
    path('avance1/', views.avance1, name='avance1'),
    path('avance2/', views.avance2, name='avance2'),
    path('avance3/', views.avance3, name='avance3'),
    path('resultados/', views.resultados, name='resultados'),
    path('complicaciones/', views.complicaciones, name='complicaciones'),
    path('equipo/', views.equipo, name='equipo'),
]
