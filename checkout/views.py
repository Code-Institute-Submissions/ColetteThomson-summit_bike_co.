from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    """ checkout function, to prevent users from manually
        accessing the url """

    # stripe keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # obtain bag from the session
    bag = request.session.get('bag', {})
    if not bag:
        # if no bag display error message
        messages.error(request, "There's nothing in your bag at the moment")
        # redirect user to products page
        return redirect(reverse('products'))

    # calculate current bag total in the view
    current_bag = bag_contents(request)
    # obtain grand_total key out of current bag
    total = current_bag['grand_total']
    # round to no decimal places (stripe needs amount charged to be an integer)
    stripe_total = round(total * 100)
    # set secret key
    stripe.api_key = stripe_secret_key
    # create payment intent with amount and currency
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # create instance of the orderform (currently empty)
    order_form = OrderForm()

    # display message if public key not set in environment
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    # create the checkout template
    template = 'checkout/checkout.html'
    # context containing the order_form
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    # render order form
    return render(request, template, context)
