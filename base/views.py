from django.shortcuts import render
from django.contrib import messages #allows toast messages
from .models import (
        Contact,
        Resume,
        Portfolio
    )
from .forms import ContactForm
from django.views import generic
from pathlib import Path
import os

# Create your views here.

class ContactView(generic.FormView):
    template_name = "contact-page.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Thank you. Message received. Bonga will get back to you promptly.")
        return super().form_valid(form)

def home(request):
    return render(request, "home-page.html")

def about(request):
    return render(request, "about-page.html")

def projects(request):
    return render(request, "projects-page.html")

# generate view for Math Portfolio/Projects 
class MathPortfolioView(generic.ListView):
    model = Portfolio
    template_name = "math-page.html"

    def get_queryset(self):
        return super().get_queryset()

# math portfolio view
class MathPortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "math-page.html"

# chem phy portfolio
class ChemPhysPortfolioView(generic.ListView):
    model = Portfolio
    template_name = "chem-phys-page.html"

    def get_queryset(self):
        return super().get_queryset()

# chem phy portfolio    
class ChemPhysPortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "chem-phys-page.html"

class CompEngPortfolioView(generic.ListView):
    model = Portfolio
    template_name = "comp-eng-page.html"

    def get_queryset(self):
        return super().get_queryset()

class CompEngPortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "comp-eng-page.html"

class ElecEngPortfolioView(generic.ListView):
    model = Portfolio
    template_name = "elec-eng-page.html"

    def get_queryset(self):
        return super().get_queryset()

class ElecEngPortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "elec-eng-page.html"