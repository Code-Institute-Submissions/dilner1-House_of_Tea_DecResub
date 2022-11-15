from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.basketView, name='basket'),
    path('add/<pk>/', views.addToBasketView, name='add_to_basket'),
    path('update/<pk>/', views.updateBasketView, name='update_basket'),
    path('remove/<pk>/', views.removeFromBasketView, name='remove_from_basket'),
]
