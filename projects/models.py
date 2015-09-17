from django.db import models

class Project(models.Model):
	name = models.CharField(max_length=200)

class Feature(models.Model):
	project = models.ForeignKey(Project)
	name = models.CharField(max_length=200)

class Test(models.Model):
	feature = models.ForeignKey(Feature)
	description = models.CharField(max_length=200)

class Browser(models.Model):
	test = models.ForeignKey(Test)
	name = models.CharField
	version = models.CharField(max_length=200)
	operating_system = models.CharField(max_length=200)