from django.contrib import admin
from .models import *

class CategoriAdmin(admin.ModelAdmin):
    list_display = ('titulo', )


class EnlaceAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'enlace')

admin.site.register(Categoria, CategoriAdmin)
admin.site.register(Enlace, EnlaceAdmin)
