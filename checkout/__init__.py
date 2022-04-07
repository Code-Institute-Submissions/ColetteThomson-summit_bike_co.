""" name of default config class for checkout app:
    CheckoutConfig (comes from apps.py, where
    signals module was imported. This line is needed
    for to django know about the custom ready method
    (and thus for our signals to work) """

default_app_config = 'checkout.apps.CheckoutConfig'
