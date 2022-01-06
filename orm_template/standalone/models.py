from django.db import models

# This is a test model (table)
class Test (models.Model):
    name = models.CharField(max_length=25)
