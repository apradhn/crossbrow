from django.conf.urls import url

from . import views

urlpatterns = [
    # /projects/
    url(r'^$', views.index, name='index'),
    # /projects/:project_id
    url(r'(?P<project_id>[0-9]+)/$', views.show, name='show'),
    # /projects/:project_id/browsers
    url(r'(?P<project_id>[0-9]+)/browsers/$', views.browsers, name='browsers'),
    # /projects/:project_id/features
    url(r'(?P<project_id>[0-9]+)/features/$', views.features, name='features')
]
