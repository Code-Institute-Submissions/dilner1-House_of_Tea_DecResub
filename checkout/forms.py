from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
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
