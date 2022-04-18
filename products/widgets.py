# used for image field on add and edit product functionality
from django.forms.widgets import ClearableFileInput
# used for translation
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """ inherits from built in class ClearableFileInput """
    # override the following fields with own values
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
