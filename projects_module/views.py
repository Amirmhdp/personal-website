from django.shortcuts import render
from django.views.generic import ListView
from projects_module.models import Project

# Create your views here.

# def project_list(request):
#     return render(request, 'projects_module/project_list.html')


class ProjectListView(ListView):
    model = Project
    template_name = 'projects_module/project_list.html'
    context_object_name = "projects"
    paginate_by = 12

def project_detail(request):
    return render(request, 'projects_module/project_detail.html')