from django.shortcuts import render

# Create your views here.
def produtosindex(request):
    return render(request, 'Produtos/produtosindex.html')