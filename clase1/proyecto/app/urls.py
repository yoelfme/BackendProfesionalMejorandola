from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home2/$', views.home2, name='home2'),
    url(r'^post/(\d+)$', views.post, name='post'),
    url(r'^api/$', views.api, name='api')
]
