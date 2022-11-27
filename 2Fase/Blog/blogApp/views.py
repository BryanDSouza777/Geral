from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Animes, Hardware, Jogos
# Create your views here.
def home(request):
    return render(request, 'blogApp/home.html')

def animes(request):
    animes = Animes.objects.all()
    return render(request, 'blogApp/animes.html',{
    'animes': animes
    })
def animeDetail(request, nomeAnime):
    animeUrl = get_object_or_404(Animes, nome=nomeAnime)
    return render(request, 'blogApp/animeDetail.html',{
        'animeUrl': animeUrl
    })
def hardware(request):
    hardware = Hardware.objects.all()
    return render(request, 'blogApp/hardware.html',{
    'hardware': hardware
    })
def hardwareDetail(request, nomeHardware):
    hardwareUrl = get_object_or_404(Hardware, nome=nomeHardware)
    return render(request, 'blogApp/hardwareDetail.html',{
        'hardwareUrl': hardwareUrl
    })
def jogos(request):
    jogos = Jogos.objects.all()
    return render(request, 'blogApp/jogos.html',{
    'jogos': jogos
    })
def jogoDetail(request, nomeJogos):
    jogoUrl = get_object_or_404(Jogos, nome=nomeJogos)
    return render(request, 'blogApp/jogoDetail.html',{
        'jogoUrl': jogoUrl
    })