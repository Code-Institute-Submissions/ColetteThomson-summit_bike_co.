from .models import Opinion
from django import forms


class OpinionForm(forms.ModelForm):
    """ OpinionForm class to inherit from the base form """
    # shows which model to use and what fields to display
    class Meta:
        model = Opinion
        fields = ('body',)
