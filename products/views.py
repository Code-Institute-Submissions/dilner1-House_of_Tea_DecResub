from django.shortcuts import render, get_object_or_404
from .models import Product, Categories
from django.db.models import Q

# Create your views here.
def productsView(request):

    category = None
    products = Product.objects.all()

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__category__in=categories)
            categories = Categories.objects.filter(category__in=categories)

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'products/products.html', context)

def productInfoView(request, pk):

    product = get_object_or_404(Product, pk=pk)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)