from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """ to return a dictionary using a context processor and make
        available to all templates across entire application"""
    # empty list to contain bag items
    bag_items = []
    # need when start adding items to bag (both initialised to zero)
    total = 0
    product_count = 0
    # obtain existing session, or initialising to empty dictionary if none
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        # if item has no sizes (is an integer and therefore a quantity only)
        if isinstance(item_data, int):
            # get product and its id
            product = get_object_or_404(Product, pk=item_id)
            # add quantity * price to total
            total += item_data * product.price_now
            # increment product count by quantity
            product_count += item_data
            # add dictionary to bag items, to gain access to other product info
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        # if item has sizes, handle as dictionary
        else:
            # get product and its id
            product = get_object_or_404(Product, pk=item_id)
            # iterate through inner dictionery of items by size
            for size, quantity in item_data['items_by_size'].items():
                # increment product count and total
                total += quantity * product.price_now
                product_count += quantity
                # items in bag dictionary, including size
                bag_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'product': product,
                    'size': size,
                })

    # check if bag total is less than free delivery threshold (settings.py)
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
