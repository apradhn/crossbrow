from django.db import models
from projects.models import Project


class Feature(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def total_tests(self):
        return self.test_set.count()
    total_tests.admin_order_field = 'total_tests'
    total_tests.short_description = 'Total Tests'
