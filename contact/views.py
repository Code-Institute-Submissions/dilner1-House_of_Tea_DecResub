from django.shortcuts import render


def contactView(request):
    """
        This view loads the newsletter signup form
    """

    return render(request, 'contact/contact.html')