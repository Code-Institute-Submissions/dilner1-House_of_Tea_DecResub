from django.shortcuts import render
from .forms import newsletterForm


def newsletterView(request):
    """
        This view loads the newsletter signup form
    """
    newsletter_form = newsletterForm()
    print(newsletter_form)
    if request.method == 'POST':

        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
        }
        newsletter_form = newsletterForm(form_data)
        if newsletter_form.is_valid():
            print("Form is valid")
            newsletter_form.save()

    context = {
        'newsletter_form': newsletter_form,
    }

    return render(request, 'newsletter/newsletter.html', context)