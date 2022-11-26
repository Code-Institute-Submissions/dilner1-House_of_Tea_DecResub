from django import forms
from .models import Newsletter


class newsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = (
            'name',
            'email'
        )

    def cleanEmail(self):
        email = self.cleaned_data.get('email')

        return email