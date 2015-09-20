from django.conf.urls import url

from . import views

urlpatterns = [
    # /browsers/
    url(r'^$', views.index, name='index'),
    # /browsers/:browser_id
    # url(r'(?P<browser_id>[0-9]+)/$', views.show, name='show')
]
