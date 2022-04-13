from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # render all fields except user (as this won't change)
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """ add placeholders and classes, remove auto-generated
        labels and set autofocus on first field """

        # call default init method to set up default form
        super().__init__(*args, **kwargs)
        # use placeholders (instead of field labels)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        # ensure cursor is placed in 'phone_number' field when page is loaded
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        # iterate through form fields
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    # add '*' to all required fields, and placeholder
                    placeholder = f'{placeholders[field]} *'
                else:
                    # display just placeholder
                    placeholder = placeholders[field]
                    # set placeholder attrs to values in placeholder dictionary
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # add css class
            self.fields[field].widget.attrs['class'] = \
                'border-black rounded-0 profile-form-input'
            # remove field labels (use placeholders instead)
            self.fields[field].label = False
