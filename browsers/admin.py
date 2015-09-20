from django.contrib import admin
from .models import Browser


class BrowserAdmin(admin.ModelAdmin):
    fields = ['name', 'operating_system', 'version', 'project']
    list_display = ('name', 'operating_system', 'project')


admin.site.register(Browser, BrowserAdmin)
