from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.contactView, name='contact'),
    path('success', views.contactSuccessView, name='contact_success'),
]
