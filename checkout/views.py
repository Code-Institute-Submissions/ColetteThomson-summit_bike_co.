from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from bag.contexts import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """ determine if user has selected the 'save info box' (checkout page) """
    try:
        # before calling confirm card payment method (stripe js)
        # first part of split (client) will be payment intent id (pid)
        pid = request.POST.get('client_secret').split('_secret')[0]
        # set up stripe with secret key
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # to modify payment intent and add metadata
        stripe.PaymentIntent.modify(pid, metadata={
            # add json dump of user's shopping bag to use ...
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        # post to the 'handle form submit' view (stripe_elements.js)
        return HttpResponse(status=200)
    except Exception as e:
        # display error message to user if payment unsuccessful
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        # return bad request
        return HttpResponse(content=e, status=400)


def checkout(request):
    """ checkout function, to prevent users from manually
        accessing the url """

    print(f'${settings.STRIPE_PUBLIC_KEY} - ${settings.STRIPE_SECRET_KEY} - ${settings.STRIPE_WH_SECRET}')

    # stripe keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    # check if request method is post
    if request.method == 'POST':
        # obtain bag from the session
        bag = request.session.get('bag', {})
        """ place form data in a dictionary (done manually as
            'save delivery info box' in checkout.html does not
            have a field on the Order model) """
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        # create instance of form using form_data
        order_form = OrderForm(form_data)
        # if form is valid, save the order
        if order_form.is_valid():
            # 'commit=false' to prevent 1st save happening
            order = order_form.save(commit=False)
            # first part of split (client) will be payment intent id (pid)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            # dump original bag to a json string
            order.original_bag = json.dumps(bag)
            order.save()
            # iterate through bag items to create each line item
            for item_id, item_data in bag.items():
                try:
                    # obtain product id from the bag
                    product = Product.objects.get(id=item_id)
                    """ if value is an integer, item doesn't have sizes
                        (will be quantity only) """
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        # if has sizes, iterate through each size
                        for size, quantity in item_data['items_by_size'].items():
                            # create line item for each
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    # if product isn't found, display error message
                    messages.error(request, (
                        "A product in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    # delete empty order
                    order.delete()
                    # return user to shopping bag page
                    return redirect(reverse('view_bag'))

            # save delivery info to user's profile if required
            request.session['save_info'] = 'save-info' in request.POST
            # redirect to checkout success page & pass order_number as argument
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            # if order not valid, display message
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    # to handle get requests
    else:
        # obtain bag from the session
        bag = request.session.get('bag', {})
        if not bag:
            # if no bag display error message
            messages.error(request, "There's nothing in your bag at present")
            # redirect user to products page
            return redirect(reverse('products'))

        # calculate current bag total in the view
        current_bag = bag_contents(request)
        # obtain grand_total key out of current bag
        total = current_bag['grand_total']
        # round to no decimal places (amount charged must be integer)
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
            Please set it in your environment')

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


def checkout_success(request, order_number):
    """ to handle successful checkouts """

    # check if user wanted to save their delivery info
    save_info = request.session.get('save_info')
    # obtain order-number from order
    order = get_object_or_404(Order, order_number=order_number)
    # attach success message to user
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    # delete user bag from this session
    if 'bag' in request.session:
        del request.session['bag']
    # set template and context
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    # render the template
    return render(request, template, context)
