from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.checkoutView, name='checkout'),
    path('checkout_success/<order_id>', views.checkoutSuccessView, name='checkout-success'),
]
