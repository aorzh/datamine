from django.conf.urls import patterns, url
from datamine.mainapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.main_page, name='main_page'),
]
