from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    projects = Project.objects
    context = {
    'projects': projects,
    }
    return render(request, 'projects/home.html', context=context)

def project_view(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {
    'project': project,
    }
    return render(request, 'projects/projectView.html', context=context)
