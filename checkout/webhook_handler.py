from django.http import HttpResponse


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
            content=f'Webhook received: {event["type"]}',
            status=200)
