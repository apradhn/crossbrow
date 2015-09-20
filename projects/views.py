from django.shortcuts import get_object_or_404, render, get_list_or_404

from .models import Project
from browsers.models import Browser


def projects_index(request):
    projects = get_list_or_404(Project)
    return render(
        request,
        'projects/index.html',
        {
            'projects': projects
        }
    )


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    features = project.feature_set.all()
    browsers = project.browser_set.all()
    return render(
        request,
        'projects/detail.html',
        {
            'project': project,
            'features': features,
            'browsers': browsers
        }
    )


def browsers_index(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    browsers = get_list_or_404(project.browser_set)
    return render(
        request,
        'browsers/index.html',
        {
            'project': project,
            'browsers': browsers
        }
    )


def browser_detail(request, project_id, browser_id):
    project = get_object_or_404(Project, pk=project_id)
    browser = get_object_or_404(Browser, pk=browser_id)
    return render(
        request,
        'browsers/show.html',
        {
            'project': project,
            'browser': browser
        }
    )


def features_index(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    features = get_list_or_404(project.feature_set)
    return render(
        request,
        'features/index.html',
        {
            'project': project,
            'features': features
        }
    )
