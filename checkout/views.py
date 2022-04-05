from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """ checkout function, to prevent users from manually
        accessing the url """

    # obtain bag from the session
    bag = request.session.get('bag', {})
    if not bag:
        # if no bag display error message
        messages.error(request, "There's nothing in your bag at the moment")
        # redirect user to products page
        return redirect(reverse('products'))

    # create instance of the orderform (currently empty)
    order_form = OrderForm()
    # create the checkout template
    template = 'checkout/checkout.html'
    # context containing the order_form
    context = {
        'order_form': order_form,
    }
    # render order form
    return render(request, template, context)
