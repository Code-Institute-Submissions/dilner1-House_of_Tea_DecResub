from django.shortcuts import render

# Create your views here.
def newsletterView(request):
    """
        This view loads the newsletter signup form
    """

    return render(request, 'newsletter/newsletter.html')