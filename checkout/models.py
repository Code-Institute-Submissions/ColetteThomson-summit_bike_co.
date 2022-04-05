# uuid is used to generate order number
import uuid

from django.db import models
# sum is used for calculations
from django.db.models import Sum
from django.conf import settings

from products.models import Product


class Order(models.Model):
    """ order details """
    # automatically generate unique and permanent order_number
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    # automatically set order date and time when a new order is created
    date = models.DateTimeField(auto_now_add=True)
    # next 3 x fields to be calculated using a model method when order is saved
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)

    # prepended with '_' (indicates a private method), only used in class Order
    def _generate_order_number(self):
        """ generate a random, unique order number using UUID """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ update grand total each time a line item is added,
        accounting for delivery costs """

        # use sum function across all line item totals for each line item
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))
        ['lineitem_total__sum']
        # calculate delivery cost, using threshold
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            # and standard delivery percentage (from settings.py)
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            # set to zero if order total higher than threshold
            self.delivery_cost = 0
        # calculate grand total
        self.grand_total = self.order_total + self.delivery_cost
        # save the instance
        self.save()

    def save(self, *args, **kwargs):
        """ override the original save method to set the order number
        if it hasn't been set already """
        if not self.order_number:
            # if no order number, generate one
            self.order_number = self._generate_order_number()
        # then execute original save method
        super().save(*args, **kwargs)

    def __str__(self):
        """ standard string method returning order number """
        return self.order_number


class OrderLineItem(models.Model):
    """ an individual shopping bag item relating to a specific order
    and referencing the product itself. When a user checks out, info is
    obtained from their payment form to create an order instance.
    Iterate through items in bag creating an order line item for each one,
    attaching to order, updating delivery_cost, order_total, grand_total """

    # foreign key link to class Order (checkout app)
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    # foreign key link to class Product (products app)
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    # product sizes: XS, S, M, L, XL
    product_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    # uneditable as is automatically calculated when line item is saved
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """ override the original save method to set the lineitem total
        and update the order total """
        # for each line item multiply price_now and quantity
        self.lineitem_total = self.product.price_now * self.quantity
        # then execute original save method
        super().save(*args, **kwargs)

    def __str__(self):
        """ standard string method returning sku and order_number """
        return f'SKU {self.product.sku} on order {self.order.order_number}'
