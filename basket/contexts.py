from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def current_basket(request):

    basket_items = []
    total = 0 
    product_quantity = 0
    basket = request.session.get('basket', {})

    for pk, quantity in basket.items():
        product = get_object_or_404(Product, pk=pk)
        total += quantity * product.price
        name = product.name
        product_quantity += quantity
        basket_items.append({
            'pk': pk,
            'total': total,
            'product': product,
            'quantity': quantity,
        })


    if total < settings.DELIVERY_CHARGE_MAX:
        delivery = total * settings.DELIVERY_CHARGE/100
        delivery_threshold = settings.DELIVERY_CHARGE_MAX - delivery

    else:
        delivery = 30
        delivery_threshold = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_quantity': product_quantity,
        'delivery': delivery,
        'delivery_threshold': delivery_threshold,
        'grand_total': grand_total,
        'delivery_charge': settings.DELIVERY_CHARGE,
        'delivery_charge_max': settings.DELIVERY_CHARGE_MAX,
    }

    return context
