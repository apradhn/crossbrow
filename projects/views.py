from django.shortcuts import get_object_or_404, render, get_list_or_404

from .models import Project
from browsers.models import Browser
from features.models import Feature
from test_cases.models import TestCase


def project_index(request):
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


def browser_index(request, project_id):
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


def feature_index(request, project_id):
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


def feature_detail(request, project_id, feature_id):
    project = get_object_or_404(Project, pk=project_id)
    feature = get_object_or_404(Feature, pk=feature_id)
    test_cases = feature.testcase_set.all()
    return render(
        request,
        'features/detail.html',
        {
            'project': project,
            'feature': feature,
            'test_cases': test_cases
        }
    )


def test_case_index(request, project_id, feature_id):
    project = get_object_or_404(Project, pk=project_id)
    feature = get_object_or_404(Feature, pk=feature_id)
    test_cases = feature.testcase_set.all()
    return render(
        request,
        'test_cases/index.html',
        {
            'project': project,
            'feature': feature,
            'test_cases': test_cases
        }

    )


def test_case_detail(request, project_id, feature_id, test_case_id):
    project = get_object_or_404(Project, pk=project_id)
    feature = get_object_or_404(Feature, pk=feature_id)
    test_case = get_object_or_404(TestCase, pk=test_case_id)
    return render(
        request,
        'test_cases/detail.html',
        {
            'project': project,
            'feature': feature,
            'test_case': test_case
        })
