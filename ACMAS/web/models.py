from django.db import models


class UploadedFile(models.Model):
    filename = models.CharField(max_length=60)
    file_dir = models.TextField()
    date_uploaded = models.CharField(max_length=50)
    flags = models.TextField()  # parse as json object text.


    def __str__(self):
        return self.filename


class Question(models.Model):
    question = models.TextField()
    Answers = models.TextField()
    Hash = models.TextField()


    def __str__(self):
        return self.question


class University(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.TextField()
    code = models.CharField(max_length=20)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    semster = models.CharField(max_length=30)
    years = models.TextField()
    test_type = models.CharField(max_length=20)
    

    def __str__(self):
        return self.name


# DEFINE ALL MODELS HERE WITH SPECS
