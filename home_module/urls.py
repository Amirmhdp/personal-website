from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about-me', views.about_me, name='about_me_page'),
    path('project-list', views.project_list, name='project_list_page'),
    path('services', views.sevices, name='services_page'),
]
