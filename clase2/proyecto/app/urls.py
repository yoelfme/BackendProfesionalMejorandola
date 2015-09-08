from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hora_actual, name='hora_actual')
]
