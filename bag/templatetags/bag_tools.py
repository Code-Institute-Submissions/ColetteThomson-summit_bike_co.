from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """calculate subtotal of shopping bag"""
    return price * quantity
