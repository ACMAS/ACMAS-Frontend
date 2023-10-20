from django.contrib import admin
from .models import UploadedFile,Course,University,Question,CroppedImg
# Register your models here.

admin.site.register(UploadedFile)
admin.site.register(Course)
admin.site.register(University)
admin.site.register(Question)
admin.site.register(CroppedImg)