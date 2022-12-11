from django.contrib import admin
from .models import Order, OrderLineItems


class OrderLineItemAdmin(admin.TabularInline):
    model = OrderLineItems
    readonly_fields = ('line_item_total',)


class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderLineItemAdmin,)

    readonly_fields = (
        'order_id',
        'date',
        'delivery_charge',
        'order_total',
        'grand_total',
         )
    fields = (
        'order_id',
        'name',
        'email',
        'phone_number',
        'country',
        'postcode',
        'city',
        'address1',
        'address2',
        'county',
        'date',
        'delivery_charge',
        'order_total',
        'grand_total',
     )

    list_display = (
        'order_id',
        'date',
        'name',
        'delivery_charge',
        'order_total',
        'grand_total',
         )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
