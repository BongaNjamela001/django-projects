from django.shortcuts import render, redirect
from django.contrib import messages #allows toast messages
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

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
    success_url = "../send_email/"

    def form_valid(self, form):
        form.save()
        form.send()
        return super().form_valid(form)

# def contact(request):
    
#     if request.method == 'post':
#         form = ContactForm(request.POST)
        
#         if form.is_valid():           
#             formdetails = form.cleaned_data 
#             mail = {
#                 'name': formdetails['name'],
#                 'email': formdetails['email'],
#                 'brief': formdetails['brief'],
#             }

#             template = render_to_string('email-template.html', mail)
            
#             subject = "Contact Form"
#             email_from = settings.EMAIL_HOST_USER
#             recipient_list = ['lungelobn@gmail.com']
#             send_mail(subject, formdetails['brief'], email_from, recipient_list, fail_silently=False, html_message=template)
#             # email.send()
#         return redirect("thankspage")
    
#     else:
#          form = ContactForm()

#     return render(request, "contact-page.html", {'form':form})

def home(request):
    return render(request, "home-page.html")


def about(request):
    return render(request, "about-page.html")

def send_email(request):
    return render(request, 'email-sent-page.html')

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