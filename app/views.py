from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'app/base-template.html')

def home(request):
    return render(request, 'app/home-template.html')

def about(request):
    return render(request, 'app/about-template.html')
