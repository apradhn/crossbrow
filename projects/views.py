from django.shortcuts import get_object_or_404
from .models import Project
from browsers.models import Browser
from features.models import Feature
from test_cases.models import TestCase
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class ProjectIndexView(generic.ListView):
    model = Project


class ProjectDetailView(generic.DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['feature_list'] = context['object'].feature_set.all()
        context['browser_list'] = context['object'].browser_set.all()
        return context


class ProjectCreateView(CreateView):
    model = Project
    fields = ['name']


class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name']
    template_name_suffix = '_update_form'


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('projects:project_index')


class BrowserIndexView(generic.ListView):
    model = Browser

    def get_queryset(self):
        return Browser.objects.filter(
            project__pk=self.kwargs['project_pk'])

    def get_context_data(self, **kwargs):
        context = super(BrowserIndexView, self).get_context_data(**kwargs)
        context['project'] = get_object_or_404(
            Project,
            pk=self.kwargs['project_pk'])
        return context


class BrowserDetailView(generic.DetailView):
    model = Browser

    def get_context_data(self, **kwargs):
        context = super(BrowserDetailView, self).get_context_data(**kwargs)
        context['project'] = get_object_or_404(
            Project,
            pk=self.kwargs['project_pk'])
        return context


class BrowserCreateView(CreateView):
    model = Browser
    fields = ['name', 'operating_system', 'version']

    def form_valid(self, form):
        project = get_object_or_404(
            Project,
            pk=self.kwargs['project_pk'])
        form.instance.project = project
        return super(BrowserCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'projects:browser_index',
            kwargs={'project_pk': self.kwargs['project_pk']})


class FeatureIndexView(generic.ListView):
    model = Feature

    def get_queryset(self):
        return Feature.objects.filter(
            project__pk=self.kwargs['project_pk'])

    def get_context_data(self, **kwargs):
        context = super(FeatureIndexView, self).get_context_data(**kwargs)
        context['project'] = get_object_or_404(
            Project,
            pk=self.kwargs['project_pk'])
        return context


class FeatureDetailView(generic.DetailView):
    model = Feature

    def get_context_data(self, **kwargs):
        context = super(FeatureDetailView, self).get_context_data(**kwargs)
        context['project'] = get_object_or_404(
            Project,
            pk=self.kwargs['project_pk'])
        context['testcase_list'] = TestCase.objects.filter(
            feature__pk=self.kwargs['pk'])
        return context


class TestCaseIndexView(generic.ListView):
    model = TestCase

    def get_queryset(self):
        return TestCase.objects.filter(feature__pk=self.kwargs['feature_pk'])

    def get_context_data(self, **kwargs):
        context = super(TestCaseIndexView, self).get_context_data(**kwargs)
        context['project'] = get_object_or_404(
            Project,
            pk=self.kwargs['project_pk'])
        context['feature'] = get_object_or_404(
            Feature,
            pk=self.kwargs['feature_pk'])
        return context


class TestCaseDetailView(generic.DetailView):
    model = TestCase

    def get_context_data(self, **kwargs):
        context = super(TestCaseDetailView, self).get_context_data(**kwargs)
        context['project'] = get_object_or_404(
            Project,
            pk=self.kwargs['project_pk'])
        context['feature'] = get_object_or_404(
            Feature,
            pk=self.kwargs['feature_pk'])
        context['browser_list'] = Browser.objects.filter(
            project__pk=self.kwargs['project_pk'])
        return context
