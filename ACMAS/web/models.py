from django.db import models

# Create your models here.
class UploadedFile(models.Model):
	filename = models.CharField(max_length=60)
	file_dir = models.CharField(max_length=80)

###DEFINE ALL MODELS HERE WITH SPECS
