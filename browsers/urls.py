from django.conf.urls import url

from . import views

urlpatterns = [
    # /browsers/
    url(r'^$', views.index, name='index'),
    url(r'(?P<browser_id>[0-9]+)/update_result/$',
        views.update_result,
        name='update_result')

]
