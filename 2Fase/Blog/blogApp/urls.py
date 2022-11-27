from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('animes/',views.animes, name='animes'),
    path('hardware/',views.hardware, name='hardware'),
    path('jogos/',views.jogos, name='jogos'),
    path('<str:nomeAnime>',views.animeDetail, name = 'animeDetail'),
    path('<str:nomeJogos>',views.jogoDetail, name = 'jogoDetail'),
    path('<str:nomeHardware>',views.hardwareDetail, name = 'hardwareDetail'),
]