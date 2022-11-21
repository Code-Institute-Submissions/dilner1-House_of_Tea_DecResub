import stripe
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import Order
from .forms import orderForm

def checkoutView(request):
    """
        This view loads the checkout page
    """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'Oops, looks like there is nothing in your basket yet.')
        return redirect(reverse('products'))

    order_form = orderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Kz0ymB7IvVSIDePssplUQzJPXoeo8xVVHgtkffF1g0SCe2ZL8Eu9bajY3FOl9gKRFyJ1HSwEZufxdL1lo7YFjD600ZWt0Dnzq',
        'client_secret': 'sk_test_51Kz0ymB7IvVSIDeP2aEl7sCMC3dvS5TyXzk1L4kBXOkAb1eJ0OhDoHegp7bNKXAVmo0KIopNblg6kH6OWqBCpmZI00ltQ9GmcO',
    }

    return render(request, template, context)