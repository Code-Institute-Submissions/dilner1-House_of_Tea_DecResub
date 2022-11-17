from django.contrib import admin
from .models import Order, OrderLineItems

class OrderLineItemAdmin(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('line_item_total',)

class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderLineItemAdmin,)

    readonly_fields = (
        'order_id',
        'data',
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

    order_id = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    address1 = models.CharField(max_length=80, null=False, blank=False)
    address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_charge = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

admin.site.register(Order, OrderAdmin)