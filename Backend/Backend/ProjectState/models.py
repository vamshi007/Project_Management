from django.db import models

# Create your models here.
class ProjectStateModel(models.Model):
    project_name = models.CharField(max_length=30)
    project_device_name = models.CharField(max_length=30)
    dvr = models.CharField(max_length=30)
    pvr = models.CharField(max_length=30)
    pra = models.CharField(max_length=30)
    sra = models.CharField(max_length=30)
    se_support = models.CharField(max_length=30)