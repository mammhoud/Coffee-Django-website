from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def coffee(request):
    return render(request, 'pages/coffee.html')

def about(request):
    return render(request, 'pages/about.html')
