from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.mainIndex, name='index'),
    url(r'^([0-9]+)/$', views.blogDetail, name='detail'),
    url(r'^create/$', views.blogCreate, name='create'),
    url(r'^update/([0-9]+)/$', views.blogUpdate, name='update'),
    url(r'^delete/([0-9]+)/$', views.blogDelete, name='delete'),
]