from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.newsletterView, name='newsletter'),
    path('success', views.newsletterSuccessView, name='newsletter_success'),
]
