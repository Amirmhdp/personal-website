from django.urls import path
from . import views

urlpatterns = [
    path('project-list', views.project_list, name='project_list_page'),
    path('project-detail', views.project_detail, name='project_detail_page'),
]
