from django.shortcuts import render

# Create your views here.
def sobreindex(request):
    return render(request, 'Sobre/sobreindex.html')