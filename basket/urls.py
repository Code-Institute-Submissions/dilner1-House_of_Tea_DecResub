from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.basketView, name='basket'),
    path('add/<pk>/', views.addToBasketView, name='add_to_basket'),
]
