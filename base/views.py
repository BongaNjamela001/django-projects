from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home-page.html")

def about(request):
    return render(request, "about-page.html")

def projects(request):
    return render(request, "projects-page.html")

def math(request):
    return render(request, "math-page.html")

def contact(request):
    return render(request, "contact-page.html")

def chemphys(request):
    return render(request, "chem-phys-page.html")

def compeng(request):
    return render(request, "comp-eng-page.html")

def eleceng(request):
    return render(request, "elec-eng-page.html")