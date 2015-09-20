from django.contrib import admin

# Register your models here.
# from .models import Project, Feature, Browser, Test
from .models import Project
from features.models import Feature
from browsers.models import Browser


class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1
    show_change_link = True


class BrowserInline(admin.TabularInline):
    model = Browser
    extra = 1
    fields = ('name', 'operating_system', 'version')
    show_change_link = True


class ProjectAdmin(admin.ModelAdmin):
    inlines = [FeatureInline, BrowserInline]


# class TestAdmin(admin.ModelAdmin):
#     list_display = ('description', 'feature', 'result')


admin.site.register(Project, ProjectAdmin)
# admin.site.register(Feature, FeatureAdmin)
# admin.site.register(Test, TestAdmin)
