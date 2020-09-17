from django.db import models
from django.conf import settings
import os

class Xray(models.Model):
    # User(작성자) 추가 예정
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True, null=True, upload_to="img/%Y%m%d")
    comment = models.TextField(null=True, blank=True)
    prediction = models.CharField(max_length=100)
    # 필요시 predict 추가 
    
    # delete 오버라이딩
    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.photo.path))
        super(Xray, self).delete(*args, **kwargs) 

    def __str__(self):
        return self.title