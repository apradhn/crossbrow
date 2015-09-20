from django.conf.urls import url

from . import views

urlpatterns = [
    # /projects/
    url(r'^$',
        views.project_index,
        name='project_index'),
    # /projects/<project_id>/browsers/
    url(r'(?P<project_id>[0-9]+)/browsers/$',
        views.browser_index,
        name='browsers_index'),
    # /projects/<project_id>/features/
    url(r'(?P<project_id>[0-9]+)/features/$',
        views.feature_index,
        name='features_index'),
    # /projects/<project_id>/features/<feature_id>
    url(r'(?P<project_id>[0-9]+)/features/(?P<feature_id>[0-9]+)/$',
        views.feature_detail,
        name='feature_detail'),
    # /projects/<project_id>/features/<feature_id>/test_cases
    url(r'(?P<project_id>[0-9]+)/features/(?P<feature_id>[0-9]+)/test_cases/$',
        views.test_case_index,
        name='test_case_index'),
    # /projects/<project_id>/features/<feature_id>/test_cases/<test_case_id>
    url(r'(?P<project_id>[0-9]+)/features/(?P<feature_id>[0-9]+)/test_cases/(?P<test_case_id>[0-9]+)$',
        views.test_case_detail,
        name='test_case_detail'),
    # /projects/<project_id>/browsers/<browser_id>/update
    url(r'(?P<project_id>[0-9]+)/browsers/(?P<browser_id>[0-9]+)/$',
        views.browser_update_result,
        name='result'),
    # /projects/<project_id>/browsers/<browser_id>
    url(r'(?P<project_id>[0-9]+)/browsers/(?P<browser_id>[0-9]+)/$',
        views.browser_detail,
        name='browser_detail'),
    # /projects/<project_id>/
    url(r'(?P<project_id>[0-9]+)/$',
        views.project_detail,
        name='project_detail'),
]
