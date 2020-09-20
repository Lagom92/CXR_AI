from django.db import models

# Create your models here.
class Center(models.Model):
    city = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    institutions = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    specimen = models.CharField(max_length=50)

    def __str__(self):
        return self.institutions