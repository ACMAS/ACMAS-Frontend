from django.forms import ModelForm
from django import forms
from .models import CroppedImg


class CroppedImgForm(ModelForm):
    class Meta:
        model = CroppedImg
        fields = ("file",)

class CroppedQuestionForm(ModelForm):
    class Meta:
        model = CroppedImg
        fields = ("text",)
        widgets = {
            'text': forms.Textarea(attrs={'rows': 30, 'cols': 80}),
        }