from django.db import models

# Create your models here.


class TableData(models.Model):
    name = models.CharField(max_length=90, blank=True)
    request_details = models.TextField(max_length=1000, blank=True)
    server = models.TextField(max_length=1000, blank=True)
