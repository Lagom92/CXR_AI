from django import forms

from .models import Xray

class UploadForm(forms.ModelForm):
    class Meta:
        model = Xray
        fields = {"title", "photo"}