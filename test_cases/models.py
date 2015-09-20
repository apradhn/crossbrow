from django.db import models
from features.models import Feature


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
