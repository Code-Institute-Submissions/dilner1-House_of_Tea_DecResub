import stripe
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import Order, OrderLineItems
from .forms import OrderForm
from products.models import Product
from basket.contexts import current_basket


@login_required(login_url='/accounts/login/')
def checkoutView(request):
    """
        This view loads the checkout page and handles stripe payment request
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_Key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'city': request.POST['city'],
            'address1': request.POST['address1'],
            'address2': request.POST['address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            print("Form is valid")
            order = order_form.save()
            for pk, product_data in basket.items():
                try:
                    product = Product.objects.get(id=pk)
                    if isinstance(product_data, int):
                        order_line_item = OrderLineItems(
                            order=order,
                            product=product,
                            quantity=product_data,
                        )
                        order_line_item.save()
                    else:
                        for weight, quantity in product_data[
                                'item_weight'].items():
                            order_line_item = OrderLineItems(
                                order=order,
                                product=product,
                                quantity=product_data,
                                product_weight=weight,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "An item in your basket is not available. ")
                    )
                    order.delete()
                    return redirect(reverse('basket'))

            print("View should be redirecting")
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_id]))
        else:
            messages.error(request, 'There was an error with your information,\
                please check the form again.')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, 'Oops, \
                looks like there is nothing in your basket yet.')
            return redirect(reverse('products'))

        basket_order = current_basket(request)
        total = basket_order['grand_total']
        stripe_total = round(total * 100)
        order_form = OrderForm()
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
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkoutSuccessView(request, order_id):
    """
        This view loads the payment success page
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_id=order_id)
    messages.success(request, f'Order successful. \
        Your order number is {order_id}. We sent you a \
        confirmation email to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
