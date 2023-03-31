from django.db import models

class SampleAttachment(models.Model):
    attachment = models.FileField()

class SampleTest(models.Model):
    name = models.CharField(max_length = 10)
    description = models.CharField(max_length = 10, null = True, blank = True)

    class Meta:
        unique_together = ('name', 'description',)
