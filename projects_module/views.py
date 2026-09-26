from django.shortcuts import render

# Create your views here.

def project_list(request):
    return render(request, 'projects_module/project_list.html')

def project_detail(request):
    return render(request, 'projects_module/project_detail.html')