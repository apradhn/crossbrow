from django.contrib import admin
from .models import Feature
from test_cases.models import TestCase


class TestInline(admin.TabularInline):
    model = TestCase
    extra = 1


class FeatureAdmin(admin.ModelAdmin):
    inlines = [TestInline]
    list_display = ('name', 'project')


admin.site.register(Feature, FeatureAdmin)
