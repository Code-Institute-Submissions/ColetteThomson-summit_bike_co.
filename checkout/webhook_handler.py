from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time

""" redundancy: to avoid a payment in stripe, but no order in the
    database - eg: if user should intentionally or
    accidentally close the browser window after the payment
    is confirmed but before the form is submitted """


class StripeWH_Handler:
    """ handle stripe webhooks"""

    # setup method called when instance of class StripeWH_Handler is created
    def __init__(self, request):
        self.request = request

    # take event (sent by stripe)
    def handle_event(self, event):
        """ handle a generic/unknown/unexpected webhook event """
        return HttpResponse(
            # indicate event was received
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ handle the payment_intent.succeeded webhook from stripe """
        # payment intent coming from stripe, once user makes a payment
        intent = event.data.object
        # obtain payment intend id
        pid = intent.id
        # obtain shopping bag
        bag = intent.metadata.bag
        # obtain user's save_info (via 'cache_checkout_data')
        save_info = intent.metadata.save_info

        # store billing, shipping and grand_total information
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # clean data in the shipping details
        for field, value in shipping_details.address.items():
            # replace any empty strings with none (null value)
            if value == "":
                shipping_details.address[field] = None

        # update profile information if save_info was selected
        # 'none' to allow anonymous users to check out
        profile = None
        username = intent.metadata.username
        # if not anonymous, will then be a authenticated user
        if username != 'AnonymousUser':
            # get user profile, using their username
            profile = UserProfile.objects.get(user__username=username)
            # if save_info box selected, update profile with shipping details
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                # save updated user's profile
                profile.save()

        # if order doesn't exist
        order_exists = False
        # introduce a delay
        attempt = 1
        # attempt to find order up to 5 times
        while attempt <= 5:
            # try to get order using payment intent info
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    # try to find order with identical customer info,
                    # shopping bag, grand total and payment intent
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                # if order is found, break out of the while loop
                break
            except Order.DoesNotExist:
                attempt += 1
                """ to prevent webhook immediately creating order
                    (if order not in database): ensure webhook handler
                    tries to find order up to 5 times over 5 seconds,
                    before giving up and creating order itself """
                time.sleep(1)

        # if order exists
        if order_exists:
            # return 200 httpresponse to stripe with verified order message
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: \
                    Verified order already in database',
                status=200)
        else:
            order = None
            try:
                # create order using payment intent info
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    # try to find order with identical customer info,
                    # shopping bag, grand total and payment intent
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            # if error, delete created order
            except Exception as e:
                if order:
                    order.delete()
                # return 500 server response error to stripe causing
                # stripe to automatically try webhook again later
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        # if webhook successful return httpresponse success message to stripe
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: \
                Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ handle the payment_intent.payment_failed webhook from stripe """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
