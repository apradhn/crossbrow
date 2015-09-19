from django.contrib import admin

# Register your models here.
from .models import Project, Feature, Browser, Test


class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    inlines = [FeatureInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Feature)
admin.site.register(Browser)
admin.site.register(Test)
