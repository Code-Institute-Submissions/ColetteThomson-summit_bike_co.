from django import forms
from .models import Product, Classification


# extends ModelForm (Classification and Product models)
class ProductForm(forms.ModelForm):
    """ product entry form for superusers """
    class Meta:
        model = Product
        # dunder field to include all fields in Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # overwrite __init__ method to make changes to fields
        super().__init__(*args, **kwargs)
        classifications = Classification.objects.all()
        # create list of tuples (list comprehension) of friendly_names
        # associated with their classification's ids
        friendly_names = [(c.id, c.get_friendly_name()) for c in classifications]

        # update classification field with friendly_name
        # (instead of using the id) - and shown in select box of form
        self.fields['classification'].choices = friendly_names
        # iterate through rest of fields
        for field_name, field in self.fields.items():
            # set class to match store theme
            field.widget.attrs['class'] = 'border-black rounded-0'
