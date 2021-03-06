from django.conf.urls import url

from . import views

urlpatterns = [
    # /projects/<project_pk>/browsers/
    url(r'(?P<project_pk>[0-9]+)/browsers/$',
        views.BrowserIndexView.as_view(),
        name='browser_index'),
    # /projects/<project_pk>/browsers/add
    url(r'(?P<project_pk>[0-9]+)/browsers/add/$',
        views.BrowserCreateView.as_view(),
        name='browser_add'),
    # /projects/<project_pk>/browsers/<browser_id>/update/
    url(r'(?P<project_pk>[0-9]+)/browsers/(?P<pk>[0-9]+)/update/$',
        views.BrowserUpdateView.as_view(),
        name='browser_update'),
    # /projects/<project_pk>/browsers/<browser_id>/delete
    url(r'(?P<project_pk>[0-9]+)/browsers/(?P<pk>[0-9]+)/delete/$',
        views.BrowserDeleteView.as_view(),
        name='browser_delete'),
    # /projects/<project_pk>/browsers/<browser_id>
    url(r'(?P<project_pk>[0-9]+)/browsers/(?P<pk>[0-9]+)/$',
        views.BrowserDetailView.as_view(),
        name='browser_detail'),
    # /projects/<project_pk>/browsers/<browser_id>/update_result/
    url(r'(?P<project_pk>[0-9]+)/browsers/(?P<pk>[0-9]+)/update_result/$',
        views.BrowserUpdateResultView.as_view(),
        name='browser_update_result'),

    # /projects/<project_pk>/features/
    url(r'(?P<project_pk>[0-9]+)/features/$',
        views.FeatureIndexView.as_view(),
        name='feature_index'),
    # /projects/<project_pk>/features/add
    url(r'(?P<project_pk>[0-9]+)/features/add$',
        views.FeatureCreateView.as_view(),
        name='feature_add'),
    # /projects/<project_pk>/features/<feature_pk>
    url(r'(?P<project_pk>[0-9]+)/features/(?P<pk>[0-9]+)/$',
        views.FeatureDetailView.as_view(),
        name='feature_detail'),
    # /projects/<project_pk>/features/<feature_pk>/update
    url(r'(?P<project_pk>[0-9]+)/features/(?P<pk>[0-9]+)/update/$',
        views.FeatureUpdateView.as_view(),
        name='feature_update'),
    # /projects/<project_pk>/features/<feature_pk>/delete
    url(r'(?P<project_pk>[0-9]+)/features/(?P<pk>[0-9]+)/delete/$',
        views.FeatureDeleteView.as_view(),
        name='feature_delete'),

    # /projects/<project_pk>/features/<feature_pk>/testcases
    url(r'(?P<project_pk>[0-9]+)/features/(?P<feature_pk>[0-9]+)/testcases/$',
        views.TestCaseIndexView.as_view(),
        name='testcase_index'),
    # /projects/<project_pk>/features/<feature_pk>/testcases/add
    url(r'(?P<project_pk>[0-9]+)/features/(?P<feature_pk>[0-9]+)/testcases/add$',
        views.TestCaseCreateView.as_view(),
        name='testcase_add'),
    # /projects/<project_pk>/features/<feature_pk>/testcases/<testcase_pk>
    url(r'(?P<project_pk>[0-9]+)/features/(?P<feature_pk>[0-9]+)/testcases/(?P<pk>[0-9]+)$',
        views.TestCaseDetailView.as_view(),
        name='testcase_detail'),
    # /projects/<project_pk>/features/<feature_pk>/testcases/<testcase_pk>/update
    url(r'(?P<project_pk>[0-9]+)/features/(?P<feature_pk>[0-9]+)/testcases/(?P<pk>[0-9]+)/update$',
        views.TestCaseUpdateView.as_view(),
        name='testcase_update'),
    # /projects/<project_pk>/features/<feature_pk>/testcases/<testcase_pk>/delete
    url(r'(?P<project_pk>[0-9]+)/features/(?P<feature_pk>[0-9]+)/testcases/(?P<pk>[0-9]+)/delete$',
        views.TestCaseDeleteView.as_view(),
        name='testcase_delete'),

    # /projects/
    url(r'^$',
        views.ProjectIndexView.as_view(),
        name='project_index'),
    # /projects/add
    url(r'add/$',
        views.ProjectCreateView.as_view(),
        name='project_add'),
    # /projects/<project_pk>/update/
    url(r'(?P<pk>[0-9]+)/update/$',
        views.ProjectUpdateView.as_view(),
        name='project_update'),
    # /projects/<project_pk>/delete/
    url(r'(?P<pk>[0-9]+)/delete/$',
        views.ProjectDeleteView.as_view(),
        name='project_delete'),
    # /projects/<project_pk>/
    url(r'(?P<pk>[0-9]+)/$',
        views.ProjectDetailView.as_view(),
        name='project_detail'),
]
