from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def productsView(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def productInfoView(request, pk):

    product = get_object_or_404(Product, pk=pk)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)