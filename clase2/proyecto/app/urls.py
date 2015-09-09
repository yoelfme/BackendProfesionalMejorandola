from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hora/$', views.hora_actual, name='hora_actual'),
    url(r'^$', views.home, name='home'),
    url(r'^plus/(\d+)$', views.plus, name='plus'),
    url(r'^minus/(\d+)$', views.minus, name='minus'),
    url(r'^categoria/(\d+)$', views.categoria, name='categoria'),
    url(r'^add/$', views.add, name='add'),
]
