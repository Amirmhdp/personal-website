from django.urls import path
from . import views

urlpatterns = [
    path('order-page', views.OrderCreateView.as_view(), name='order_page')
]
