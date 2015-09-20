from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Test(models.Model):
    PASS = 'P'
    FAIL = 'F'
    RESULTS = (
        (PASS, 'Pass'),
        (FAIL, 'Fail')
    )
    feature = models.ForeignKey(Feature)
    description = models.CharField(max_length=200)
    result = models.CharField(max_length=10, blank=True, choices=RESULTS)

    def __str__(self):
        return self.description



