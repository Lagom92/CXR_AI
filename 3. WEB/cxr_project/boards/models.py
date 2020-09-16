from django.db import models


class Xray(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, null=True, upload_to="img/%Y%m%d")
    
    def __str__(self):
        return self.title