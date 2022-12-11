from django.shortcuts import render


def index(request):
    """
        This view loads the index page
    """

    return render(request, 'home/index.html')
