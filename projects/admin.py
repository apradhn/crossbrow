from django.contrib import admin

# Register your models here.
from .models import Project, Feature, Browser, Test


class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    inlines = [FeatureInline]


class TestInline(admin.TabularInline):
    model = Test
    extra = 3


class FeatureAdmin(admin.ModelAdmin):
    inlines = [TestInline]
    list_display = ('name', 'project')


class BrowserInline(admin.TabularInline):
    model = Browser
    extra = 3


class TestAdmin(admin.ModelAdmin):
    inlines = [BrowserInline]
    list_display = ('description', 'feature')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Browser)
