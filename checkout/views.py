import stripe
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .models import Order
from .forms import orderForm
from basket.contexts import current_basket


def checkoutView(request):
    """
        This view loads the checkout page
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_Key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'Oops, looks like there is nothing in your basket yet.')
        return redirect(reverse('products'))

    basket_order = current_basket(request)
    total = basket_order['grand_total']
    stripe_total = round(total * 100)
    order_form = orderForm()
    template = 'checkout/checkout.html'
    stripe.api_key = stripe_secret_Key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency='gbp',
    )

    print(intent)
    if not stripe_public_key:
        message.warning(request, 'Stripe public key is not present, \
            you need to set this in the environment before proceeding.')

    context = {
        'order_form': order_form,
        'stripe_public_key': 'stripe_public_key',
        'client_secret': 'stripe_secret_Key',
    }

    return render(request, template, context)