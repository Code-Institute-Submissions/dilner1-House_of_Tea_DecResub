from django.shortcuts import render
from .forms import newsletterForm
from .models import Newsletter


def newsletterView(request):
    """
        This view loads the newsletter signup form
    """
    newsletter_form = newsletterForm(request.POST or None)
    if request.method == 'POST':
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
        }
        newsletter_form = newsletterForm(form_data)
        if newsletter_form.is_valid():
            instance = newsletter_form.save(commit=False)
            print("Form is valid")
            if Newsletter.objects.filter(email=instance.email).exists():
                print('removing email address')
                Newsletter.objects.filter(email=instance.email).delete()
            else:
                instance.save()

    context = {
            'newsletter_form': newsletter_form,
        }

    return render(request, 'newsletter/newsletter.html', context)