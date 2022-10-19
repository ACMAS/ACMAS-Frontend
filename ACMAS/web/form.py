from django.forms import ModelForm
from .models import CroppedImg


class CroppedImgForm(ModelForm):
    class Meta:
        model = CroppedImg
        fields = ("file",)