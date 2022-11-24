from django.shortcuts import render


def newsletterView(request):
    """
        This view loads the newsletter signup form
    """

    return render(request, 'newsletter/newsletter.html')