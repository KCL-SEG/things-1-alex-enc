from django.db import models
# Create your models here.
class Thing():
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=520, blank=True)
    quantity = models.IntegerField(blank=False)
