from django.urls import path
from . import views

urlpatterns = [
    path('project-list', views.ProjectListView.as_view(), name='project_list_page'),
    path('project-detail/<pk>/<title>', views.project_detail, name='project_detail_page'),
    path('change-img/<id>', views.change_img, name='change_img')
]
