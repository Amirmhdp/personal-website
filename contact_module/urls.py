from django.urls import path
from . import views

urlpatterns = [
    path('contact-me', views.ContactCreateView.as_view(), name='contact_me_page')
]
