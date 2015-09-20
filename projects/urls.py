from django.conf.urls import url

from . import views

urlpatterns = [
    # /projects/
    url(r'^$',
        views.ProjectIndexView.as_view(),
        name='project_index'),
    # /projects/create
    url(r'create/^$',
        views.ProjectCreateView.as_view(),
        name='project_create'),
    # /projects/<project_pk>/browsers/
    url(r'(?P<project_pk>[0-9]+)/browsers/$',
        views.BrowserIndexView.as_view(),
        name='browsers_index'),
    # /projects/<project_pk>/features/
    url(r'(?P<project_pk>[0-9]+)/features/$',
        views.FeatureIndexView.as_view(),
        name='features_index'),
    # /projects/<project_pk>/features/<feature_pk>
    url(r'(?P<project_pk>[0-9]+)/features/(?P<pk>[0-9]+)/$',
        views.FeatureDetailView.as_view(),
        name='feature_detail'),
    # /projects/<project_pk>/features/<feature_pk>/testcases
    url(r'(?P<project_pk>[0-9]+)/features/(?P<feature_pk>[0-9]+)/testcases/$',
        views.TestCaseIndexView.as_view(),
        name='testcase_index'),
    # /projects/<project_pk>/features/<feature_pk>/testcases/<testcase_pk>
    url(r'(?P<project_pk>[0-9]+)/features/(?P<feature_pk>[0-9]+)/testcases/(?P<pk>[0-9]+)$',
        views.TestCaseDetailView.as_view(),
        name='testcase_detail'),
    # /projects/<project_pk>/browsers/<browser_id>
    url(r'(?P<project_pk>[0-9]+)/browsers/(?P<pk>[0-9]+)/$',
        views.BrowserDetailView.as_view(),
        name='browser_detail'),
    # /projects/<project_pk>/
    url(r'(?P<pk>[0-9]+)/$',
        views.ProjectDetailView.as_view(),
        name='project_detail'),
]
