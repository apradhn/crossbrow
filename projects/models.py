from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Feature(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Test(models.Model):
    feature = models.ForeignKey(Feature)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Browser(models.Model):
    test = models.ForeignKey(Test)
    name = models.CharField(max_length=200, default='browser name')
    version = models.CharField(max_length=200)
    operating_system = models.CharField(max_length=200)

    def __str__(self):
        return self.name
