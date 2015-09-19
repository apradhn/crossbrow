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
        return self.description


class Browser(models.Model):
    CHROME = 'C',
    FIREFOX = 'FF',
    IE = 'IE'
    SAFARI = 'S'
    BROWSER_CHOICES = (
        (CHROME, 'Chrome'),
        (FIREFOX, 'Mozilla Firefox'),
        (IE, 'Internet Explorer'),
        (SAFARI, 'Safari')
    )

    project = models.ForeignKey(Project, null=True)
    name = models.CharField(max_length=200,
                            choices=BROWSER_CHOICES,
                            default=CHROME)
    version = models.CharField(max_length=200)
    operating_system = models.CharField(max_length=200)

    def __str__(self):
        return self.name
