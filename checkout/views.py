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
    }

    return render(request, template, context)