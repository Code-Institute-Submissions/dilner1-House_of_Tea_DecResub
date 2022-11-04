from django.shortcuts import render

# Create your views here.
def productsView(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)