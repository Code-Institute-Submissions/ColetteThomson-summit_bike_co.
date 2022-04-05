from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ identify a new signal module with listeners in it """
    name = 'checkout'

    def ready(self):
        import checkout.signals
