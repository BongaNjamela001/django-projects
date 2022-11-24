from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("projects/", views.projects, name="projects"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("math/", views.MathPortfolioView.as_view(), name="math"),
    path("math/<slug:slug>", views.MathPortfolioDetailView.as_view(), name="math"),
    path("eleceng/", views.ElecEngPortfolioView.as_view(), name="eleceng"),
    path("eleceng/<slug:slug>", views.ElecEngPortfolioDetailView.as_view(), name="eleceng"),
    path("compeng/", views.CompEngPortfolioView.as_view(), name="compeng"),
    path("compeng/<slug:slug>", views.CompEngPortfolioDetailView.as_view(), name="compeng"),
    path("chemphys/", views.ChemPhysPortfolioView.as_view(), name="chemphy"),
    path("chemphys/<slug:slug>", views.ChemPhysPortfolioDetailView.as_view(), name="chemphy"),
]