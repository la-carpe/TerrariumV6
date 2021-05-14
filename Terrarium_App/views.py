from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home (request):
    return render(request, 'home.html', {})

def graphiques (request):
    return render(request, 'graphiques.html', {})

