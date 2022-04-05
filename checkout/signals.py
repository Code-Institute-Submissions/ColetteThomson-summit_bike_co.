""" from models.signals: the import 'post_..' (in this case) means after
    - thus signals are sent by django to entire application after a
    model instance is saved and after its deleted respectively """
from django.db.models.signals import post_save, post_delete
# to receive above signals
from django.dispatch import receiver
# to listen for above signals
from .models import OrderLineItem


# receive post saved signals from OrderLineItem model
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """ to handle signals from the post-save event. These
        parameters refer to the 'sender of the signal (OrderLineItem');
        the actual instance of the model that sent it; a boolean
        ('created') referring to whether this is a new instance, or
        one that is being updated and any key word arguments """

    # access instance.order (update specific line item)
    instance.order.update_total()


# receive post deleted signals from OrderLineItem model
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """ update order total on lineitem delete """

    # access instance.order (update specific line item)
    instance.order.update_total()
