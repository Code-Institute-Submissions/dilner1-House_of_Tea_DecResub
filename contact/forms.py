from django import forms
from .models import Contact


class contactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'title', 
            'Body',
            'urgent',
            'order_id',
        )

    def cleanEmail(self):
        email = self.cleaned_data.get('email')

        return email
