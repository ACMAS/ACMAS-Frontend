from django.forms import ModelForm
from .models import CroppedImg


class CroppedImgForm(ModelForm):
    class Meta:
        model = CroppedImg
        fields = ("file",)

class CroppedQuestionForm(ModelForm):
    class Meta:
        model = CroppedImg
        fields = ("text",)