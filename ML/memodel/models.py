from django.db import models

# Create your models here.
class interest(models.Model):
    """The interest of each persion."""
    first = models.CharField(null=False,max_length=255)
    second = models.CharField(null=True,max_length=255)
    third = models.CharField(null=True,max_length=255)
