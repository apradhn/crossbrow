from django.shortcuts import get_object_or_404, render, get_list_or_404

from .models import Project


def index(request):
    projects = get_list_or_404(Project)
    return render(
        request,
        'projects/index.html',
        {
            'projects': projects
        }
    )


def show(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(
        request,
        'projects/show.html',
        {
            'project': project
        }
    )


def browsers(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    browsers = get_list_or_404(project.browser_set)
    return render(
        request,
        'projects/browsers.html',
        {
            'project': project,
            'browsers': browsers
        }
    )


def features(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    features = get_list_or_404(project.feature_set)
    return render(
        request,
        'projects/features.html',
        {
            'project': project,
            'features': features
        }
    )
