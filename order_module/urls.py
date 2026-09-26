from django.urls import path
from . import views

urlpatterns = [
    path('order-page', views.order_page, name='order_page')
]
