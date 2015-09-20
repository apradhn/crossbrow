from django.conf.urls import url

from . import views

urlpatterns = [
    # /projects/
    url(r'^$', views.index, name='projects_index'),
    # /projects/<project_id>/browsers/
    url(r'(?P<project_id>[0-9]+)/browsers/$', views.browsers,
        name='browsers_index'),
    # /projects/<project_id>/browsers/<browser_id>
    url(r'(?P<project_id>[0-9]+)/browsers/(?P<browser_id>[0-9]+)/$',
        views.browser_show, name='browser_show'),
    # /projects/<project_id>/
    url(r'(?P<project_id>[0-9]+)/$', views.detail, name='project_detail'),
]
