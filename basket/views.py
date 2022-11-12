from django.shortcuts import render, redirect


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