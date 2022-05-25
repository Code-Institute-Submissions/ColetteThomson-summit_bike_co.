from django import forms
# used for image field on add and edit product functionality
from .widgets import CustomClearableFileInput

from .models import Product, Classification


# extends ModelForm (Classification and Product models)
class ProductForm(forms.ModelForm):
    """ product entry form for superusers """
    class Meta:
        model = Product
        # dunder field to include all fields in Product
        fields = '__all__'
    # use widget for image field
    image = forms.ImageField(label='Bike Model Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        # overwrite __init__ method to make changes to fields
        super().__init__(*args, **kwargs)
        classifications = Classification.objects.all()
        # create list of tuples (list comprehension) of friendly_names
        # associated with their classification's ids
        friendly_names = [(c.id, c.get_friendly_name()) for c in
                          classifications]

        # update classification field with friendly_name
        # (instead of using the id) - and shown in select box of form
        self.fields['classification'].choices = friendly_names
