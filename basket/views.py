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
    basket = request.session.get('basket', {})

    if pk in list(basket.keys()):
        basket[pk] += quantity
    else:
        basket[pk] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)