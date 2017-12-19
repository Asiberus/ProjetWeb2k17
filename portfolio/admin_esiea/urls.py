from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.admin_login, name="admin_login"),
    url(r'^photo/add/(?P<password_hash>\w+)$', views.photo_add, name="photo_add"),
    url(r'^photo/edit/(?P<id>\d+)/(?P<password_hash>\w+)$', views.photo_edit, name="photo_edit"),
    url(r'^photo/delete/(?P<id>\d+)/(?P<password_hash>\w+)$', views.photo_delete, name="photo_delete"),
    url(r'^video/add/(?P<password_hash>\w+)$', views.video_add, name="video_add"),
    url(r'^video/edit/(?P<id>\d+)/(?P<password_hash>\w+)$', views.video_edit, name="video_edit"),
    url(r'^video/delete/(?P<id>\d+)/(?P<password_hash>\w+)$', views.video_delete, name="video_delete"),
    url(r'^(?P<password_hash>\w+)', views.admin, name="admin"),

]



