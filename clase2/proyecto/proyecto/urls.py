from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('app.urls'))
]

if not settings.DEBUG:
    urlpatterns += (
        url(r'^static/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
        # url(r'^media/(?P<path>.*)$',
        #     'django.views.static.serve',
        #     {'document_root': settings.MEDIA_ROOT}),
    )
