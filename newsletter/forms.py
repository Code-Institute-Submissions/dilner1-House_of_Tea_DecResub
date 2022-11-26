from django import forms
from .models import Newsletter


class newsletterForm(forms.Form):
    class Meta:
        model = Newsletter
        fields = (
            'name',
            'email',
        )
        
        # def __init__(self, *args, **kwargs):
        #     """
        #     Add placeholders and classes, remove auto-generated
        #     labels and set autofocus on first field
        #     """
        #     super().__init__(*args, **kwargs)
        #     placeholders = {
        #         'name': ' Name',
        #         'email': 'Email Address',
        #     }
