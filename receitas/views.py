from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def receita(request):
    return render(request, 'receita.html')
