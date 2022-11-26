from django.shortcuts import render, redirect, reverse
from .forms import contactForm


def contactView(request):
    """
        This view loads the customer contact form
    """
    contact_form = contactForm(request.POST or None)
    if request.method == 'POST':
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'title': request.POST['title'],
            'body': request.POST['body'],
            'urgent': request.POST['urgent'],
            'order_id': request.POST['order_id'],
        }
        contact_form = contactForm(form_data)
        if contact_form.is_valid():
            instance = contact_form.save(commit=False)
            print("Form is valid")
            instance.save()
            return redirect(reverse('contact_success'))

    context = {
            'contact_form': contact_form,
        }

    template = 'contact/contact.html'

    return render(request, template, context)

def contactSuccessView(request):
    """
        This view loads the customer contact success page
    """

    template = 'contact/contact_success.html'

    return render(request, template)