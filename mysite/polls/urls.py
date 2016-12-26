from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^butt$', views.ButtView.as_view(), name='butt'),
]
