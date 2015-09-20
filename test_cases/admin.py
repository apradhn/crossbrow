from django.contrib import admin
from .models import TestCase


class TestAdmin(admin.ModelAdmin):
    list_display = ('description', 'feature', 'result')


admin.site.register(TestCase, TestAdmin)
