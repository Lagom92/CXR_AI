from django.db import models
from django.conf import settings
import os

class Xray(models.Model):
    # User(작성자) 추가 예정
    created_at = models.DateTimeField(auto_now_add=True)
    prediction = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(blank=True, null=True, upload_to="img/%Y%m%d")
    heatmap = models.ImageField(blank=True, null=True, upload_to="heat/%Y%m%d")
    
    # delete 오버라이딩
    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.photo.path))
        super(Xray, self).delete(*args, **kwargs) 

    def __str__(self):
        return self.title