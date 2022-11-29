from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'account/login.html')
def logout(request):
    return render(request,'account/logout.html')
def cadastro(request):
    return render(request,'account/cadastro.html')
def dashboard(request):
    return render(request,'account/dashboard.html')