from django.contrib import admin

# Register your models here.
from .models import Project, Feature, Browser, Test


class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1


class BrowserInline(admin.TabularInline):
    model = Browser
    extra = 1
    fields = ('name', 'operating_system', 'version')


class ProjectAdmin(admin.ModelAdmin):
    inlines = [FeatureInline, BrowserInline]


class TestInline(admin.TabularInline):
    model = Test
    extra = 3


class FeatureAdmin(admin.ModelAdmin):
    inlines = [TestInline]
    list_display = ('name', 'project')


class TestAdmin(admin.ModelAdmin):
    list_display = ('description', 'feature')


class BrowserAdmin(admin.ModelAdmin):
    fields = ['name', 'operating_system', 'version', 'project']
    list_display = ('name', 'operating_system', 'project')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Browser, BrowserAdmin)
