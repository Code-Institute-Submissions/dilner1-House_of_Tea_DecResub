from django.shortcuts import render
from .models import Order

def checkoutView(request):
    """
        This view loads the index page
    """
    
    return render(request, 'checkout/checkout.html')