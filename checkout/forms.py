from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """ order form with customer details """
    class Meta:
        model = Order
        # render only fields that user will complete (no automatic fields)
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """ add placeholders and classes, remove auto-generated
        labels and set autofocus on first field """

        # call default init method to set up default form
        super().__init__(*args, **kwargs)
        # use placeholders (instead of field labels)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        # ensure cursor is placed in 'full_name' field when page is loaded
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # iterate through form fields
        for field in self.fields:
            if self.fields[field].required:
                # add '*' to all required fields, and placeholder
                placeholder = f'{placeholders[field]} *'
            else:
                # display just placeholder
                placeholder = placeholders[field]
            # set placeholder attrs to values in placeholder dictionary
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # add css class
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # remove field labels (use placeholders instead)
            self.fields[field].label = False
