from django.conf.urls import url

from . import views

urlpatterns = [
    # /browsers/
    url(r'^$', views.index, name='index'),
]
