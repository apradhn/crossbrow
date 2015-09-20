from django.conf.urls import url

from . import views

urlpatterns = [
    # /projects/
    url(r'^$', views.projects_index, name='projects_index'),
    # /projects/<project_id>/browsers/
    url(r'(?P<project_id>[0-9]+)/browsers/$', views.browsers_index,
        name='browsers_index'),
    # /projects/<project_id>/features/
    url(r'(?P<project_id>[0-9]+)/features/$', views.features_index,
        name='features_index'),
    # /projects/<project_id>/browsers/<browser_id>
    url(r'(?P<project_id>[0-9]+)/browsers/(?P<browser_id>[0-9]+)/$',
        views.browser_detail, name='browser_detail'),
    # /projects/<project_id>/
    url(r'(?P<project_id>[0-9]+)/$', views.project_detail,
        name='project_detail'),
]
