from django.db import models

# Create your models here.
class UploadedFile(models.Model):
	filename = models.charField(max_length=60)
	file_dir = models.charField(max_length=80)

class OCR(models.Model):
	sourcefile = models.Foreignkey(UploadedFile,on_delete = models.CASCADE)