from django.shortcuts import render
from projects.models import Project


def home(request):
    project_list = Project.objects.all()
    return render(
        request,
        'home/index.html',
        {'project_list': project_list})
