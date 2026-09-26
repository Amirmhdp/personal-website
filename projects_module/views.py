from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from projects_module.models import Project, ProjectImage, ProjectFeature, ProjectChallenge


# Create your views here.

# def project_list(request):
#     return render(request, 'projects_module/project_list.html')


class ProjectListView(ListView):
    model = Project
    template_name = 'projects_module/project_list.html'
    context_object_name = "projects"
    paginate_by = 12
    def get_queryset(self):
        return (
            Project.objects.prefetch_related('skill')
        )

def project_detail(request, pk, title):
    project = Project.objects.filter(title__iexact=title).prefetch_related('skill').first()
    galleries = ProjectImage.objects.filter(project_id=pk)
    project_features = ProjectFeature.objects.filter(project_id=pk)
    challenges = ProjectChallenge.objects.filter(project_id=pk)
    context = {
        'project': project,
        'galleries': galleries,
        'project_features': project_features,
        'challenges': challenges
    }
    return render(request, 'projects_module/project_detail.html', context)

def change_img(request, id):
    image = ProjectImage.objects.filter(id=id).first()
    return JsonResponse({
        'src': image.image.url
    })