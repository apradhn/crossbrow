from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Project
from browsers.models import Browser
from features.models import Feature
from test_cases.models import TestCase
from django.views import generic


class ProjectIndexView(generic.ListView):
    model = Project


class ProjectDetailView(generic.DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['features'] = context['object'].feature_set.all()
        context['browsers'] = context['object'].browser_set.all()
        return context


class BrowserIndexView(generic.ListView):
    model = Browser


class BrowserDetailView(generic.DetailView):
    template_name = 'browsers/browser_detail.html'

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['project_pk'])
        browser = get_object_or_404(Browser, pk=kwargs['browser_pk'])
        context = dict(project=project, browser=browser)
        return render(request, self.template_name, context)


class FeatureIndexView(generic.ListView):
    template_name = 'features/feature_list.html'

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['project_pk'])
        feature_list = project.feature_set.all()
        context = dict(project=project, feature_list=feature_list)
        return render(request, self.template_name, context)


class FeatureDetailView(generic.DetailView):
    template_name = 'features/feature_detail.html'

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['project_pk'])
        feature = get_object_or_404(Feature, pk=kwargs['feature_pk'])
        testcase_list = feature.testcase_set.all()
        context = dict(
            project=project,
            feature=feature,
            testcase_list=testcase_list)
        return render(request, self.template_name, context)


class TestCaseIndexView(generic.ListView):
    template_name = 'testcases/testcase_index.html'

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['project_pk'])
        feature = get_object_or_404(Feature, pk=kwargs['feature_pk'])
        testcase_list = feature.testcase_set.all()
        context = dict(
            project=project,
            feature=feature,
            testcase_list=testcase_list)
        return render(request, self.template_name, context)


class TestCaseDetailView(generic.DetailView):
    template_name = 'testcases/testcase_detail.html'

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['project_pk'])
        feature = get_object_or_404(Feature, pk=kwargs['feature_pk'])
        testcase = get_object_or_404(TestCase, pk=kwargs['testcase_pk'])
        browsers = get_list_or_404(project.browser_set)
        context = dict(
            project=project,
            feature=feature,
            testcase=testcase,
            browsers=browsers)
        return render(request, self.template_name, context)
