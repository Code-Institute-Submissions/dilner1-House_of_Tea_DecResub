from django.shortcuts import render, redirect, reverse, HttpResponse


# Create your views here.
def basketView(request):
    """
        This view loads the basket page
    """
    return render(request, 'basket/basket.html')

def addToBasketView(request, pk):
    """
        This view adds an item to the basket
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    weight = None

    if 'product_weight' in request.POST:
        weight = request.POST['product_weight']
    basket = request.session.get('basket', {})
    if weight:
        if pk in list(basket.keys()):
            if weight in basket[pk]['item_weight'].keys():
                basket[pk]['item_weight'][weight] += quantity
            else:
                basket[pk]['item_weight'][weight] = quantity
        else:
            basket[pk] = {'item_weight': {weight: quantity}}
    else:
        if pk in list(basket.keys()):
            basket[pk] += quantity
        else:
            basket[pk] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)

def updateBasketView(request, pk):
    """
        This view adds an item to the basket
    """
    quantity = int(request.POST.get('quantity'))
    weight = None

    if 'product_weight' in request.POST:
        weight = request.POST['product_weight']
    basket = request.session.get('basket', {})
    if weight:
        if quantity > 0:
            basket[pk][product_weight][weight] = quantity
        else:
            del basket[pk][product_weight][weight]
    else:
        if quantity > 0:
            basket[pk] = quantity
        else:
            basket.pop(pk)

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(reverse(basketView))
    
def removeFromBasketView(request, pk):
    """
        This view removes an item from the basket
    """

    try:
        weight = None

        if 'product_weight' in request.POST:
            weight = request.POST['weight']
        basket = request.session.get('basket', {})
        if weight:
            del basket[pk]['product_weight'][weight]
            if not basket[pk]['product_weight']:
                basket.pop(pk)
        else:
            basket.pop(pk)

        request.session['basket'] = basket
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)