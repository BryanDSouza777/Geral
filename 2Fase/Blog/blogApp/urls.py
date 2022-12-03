from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('animes/',views.animes, name='animes'),
    path('hardware/',views.hardware, name='hardware'),
    path('jogos/',views.jogos, name='jogos'),
    
    path('searchAnimes/', views.searchAnimes, name='searchAnimes'),
    path('searchHardware/', views.searchHardware, name='searchHardware'),
    path('searchJogos/', views.searchJogos, name='searchJogos'),
    
    path('jogos/<str:nomeJogos>',views.jogoDetail, name = 'jogoDetail'),
    path('hardware/<str:nomeHardware>',views.hardwareDetail, name = 'hardwareDetail'),
    path('animes/<str:nomeAnime>',views.animeDetail, name = 'animeDetail'),
]