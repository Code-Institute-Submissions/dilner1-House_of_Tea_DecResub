from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItems

@receiver(post_save, OrderLineItems)
def save_update_signal(sender, instance, created, **kwargs):

    instance.order.update_order_total()

@receiver(post_save, OrderLineItems)
def delete_update_signal(sender, instance, **kwargs):

    instance.order.update_order_total()