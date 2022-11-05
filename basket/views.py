from django.shortcuts import render

# Create your views here.
def basketView(request):
    """
        This view loads the basket page
    """
    return render(request, 'basket/basket.html')