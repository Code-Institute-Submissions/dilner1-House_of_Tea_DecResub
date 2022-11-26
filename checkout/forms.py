from django import forms
from .models import Order

class orderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'name',
            'email',
            'phone_number',
            'country',
            'postcode',
            'city',
            'address1',
            'address2',
            'county',
        )
        def cleanEmail(self):
            email = self.cleaned_data.get('email')

            return email
