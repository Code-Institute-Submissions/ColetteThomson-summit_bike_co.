# to obtain webhook and stripe api key
from django.conf import settings
# for exception handlers to work
from django.http import HttpResponse
# require_post needed (and will reject get requests)
from django.views.decorators.http import require_POST
# csrf_exempt as stripe won't send a csrf token
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe

""" code adapted from Stripe docs """


@require_POST
@csrf_exempt
def webhook(request):
    """listen for webhooks from stripe"""
    # setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # set up a webhook handler (pass event)
    handler = StripeWH_Handler(request)

    # map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # get the webhook type from stripe
    # (returns either of above event_map dictionary keys)
    event_type = event['type']

    # if there's a handler for it, get it from the event_map
    # use the generic one by default (i.e. 'unhandled webhook received')
    event_handler = event_map.get(event_type, handler.handle_event)

    # call the event handler with the event
    response = event_handler(event)
    # return response to stripe
    return response
