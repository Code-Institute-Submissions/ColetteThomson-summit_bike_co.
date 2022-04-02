from decimal import Decimal
from django.conf import settings

def bag_contents(request):
    """ to return a dictionary using a context processor and make
        available to all templates across entire application"""
    # empty list to contain bag items
    bag_items = []
    # need when start adding items to bag (both initialised to zero)
    total = 0
    product_count = 0
    # check if bag total is less than free delivery threshold (from settings.py)
    if total < settings.FREE_DELIVERY_THRESHOLD:
        # total multiplied by standard delivery percentage (from settings.py)
        # use 'decimal' to prevent rounding errors
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        # remind user how much more they need to spend to get free delivery
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        # if total is greater than or equal to threshold
        delivery = 0
        free_delivery_delta = 0
    # add delivery charge to total
    grand_total = delivery + total
    # add above to context dictionary
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    # return context dictionary
    return context
