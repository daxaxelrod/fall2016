__author__ = 'davidaxelrod'

from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.home, name="portal"),


]
