from django.shortcuts import render


def suppliersView(request):
    """
        This view loads the newsletter signup form
    """

    return render(request, 'suppliers/suppliers.html')