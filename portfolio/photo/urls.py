from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.photo_show_all, name="accueil"),
    url(r'^photo/$', views.photo_show_all, name="photo_show_all"),
    url(r'^photo/(?P<slug>.+)$', views.photo_show_one, name="photo_show_one"),
    url(r'^video/$', views.video_show_all, name="video_show_all"),
    url(r'^video/(?P<slug>.+)$', views.video_show_one, name="video_show_one"),
    url(r'^contact$', views.contact, name="contact"),
    
]