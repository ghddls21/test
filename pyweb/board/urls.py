from django.conf.urls import url
from board import views

urlpatterns = [
    url(r'^$', views.mainIndex, name ='index'),
    url(r'^([0-9]+)/$', views.boardDetail),
    url(r'^create/$', views.boardCreate),
    url(r'^update/([0-9]+)/$', views.boardUpdate),
    url(r'^delete/([0-9]+)/$', views.boardDelete),
]