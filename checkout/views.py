from django.shortcuts import render

def checkoutView(request):
    """
        This view loads the index page
    """
    
    return render(request, 'checkout/checkout.html')