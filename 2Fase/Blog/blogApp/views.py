from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Animes, Hardware, Jogos
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
def home(request):
    return render(request, 'blogApp/home.html')

def animes(request):
    animes = Animes.objects.order_by('nome').filter(
        mostrar = True
    )
    paginator = Paginator(animes, 5)
    page = request.GET.get('page')
    animes = paginator.get_page(page)
    return render(request, 'blogApp/animes.html',{
    'animes': animes
    })
def animeDetail(request, nomeAnime):
    animeUrl = get_object_or_404(Animes, nome=nomeAnime)
    if not animeUrl.mostrar:
        raise Http404()
    return render(request, 'blogApp/animeDetail.html',{
        'animeUrl': animeUrl
    })
def hardware(request):
    hardware = Hardware.objects.order_by('nome').filter(
        mostrar = True
    )
    paginator = Paginator(hardware, 5)
    page = request.GET.get('page')
    hardware = paginator.get_page(page)

    return render(request, 'blogApp/hardware.html',{
    'hardware': hardware
    })
def hardwareDetail(request, nomeHardware):
    hardwareUrl = get_object_or_404(Hardware, nome=nomeHardware)
    if not hardwareUrl.mostrar:
        raise Http404()
    return render(request, 'blogApp/hardwareDetail.html',{
        'hardwareUrl': hardwareUrl
    })
def jogos(request):
    jogos = Jogos.objects.order_by('nome').filter(
        mostrar = True
    )
    paginator = Paginator(jogos, 5)
    page = request.GET.get('page')
    jogos = paginator.get_page(page)
    return render(request, 'blogApp/jogos.html',{
    'jogos': jogos
    })
def jogoDetail(request, nomeJogos):
    jogoUrl = get_object_or_404(Jogos, nome=nomeJogos)
    if not jogoUrl.mostrar:
        raise Http404()
    return render(request, 'blogApp/jogoDetail.html',{
        'jogoUrl': jogoUrl
    })
def searchAnimes(request):
    searchAnimes = request.GET.get('searchAnimes')
    animes = Animes.objects.order_by('nome').filter(
    Q(nome__icontains=searchAnimes),
    mostrar=True
    )
    paginator = Paginator(animes, 5)
    page = request.GET.get('page')
    animes = paginator.get_page(page)
    return render(request, 'blogApp/searchAnimes.html',{
        'animes': animes
    })
def searchHardware(request):
    searchHardware = request.GET.get('searchHardware')
    hardware = Hardware.objects.order_by('nome').filter(
    Q(nome__icontains=searchHardware),
    mostrar=True
    )
    paginator = Paginator(hardware, 5)
    page = request.GET.get('page')
    hardware = paginator.get_page(page)
    return render(request, 'blogApp/searchHardware.html',{
        'hardware': hardware
    })
def searchJogos(request):
    searchJogos = request.GET.get('searchJogos')
    jogos = Jogos.objects.order_by('nome').filter(
    Q(nome__icontains=searchJogos),
    mostrar=True
    )
    paginator = Paginator(jogos, 5)
    page = request.GET.get('page')
    jogos = paginator.get_page(page)
    return render(request, 'blogApp/searchJogos.html',{
        'jogos': jogos
    })