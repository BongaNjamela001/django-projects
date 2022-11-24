from .models import Portfolio

def portfolio_context(request):

    portfolio = Portfolio.objects.all()

    return {'portfolio':  portfolio}