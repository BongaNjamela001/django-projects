from django.urls import path
from . import views

app_name = 'njamelaswebsite'

urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("projects/", views.projects, name="projects"),
    path("contact/", views.contact, name="contact"),
    path("math/", views.math, name="math"),
    path("eleceng/", views.eleceng, name="eleceng"),
    path("compeng/", views.compeng, name="compeng"),
    path("chemphys/", views.chemphys, name="chemphy"),
]