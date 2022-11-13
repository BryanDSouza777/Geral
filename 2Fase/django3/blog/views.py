from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request,'blog/home.html')
    
def sobre(request):
    return render(request,'blog/sobre.html')