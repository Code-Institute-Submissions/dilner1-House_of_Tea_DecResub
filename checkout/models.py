import uuid

from django.db import models
from django.conf import settings
from django.db.models import Sum

from products.models import Product

class Order(models.Model):
    order_id = models.CharField(max_length=32, null=False, editable=False)
    name = models.CharField(max_length=50, null=False, blank=False)
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

    def _create_order_id(self):

        return uuid.uuid4().hex.upper()

    def update_order_total(self):
        self.order_total = self.lineitems.aggregate(Sum('line_item_total'))['line_item_total__sum'] or 0
        if self.order_total < settings.DELIVERY_CHARGE_MAX:
            self.delviery_charge = self.order_total * settings.DELIVERY_CHARGE / 50
        else: 
            self.delviery_charge = 30
            self.grand_total = order_total + delivery_charge
            self.save()

    def save(self, *args, **kwargs):
        """
            Function overides model save method
        """
        if not self.order_id:
            self.order_id = self._create_order_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_id

class OrderLineItems(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_weight = models.CharField(max_length=4 ,null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    line_item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
            Function overides model save method
        """

        # if dictionary loop over each dictionary and work out price based on weight
        
        # else
        self.line_item_total = self.product.price * self.quantity
        # end of if statement
        super().save(*args, **kwargs)

        def __str__(self):
            return f'SKU {self.product.sku} on order {self.order.order_id}'
