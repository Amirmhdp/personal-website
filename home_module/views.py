from django.shortcuts import render

# Create your views here.
from home_module.models import Public, FooterLink
from projects_module.models import Project, Skill


def home(request):
    projects = Project.objects.filter(is_active=True).prefetch_related('skill')
    skills = Skill.objects.filter(is_active=True).order_by('id')

    context = {
        'projects': projects,
        'skills': skills
    }
    return render(request, 'home_module/home.html', context)

def header_partial(request):
    information = Public.objects.filter(is_active=True).first()
    context = {
        'information': information
    }
    return render(request, 'shared/header.html', context)

def footer_partial(request):
    information = Public.objects.filter(is_active=True).first()
    fast_links = FooterLink.objects.filter(is_active=True, link_type='quick')
    service_links = FooterLink.objects.filter(is_active=True, link_type='site')
    context = {
        'information': information,
        'fast_links': fast_links,
        'service_links': service_links,
    }
    return render(request, 'shared/footer.html', context)

def about_me(request):
    skills = Skill.objects.filter(is_active=True)
    information = Public.objects.filter(is_active=True).first()
    context = {
        'skills': skills,
        'information': information
    }
    return render(request, 'home_module/about_me.html', context)

def sevices(request):
    information = Public.objects.filter(is_active=True).first()
    context = {
        'information': information
    }
    return render(request, 'home_module/services.html', context)

def skills(request):
    information = Public.objects.filter(is_active=True).first()
    skills = Skill.objects.filter(is_active=True).order_by('id')

    context = {
        'information': information,
        'skills': skills
    }
    return render(request, 'home_module/skills.html', context)