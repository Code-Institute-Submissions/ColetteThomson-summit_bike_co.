from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price_now, quantity):
    """calculate subtotal of shopping bag"""
    return price_now * quantity
