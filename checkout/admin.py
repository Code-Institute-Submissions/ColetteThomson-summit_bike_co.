from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """ inline admin class to inherit from admin.TabularInline.
        enables adding, editing of ine items in admin panel
        from inside Order model (rather than having to go to
        order line item interface) """
    # link to OrderLineItem model
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """ class with uneditable fields to prevent
    compromising integrity of an order """
    # link to inline admin class
    inlines = (OrderLineItemAdminInline,)

    # fields to be calculated by model methods
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    # allow specific ordering of fields in admin panel
    # (needed if readonly_fields are used)
    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total',)

    # list key items in admin panel
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    # ordered in reverse chronological order (most recent on top)
    ordering = ('-date',)


""" register Order and OrderAdmin models.
    (don't need to register OrderLineItem model, as is
    accessible via the inline on Order model) """
admin.site.register(Order, OrderAdmin)
