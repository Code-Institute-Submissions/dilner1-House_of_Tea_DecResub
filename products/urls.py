from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.productsView, name='products'),
    path('<int:pk>/', views.productInfoView, name='product_info'),
]
