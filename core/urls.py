from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar-habilidade/', views.adicionar_habilidade, name='adicionar_habilidade'),
    path('minhas-habilidades/', views.minhas_habilidades, name='minhas_habilidades'),
]
