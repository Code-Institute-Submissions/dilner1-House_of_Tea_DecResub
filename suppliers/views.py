from django.shortcuts import render
from .models import Supplier


def suppliersView(request):
    """
        This view loads the newsletter signup form
    """
    suppliers = Supplier.objects.all()

    context = {
        'suppliers': suppliers,
        }

    return render(request, 'suppliers/suppliers.html', context)
