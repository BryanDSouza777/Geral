from django.shortcuts import render
from .models import Contato
# Create your views here.
def home(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/home.html',{
        'contatos': contatos,
    })