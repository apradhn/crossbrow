from django.db import models
from projects.models import Project


class Browser(models.Model):
    CHROME = 'Google Chrome'
    FIREFOX = 'Mozilla Firefox'
    IE = 'Internet Explorer'
    SAFARI = 'Safari'
    BROWSER_CHOICES = (
        (CHROME, 'Google Chrome'),
        (FIREFOX, 'Mozilla Firefox'),
        (IE, 'Internet Explorer'),
        (SAFARI, 'Safari')
    )

    OSX = 'OSX'
    WIN7 = 'Win7'
    WIN8 = 'Win8'
    WIN10 = 'Win10'
    OS_CHOICES = (
        (OSX, 'OSX'),
        (WIN7, 'Windows 7'),
        (WIN8, 'Windows 8'),
        (WIN10, 'Windows 10'),
    )
    PASS = 'Pass',
    FAIL = 'Fail'
    RESULT_CHOICES = (
        (PASS, 'Pass'),
        (FAIL, 'Fail')
    )

    project = models.ForeignKey(Project,
                                null=True)
    name = models.CharField(max_length=200,
                            choices=BROWSER_CHOICES,
                            default=CHROME)
    version = models.CharField(max_length=200, blank=True)
    operating_system = models.CharField(max_length=200,
                                        choices=OS_CHOICES,
                                        default=OSX)
    result = models.CharField(max_length=200, blank=True, choices=RESULT_CHOICES)

    def __str__(self):
        return self.name
